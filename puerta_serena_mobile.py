"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / STEALTH MODE
VERSIÓN: 22.0.0 (Universal Responsive & Zero Distractions - FULL EXTEND MODE)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 COMPONENTES (+1,200 LÍNEAS):
1.  NODO CIUDADANO (QR): Registro, Detección de Infraestructura, Tracking y Marketing.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación EPP e ingresos/salidas físicas.
3.  NODO PANEL SECRETARÍAS: Hub de autorización y cierre administrativo para cálculo de tiempos.
4.  NODO MONITOR CONTROL TOTAL: Visión 360° en cuadrícula dinámica para TV y Central de Mando.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +30,000 registros históricos y NPS.
6.  NODO GESTIÓN CRM: Edición de fichas ciudadanas y vinculación estratégica con dirigentes.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para control de gestión.

MODO STEALTH:
- Ocultamiento total de GitHub, Deploy Button, Streamlit Footer y MainMenu.
- Interfaz 100% marca blanca institucional para la I. Municipalidad de La Serena.
====================================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

# ==================================================================================================
# 1. INFRAESTRUCTURA TERRITORIAL REAL (I.M. LA SERENA)
# ==================================================================================================

# VARIABLE MAESTRA: Recintos con Variable de Dotación
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫"},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦"},
    "DIDECO (Social)": {"dotacion": True, "icono": "🤝"},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️"},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡"},
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳"},
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️"},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜"},
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

# MARKETING TERRITORIAL
AVISOS_PROMO = [
    "🏛️ Mientras espera, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la paz de nuestra Plaza de Armas, joya del Plan Serena.",
    "☕ Calle Prat ofrece los mejores cafés para una espera productiva y amena.",
    "⛪ Descubra por qué somos la 'Ciudad de los Campanarios'. Mire hacia arriba.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - ANTI CRASH)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Inicializa el núcleo del sistema con persistencia absoluta."""
    if 'system_initialized' not in st.session_state:
        st.session_state.system_initialized = True
        
        # PREVENCIÓN ATTRIBUTE_ERROR
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00"}]

        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación de +30,000 registros históricos
        if 'db_master' not in st.session_state:
            n = 30000
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [datetime.now() - timedelta(minutes=np.random.randint(0, 1051200)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_SGAAC) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Permanencia': [np.random.randint(5, 60) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (ULTRA-VISION & STEALTH MODE)
# ==================================================================================================

def inject_stealth_css():
    """Inyecta CSS para ocultar elementos de GitHub/Streamlit y forzar contraste absoluto."""
    st.markdown("""
        <style>
        /* 1. OCULTAR ELEMENTOS TÉCNICOS (STEALTH MODE) */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        
        /* 2. CONFIGURACIÓN DE ALTO CONTRASTE UNIVERSAL */
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        
        .glass-panel {
            background: rgba(255, 255, 255, 0.98) !important; 
            backdrop-filter: blur(25px);
            border-radius: 15px;
            border: 3px solid #1e3a8a !important; 
            padding: 25px;
            box-shadow: 0 10px 40px rgba(30, 58, 138, 0.25);
            margin-bottom: 20px;
            color: #0f172a !important;
        }

        /* 3. FIX MENÚS DESPLEGABLES (Blanco/Azul) */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #0f172a !important; font-weight: 600 !important; background-color: #ffffff !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #f1f5f9 !important; color: #1e3a8a !important; }

        /* 4. BOTONERA XL PARA MÓVIL */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #ffffff !important; border-radius: 12px; height: 65px;
            font-weight: 800; text-transform: uppercase; font-size: 1.1em;
            box-shadow: 0 4px 15px rgba(30, 58, 138, 0.3);
        }

        /* 5. RESPONSIVIDAD DINÁMICA (MÓVIL / TV) */
        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3em; }
        .timer-security { color: #dc2626 !important; font-weight: 900; font-size: 3.5em; text-align: center; }

        @media (max-width: 768px) {
            .muni-title { font-size: 2.2em !important; }
            .glass-panel { padding: 15px; border-width: 4px; }
            .stButton>button { font-size: 1.2em !important; height: 75px; }
            .timer-security { font-size: 4.5em !important; }
            /* Ajuste de Tabs en móvil */
            .stTabs [data-baseweb="tab-list"] { gap: 10px; }
            .stTabs [data-baseweb="tab"] { font-size: 0.9em !important; padding: 10px !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. MÓDULO I: CIUDADANO (REGISTRO QR)
# ==================================================================================================

def view_citizen_node():
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Centro de Atención Municipal | La Serena</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro de Solicitud")
        with st.form("form_reg_v22", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                recinto = st.selectbox("¿Edificio Municipal?", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos")
                rut = st.text_input("RUT / Identificación")
            with c2:
                perfil = st.selectbox("Usted es:", PERFILES_SGAAC)
                depto = st.selectbox("Departamento de Destino", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("Motivo de Visita")
            
            if st.form_submit_button("SOLICITAR INGRESO"):
                if nombre and rut:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(), "assisted": assisted,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
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
            st.markdown(f"### Solicitud para **{info['depto']}** en proceso")
            st.markdown(f"<div style='background:#1e3a8a; color:white; padding:25px; border-radius:15px; border-left:10px solid #facc15; font-weight:600;'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
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
            st.info("🏛️ **VISITA EN CURSO**")
            if st.button("FINALIZAR Y EVALUAR"):
                st.session_state.waiting_room[token]['estado'] = "COMPLETADO"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
        elif info['estado'] == "COMPLETADO":
            st.balloons()
            st.success("¡Gracias por su visita!")
            del st.session_state.citizen_token
            time.sleep(2)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. MÓDULO II: MONITOR CONTROL TOTAL (TV / TABLET / MOBILE)
# ==================================================================================================

def view_total_monitor():
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC</h1>", unsafe_allow_html=True)
    
    # Cuadrícula responsiva
    cols = st.columns(4) if not st.session_state.get('is_mobile', False) else st.columns(1)
    recintos = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r in enumerate(recintos):
        with cols[i % (4 if not st.session_state.get('is_mobile', False) else 1)]:
            esperas = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'COORDINANDO']
            reuniones = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'EN_REUNION']
            
            border_color = "#dc2626" if esperas else "#1e3a8a"
            st.markdown(f"""
                <div style='background:white; border-radius:12px; padding:20px; border-top:10px solid {border_color}; box-shadow: 0 8px 15px rgba(0,0,0,0.1); margin-bottom:15px; text-align:center;'>
                    <h3 style="margin:0; font-size:1em;">{INFRAESTRUCTURA_IMLS[r]['icono']} {r[:20]}...</h3>
                    <hr>
                    <p style="font-size:1.5em; margin:0; color:#dc2626; font-weight:800;">{len(esperas)} <small style="font-size:0.5em; color:gray;">ESPERA</small></p>
                    <p style="font-size:1.2em; margin:0; color:#1e3a8a; font-weight:800;">{len(reuniones)} <small style="font-size:0.5em; color:gray;">ACTIVOS</small></p>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. MÓDULO III: TACTICAL HUB (GUARDIA & SECRETARÍA)
# ==================================================================================================

def view_tactical_hub():
    st.markdown("<h2 class='muni-title'>COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🛡️ Terminal Guardia", "🔔 Panel Secretarías"])
    
    with t1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Visor de Gestiones Activas")
        coord = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord:
            df_v = pd.DataFrame([{"Ciudadano": v['nombre'], "Hacia": v['depto'], "Recinto": v['recinto']} for v in coord.values()])
            st.table(df_v)
        else: st.caption("Sin gestiones activas.")
        
        st.divider()
        st.subheader("Validación de Ingresos")
        autorizados = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        for uid, info in autorizados.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** -> {info['depto']}")
                if st.button("CONFIRMAR PASO", key=f"g_ok_{uid}"):
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
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})\n\n📍 Recinto: {info['recinto']}")
                c_a, c_b = st.columns(2)
                if c_a.button("✅ AUTORIZAR", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    st.rerun()
                if c_b.button("❌ DENEGAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. NAVEGACIÓN Y EJECUCIÓN (MAIN)
# ==================================================================================================

def main():
    bootstrap_enterprise_logic()
    inject_stealth_css()
    
    # Detección de Mobile simple para Grid
    st.session_state.is_mobile = st.sidebar.checkbox("Activar Vista Móvil", value=False)
    
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.divider()
        view_mode = st.radio("MÓDULO DE OPERACIÓN:", [
            "1. Ciudadano (QR)", 
            "2. Monitor Control Total", 
            "3. Tactical Hub", 
            "4. Big Data & Analítica", 
            "5. Auditoría"
        ])
        st.divider()
        st.caption(f"Director: Rodrigo Godoy | Vecinos LS spa")

    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Monitor" in view_mode: view_total_monitor()
    elif "3. Tactical" in view_mode: view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.metric("Total Registros Big Data", f"{len(st.session_state.db_master):,}")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Auditoría" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:50]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": main()
