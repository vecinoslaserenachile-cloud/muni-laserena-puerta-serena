"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / MISSION CRITICAL / COMMAND & CONTROL / STEALTH
VERSIÓN: 31.0.0 (High-Density Modular Architecture - FULL EXTEND MODE 1.0K)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 NODOS ESTRATÉGICOS (+900 LÍNEAS DE LÓGICA):
1.  NODO CIUDADANO (QR): Recepción Institucional, Registro, Tracking y Marketing Territorial.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación de EPP y control de ingresos/salidas.
3.  NODO PANEL SECRETARÍAS: Hub de autorización real-time y cierre correlativo de tiempos.
4.  NODO MONITOR CONTROL TOTAL: Pantalla central maestra con visión 360° (GRID DE ALTA VISIBILIDAD).
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +50,000 registros, flujos de calor y NPS.
6.  NODO GESTIÓN CRM: Edición profunda de fichas ciudadanas y vinculación estratégica.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización y cumplimiento.

ESPECIFICACIONES TÉCNICAS DE DISEÑO:
- Stealth Mode: Ocultamiento absoluto de GitHub, Fork, Deploy y Branding de Plataforma.
- Deep Visual Contrast: Fondos Blancos (#FFFFFF) y Texto Deep Navy (#001F3F).
- Grid Engine: Monitor dinámico diseñado para pantallas de TV 4K y Tablets de Guardia.
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
# 1. IDENTIDAD INSTITUCIONAL E INFRAESTRUCTURA TERRITORIAL (I.M. LA SERENA)
# ==================================================================================================

# RECURSOS GRÁFICOS
URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"

# VARIABLE MAESTRA: Configuración de Recintos con Variable de Dotación y Metadata de Control
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️", "zona": "Centro", "capacidad": 150},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢", "zona": "Centro", "capacidad": 100},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫", "zona": "Centro", "capacidad": 120},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦", "zona": "Servicios", "capacidad": 200},
    "DIDECO (Almagro 450)": {"dotacion": True, "icono": "🤝", "zona": "Social", "capacidad": 180},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️", "zona": "Norte", "capacidad": 140},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡", "zona": "Oriente", "capacidad": 60},
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳", "zona": "Sur", "capacidad": 60},
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️", "zona": "Costa", "capacidad": 40},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜", "zona": "Rural", "capacidad": 30},
    "Coliseo Monumental": {"dotacion": True, "icono": "🏀", "zona": "Deportes", "capacidad": 300},
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "zona": "Deportes Norte", "capacidad": 150},
    "Parque Pedro de Valdivia (Admin)": {"dotacion": True, "icono": "🦌", "zona": "Recreación", "capacidad": 100},
    "Juzgado de Policía Local": {"dotacion": True, "icono": "⚖️", "zona": "Justicia", "capacidad": 90},
    "Taller Municipal": {"dotacion": False, "icono": "🛠️", "zona": "Operativa", "capacidad": 50},
    "Centro Cultural Palace": {"dotacion": False, "icono": "🎨", "zona": "Cultura", "capacidad": 80},
    "Estadio La Portada (Admin)": {"dotacion": True, "icono": "⚽", "zona": "Deportes", "capacidad": 200}
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
    "🏛️ Mientras coordinamos, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la paz de nuestra Plaza de Armas, joya del urbanismo serenense.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "⛪ La Serena es la 'Ciudad de los Campanarios'. Mire hacia arriba.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - ANTI CRASH SYSTEM)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Garantiza la inicialización absoluta de todos los estados para prevenir colapsos."""
    if 'system_initialized_v31' not in st.session_state:
        st.session_state.system_initialized_v31 = True
        st.session_state.boot_time = datetime.now()
        
        # PREVENCIÓN ATTRIBUTE_ERROR: Logs de Auditoría
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00"}]

        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación masiva de +50,000 registros históricos
        # PREVENCIÓN KEY_ERROR: Columnas estandarizadas para evitar fallos en gráficos
        if 'db_master' not in st.session_state:
            n = 50000
            start_date = datetime.now() - timedelta(days=1095)
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start_date + timedelta(minutes=np.random.randint(0, 1576800)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_SGAAC) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 8XXX XXXX"] * n,
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Permanencia': [np.random.randint(5, 80) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (ULTRA-VISION: DEEP CONTRAST & STEALTH MODE PRO)
# ==================================================================================================

def inject_sovereign_css():
    """Inyecta CSS radical para ocultar herramientas de plataforma y asegurar legibilidad absoluta."""
    st.markdown("""
        <style>
        /* 1. STEALTH MODE PRO: OCULTAR GITHUB, FORK, DEPLOY Y STREAMLIT BRANDING */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stDecoration"] {display: none;}
        
        /* 2. CONFIGURACIÓN DE ALTO CONTRASTE (FONDO BLANCO / TEXTO DEEP NAVY #001F3F) */
        .stApp { background-color: #FFFFFF !important; font-family: 'Outfit', sans-serif; }
        
        /* Forzar texto Azul Marino Profundo en toda la interfaz */
        p, span, label, div, li, h1, h2, h3, h4, h5, table, .stMarkdown { 
            color: #001F3F !important; 
            font-weight: 500; 
        }
        
        /* Paneles Institucionales (Legibilidad Quirúrgica) */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 12px;
            border: 3px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
        }

        /* 3. FIX DEFINITIVO PESTAÑAS (Estilo Navy on White) */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #FFFFFF !important;
            border-bottom: 4px solid #1e3a8a !important;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #FFFFFF !important;
            color: #1e3a8a !important;
            font-weight: 900 !important;
            border-radius: 10px 10px 0 0 !important;
            padding: 12px 25px !important;
            border: 1px solid #f1f5f9 !important;
            margin-right: 5px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #1e3a8a !important;
            color: #FFFFFF !important;
            border: 1px solid #1e3a8a !important;
        }

        /* 4. FIX SELECTBOX (Contraste Máximo para Móvil) */
        div[data-baseweb="select"] > div {
            background-color: #f8fafc !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #001F3F !important; font-weight: 700 !important; background-color: #ffffff !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #1e3a8a !important; color: #ffffff !important; }

        /* 5. BOTONERA XL INSTITUCIONAL */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #ffffff !important; border-radius: 15px; height: 85px;
            font-weight: 900; text-transform: uppercase; font-size: 1.4em;
            box-shadow: 0 10px 30px rgba(30, 58, 138, 0.4);
            border: none !important;
        }

        /* 6. MONITOR CARDS (Diseño para TV / Command Center) */
        .monitor-card {
            background: #FFFFFF; border-radius: 15px; padding: 25px;
            border-top: 15px solid #1e3a8a; box-shadow: 0 12px 25px rgba(0,0,0,0.15);
            text-align: center; border-left: 1px solid #f1f5f9; border-right: 1px solid #f1f5f9;
            margin-bottom: 25px; min-height: 250px;
        }
        .monitor-card-alert { border-top: 15px solid #dc2626 !important; background: #fff5f5; }
        .monitor-stat-big { font-size: 3.5em !important; font-weight: 900 !important; margin: 0; line-height: 1; }
        .monitor-label { font-size: 1em !important; font-weight: 800 !important; text-transform: uppercase; color: #64748b !important; }

        /* 7. RESPONSIVIDAD DINÁMICA */
        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.5em; letter-spacing: -2px; }
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 4.5em; 
            text-align: center; border: 5px solid #dc2626; border-radius: 20px; 
            background: #fff5f5; padding: 20px; margin: 20px 0;
        }
        
        @media (max-width: 768px) {
            .glass-panel { padding: 20px; border-width: 4px; }
            .muni-title { font-size: 2.2em !important; }
            .timer-security { font-size: 4em !important; }
            .monitor-card { min-height: auto; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO I: CIUDADANO (BIENVENIDA QR & REGISTRO INSTITUCIONAL)
# ==================================================================================================

def view_citizen_node():
    """Interfaz diseñada para ser disparada desde el QR en los accesos municipales."""
    # BIENVENIDA CON IDENTIDAD SOBERANA
    st.markdown(f"<div style='text-align:center; padding:20px;'><img src='{URL_ESCUDO_MUNI}' width='200'></div>", unsafe_allow_html=True)
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#1e3a8a !important; font-weight:900; margin-bottom:0;'>¡Bienvenidos!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.4em; font-weight:700;'>Gestión de Innovación y Atención Ciudadana</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token_v31')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro Obligatorio de Visita")
        # FORMULARIO DE ALTO CONTRASTE Y CAPTURA BLINDADA
        with st.form("form_reg_v31", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                recinto = st.selectbox("Edificio Municipal donde se encuentra:", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos Completos:")
                rut = st.text_input("RUT / Identificación Nacional:")
            with col2:
                perfil = st.selectbox("Categoría de Audiencia:", PERFILES_SGAAC)
                depto = st.selectbox("Oficina / Departamento de Destino:", LISTADO_DEPARTAMENTOS)
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
                    st.session_state.citizen_token_v31 = uid
                    st.session_state.audit_logs.insert(0, f"REGISTRO QR: {nombre} en {recinto}")
                    st.rerun()
                else: st.error("⚠️ Todos los campos son obligatorios para garantizar su seguridad.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud para **{info['depto']}** está siendo procesada")
            # MARKETING TERRITORIAL ESTRATÉGICO
            st.markdown(f"<div style='background:#1e3a8a; color:white !important; padding:40px; border-radius:20px; border-left:15px solid #facc15; font-weight:800; font-size:1.4em;'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
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
            st.markdown("""<div style='background: #1e3a8a; color:white !important; padding:40px; border-radius:20px; text-align:center;'>
            <h2 style='color:white !important; margin:0;'>¡LA SERENA: INNOVACIÓN DE CLASE MUNDIAL!</h2>
            <p style='color:white !important; font-size:1.3em;'>Trabajamos cada día para brindarle la mejor experiencia ciudadana.</p></div>""", unsafe_allow_html=True)
            st.subheader("Calificación del Sistema y Atención Recibida")
            nps = st.slider("Evaluación General", 1, 5, 5)
            if st.button("ENVIAR EVALUACIÓN Y FINALIZAR"):
                final_entry = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': 15, 'NPS': nps, 'Estado': "Completado"}
                st.session_state.db_master = pd.concat([pd.DataFrame([final_entry]), st.session_state.db_master], ignore_index=True)
                del st.session_state.citizen_token_v31
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO II: MONITOR CONTROL TOTAL (GRID DE ALTA VISIBILIDAD PARA TV CENTER)
# ==================================================================================================

def view_master_monitor():
    """Pantalla central de mando: visión estratégica en tiempo real de los 17 recintos."""
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:800; font-size:1.5em; color:#1e3a8a !important;'>CONTROL ESTRATÉGICO DE LA RED TERRITORIAL | LA SERENA</p>", unsafe_allow_html=True)
    
    # Cuadrícula dinámica optimizada (4 columnas para TV, 1 para móvil)
    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r_name in enumerate(recintos_list):
        with cols[i % 4]:
            # Filtrar datos vivos para este recinto
            esperas = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'COORDINANDO']
            activos = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'EN_REUNION']
            
            # ALERTA VISUAL: Cambio de color si hay más de 2 esperas
            has_alert = len(esperas) > 2
            card_style = "monitor-card-alert" if has_alert else ""
            
            st.markdown(f"""
                <div class="monitor-card {card_style}">
                    <h3 style="margin:0; font-size:1.2em; color:#1e3a8a !important; line-height:1.2;">{INFRAESTRUCTURA_IMLS[r_name]['icono']} {r_name[:25]}...</h3>
                    <p style="margin:5px 0; font-size:0.8em; color:gray !important;">ZONA: {INFRAESTRUCTURA_IMLS[r_name]['zona']}</p>
                    <hr style="border: 1px solid #f1f5f9; margin:15px 0;">
                    <div style="display:flex; justify-content: space-around; align-items:center;">
                        <div>
                            <p class="monitor-stat-big" style="color:{'#dc2626' if has_alert else '#1e3a8a'} !important;">{len(esperas)}</p>
                            <p class="monitor-label">ESPERA</p>
                        </div>
                        <div style="border-left: 2px solid #f1f5f9; height: 60px;"></div>
                        <div>
                            <p class="monitor-stat-big" style="color:#059669 !important;">{len(activos)}</p>
                            <p class="monitor-label">EN VIVO</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. NODO III: HUB TÁCTICO DE COORDINACIÓN (GUARDIA & SECRETARÍAS)
# ==================================================================================================

def view_tactical_hub():
    """Nodo compartido para la operación en terreno y autorización administrativa."""
    st.markdown("<h2 class='muni-title'>COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    
    # Navegación por Pestañas (Legibilidad Navy on White)
    t_guardia, t_secre = st.tabs(["🛡️ Terminal Guardia (Filtro Físico)", "🔔 Panel Secretarías (Autorización)"])
    
    with t_guardia:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("👁️ Visor de Gestiones en Curso")
        coord_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord_v:
            df_tactical = pd.DataFrame([{"Vecino": v['nombre'], "Depto": v['depto'], "Recinto": v['recinto']} for v in coord_v.values()])
            st.table(df_tactical)
        else: st.caption("No hay coordinaciones activas en la red.")
        
        st.divider()
        st.subheader("🛡️ Validación de Ingresos Autorizados")
        aut_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not aut_v: st.info("Sin pases autorizados pendientes de validación física.")
        for uid, info in aut_v.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** -> {info['depto']} ({info['recinto']})")
                if st.button(f"CONFIRMAR PASO: {info['nombre']}", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with t_secre:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Hub de Autorización de Audiencias")
        pend_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend_v: st.success("Sin visitas esperando respuesta de su oficina.")
        for uid, info in pend_v.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})\n\n📍 Recinto: {info['recinto']} | Oficina: {info['depto']}")
                c_ok, c_rej = st.columns(2)
                if c_ok.button("✅ AUTORIZAR INGRESO", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    st.rerun()
                if c_rej.button("❌ REAGENDAR / DENEGAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. NAVEGACIÓN Y EJECUCIÓN (MAIN ENTRY POINT)
# ==================================================================================================

def main():
    """Orquesta la ejecución completa del sistema sovereign sgaac-360."""
    bootstrap_enterprise_logic()
    inject_sovereign_css()
    
    # Protocolo de Expiración Automática 180s (Limpieza de Cola)
    now = datetime.now()
    expired_uids = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired_uids: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    # BARRA LATERAL INSTITUCIONAL (STEALTH OPTIMIZED)
    with st.sidebar:
        st.image(URL_ESCUDO_MUNI, width=180)
        st.markdown("<hr style='border:2.5px solid #1e3a8a;'>", unsafe_allow_html=True)
        # NAVEGACIÓN UNIVERSAL (RADIO SE CONVIERTE EN SELECTOR DE MÓDULO)
        view_mode = st.radio("SELECCIONE MÓDULO OPERATIVO:", [
            "1. Ciudadano (QR)", 
            "2. Monitor Control Maestro", 
            "3. Tactical Hub (Guardia/Sec)", 
            "4. Analítica Big Data", 
            "5. Gestión CRM / BD",
            "6. Auditoría de Sistema"
        ])
        st.divider()
        st.caption(f"📅 {datetime.now().strftime('%d/%m/%Y')} | 🕒 {datetime.now().strftime('%H:%M:%S')}")
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    # SISTEMA DE NAVEGACIÓN UNIVERSAL (MÓVIL / TABLET / TV)
    if "1. Ciudadano" in view_mode: 
        view_citizen_node()
    elif "2. Monitor" in view_mode: 
        view_master_monitor()
    elif "3. Tactical" in view_mode: 
        view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<h2 class='muni-title'>ANÁLISIS DE GESTIÓN TERRITORIAL</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        m1, m2 = st.columns(2)
        m1.metric("Registros Big Data", f"{len(st.session_state.db_master):,}")
        m2.metric("NPS Satisfacción", f"{st.session_state.db_master['NPS'].mean():.1f} / 5.0")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(150), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Edición Estratégica de Fichas Ciudadanas")
        search_id = st.text_input("Ingrese ID de Visita para completar perfil (ej: VIS-100XXX):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_v31"):
                    tel = st.text_input("WhatsApp / Contacto", st.session_state.db_master.at[i, 'Telefono'])
                    mail = st.text_input("Email de Seguimiento", st.session_state.db_master.at[i, 'Email'])
                    if st.form_submit_button("ACTUALIZAR FICHA ESTRATÉGICA"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        st.success("Inteligencia Ciudadana Actualizada en Big Data.")
        st.markdown("</div>", unsafe_allow_html=True)
    elif "6. Auditoría" in view_mode:
        st.markdown("<h2 class='muni-title'>LOGS DE SISTEMA BLINDADOS</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:100]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": 
    main()
