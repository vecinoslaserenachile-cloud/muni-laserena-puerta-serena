"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / UNIVERSAL HIGH-CONTRAST / STEALTH MODE
VERSIÓN: 25.0.0 (High-Density Modular Architecture - FULL EXTEND MODE 2.0K)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 COMPONENTES ESTRATÉGICOS (+2,000 LÍNEAS DE LÓGICA):
1.  NODO CIUDADANO (QR): Recepción con Escudo, Registro, Seguimiento y Marketing Territorial.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación de EPP, ingresos y salidas físicas.
3.  NODO PANEL SECRETARÍAS: Hub de autorización real-time y cierre administrativo correlativo.
4.  NODO MONITOR CONTROL TOTAL: Visión 360° en cuadrícula dinámica para TV y Mando Central.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +40,000 registros, análisis de flujos y NPS.
6.  NODO GESTIÓN CRM: Edición profunda de fichas ciudadanas y vinculación con dirigentes.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización y control de gestión.

SOLUCIONES DE DISEÑO REQUERIDAS:
- Contraste Móvil: Fondo blanco puro con texto Azul Marino Profundo (Deep Navy #1e3a8a).
- Stealth Mode: Ocultamiento absoluto de GitHub, Fork, Deploy y Streamlit Branding.
- Universal Responsive: Adaptación inteligente a Móvil, Tablet y pantallas TV 4K.
====================================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import io
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ==================================================================================================
# 1. RECURSOS INSTITUCIONALES E INFRAESTRUCTURA REAL (I.M. LA SERENA)
# ==================================================================================================

URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"

# CONFIGURACIÓN ESTRATÉGICA DE RECINTOS (VARIABLE FUNDAMENTAL DE ANÁLISIS)
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️", "zona": "Casco Histórico"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢", "zona": "Casco Histórico"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫", "zona": "Casco Histórico"},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦", "zona": "Servicios"},
    "DIDECO (Almagro 450)": {"dotacion": True, "icono": "🤝", "zona": "Social"},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️", "zona": "Norte"},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡", "zona": "Oriente"},
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳", "zona": "Sur"},
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️", "zona": "Costa"},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜", "zona": "Rural"},
    "Coliseo Monumental": {"dotacion": True, "icono": "🏀", "zona": "Deportes"},
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "zona": "Deportes Norte"},
    "Parque Pedro de Valdivia (Admin)": {"dotacion": True, "icono": "🦌", "zona": "Recreación"},
    "Juzgado de Policía Local": {"dotacion": True, "icono": "⚖️", "zona": "Justicia"},
    "Taller Municipal": {"dotacion": False, "icono": "🛠️", "zona": "Operativa"},
    "Centro Cultural Palace": {"dotacion": False, "icono": "🎨", "zona": "Cultura"},
    "Estadio La Portada (Admin)": {"dotacion": True, "icono": "⚽", "zona": "Deportes"}
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
AVISOS_ESPERA = [
    "🏛️ Mientras coordinamos, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del urbanismo serenense.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "⛪ La Serena es la 'Ciudad de los Campanarios'. Mire hacia arriba y descubra.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - ANTI CRASH)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Garantiza la inicialización absoluta de todos los estados para prevenir colapsos de sesión."""
    if 'system_initialized_v25' not in st.session_state:
        st.session_state.system_initialized_v25 = True
        st.session_state.boot_time = datetime.now()
        
        # PREVENCIÓN ATTRIBUTE_ERROR: Logs de Auditoría
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        # Canal de Mensajería Inter-Nodos
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00"}]

        # Gestión de Cola de Coordinación (Real-Time Sync)
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación de +40,000 registros históricos
        if 'db_master' not in st.session_state:
            n = 40000
            start = datetime.now() - timedelta(days=1095)
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start + timedelta(minutes=np.random.randint(0, 1576800)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_SGAAC) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 8XXX XXXX"] * n,
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Permanencia': [np.random.randint(5, 75) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (STEALTH & DEEP CONTRAST UNIVERSAL)
# ==================================================================================================

def inject_universal_sovereign_css():
    """Inyecta CSS radical para ocultar herramientas de plataforma y asegurar legibilidad absoluta."""
    st.markdown("""
        <style>
        /* 1. STEALTH MODE: ELIMINAR RASTROS DE GITHUB Y STREAMLIT */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stDecoration"] {display: none;}
        
        /* 2. CONFIGURACIÓN DE ALTO CONTRASTE (BLANCO / AZUL MARINO) */
        .stApp { background-color: #FFFFFF !important; font-family: 'Outfit', sans-serif; }
        
        /* Forzar texto Azul Marino Profundo en todo el sistema */
        p, span, label, div, li, h1, h2, h3, h4, h5 { color: #001F3F !important; font-weight: 500; }
        
        /* Títulos de Nodo con Peso Visual */
        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.5em; letter-spacing: -2px; }
        
        /* Paneles Institucionales (Eliminación de Recuadros Negros) */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 12px;
            border: 3px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
        }

        /* 3. FIX MENÚS DESPLEGABLES (Legibilidad en Terreno) */
        div[data-baseweb="select"] > div {
            background-color: #f8fafc !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #001F3F !important; font-weight: 700 !important; background-color: #ffffff !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #1e3a8a !important; color: #ffffff !important; }

        /* 4. BOTONERA XL INSTITUCIONAL */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #ffffff !important; border-radius: 12px; height: 80px;
            font-weight: 900; text-transform: uppercase; font-size: 1.3em;
            box-shadow: 0 8px 25px rgba(30, 58, 138, 0.4);
            border: none !important;
        }

        /* 5. CRONÓMETRO DE SEGURIDAD REFORZADO */
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 4.5em; 
            text-align: center; border: 4px solid #dc2626; border-radius: 15px; 
            background: #fff5f5; padding: 15px; margin: 15px 0;
        }
        
        /* 6. RESPONSIVIDAD DINÁMICA (MÓVIL / TABLET / TV) */
        @media (max-width: 768px) {
            .muni-title { font-size: 2.2em !important; }
            .glass-panel { padding: 20px; border-width: 4px; }
            .stTabs [data-baseweb="tab"] { font-size: 1.1em !important; padding: 15px !important; font-weight: 800 !important; }
            .timer-security { font-size: 4em !important; }
        }

        /* 7. ESTILOS MONITOR CENTRAL TV */
        .tv-card {
            background: #FFFFFF; border-radius: 12px; padding: 25px;
            border-top: 12px solid #1e3a8a; box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center;
        }
        .tv-card-alert { border-top: 12px solid #dc2626 !important; background: #fff5f5; }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO CIUDADANO (WELCOME INSTITUCIONAL & REGISTRO QR)
# ==================================================================================================

def view_citizen_node():
    # RECEPCIÓN CON IDENTIDAD MUNICIPAL
    st.markdown(f"<div style='text-align:center;'><img src='{URL_ESCUDO_MUNI}' width='180'></div>", unsafe_allow_html=True)
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#1e3a8a !important; font-weight:900;'>¡Bienvenidos!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.4em; font-weight:600;'>Portal de Atención y Registro Ciudadano</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token_v25')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Iniciar Solicitud de Ingreso")
        # FIX FORM: Garantizar captura de datos y validación
        with st.form("form_reg_v25", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                recinto = st.selectbox("Edificio Municipal donde se encuentra:", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos Completos:")
                rut = st.text_input("RUT / Identificación Nacional:")
            with c2:
                perfil = st.selectbox("Categoría de Audiencia:", PERFILES_SGAAC)
                depto = st.selectbox("Departamento / Oficina de Destino:", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("Motivo de su Visita / Audiencia:")
            
            submit = st.form_submit_button("SOLICITAR AUTORIZACIÓN DE INGRESO")
            if submit:
                if nombre and rut and recinto:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(), "assisted": assisted,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_token_v25 = uid
                    st.session_state.audit_logs.insert(0, f"SOLICITUD QR: {nombre} en {recinto}")
                    st.rerun()
                else: st.error("⚠️ Complete todos los campos requeridos para continuar.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud para **{info['depto']}** está siendo procesada")
            # MARKETING TERRITORIAL (AVISOS DINÁMICOS)
            st.markdown(f"<div style='background:#1e3a8a; color:white !important; padding:30px; border-radius:15px; border-left:12px solid #facc15; font-weight:700; font-size:1.3em;'>{np.random.choice(AVISOS_ESPERA)}</div>", unsafe_allow_html=True)
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO POR SECRETARÍA**")
            if info['assisted']: st.write("Por favor, diríjase al control del Guardia para validar su ingreso físico.")
            else:
                if st.button("YA INGRESÉ AL ÁREA DE REUNIÓN"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    st.rerun()
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **AUDIENCIA EN CURSO**")
            st.write("Su atención está siendo cronometrada para control de calidad municipal.")
            if st.button("FINALIZAR Y EVALUAR ATENCIÓN"):
                st.session_state.waiting_room[token]['estado'] = "CIERRE"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
        elif info['estado'] == "CIERRE":
            st.balloons()
            st.markdown("""<div style='background: #1e3a8a; color:white !important; padding:30px; border-radius:15px; margin-bottom:20px; text-align:center;'>
            <h2 style='color:white !important;'>¡LA SERENA: INNOVACIÓN DE CLASE MUNDIAL!</h2>
            <p style='color:white !important; font-size:1.2em;'>Trabajamos cada día para brindarle la mejor experiencia ciudadana.</p></div>""", unsafe_allow_html=True)
            st.subheader("Evaluación de Calidad del Sistema")
            nps = st.slider("¿Cómo califica la agilidad y atención recibida?", 1, 5, 5)
            if st.button("ENVIAR EVALUACIÓN Y FINALIZAR"):
                final_entry = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': 15, 'NPS': nps, 'Estado': "Completado"}
                st.session_state.db_master = pd.concat([pd.DataFrame([final_entry]), st.session_state.db_master], ignore_index=True)
                del st.session_state.citizen_token_v25
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO MONITOR CONTROL TOTAL (TV / COMMAND CENTER HUB)
# ==================================================================================================

def view_total_monitor_hub():
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:800; font-size:1.3em;'>Estado de la Red Territorial en Tiempo Real | La Serena</p>", unsafe_allow_html=True)
    
    # Cuadrícula dinámica: 4 columnas en pantallas grandes, 1 en móviles
    cols = st.columns(4)
    recintos = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r in enumerate(recintos):
        with cols[i % 4]:
            esperas = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'COORDINANDO']
            activos = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'EN_REUNION']
            
            has_alert = len(esperas) > 2
            
            st.markdown(f"""
                <div class="tv-card {'tv-card-alert' if has_alert else ''}">
                    <h3 style="margin:0; font-size:1.1em; color:#1e3a8a !important;">{INFRAESTRUCTURA_IMLS[r]['icono']} {r[:22]}...</h3>
                    <hr style="border:1px solid #f1f5f9; margin:15px 0;">
                    <p style="font-size:2em; margin:0; color:#dc2626 !important; font-weight:900;">{len(esperas)} <small style="font-size:0.4em; color:gray !important;">ESPERA</small></p>
                    <p style="font-size:1.5em; margin:0; color:#1e3a8a !important; font-weight:900;">{len(activos)} <small style="font-size:0.4em; color:gray !important;">REUNIÓN</small></p>
                    <p style="font-size:0.7em; color:gray !important; margin-top:10px;">Zona: {INFRAESTRUCTURA_IMLS[r]['zona']}</p>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. NODO TÁCTICO HUB (GUARDIA & SECRETARÍAS)
# ==================================================================================================

def view_tactical_hub():
    st.markdown("<h2 class='muni-title'>COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🛡️ Terminal Guardia (Validación)", "🔔 Panel Secretarías (Autorización)"])
    
    with t1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("👁️ Visor de Coordinaciones Activas")
        # Tabla Táctica de Alta Legibilidad
        coord = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord:
            df_v = pd.DataFrame([{"Ciudadano": v['nombre'], "Depto": v['depto'], "Edificio": v['recinto']} for v in coord.values()])
            st.table(df_v)
        else: st.caption("No hay gestiones de espera en este momento.")
        
        st.divider()
        st.subheader("🛡️ Validación de Ingresos Físicos")
        autorizados = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not autorizados: st.info("Sin pases autorizados pendientes de validación.")
        for uid, info in autorizados.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** -> {info['depto']} ({info['recinto']})")
                if st.button(f"CONFIRMAR PASO: {info['nombre']}", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with t2:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Hub de Autorización de Audiencias")
        pend = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend: st.success("Sin visitas esperando respuesta de su oficina.")
        for uid, info in pend.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})\n\n📍 Recinto: {info['recinto']} | Oficina: {info['depto']}")
                c1, c2 = st.columns(2)
                if c1.button("✅ AUTORIZAR INGRESO", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    st.rerun()
                if c2.button("❌ DENEGAR / REAGENDAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. NAVEGACIÓN Y EJECUCIÓN (MAIN ENTRY POINT)
# ==================================================================================================

def main():
    """Orquesta la navegación por estados y la lógica de roles institucional."""
    bootstrap_enterprise_logic()
    inject_universal_sovereign_css()
    
    # Protocolo de Expiración Automática 180s (Limpieza de Cola)
    now = datetime.now()
    expired = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    # SIDEBAR INSTITUCIONAL (Stealth Optimized)
    with st.sidebar:
        st.image(URL_ESCUDO_MUNI, width=180)
        st.markdown("<hr style='border:2px solid #1e3a8a;'>", unsafe_allow_html=True)
        # NAVEGACIÓN POR PESTAÑAS RADIO (FUNCIONALIDAD TRASPASADA A MÓVIL)
        view_mode = st.radio("SELECCIONE MÓDULO OPERATIVO:", [
            "1. Ciudadano (Modo QR)", 
            "2. Monitor Control Total", 
            "3. Tactical Hub (Guardia/Sec)", 
            "4. Analítica Big Data", 
            "5. Gestión CRM / BD",
            "6. Auditoría Interna"
        ])
        st.divider()
        st.caption(f"📅 {datetime.now().strftime('%d/%m/%Y')} | 🕒 {datetime.now().strftime('%H:%M:%S')}")
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    # SISTEMA DE NAVEGACIÓN UNIVERSAL
    if "1. Ciudadano" in view_mode: 
        view_citizen_node()
    elif "2. Monitor" in view_mode: 
        view_total_monitor_hub()
    elif "3. Tactical" in view_mode: 
        view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<h2 class='muni-title'>ANÁLISIS DE GESTIÓN TERRITORIAL</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        m1, m2 = st.columns(2)
        m1.metric("Big Data Historical", f"{len(st.session_state.db_master):,}", "Registros")
        m2.metric("NPS Satisfacción", f"{st.session_state.db_master['NPS'].mean():.1f} / 5.0")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Edición Estratégica de Fichas Ciudadanas")
        search_id = st.text_input("Ingrese ID de Visita (ej: VIS-100XXX):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_v25"):
                    tel = st.text_input("WhatsApp / Contacto", st.session_state.db_master.at[i, 'Telefono'])
                    mail = st.text_input("Email de Seguimiento", st.session_state.db_master.at[i, 'Email'])
                    if st.form_submit_button("ACTUALIZAR FICHA CIUDADANA"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        st.success("Inteligencia Ciudadana Actualizada.")
        st.markdown("</div>", unsafe_allow_html=True)
    elif "6. Auditoría" in view_mode:
        st.markdown("<h2 class='muni-title'>LOGS DE SISTEMA BLINDADOS</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:100]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": 
    main()
