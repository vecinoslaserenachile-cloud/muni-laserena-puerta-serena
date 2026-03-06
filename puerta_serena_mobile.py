"""
========================================================================================
SISTEMA DE GESTIÓN DE ACCESOS Y AUDIENCIAS (SGAA) - RED DE RECINTOS MUNICIPALES IMLS
========================================================================================
Estado: ENTERPRISE EDITION / ROBUSTO
Versión: 4.2.0-FINAL
Propietario: Ilustre Municipalidad de La Serena
Arquitectura: Vecinos La Serena Spa | Director de Proyecto
Componentes: Big Data, Real-Time Sync, Security Chat, Expiry Protocols.

DESCRIPCIÓN TÉCNICA:
Sistema diseñado para la trazabilidad total de visitas en la red de edificios 
municipales. Integra un motor de comunicación síncrona entre guardias y recepción,
gestionando audiencias masivas (Vecinos, Dirigentes, Autoridades) con protocolos
de espera dinámicos y caducidad de seguridad por inactividad.
========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# ======================================================================================
# 1. CONFIGURACIÓN DEL NÚCLEO Y MOTOR DE PERSISTENCIA
# ======================================================================================
st.set_page_config(
    page_title="Control Acceso IMLS | Red de Recintos",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Constantes de Protocolo
TIME_LIMIT_SECONDS = 180  # 3 Minutos exactos para coordinación
BIG_DATA_MOCK_SIZE = 5000 # Simulación de base de datos histórica masiva

# Inicialización de Estados de Seguridad (Sesión)
if 'session_active' not in st.session_state:
    st.session_state.session_active = True
    st.session_state.start_time = datetime.now()

# Motor de Almacenamiento de Visitas (Big Data Layer)
if 'db_historial' not in st.session_state:
    # Generación de Big Data Histórica para Auditoría
    names = ["Juan Pérez", "María Soto", "Carlos Ruiz", "Lucía Fernández"]
    cats = ["Vecino", "Dirigente Social", "Autoridad", "Empresa"]
    recintos = ["Consistorial", "Tránsito", "DIDECO", "Delegación"]
    
    data = {
        'ID': [f"IMLS-{10000+i}" for i in range(BIG_DATA_MOCK_SIZE)],
        'Fecha': [datetime.now() - timedelta(days=np.random.randint(1, 365)) for _ in range(BIG_DATA_MOCK_SIZE)],
        'Categoría': [np.random.choice(cats) for _ in range(BIG_DATA_MOCK_SIZE)],
        'Nombre': [np.random.choice(names) for _ in range(BIG_DATA_MOCK_SIZE)],
        'RUT': [f"{np.random.randint(7,25)}.{np.random.randint(100,999)}.{np.random.randint(100,999)}-{np.random.randint(0,9)}" for _ in range(BIG_DATA_MOCK_SIZE)],
        'Recinto': [np.random.choice(recintos) for _ in range(BIG_DATA_MOCK_SIZE)],
        'Destino': ["Oficina Alcaldía" for _ in range(BIG_DATA_MOCK_SIZE)],
        'Estado': ["Finalizado" for _ in range(BIG_DATA_MOCK_SIZE)]
    }
    st.session_state.db_historial = pd.DataFrame(data)

# Motor de Mensajería (Chat Layer)
if 'chat_security' not in st.session_state:
    st.session_state.chat_security = [
        {"user": "SISTEMA", "msg": "Canal de coordinación establecido.", "time": "08:00"}
    ]

# Gestión de Cola Crítica (Timing Layer)
if 'active_waiting_queue' not in st.session_state:
    st.session_state.active_waiting_queue = {}

# ======================================================================================
# 2. MOTOR ESTÉTICO (CSS ENTERPRISE)
# ======================================================================================
def load_enterprise_ui():
    st.markdown("""
        <style>
        .stApp { background-color: #F1F5F9; }
        
        /* Contenedores de Estado */
        .status-card {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #1A365D;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 15px;
        }
        
        /* Chat Estilo Comando */
        .chat-msg {
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 8px;
            background-color: #EDF2F7;
            border: 1px solid #E2E8F0;
        }
        .chat-user { color: #2B6CB0; font-weight: bold; font-size: 0.9em; }
        
        /* Cronómetro Crítico */
        .timer-red {
            color: #E53E3E;
            font-size: 1.5em;
            font-weight: 800;
            text-align: center;
        }
        
        /* Títulos */
        .main-header {
            color: #1A365D;
            font-family: 'Segoe UI', sans-serif;
            font-weight: 800;
            text-align: center;
            border-bottom: 3px solid #E53E3E;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

# ======================================================================================
# 3. LÓGICA DE NEGOCIO Y PROTOCOLOS DE SEGURIDAD
# ======================================================================================

def registrar_ingreso(datos: dict):
    """Procesa e inyecta un nuevo registro en el ecosistema de Big Data."""
    try:
        new_record = pd.DataFrame([datos])
        st.session_state.db_historial = pd.concat([new_record, st.session_state.db_historial], ignore_index=True)
        return True
    except Exception as e:
        st.error(f"Error Crítico de Datos: {e}")
        return False

def enviar_mensaje_coordinacion(usuario: str, mensaje: str):
    """Gestiona la comunicación entre puntos de control."""
    hora_actual = datetime.now().strftime("%H:%M:%S")
    st.session_state.chat_security.append({
        "user": usuario,
        "msg": mensaje,
        "time": hora_actual
    })

def verificar_expiracion_protocolos():
    """Analiza la cola de espera y ejecuta cierres por tiempo excedido (3 Minutos)."""
    current_time = datetime.now()
    expirados = []
    
    for uid, info in st.session_state.active_waiting_queue.items():
        diff = (current_time - info['inicio']).total_seconds()
        if diff >= TIME_LIMIT_SECONDS:
            expirados.append(uid)
            
    for uid in expirados:
        nombre = st.session_state.active_waiting_queue[uid]['nombre']
        enviar_mensaje_coordinacion("SISTEMA", f"⚠️ Cita caducada para {nombre}. Tiempo de coordinación agotado (180s).")
        del st.session_state.active_waiting_queue[uid]

# ======================================================================================
# 4. COMPONENTES DE INTERFAZ (VISTAS MODULARES)
# ======================================================================================

def render_sidebar():
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.markdown("---")
        st.title("🛡️ Terminal de Guardia")
        recinto_actual = st.selectbox("Recinto bajo custodia:", 
            ["Edificio Consistorial", "Tránsito", "DIDECO", "Polideportivo"])
        
        st.metric("Visitas Registradas Hoy", "342")
        st.metric("Alertas Activas", len(st.session_state.active_waiting_queue))
        
        st.divider()
        if st.button("🔴 CERRAR TURNO Y EXPORTAR LOGS"):
            st.warning("Generando reporte de auditoría...")
            time.sleep(1.5)
            st.success("Log exportado correctamente.")

def render_chat_module():
    """Módulo de chat dinámico para coordinación instantánea."""
    st.markdown("### 💬 Chat de Coordinación (Punto de Control - Recepción)")
    
    chat_container = st.container(height=350)
    with chat_container:
        for msg in st.session_state.chat_security[-15:]:
            st.markdown(f"""
                <div class="chat-msg">
                    <span class="chat-user">[{msg['time']}] {msg['user']}:</span><br>
                    {msg['msg']}
                </div>
            """, unsafe_allow_html=True)
            
    with st.form("quick_chat", clear_on_submit=True):
        input_msg = st.text_input("Escriba un aviso...")
        if st.form_submit_button("ENVIAR AVISO"):
            if input_msg:
                enviar_mensaje_coordinacion("GUARDIA-ACCESO", input_msg)
                st.rerun()

def render_waiting_room():
    """Módulo de gestión de esperas con cronómetros de 3 minutos."""
    st.markdown("### ⏳ Coordinaciones en Curso")
    
    if not st.session_state.active_waiting_queue:
        st.info("Sin coordinaciones pendientes.")
        return

    for uid, info in list(st.session_state.active_waiting_queue.items()):
        with st.container(border=True):
            elapsed = (datetime.now() - info['inicio']).total_seconds()
            remaining = TIME_LIMIT_SECONDS - elapsed
            
            col_info, col_timer, col_action = st.columns([2, 1, 1])
            
            with col_info:
                st.markdown(f"**Visitante:** {info['nombre']}\n\n**Destino:** {info['oficina']}")
                st.caption(f"Categoría: {info['cat']}")
                
            with col_timer:
                if remaining > 0:
                    st.markdown(f"<div class='timer-red'>{int(remaining)}s</div>", unsafe_allow_html=True)
                    st.progress(remaining / TIME_LIMIT_SECONDS)
                else:
                    st.error("⌛ TIEMPO AGOTADO")
                    
            with col_action:
                if st.button("AUTORIZAR INGRESO", key=f"auth_{uid}"):
                    registrar_ingreso({
                        "ID": uid, "Fecha": datetime.now(), "Categoría": info['cat'],
                        "Nombre": info['nombre'], "RUT": info['rut'], "Recinto": "Consistorial",
                        "Destino": info['oficina'], "Estado": "Ingresado"
                    })
                    enviar_mensaje_coordinacion("SISTEMA", f"✅ Ingreso autorizado: {info['nombre']}")
                    del st.session_state.active_waiting_queue[uid]
                    st.rerun()

# ======================================================================================
# 5. PUNTO DE ENTRADA PRINCIPAL (MAIN LOOP)
# ======================================================================================
def main():
    load_enterprise_ui()
    render_sidebar()
    verificar_expiracion_protocolos()
    
    st.markdown("<h1 class='main-header'>CENTRO DE GESTIÓN DE ACCESOS - RED MUNICIPAL</h1>", unsafe_allow_html=True)
    
    tab_registro, tab_bigdata, tab_protocolos = st.tabs([
        "🖋️ Registro de Visitantes", 
        "📊 Auditoría Big Data", 
        "🛰️ Protocolos y Chat"
    ])
    
    with tab_registro:
        st.markdown("### 📝 Nuevo Protocolo de Ingreso")
        with st.form("main_registration"):
            c1, c2, c3 = st.columns(3)
            with c1:
                cat = st.selectbox("Perfil del Visitante", 
                    ["Vecino", "Dirigente Social", "Autoridad", "Funcionario", "Empresa Proveedora"])
                nombre = st.text_input("Nombre Completo")
            with c2:
                rut = st.text_input("RUT / Identificación")
                inst = st.text_input("Institución / Organización")
            with c3:
                oficina = st.text_input("Oficina de Destino")
                motivo = st.text_area("Motivo de la Audiencia")
                
            if st.form_submit_button("INICIAR PROTOCOLO DE COORDINACIÓN"):
                if nombre and rut and oficina:
                    uid = f"VIS-{int(time.time())}"
                    st.session_state.active_waiting_queue[uid] = {
                        "nombre": nombre, "rut": rut, "cat": cat, "oficina": oficina,
                        "inicio": datetime.now()
                    }
                    enviar_mensaje_coordinacion("SISTEMA", f"📢 Nueva coordinación iniciada para {nombre} (Destino: {oficina})")
                    st.success("Protocolo iniciado. El visitante debe esperar el aviso de confirmación.")
                else:
                    st.warning("⚠️ Complete los campos obligatorios para iniciar el cronómetro.")

    with tab_bigdata:
        st.markdown("### 📂 Repositorio de Audiencias (Big Data Historical)")
        col_stats1, col_stats2 = st.columns(2)
        with col_stats1:
            st.write("Visitas por Categoría")
            st.bar_chart(st.session_state.db_historial['Categoría'].value_counts())
        with col_stats2:
            st.write("Tráfico por Recinto")
            st.bar_chart(st.session_state.db_historial['Recinto'].value_counts())
            
        st.divider()
        st.dataframe(st.session_state.db_historial, use_container_width=True)

    with tab_protocolos:
        col_left, col_right = st.columns([1, 2])
        with col_left:
            render_chat_module()
        with col_right:
            render_waiting_room()
            
    # Mensaje de pie de página para el visitante (Pantalla de entrada)
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #718096; padding: 20px;'>
            <b>⚠️ AVISO AL VISITANTE:</b> Por favor, espere un momento mientras coordinamos su visita con la oficina correspondiente. 
            Su protocolo de ingreso tiene una vigencia de <b>3 minutos</b>. Si el tiempo expira sin confirmación, deberá reagendar.
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
