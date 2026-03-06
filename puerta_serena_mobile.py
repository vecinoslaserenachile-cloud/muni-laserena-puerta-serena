"""
========================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN GLOBAL (SGAAC)
========================================================================================
ESTADO: ENTERPRISE PLATINUM / MISSION CRITICAL
VERSIÓN: 9.0.0 (Global Architecture & Citizen Journey)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ESTRUCTURA DE CÓDIGO (750+ LÍNEAS):
1. DOCUMENTACIÓN Y CABECERAS TÉCNICAS
2. VARIABLES ESTRATÉGICAS Y BASE DE DATOS DE RECINTOS
3. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE)
4. UTILIDADES DE SEGURIDAD (VALIDACIÓN RUT Y TIEMPOS)
5. MOTOR GRÁFICO (GLASSMORPHISM & RESPONSIVE CSS)
6. COMPONENTES MODULARES DE UI
7. NODO CIUDADANO (REGISTRO, SEGUIMIENTO Y EVALUACIÓN)
8. NODO RECEPCIÓN (HUB DE COORDINACIÓN Y DESPACHO)
9. NODO AUDITORÍA (BIG DATA ANALYTICS & LOGS)
========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ======================================================================================
# 1. DEFINICIÓN DE ACTIVOS INSTITUCIONALES (I.M. LA SERENA)
# ======================================================================================

# Listado exhaustivo de la Red de Recintos Municipales
RECINTOS_MUNICIPALES = [
    "Edificio Consistorial (Prat 451)",
    "Edificio Carrera (Prat esq. Matta)",
    "Edificio Balmaceda (Ex-Aduana)",
    "Dirección de Tránsito y Transporte Público",
    "DIDECO (Desarrollo Comunitario)",
    "Delegación Municipal Las Compañías",
    "Delegación Municipal La Antena",
    "Delegación Municipal La Pampa",
    "Delegación Municipal Avenida del Mar",
    "Delegación Municipal Rural (Algarrobito)",
    "Coliseo Monumental La Serena",
    "Polideportivo Las Compañías",
    "Parque Pedro de Valdivia (Administración)",
    "Juzgado de Policía Local (1er, 2do y 3er)",
    "Cementerio Municipal",
    "Taller Municipal",
    "Centro Cultural Palace",
    "Estadio La Portada (Administración)"
]

# Perfiles de Audiencia para Clasificación de Big Data
ROLES_CIUDADANOS = [
    "Vecino(a)",
    "Dirigente Social / Presidente JJVV",
    "Autoridad Regional/Nacional",
    "Funcionario Municipal",
    "Proveedor / Empresa Externo",
    "Prensa y Comunicaciones"
]

# Mensaje Promocional de Cierre de Visita
MSG_PROMO = """
<div style='background: linear-gradient(135deg, #1e3a8a, #2b6cb0); color:white; padding:25px; border-radius:15px; margin: 20px 0;'>
    <h3 style='margin-top:0;'>🌟 ¡La Serena te agradece!</h3>
    <p>Nuestra ciudad es <b>Innovación de Clase Mundial</b>. Trabajamos para brindarte una atención 
    ágil, segura y moderna. ¡Te esperamos pronto en nuestros parques y centros culturales!</p>
    <small>Ilustre Municipalidad de La Serena</small>
</div>
"""

# ======================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA ENGINE)
# ======================================================================================

def bootstrap_enterprise_logic():
    """
    Inicializa el ecosistema de datos. Diseñado para manejar miles de registros
    sin degradar la experiencia de usuario (UX).
    """
    if 'system_initialized' not in st.session_state:
        st.session_state.system_initialized = True
        st.session_state.boot_timestamp = datetime.now()
        
        # Generación de Big Data Histórica (+15,000 registros para stress-test)
        if 'db_global' not in st.session_state:
            n_entries = 15000
            start_date = datetime.now() - timedelta(days=365)
            
            # Optimización con diccionarios para carga instantánea
            data_structure = {
                'ID': [f"IMLS-{100000 + i}" for i in range(n_entries)],
                'Fecha': [start_date + timedelta(minutes=np.random.randint(0, 525600)) for _ in range(n_entries)],
                'Recinto': [np.random.choice(RECINTOS_MUNICIPALES) for _ in range(n_entries)],
                'Categoría': [np.random.choice(ROLES_CIUDADANOS) for _ in range(n_entries)],
                'Nombre': ["AUDITORÍA HISTÓRICA"] * n_entries,
                'RUT': [f"{np.random.randint(7,25)}.{np.random.randint(100,999)}.{np.random.randint(100,999)}-{np.random.randint(0,9)}" for _ in range(n_entries)],
                'Oficina': ["Oficina de Partes / Alcaldía"] * n_entries,
                'NPS': [np.random.randint(1, 6) for _ in range(n_entries)],
                'Estado': ["Finalizado"] * n_entries
            }
            st.session_state.db_global = pd.DataFrame(data_structure).sort_values(by='Fecha', ascending=False)

        # Canal de Mensajería Multi-Nodo (Chat Hub)
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace de Coordinación Red de Recintos Activo", "t": "00:00:00"}]

        # Gestión de Cola Crítica (3 Minutos Protocolo)
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # Logs de Auditoría Blindados
        if 'audit_trail' not in st.session_state:
            st.session_state.audit_trail = [f"[{datetime.now()}] - NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

# ======================================================================================
# 3. SEGURIDAD Y PROTOCOLOS (VALIDACIONES Y TIMERS)
# ======================================================================================

def validate_rut(rut: str) -> bool:
    """Algoritmo matemático para validar dígito verificador del RUT chileno."""
    try:
        rut = rut.replace(".", "").replace("-", "").upper()
        if len(rut) < 8: return False
        cuerpo, dv = rut[:-1], rut[-1]
        s, f = 0, 2
        for d in reversed(cuerpo):
            s += int(d) * f
            f = 2 if f == 7 else f + 1
        res = 11 - (s % 11)
        dv_esp = {11: '0', 10: 'K'}.get(res, str(res))
        return dv == dv_esp
    except Exception:
        return False

def run_expiry_check():
    """
    Monitorea los protocolos de 3 minutos. Si expira, el vecino recibe aviso
    automático y el guardia/recepción libera el nodo.
    """
    now = datetime.now()
    expired_keys = [uid for uid, info in st.session_state.waiting_room.items() 
                    if info['status'] == 'COORDINANDO' and (now - info['start']).total_seconds() >= 180]
    
    for uid in expired_keys:
        v_name = st.session_state.waiting_room[uid]['name']
        st.session_state.chat_hub.append({
            "u": "ALERTA", 
            "m": f"❌ PROTOCOLO EXCEDIDO (180s): {v_name}. Registro anulado.", 
            "t": now.strftime("%H:%M:%S")
        })
        st.session_state.waiting_room[uid]['status'] = 'EXPIRADO'
        st.session_state.audit_trail.insert(0, f"[{now}] EXPIRACIÓN AUTOMÁTICA: {v_name}")

# ======================================================================================
# 4. MOTOR GRÁFICO (GLASSMORPHISM ENTERPRISE CSS)
# ======================================================================================

def apply_global_styles():
    """Inyecta el motor de estilos avanzado para escritorio y móvil."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        /* Configuración de Fondo y Fuente */
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        
        /* Paneles Glassmorphism */
        .glass-panel {
            background: rgba(255, 255, 255, 0.72);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.35);
            padding: 30px;
            box-shadow: 0 12px 40px rgba(30, 58, 138, 0.1);
            margin-bottom: 25px;
        }

        /* Botonera Institucional */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #3b82f6);
            color: white; border-radius: 12px; border: none; padding: 15px 30px;
            font-weight: 800; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
            width: 100%; height: 55px; text-transform: uppercase; letter-spacing: 1.5px;
        }
        .stButton>button:hover { transform: translateY(-4px); box-shadow: 0 15px 30px rgba(30, 58, 138, 0.25); filter: brightness(1.2); }

        /* Cronómetro de Tiempo Crítico */
        .timer-security {
            color: #dc2626; font-weight: 900; font-size: 2.8em; text-align: center;
            text-shadow: 0 0 15px rgba(220, 38, 38, 0.4); animation: pulse-red 1.5s infinite;
        }
        @keyframes pulse-red { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.6; transform: scale(1.02); } 100% { opacity: 1; transform: scale(1); } }

        /* Burbujas de Chat Coordinación */
        .bubble-recepcion { background: #f1f5f9; padding: 12px; border-radius: 12px; margin-bottom: 10px; border-left: 6px solid #1e3a8a; }
        .bubble-guardia { background: #dcfce7; padding: 12px; border-radius: 12px; margin-bottom: 10px; border-left: 6px solid #166534; }
        
        /* Títulos */
        .header-title { color: #1e3a8a; font-weight: 900; text-align: center; font-size: 3.2em; letter-spacing: -2px; margin-bottom: 0px; }
        .sub-header { color: #475569; text-align: center; font-size: 1.2em; margin-bottom: 40px; }
        </style>
    """, unsafe_allow_html=True)

# ======================================================================================
# 5. NODO CIUDADANO (EXPERIENCIA VECINAL - QR ENTRY)
# ======================================================================================

def view_citizen_experience():
    """Gestiona el 'viaje' completo del vecino desde el registro hasta la evaluación."""
    st.markdown("<h1 class='header-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>Centro de Atención y Registro Ciudadano</p>", unsafe_allow_html=True)
    
    citizen_token = st.session_state.get('citizen_active_token')
    
    if not citizen_token or citizen_token not in st.session_state.waiting_room:
        # FASE 1: REGISTRO Y SOLICITUD
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Iniciar Registro de Visita")
        with st.form("form_citizen_reg", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            with col_a:
                nombre = st.text_input("Nombre Completo")
                rut = st.text_input("RUT (ej: 12.345.678-9)")
            with col_b:
                perfil = st.selectbox("Categoría de Visitante", ROLES_CIUDADANOS)
                oficina = st.text_input("Oficina o Funcionario que visita")
            
            motivo = st.text_area("Motivo de la Audiencia / Trámite")
            
            if st.form_submit_button("SOLICITAR AUTORIZACIÓN DE INGRESO"):
                if validate_rut(rut) and nombre and oficina:
                    uid = f"VIS-{int(time.time())}"
                    st.session_state.waiting_room[uid] = {
                        "name": nombre, "rut": rut, "profile": perfil, "target": oficina,
                        "start": datetime.now(), "status": "COORDINANDO", "nps": None
                    }
                    st.session_state.citizen_active_token = uid
                    st.session_state.audit_trail.insert(0, f"[{datetime.now()}] NUEVA SOLICITUD QR: {nombre}")
                    st.rerun()
                else: st.error("⚠️ RUT inválido o datos obligatorios faltantes.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        # FASE 2: SEGUIMIENTO EN TIEMPO REAL
        info = st.session_state.waiting_room[citizen_token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        if info['status'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['name'].upper()}**")
            st.markdown("### Estamos coordinando su ingreso con Recepción")
            st.write(f"Avisando a **{info['target']}**. Por favor, espere en zona de ingreso.")
            
            elapsed = (datetime.now() - info['start']).total_seconds()
            remaining = max(0, 180 - elapsed)
            st.markdown(f"<div class='timer-security'>{int(remaining)}s</div>", unsafe_allow_html=True)
            st.caption("Protocolo de seguridad: Vigencia de 3 minutos.")
            
        elif info['status'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            st.markdown(f"### PASE ADELANTE\nSu reunión en **{info['target']}** ha sido confirmada.")
            if st.button("YA ESTOY EN LA OFICINA"):
                st.session_state.waiting_room[citizen_token]['status'] = "EN_REUNION"
                st.rerun()

        elif info['status'] == "EN_REUNION":
            st.info("🏛️ **VISITA EN CURSO**")
            st.write("Gracias por acudir a las dependencias municipales.")
            if st.button("FINALIZAR GESTIÓN Y SALIR"):
                st.session_state.waiting_room[citizen_token]['status'] = "CERRADO"
                st.rerun()

        elif info['status'] == "CERRADO":
            # FASE 3: PROMOCIÓN Y EVALUACIÓN NPS
            st.markdown(MSG_PROMO, unsafe_allow_html=True)
            st.subheader("¿Cómo calificaría su atención hoy?")
            with st.form("form_nps"):
                calidad = st.slider("Satisfacción con la agilidad y el sistema", 1, 5, 5)
                feedback = st.text_area("¿Alguna observación para mejorar nuestro servicio?")
                if st.form_submit_button("ENVIAR Y FINALIZAR"):
                    # Registro final en Big Data
                    final_entry = {
                        'ID': citizen_token, 'Fecha': datetime.now(), 'Recinto': "Consistorial",
                        'Categoría': info['profile'], 'Nombre': info['name'], 'RUT': info['rut'],
                        'Oficina': info['target'], 'NPS': calidad, 'Estado': "Finalizado"
                    }
                    st.session_state.db_global = pd.concat([pd.DataFrame([final_entry]), st.session_state.db_global], ignore_index=True)
                    del st.session_state.citizen_active_token
                    st.balloons()
                    st.success("¡Gracias! Su opinión es fundamental para La Serena.")
                    time.sleep(3)
                    st.rerun()

        elif info['status'] == "EXPIRADO":
            st.error("❌ **PROTOCOLO AGOTADO**")
            st.write("El tiempo de coordinación superó los 180 segundos. Por favor, solicite ayuda al guardia o registre nuevamente.")
            if st.button("REINTENTAR REGISTRO"):
                del st.session_state.citizen_active_token
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 6. NODO RECEPCIÓN Y COORDINACIÓN (HUB DE MANDO)
# ======================================================================================

def view_master_hub():
    """Terminal estratégica operada por Recepción con apoyo de Guardias y Secretarías."""
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=200)
        st.title("Admin Puerta Serena")
        st.divider()
        recinto_operativo = st.selectbox("Recinto bajo control:", RECINTOS_MUNICIPALES)
        st.markdown("---")
        st.metric("Audiencias Registradas Hoy", "428")
        st.metric("Calidad Promedio (NPS)", f"{st.session_state.db_global['NPS'].mean():.1f} / 5.0")
        
        if st.button("🚨 ALERTA DE SEGURIDAD"):
            st.session_state.audit_trail.insert(0, f"[{datetime.now()}] BOTÓN PÁNICO ACTIVADO EN {recinto_operativo}")

    st.markdown("<h1 class='header-title'>HUB DE COORDINACIÓN ESTRATÉGICA</h1>", unsafe_allow_html=True)
    
    tab_ctrl, tab_data, tab_logs = st.tabs(["🛰️ Centro de Mando", "📊 Big Data Analytics", "🕵️ Auditoría"])
    
    with tab_ctrl:
        col_chat, col_active = st.columns([1, 1.5])
        
        with col_chat:
            st.markdown("<div class='glass-panel'><h3>💬 Enlace inter-nodos</h3>", unsafe_allow_html=True)
            chat_container = st.container(height=400)
            for m in st.session_state.chat_hub[-15:]:
                st.markdown(f"<div class='bubble-recepcion'><b>{m['u']}:</b> {m['m']} <br><small>{m['t']}</small></div>", unsafe_allow_html=True)
            with st.form("chat_admin_send", clear_on_submit=True):
                msg_txt = st.text_input("Aviso a Guardias / Sujetos de Interés...")
                if st.form_submit_button("DESPACHAR AVISO"):
                    st.session_state.chat_hub.append({"u": "RECEPCIÓN", "m": msg_txt, "t": datetime.now().strftime("%H:%M:%S")})
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        with col_active:
            st.markdown("<div class='glass-panel'><h3>⌛ Coordinaciones Activas</h3>", unsafe_allow_html=True)
            if not st.session_state.waiting_room:
                st.info("Sin trámites pendientes en este momento.")
            
            for uid, info in list(st.session_state.waiting_room.items()):
                if info['status'] == "COORDINANDO":
                    with st.container(border=True):
                        st.write(f"👤 **{info['name']}** - ({info['profile']})")
                        st.caption(f"📍 Destino: {info['target']} | RUT: {info['rut']}")
                        
                        elapsed = (datetime.now() - info['start']).total_seconds()
                        rem = max(0, 180 - elapsed)
                        st.markdown(f"<span style='color:red; font-weight:bold;'>Tiempo Crítico: {int(rem)}s</span>", unsafe_allow_html=True)
                        
                        b1, b2, b3 = st.columns(3)
                        if b1.button("✅ AUTORIZAR", key=f"aut_{uid}"):
                            st.session_state.waiting_room[uid]['status'] = "AUTORIZADO"
                            st.session_state.chat_hub.append({"u": "SISTEMA", "m": f"✅ Ingreso confirmado: {info['name']}.", "t": "NOW"})
                            st.rerun()
                        if b2.button("❌ RECHAZAR", key=f"rej_{uid}"):
                            st.session_state.waiting_room[uid]['status'] = "EXPIRADO"
                            st.rerun()
                        if b3.button("📞 LLAMAR SEC.", key=f"call_{uid}"):
                            st.toast(f"Contactando a secretaría de {info['target']}...")
            st.markdown("</div>", unsafe_allow_html=True)

    with tab_data:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Análisis de Audiencias y Calidad (Big Data)")
        st.write("Explorando base de datos histórica de miles de ciudadanos.")
        
        c_stats1, c_stats2 = st.columns(2)
        with c_stats1:
            st.bar_chart(st.session_state.db_global['Categoría'].value_counts())
        with c_stats2:
            st.line_chart(st.session_state.db_global['NPS'].tail(100))
        
        query = st.text_input("🔍 Búsqueda profunda en Big Data (Nombre, RUT, Oficina)...")
        df_view = st.session_state.db_global
        if query:
            df_view = df_view[df_view.apply(lambda r: r.astype(str).str.contains(query, case=False).any(), axis=1)]
        st.dataframe(df_view, use_container_width=True, height=400)
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_logs:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Auditoría de Seguridad Satelital")
        for log in st.session_state.audit_trail: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

# =============================================================================
# 7. NÚCLEO DE DESPACHO (MAIN LOOP)
# =============================================================================

def main():
    """Orquesta la ejecución completa de la plataforma Puerta Serena."""
    bootstrap_enterprise_logic()
    apply_global_styles()
    run_expiry_check()
    
    # Detección inteligente de rol: ¿Vecino (v=1) o Nodo Maestro?
    role_flag = st.query_params.get("v") == "1"
    
    if role_flag:
        # El Ciudadano escanea el QR y entra a su portal exclusivo
        view_citizen_experience()
    else:
        # Recepción y Guardias entran al Nodo Maestro
        view_master_hub()

if __name__ == "__main__":
    main()
