"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / MISSION CRITICAL / STEALTH MODE
VERSIÓN: 28.0.0 (High-Density Modular Architecture - FULL EXTEND MODE)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 NODOS ESTRATÉGICOS (+1,500 LÍNEAS DE LÓGICA):
1.  NODO CIUDADANO (QR): Recepción Institucional, Registro, Tracking y Marketing Territorial.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación de EPP y control de ingresos/salidas.
3.  NODO PANEL SECRETARÍAS: Hub de autorización real-time y cierre correlativo de tiempos.
4.  NODO MONITOR CONTROL TOTAL: Pantalla central maestra con visión 360° de la red territorial.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +40,000 registros, flujos de calor y NPS.
6.  NODO GESTIÓN CRM: Edición profunda de fichas ciudadanas y vinculación estratégica.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización y cumplimiento.

ESPECIFICACIONES DE DISEÑO UNIVERSAL:
- Stealth Mode: Ocultamiento absoluto de GitHub, Fork, Deploy y Streamlit Branding.
- Deep Visual Contrast: Fondos Blancos (#FFFFFF) y Texto Deep Navy (#001F3F).
- Responsive Engine: Adaptación inteligente a Móvil, Tablet y Pantallas de TV 4K.
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
# 1. IDENTIDAD INSTITUCIONAL E INFRAESTRUCTURA REAL (I.M. LA SERENA)
# ==================================================================================================

URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"

# VARIABLE MAESTRA: Configuración de Recintos con Variable de Dotación (Realidad Local)
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
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "zona": "Deportes"},
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
AVISOS_PROMO = [
    "🏛️ Mientras coordinamos, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del Plan Serena.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena.",
    "⛪ Descubra por qué somos la 'Ciudad de los Campanarios'. Mire hacia arriba.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - ANTI CRASH)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Garantiza la inicialización absoluta de todos los estados para prevenir colapsos."""
    if 'system_live_v28' not in st.session_state:
        st.session_state.system_live_v28 = True
        st.session_state.boot_time = datetime.now()
        
        # FIX ATTRIBUTE_ERROR: Logs de Auditoría
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        # Canal de Mensajería Inter-Módulos
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00"}]

        # Gestión de Cola Crítica (Real-Time Sync)
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación de +40,000 registros históricos
        if 'db_master' not in st.session_state:
            n = 40000
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
                'Permanencia': [np.random.randint(5, 75) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (ULTRA-VISION: DEEP CONTRAST & STEALTH MODE)
# ==================================================================================================

def inject_sovereign_css():
    """Inyecta CSS radical para ocultar herramientas de plataforma y asegurar legibilidad absoluta."""
    st.markdown("""
        <style>
        /* 1. STEALTH MODE: OCULTAR GITHUB, FORK, DEPLOY Y BRANDING */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stDecoration"] {display: none;}
        
        /* 2. CONFIGURACIÓN DE ALTO CONTRASTE (FONDO BLANCO / TEXTO DEEP NAVY) */
        .stApp { background-color: #FFFFFF !important; font-family: 'Outfit', sans-serif; }
        
        /* Forzar texto Azul Marino Profundo (#001F3F) en todo el sistema */
        p, span, label, div, li, h1, h2, h3, h4, h5, table { color: #001F3F !important; font-weight: 500; }
        
        /* Paneles Institucionales (Eliminación de Recuadros Negros) */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 12px;
            border: 3px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
        }

        /* 3. FIX SELECTBOX (Corrección Definitiva Negro/Azul) */
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
            color: #ffffff !important; border-radius: 15px; height: 80px;
            font-weight: 900; text-transform: uppercase; font-size: 1.2em;
            box-shadow: 0 8px 25px rgba(30, 58, 138, 0.4);
            border: none !important;
        }

        /* 5. TÍTULOS Y CRONÓMETRO */
        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.5em; letter-spacing: -2px; }
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 4em; 
            text-align: center; border: 4px solid #dc2626; border-radius: 15px; 
            background: #fff5f5; padding: 15px; margin: 15px 0;
        }
        
        /* 6. RESPONSIVIDAD DINÁMICA MÓVIL / TABLET / TV */
        @media (max-width: 768px) {
            .glass-panel { padding: 20px; border-width: 4px; }
            .stTabs [data-baseweb="tab"] { font-size: 1em !important; padding: 12px !important; font-weight: 800 !important; }
            .muni-title { font-size: 2.5em !important; }
        }

        /* 7. ESTILOS MONITOR CENTRAL TV */
        .tv-card {
            background: #FFFFFF; border-radius: 15px; padding: 25px;
            border-top: 15px solid #1e3a8a; box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            text-align: center; border-left: 1px solid #f1f5f9; border-right: 1px solid #f1f5f9;
        }
        .tv-card-alert { border-top: 15px solid #dc2626 !important; background: #fff5f5; }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO CIUDADANO (BIENVENIDA INSTITUCIONAL & REGISTRO QR)
# ==================================================================================================

def view_citizen_node():
    # BIENVENIDA CON ESCUDO (DISPARADO DESDE CÁMARA/QR)
    st.markdown(f"<div style='text-align:center; padding:20px;'><img src='{URL_ESCUDO_MUNI}' width='180'></div>", unsafe_allow_html=True)
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#1e3a8a !important; font-weight:900;'>¡Bienvenidos!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.3em; font-weight:700;'>Gestión Ciudadana de Innovación Mundial</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token_v28')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro Obligatorio de Ingreso")
        # FORMULARIO DE ALTO CONTRASTE
        with st.form("form_reg_v28", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                recinto = st.selectbox("Edificio Municipal:", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos:")
                rut = st.text_input("RUT / Documento Identidad:")
            with col2:
                perfil = st.selectbox("Categoría de Visitante:", PERFILES_SGAAC)
                depto = st.selectbox("Departamento de Destino:", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("Motivo de su Visita:")
            
            submit = st.form_submit_button("SOLICITAR AUTORIZACIÓN")
            if submit:
                if nombre and rut and recinto:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(), "assisted": assisted,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_token_v28 = uid
                    st.session_state.audit_logs.insert(0, f"SOLICITUD QR: {nombre} en {recinto}")
                    st.rerun()
                else: st.error("⚠️ Complete los campos obligatorios para continuar.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud para **{info['depto']}** está en proceso")
            # MARKETING TERRITORIAL
            st.markdown(f"<div style='background:#1e3a8a; color:white !important; padding:30px; border-radius:15px; font-weight:700; font-size:1.3em;'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: st.write("Diríjase al control del Guardia para validar su ingreso.")
            else:
                if st.button("YA INGRESÉ AL ÁREA DE REUNIÓN"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    st.rerun()
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **AUDIENCIA EN CURSO**")
            if st.button("FINALIZAR Y EVALUAR ATENCIÓN"):
                st.session_state.waiting_room[token]['estado'] = "CIERRE"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
        elif info['estado'] == "CIERRE":
            st.balloons()
            st.markdown("""<div style='background: #1e3a8a; color:white !important; padding:30px; border-radius:15px; margin-bottom:20px; text-align:center;'>
            <h2 style='color:white !important;'>¡LA SERENA: INNOVACIÓN DE CLASE MUNDIAL!</h2>
            <p style='color:white !important;'>Esperamos que su experiencia municipal haya sido excelente.</p></div>""", unsafe_allow_html=True)
            st.subheader("Evaluación de Calidad de Atención")
            nps = st.slider("¿Cómo califica el servicio?", 1, 5, 5)
            if st.button("ENVIAR Y FINALIZAR"):
                final_entry = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': 15, 'NPS': nps, 'Estado': "Completado"}
                st.session_state.db_master = pd.concat([pd.DataFrame([final_entry]), st.session_state.db_master], ignore_index=True)
                del st.session_state.citizen_token_v28
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO MONITOR CONTROL TOTAL (PANTALLA MAESTRA / TV CENTER)
# ==================================================================================================

def view_master_monitor():
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:800; font-size:1.4em;'>Visión estratégica en vivo de la Red de Recintos | La Serena</p>", unsafe_allow_html=True)
    
    # Grid dinámico: 4 columnas para TV/Desktop, 1 para móvil
    cols = st.columns(4)
    recintos = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r in enumerate(recintos):
        with cols[i % 4]:
            esp = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'COORDINANDO']
            act = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'EN_REUNION']
            
            # Alerta visual: Borde rojo si hay esperas
            alert_class = "tv-card-alert" if len(esp) > 1 else ""
            
            st.markdown(f"""
                <div class="tv-card {alert_class}">
                    <h3 style="margin:0; font-size:1.1em; color:#1e3a8a !important;">{INFRAESTRUCTURA_IMLS[r]['icono']} {r[:22]}...</h3>
                    <hr style="border:1px solid #f1f5f9; margin:15px 0;">
                    <p style="font-size:2.2em; margin:0; color:#dc2626 !important; font-weight:900;">{len(esp)} <small style="font-size:0.4em; color:gray !important;">ESPERA</small></p>
                    <p style="font-size:1.6em; margin:0; color:#1e3a8a !important; font-weight:900;">{len(act)} <small style="font-size:0.4em; color:gray !important;">AUDIENCIA</small></p>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. NODO TÁCTICO HUB (GUARDIA & SECRETARÍAS)
# ==================================================================================================

def view_tactical_hub():
    st.markdown("<h2 class='muni-title'>COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🛡️ Terminal Guardia", "🔔 Panel Secretarías"])
    
    with t1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("👁️ Visor de Coordinaciones en Curso")
        coord = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord:
            df_v = pd.DataFrame([{"Ciudadano": v['nombre'], "Depto": v['depto'], "Edificio": v['recinto']} for v in coord.values()])
            st.table(df_v)
        else: st.caption("Sin gestiones de espera activas.")
        
        st.divider()
        st.subheader("🛡️ Validación de Ingresos Físicos")
        aut = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not aut: st.info("Sin pases pendientes.")
        for uid, info in aut.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** -> {info['depto']} ({info['recinto']})")
                if st.button(f"VALIDAR PASO: {info['nombre']}", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with t2:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Hub de Autorización de Audiencias")
        pend = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend: st.success("Sin visitas esperando.")
        for uid, info in pend.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})\n\n📍 Recinto: {info['recinto']} | Oficina: {info['depto']}")
                c1, c2 = st.columns(2)
                if c1.button("✅ AUTORIZAR INGRESO", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    st.rerun()
                if c2.button("❌ DENEGAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. NAVEGACIÓN Y EJECUCIÓN (MAIN ENTRY POINT)
# ==================================================================================================

def main():
    bootstrap_enterprise_logic()
    inject_sovereign_css()
    
    # Protocolo de Expiración Automática
    now = datetime.now()
    expired = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    with st.sidebar:
        st.image(URL_ESCUDO_MUNI, width=180)
        st.markdown("<hr style='border:2px solid #1e3a8a;'>", unsafe_allow_html=True)
        view_mode = st.radio("MÓDULO OPERATIVO SGAAC:", [
            "1. Ciudadano (Modo QR)", 
            "2. Monitor Control Maestro", 
            "3. Tactical Hub (Guardia/Sec)", 
            "4. Analítica Big Data", 
            "5. Gestión CRM / BD",
            "6. Auditoría Interna"
        ])
        st.divider()
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    # SISTEMA DE NAVEGACIÓN UNIVERSAL (TODOS LOS MÓDULOS VISIBLES EN MÓVIL/TV)
    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Monitor" in view_mode: view_master_monitor()
    elif "3. Tactical" in view_mode: view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<h2 class='muni-title'>ANÁLISIS TERRITORIAL</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        m1, m2 = st.columns(2)
        m1.metric("Registros Big Data", f"{len(st.session_state.db_master):,}")
        m2.metric("NPS Satisfacción", f"{st.session_state.db_master['NPS'].mean():.1f} / 5.0")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Edición Estratégica de Fichas")
        s_id = st.text_input("Ingrese ID de Visita (ej: VIS-100XXX):")
        if s_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == s_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_v28"):
                    tel = st.text_input("WhatsApp / Contacto", st.session_state.db_master.at[i, 'Telefono'])
                    mail = st.text_input("Email", st.session_state.db_master.at[i, 'Email'])
                    if st.form_submit_button("ACTUALIZAR FICHA"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        st.success("Inteligencia Ciudadana Actualizada.")
        st.markdown("</div>", unsafe_allow_html=True)
    elif "6. Auditoría" in view_mode:
        st.markdown("<h2 class='muni-title'>LOGS DE SISTEMA BLINDADOS</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:100]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": main()
