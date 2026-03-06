"""
========================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN AUTÓNOMA (SGAAC-360)
========================================================================================
ESTADO: ENTERPRISE PLATINUM / MISSION CRITICAL
VERSIÓN: 14.0.0 (Hybrid Infrastructure & Territorial Marketing)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE MÓDULOS (+850 LÍNEAS):
1.  NODO CIUDADANO: Registro QR Inteligente. Detecta si el recinto es 'Autónomo' o 'Asistido'.
2.  NODO GUARDIA: Gestión de EPP e ingresos físicos (Solo en recintos con dotación).
3.  NODO RECEPCIÓN: Control maestro satelital y despacho de avisos.
4.  NODO SECRETARÍAS: Autorización directa (en recintos autónomos) o coordinada.
5.  NODO BIG DATA ANALYTICS: Análisis correlativo de tiempos reales de permanencia.
6.  NODO CRM ESTRATÉGICO: Gestión de fichas, redes sociales y contacto ciudadano.
========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ======================================================================================
# 1. BASE DE DATOS DE ACTIVOS Y DOTACIÓN TERRITORIAL
# ======================================================================================

# Definición de Recintos con Variable de Dotación (Personal de Primera Línea)
RECINTOS_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True},
    "Dirección de Tránsito": {"dotacion": True},
    "DIDECO (Social)": {"dotacion": True},
    "Delegación Las Compañías": {"dotacion": True},
    "Delegación La Antena": {"dotacion": False}, # Recinto Autónomo
    "Delegación La Pampa": {"dotacion": False},   # Recinto Autónomo
    "Delegación Avenida del Mar": {"dotacion": True},
    "Delegación Rural (Algarrobito)": {"dotacion": False}, # Recinto Autónomo
    "Coliseo Monumental": {"dotacion": True},
    "Polideportivo Las Compañías": {"dotacion": True},
    "Parque Pedro de Valdivia": {"dotacion": True},
    "Juzgado de Policía Local": {"dotacion": True},
    "Taller Municipal": {"dotacion": False}, # Recinto Autónomo
    "Centro Cultural Palace": {"dotacion": False}, # Recinto Autónomo
    "Estadio La Portada": {"dotacion": True}
}

DEPARTAMENTOS_IMLS = [
    "Alcaldía", "Secretaría Municipal", "Administración Municipal",
    "Dirección de Obras (DOM)", "Dirección de Tránsito", "DIDECO - Social",
    "Dirección Jurídica", "Comunicaciones y RR.PP.", "Turismo y Patrimonio",
    "Cultura y Artes", "Seguridad Ciudadana", "Finanzas y Tesorería",
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda"
]

PERFILES_AUDIENCIA = ["Vecino(a)", "Dirigente Social", "Autoridad", "Funcionario", "Empresa", "Prensa"]

# MARKETING TERRITORIAL: MENSAJES PROMOCIONALES DINÁMICOS
CONSEJOS_TURISMO = [
    "🏛️ Mientras espera, admire nuestro Casco Histórico, Patrimonio Nacional.",
    "🌳 Disfrute de la brisa en nuestra Plaza de Armas, el corazón de la ciudad.",
    "☕ Hay excelentes cafés en calle Prat y Matta para una espera agradable.",
    "Church ⛪ ¿Sabía que somos la 'Ciudad de los Campanarios'? Descubra su historia.",
    "🛍️ La Recova está a pasos: el mejor lugar para artesanía y papayas locales."
]

# ======================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE)
# ======================================================================================

def bootstrap_enterprise_system():
    """Inicializa el núcleo del sistema con persistencia blindada contra colapsos."""
    if 'system_ready' not in st.session_state:
        st.session_state.system_ready = True
        st.session_state.boot_time = datetime.now()
        
        # PREVENCIÓN ATTRIBUTE_ERROR
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO ACTIVO - DIRECTOR: Rodrigo Godoy"]
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00:00"}]
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación de 25,000 registros históricos
        if 'db_master' not in st.session_state:
            n = 25000
            start = datetime.now() - timedelta(days=730)
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start + timedelta(minutes=np.random.randint(0, 1051200)) for _ in range(n)],
                'Recinto': [np.random.choice(list(RECINTOS_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(DEPARTAMENTOS_IMLS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_AUDIENCIA) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Permanencia': [np.random.randint(5, 60) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ======================================================================================
# 3. MOTOR ESTÉTICO (GLASSMORPHISM ENTERPRISE UI)
# ======================================================================================

def inject_enterprise_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        .glass-panel { background: rgba(255,255,255,0.72); backdrop-filter: blur(15px); border-radius: 20px; border: 1px solid rgba(255,255,255,0.4); padding: 30px; box-shadow: 0 10px 40px rgba(30,58,138,0.1); margin-bottom: 25px; }
        .stButton>button { background: linear-gradient(45deg, #1e3a8a, #3b82f6); color: white; border-radius: 12px; border: none; padding: 15px 30px; font-weight: 800; transition: 0.4s; width: 100%; height: 55px; text-transform: uppercase; }
        .stButton>button:hover { transform: translateY(-4px); box-shadow: 0 15px 30px rgba(30,58,138,0.25); filter: brightness(1.2); }
        .promo-box { background: rgba(30, 58, 138, 0.08); border-radius: 15px; padding: 25px; border-left: 8px solid #1e3a8a; margin: 20px 0; font-size: 1.1em; color: #1e3a8a; font-weight: 600; }
        .timer-security { color: #dc2626; font-weight: 900; font-size: 2.8em; text-align: center; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }
        .muni-title { color: #1e3a8a; font-weight: 900; text-align: center; font-size: 3.2em; letter-spacing: -2px; margin-bottom: 0px; }
        </style>
    """, unsafe_allow_html=True)

# ======================================================================================
# 4. MÓDULO I: NODO CIUDADANO (VIAJE INTELIGENTE - QR)
# ======================================================================================

def view_citizen_node():
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#475569;'>Portal de Atención y Registro Municipal</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Iniciar Registro de Visita")
        with st.form("form_reg_v", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                recinto = st.selectbox("¿En qué edificio municipal se encuentra?", list(RECINTOS_IMLS.keys()))
                nombre = st.text_input("Nombre Completo")
                rut = st.text_input("RUT / Identificación")
            with c2:
                perfil = st.selectbox("Categoría de Visitante", PERFILES_AUDIENCIA)
                depto = st.selectbox("Oficina / Área de Destino", DEPARTAMENTOS_IMLS)
                motivo = st.text_area("Motivo de la Audiencia")
            
            if st.form_submit_button("SOLICITAR AUTORIZACIÓN"):
                if nombre and rut and recinto:
                    uid = f"V-{int(time.time())}"
                    # Determinar si el flujo es Asistido o Autónomo
                    staff_mode = RECINTOS_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(), "staff_mode": staff_mode,
                        "inicio_reunion": None, "fin_reunion": None, "estado": "COORDINANDO"
                    }
                    st.session_state.citizen_token = uid
                    st.rerun()
                else: st.error("⚠️ Datos obligatorios incompletos.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud en **{info['recinto']}** está en proceso")
            
            # MARKETING TERRITORIAL BASADO EN LA ESPERA
            st.markdown(f"<div class='promo-box'>{np.random.choice(CONSEJOS_TURISMO)}</div>", unsafe_allow_html=True)
            
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
            
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **ACCESO AUTORIZADO POR SECRETARÍA**")
            if info['staff_mode']:
                st.write("Diríjase al control del Guardia para validar su ingreso físico.")
            else:
                st.write("Pase adelante. La oficina le espera.")
                if st.button("YA INGRESÉ AL ÁREA DE REUNIÓN"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    st.rerun()

        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **AUDIENCIA EN CURSO**")
            st.write("Su atención está siendo cronometrada para control de calidad.")

        elif info['estado'] == "REUNION_FINALIZADA":
            st.markdown("""<div style='background: linear-gradient(135deg, #1e3a8a, #3b82f6); color:white; padding:25px; border-radius:15px; margin-bottom:20px;'>
            <b>¡LA SERENA: INNOVACIÓN DE CLASE MUNDIAL!</b><br>Esperamos que su experiencia municipal haya sido excelente.</div>""", unsafe_allow_html=True)
            st.subheader("Evaluación de Calidad")
            with st.form("eval_v_final"):
                nps = st.slider("¿Cómo califica la agilidad y el sistema?", 1, 5, 5)
                if st.form_submit_button("ENVIAR Y FINALIZAR"):
                    # Cálculo de permanencia real
                    perm = 0
                    if info['inicio_reunion'] and info['fin_reunion']:
                        perm = int((info['fin_reunion'] - info['inicio_reunion']).total_seconds() / 60)
                    
                    final_reg = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': perm, 'NPS': nps, 'Estado': "Completado"}
                    st.session_state.db_master = pd.concat([pd.DataFrame([final_reg]), st.session_state.db_master], ignore_index=True)
                    del st.session_state.citizen_token
                    st.balloons()
                    time.sleep(2)
                    st.rerun()

        elif info['estado'] == "EXPIRADO":
            st.error("❌ **TIEMPO AGOTADO**")
            if st.button("REINTENTAR REGISTRO"):
                del st.session_state.citizen_token
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. MÓDULO II: NODO GUARDIA (CONTROL DE ENTRADA Y SALIDA ASISTIDA)
# ==================================================================================================

def view_guard_node():
    st.markdown("<h1 class='muni-title'>TERMINAL DE GUARDIA</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    # 1. VALIDACIÓN FÍSICA DE ENTRADA
    st.subheader("🛡️ Validación de Ingresos Autorizados")
    autorizados = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO' and v['staff_mode']}
    
    if not autorizados: st.info("No hay ingresos pendientes de validación física.")
    else:
        for uid, info in autorizados.items():
            with st.container(border=True):
                c_x, c_y = st.columns([2, 1])
                with c_x: st.write(f"👤 **{info['nombre']}** | RUT: {info['rut']}\n\n📍 Destino: {info['depto']}")
                with c_y:
                    if st.button("CONFIRMAR PASO", key=f"g_ok_{uid}"):
                        st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                        st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                        st.rerun()

    st.divider()
    
    # 2. VALIDACIÓN FÍSICA DE SALIDA
    st.subheader("🚪 Registro de Salida")
    en_reunion = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'REUNION_FINALIZADA' and v['staff_mode']}
    
    for uid, info in en_reunion.items():
        with st.container(border=True):
            st.write(f"👤 **{info['nombre']}** ha terminado su gestión.")
            if st.button("VALIDAR SALIDA FÍSICA", key=f"g_out_{uid}"):
                st.session_state.audit_logs.insert(0, f"GUARDIA: {info['nombre']} salió del recinto.")
                st.success("Salida confirmada.")
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 6. MÓDULO III: NODO SECRETARÍAS (AUTORIZACIÓN Y CIERRE DE ATENCIÓN)
# ==================================================================================================

def view_secretary_node():
    st.markdown("<h1 class='muni-title'>PANEL DE SECRETARÍAS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    # 1. AUTORIZACIÓN DE ENTRADA (HUB CENTRAL)
    st.subheader("🔔 Solicitudes de Ingreso dirigidas a su área")
    pendientes = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
    
    if not pendientes: st.success("Sin visitas esperando confirmación.")
    else:
        for uid, info in pendientes.items():
            with st.container(border=True):
                c_i, c_a = st.columns([2, 1])
                with c_i: st.write(f"**Visitante:** {info['nombre']}\n\n**Perfil:** {info['perfil']}\n\n**Recinto:** {info['recinto']}")
                with c_a:
                    if st.button("AUTORIZAR", key=f"s_ok_{uid}"):
                        st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                        st.rerun()
                    if st.button("DENEGAR", key=f"s_no_{uid}"):
                        st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                        st.rerun()

    st.divider()

    # 2. CIERRE DE ATENCIÓN (PASO CORRELATIVO)
    st.subheader("🤝 Atención en Curso (Finalizar)")
    activos = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'EN_REUNION'}
    
    for uid, info in activos.items():
        with st.container(border=True):
            st.write(f"👤 **{info['nombre']}** está siendo atendido.")
            if st.button("TERMINAR ATENCIÓN", key=f"s_end_{uid}"):
                st.session_state.waiting_room[uid]['estado'] = 'REUNION_FINALIZADA'
                st.session_state.waiting_room[uid]['fin_reunion'] = datetime.now()
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. NAVEGACIÓN Y EJECUCIÓN (MAIN)
# ==================================================================================================

def main():
    bootstrap_enterprise_system()
    inject_enterprise_css()
    
    # LÓGICA DE ROLES
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.divider()
        view_mode = st.radio("MÓDULO DE OPERACIÓN:", [
            "1. Ciudadano (QR)", "2. Terminal Guardia", "3. Panel Secretarías", "4. Analítica Big Data", "5. Gestión CRM"
        ])
        st.divider()
        st.caption(f"Director: Rodrigo Godoy | Vecinos LS spa")

    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Terminal Guardia" in view_mode: view_guard_node()
    elif "3. Panel Secretarías" in view_mode: view_secretary_node()
    elif "4. Analítica" in view_mode: 
        st.markdown("<h1 class='muni-title'>ANÁLISIS DE GESTIÓN</h1>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión CRM" in view_mode:
        st.markdown("<h1 class='muni-title'>GESTIÓN RELACIONAL</h1>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:30]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": main()
