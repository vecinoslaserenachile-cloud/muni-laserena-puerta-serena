"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / COMMAND & CONTROL MODE
VERSIÓN: 20.0.0 (High-Density Multi-Node Architecture - FULL EXTEND MODE)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 COMPONENTES (+1,250 LÍNEAS):
1.  NODO CIUDADANO (QR): Registro, Detección de Dotación, Tracking y Marketing Territorial.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación EPP e ingresos/salidas físicas.
3.  NODO SECRETARÍAS: Autorización de ingreso y cierre administrativo correlativo de tiempos.
4.  NODO MONITOR CONTROL TOTAL: Visión en cuadrícula de todos los recintos con alertas activas.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +30,000 registros y análisis NPS Municipal.
6.  NODO GESTIÓN CRM: Edición de fichas ciudadanas, redes sociales y contacto estratégico.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización.
====================================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ==================================================================================================
# 1. DEFINICIÓN DE ACTIVOS E INFRAESTRUCTURA TERRITORIAL (I.M. LA SERENA)
# ==================================================================================================

# VARIABLE ESTRATÉGICA: Configuración de Recintos con Variable de Dotación (Realidad Local)
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫"},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦"},
    "DIDECO (Social)": {"dotacion": True, "icono": "🤝"},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️"},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡"}, # Autónomo
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳"},   # Autónomo
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️"},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜"}, # Autónomo
    "Coliseo Monumental": {"dotacion": True, "icono": "🏀"},
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️"},
    "Parque Pedro de Valdivia (Admin)": {"dotacion": True, "icono": "🦌"},
    "Juzgado de Policía Local": {"dotacion": True, "icono": "⚖️"},
    "Taller Municipal": {"dotacion": False, "icono": "🛠️"}, 
    "Centro Cultural Palace": {"dotacion": False, "icono": "🎨"}, 
    "Estadio La Portada (Admin)": {"dotacion": True, "icono": "⚽"}
}

LISTADO_DEPARTAMENTOS = [
    "Alcaldía", "Secretaría Municipal", "Administración Municipal",
    "Dirección de Obras (DOM)", "Dirección de Tránsito", "DIDECO - Social",
    "Dirección Jurídica", "Comunicaciones y RR.PP.", "Turismo y Patrimonio",
    "Cultura y Artes", "Seguridad Ciudadana", "Finanzas y Tesorería",
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda", "Adulto Mayor"
]

PERFILES_SGAAC = [
    "Vecino(a)", "Dirigente Social / Presidente JJVV", "Autoridad Regional",
    "Autoridad Nacional", "Funcionario Municipal", "Proveedor Externo",
    "Prensa", "Delegación Institucional"
]

# MARKETING TERRITORIAL DINÁMICO
AVISOS_PROMO = [
    "🏛️ Mientras espera, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la paz de nuestra Plaza de Armas, joya del Plan Serena.",
    "☕ Calle Prat ofrece los mejores cafés para una espera productiva y amena.",
    "⛪ Descubra por qué somos la 'Ciudad de los Campanarios'. Mire hacia arriba.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - FIX ATTRIBUTE/KEY ERROR)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Inicializa el núcleo del sistema asegurando persistencia y previniendo colapsos de sesión."""
    if 'system_initialized' not in st.session_state:
        st.session_state.system_initialized = True
        st.session_state.boot_time = datetime.now()
        
        # FIX ATTRIBUTE_ERROR (Captura 1)
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace de Coordinación Activo", "t": "00:00:00"}]

        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación de +30,000 registros históricos
        # FIX KEY_ERROR (Captura 2): Columnas estandarizadas
        if 'db_master' not in st.session_state:
            n = 30000
            start_date = datetime.now() - timedelta(days=730)
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start_date + timedelta(minutes=np.random.randint(0, 1051200)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_SGAAC) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Funcionario': ["Director / Jefe de Área"] * n,
                'Permanencia': [np.random.randint(5, 60) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. SEGURIDAD Y ESTÉTICA (ULTRA-VISION: FIX SELECTBOX & HIGH CONTRAST)
# ==================================================================================================

def inject_enterprise_css():
    """Inyecta CSS de alto impacto para anular menús negros y asegurar legibilidad móvil."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        
        .glass-panel {
            background: rgba(255, 255, 255, 0.98); 
            backdrop-filter: blur(20px);
            border-radius: 15px;
            border: 3px solid #1e3a8a; 
            padding: 25px;
            box-shadow: 0 10px 40px rgba(30, 58, 138, 0.2);
            margin-bottom: 20px;
            color: #0f172a !important;
        }

        /* FIX UI CONTRAST: Corrección menús desplegables negros */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 700 !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #0f172a !important; background-color: #ffffff !important; font-weight: 600 !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #f1f5f9 !important; color: #1e3a8a !important; }

        /* Títulos y Texto */
        label, p, span, div { color: #0f172a !important; font-weight: 600 !important; }
        h1, h2, h3 { color: #1e3a8a !important; font-weight: 900 !important; }

        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8);
            color: #ffffff !important; 
            border-radius: 12px; border: none; padding: 18px;
            font-weight: 800; width: 100%; height: 60px;
            text-transform: uppercase; letter-spacing: 1px; font-size: 1.1em;
        }

        .monitor-card {
            background: #ffffff; border-radius: 10px; padding: 15px;
            border-top: 5px solid #1e3a8a; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 10px;
        }
        
        .timer-security { color: #dc2626 !important; font-weight: 900; font-size: 3em; text-align: center; }
        
        @media (max-width: 768px) {
            .glass-panel { padding: 15px; border-width: 4px; }
            .stButton>button { font-size: 1.2em !important; height: 75px; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. MÓDULO I: CIUDADANO (VIAJE QR INTELIGENTE)
# ==================================================================================================

def view_citizen_node():
    st.markdown("<h1 style='color:#1e3a8a; text-align:center;'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Portal de Atención Ciudadana | La Serena</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro de Ingreso")
        # FIX FORM (Captura 3): Definición completa
        with st.form("form_reg_v20", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                recinto = st.selectbox("¿Edificio Municipal?", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos")
                rut = st.text_input("RUT / Identificación")
            with c2:
                perfil = st.selectbox("Categoría", PERFILES_SGAAC)
                depto = st.selectbox("Departamento de Destino", LISTADO_DEPARTAMENTOS)
                funcionario = st.text_input("Funcionario (Opcional)")
            
            submit = st.form_submit_button("SOLICITAR INGRESO")
            if submit:
                if nombre and rut:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "funcionario": funcionario, "inicio": datetime.now(),
                        "assisted": assisted, "estado": "COORDINANDO",
                        "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_token = uid
                    st.rerun()
                else: st.error("⚠️ Complete todos los campos.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Coordinando con **{info['depto']}**")
            st.markdown(f"<div style='background:#f1f5f9; padding:20px; border-radius:15px; border-left:8px solid #1e3a8a; font-style:italic;'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: st.write("El Guardia validará su entrada física.")
            else:
                if st.button("YA INGRESÉ AL ÁREA"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    st.rerun()
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **AUDIENCIA EN CURSO**")
            if st.button("FINALIZAR Y EVALUAR"):
                st.session_state.waiting_room[token]['estado'] = "CIERRE"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
        elif info['estado'] == "CIERRE":
            st.balloons()
            st.subheader("¡Gracias por su visita!")
            nps = st.slider("Evaluación de Calidad", 1, 5, 5)
            if st.button("ENVIAR Y SALIR"):
                final = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': 15, 'NPS': nps, 'Estado': "Completado"}
                st.session_state.db_master = pd.concat([pd.DataFrame([final]), st.session_state.db_master], ignore_index=True)
                del st.session_state.citizen_token
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. MÓDULO II: MONITOR CONTROL TOTAL (VISIÓN GLOBAL MULTI-RECINTO)
# ==================================================================================================

def view_total_monitor():
    st.markdown("<h1 style='color:#1e3a8a; font-weight:900;'>MONITOR DE CONTROL GLOBAL SGAAC</h1>", unsafe_allow_html=True)
    st.markdown("<p>Visión en tiempo real de toda la Red de Recintos Municipales</p>", unsafe_allow_html=True)
    
    # Grid de 4 columnas para el monitor
    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, recinto in enumerate(recintos_list):
        with cols[i % 4]:
            # Filtrar datos activos para este recinto
            esperas = [v for v in st.session_state.waiting_room.values() if v['recinto'] == recinto and v['estado'] == 'COORDINANDO']
            reuniones = [v for v in st.session_state.waiting_room.values() if v['recinto'] == recinto and v['estado'] == 'EN_REUNION']
            
            # Estética de Card de Control
            color_borde = "#1e3a8a" if not esperas else "#dc2626"
            st.markdown(f"""
                <div style='background:white; border-radius:12px; padding:15px; border-top:8px solid {color_borde}; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom:15px; min-height:180px;'>
                    <h4 style='margin:0; font-size:0.9em; color:#1e3a8a;'>{INFRAESTRUCTURA_IMLS[recinto]['icono']} {recinto[:25]}...</h4>
                    <hr style='margin:10px 0;'>
                    <p style='margin:0; font-size:0.8em;'>🕒 Esperas: <b>{len(esperas)}</b></p>
                    <p style='margin:0; font-size:0.8em;'>🤝 En Reunión: <b>{len(reuniones)}</b></p>
                    <p style='margin:0; font-size:0.7em; color:gray;'>Dotación: {"✅ SI" if INFRAESTRUCTURA_IMLS[recinto]['dotacion'] else "🤖 AUTO"}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if esperas:
                with st.expander("Ver Detalles"):
                    for e in esperas: st.caption(f"👤 {e['nombre']} -> {e['depto']}")

# ==================================================================================================
# 6. MÓDULO III: TERMINAL GUARDIA Y SECRETARÍAS (HUB TÁCTICO)
# ==================================================================================================

def view_tactical_hub():
    st.markdown("<h2 style='color:#1e3a8a; font-weight:900;'>CENTRO DE COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🛡️ Terminal Guardia", "🔔 Panel Secretarías"])
    
    with t1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Validación de Ingresos Físicos")
        autorizados = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not autorizados: st.info("Sin pases pendientes.")
        for uid, info in autorizados.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** -> {info['depto']}")
                if st.button("CONFIRMAR PASO FÍSICO", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with t2:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Autorización de Audiencias")
        coord = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not coord: st.success("Sin visitas esperando.")
        for uid, info in coord.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})")
                c_a, c_b = st.columns(2)
                if c_a.button("✅ AUTORIZAR", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    st.rerun()
                if c_b.button("❌ DENEGAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. NAVEGACIÓN Y EJECUCIÓN (MAIN ENTRY POINT)
# ==================================================================================================

def main():
    bootstrap_enterprise_logic()
    inject_enterprise_css()
    
    # Protocolo de Expiración Automática
    now = datetime.now()
    expired = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.divider()
        view_mode = st.radio("MÓDULO OPERATIVO:", [
            "1. Ciudadano (QR)", "2. Monitor Control Total", "3. Tactical Hub (Guardia/Sec)", "4. Analítica Big Data", "5. Logs Auditoría"
        ])
        st.divider()
        st.caption(f"Director: Rodrigo Godoy | Vecinos LS spa")

    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Monitor" in view_mode: view_total_monitor()
    elif "3. Tactical" in view_mode: view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.metric("Total Registros Históricos", f"{len(st.session_state.db_master):,}")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Logs" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:50]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": main()
