"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / UNIVERSAL SOVEREIGN MODE
VERSIÓN: 24.0.0 (High-Density Modular Architecture - FULL EXTEND MODE 1.5K)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA SISTÉMICA DE 7 NODOS:
1.  NODO CIUDADANO (QR): Recepción con Escudo, Registro, Tracking y Marketing Territorial.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación física y control de seguridad.
3.  NODO PANEL SECRETARÍAS: Hub de autorización y cierre correlativo de tiempos de atención.
4.  NODO MONITOR CONTROL TOTAL: Visión 360° en cuadrícula dinámica para TV y Central de Mando.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +40,000 registros, flujos y NPS Municipal.
6.  NODO GESTIÓN CRM: Edición profunda de fichas ciudadanas y vinculación con dirigentes.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización y cumplimiento.

ESPECIFICACIONES DE DISEÑO:
- Stealth Mode: Ocultamiento de GitHub, Fork, Deploy y Streamlit Branding.
- High Contrast: Fondos claros y textos oscuros para legibilidad en terreno.
- Universal Responsive: Optimización para Móvil, Tablet y Pantallas de TV 4K.
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
# 1. RECURSOS INSTITUCIONALES E IDENTIDAD (I.M. LA SERENA)
# ==================================================================================================

URL_ESCUDO = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"

# VARIABLE MAESTRA: Recintos Reales con Variable de Dotación
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️", "zona": "Centro"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢", "zona": "Centro"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫", "zona": "Centro"},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦", "zona": "Servicios"},
    "DIDECO (Almagro 450)": {"dotacion": True, "icono": "🤝", "zona": "Social"},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️", "zona": "Norte"},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡", "zona": "Oriente"},
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳", "zona": "Sur"},
    "Delegación Municipal Avenida del Mar": {"dotacion": True, "icono": "🏖️", "zona": "Costa"},
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

# MARKETING TERRITORIAL DINÁMICO (LA SERENA SMARTCITY)
AVISOS_PROMO = [
    "🏛️ Mientras espera, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la paz de nuestra Plaza de Armas, joya del urbanismo serenense.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "⛪ La Serena es la 'Ciudad de los Campanarios'. Mire hacia arriba y descubra.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - ANTI CRASH)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Garantiza la inicialización absoluta de todos los estados de sesión."""
    if 'system_initialized_v24' not in st.session_state:
        st.session_state.system_initialized_v24 = True
        st.session_state.boot_time = datetime.now()
        
        # PREVENCIÓN ATTRIBUTE_ERROR
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00"}]

        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación de +40,000 registros históricos (Stress-test Territorial)
        # PREVENCIÓN KEY_ERROR: Columnas estandarizadas
        if 'db_master' not in st.session_state:
            n = 40000
            start_date = datetime.now() - timedelta(days=1095) # 3 años de historia
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start_date + timedelta(minutes=np.random.randint(0, 1576800)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_SGAAC) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Permanencia': [np.random.randint(5, 75) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (STEALTH & HIGH CONTRAST UNIVERSAL)
# ==================================================================================================

def inject_sovereign_css():
    """Inyecta CSS radical para ocultar herramientas técnicas y asegurar legibilidad absoluta."""
    st.markdown("""
        <style>
        /* 1. STEALTH MODE: OCULTAR GITHUB, FORK, DEPLOY Y STREAMLIT UI */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stSidebarNav"] {display: block !important;}
        
        /* 2. CONFIGURACIÓN DE ALTO CONTRASTE (BLANCO / NEGRO / AZUL MARINO) */
        .stApp { background: #FFFFFF !important; font-family: 'Outfit', sans-serif; }
        
        /* Eliminación de recuadros negros - Uso de Paneles Blancos con Bordes Sólidos */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 12px;
            border: 3px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            margin-bottom: 25px;
            color: #0f172a !important;
        }

        /* 3. FIX MENÚS DESPLEGABLES (Legibilidad en Móvil) */
        div[data-baseweb="select"] > div {
            background-color: #f8fafc !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #0f172a !important; background-color: #ffffff !important; font-weight: 700 !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #1e3a8a !important; color: #ffffff !important; }

        /* 4. TEXTO Y TÍTULOS */
        label, p, span, div, li { color: #0f172a !important; font-weight: 600 !important; }
        h1, h2, h3 { color: #1e3a8a !important; font-weight: 900 !important; }

        /* 5. BOTONERA XL INSTITUCIONAL */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #ffffff !important; border-radius: 12px; height: 75px;
            font-weight: 800; text-transform: uppercase; font-size: 1.2em;
            box-shadow: 0 8px 20px rgba(30, 58, 138, 0.4);
        }

        /* 6. CRONÓMETRO Y ALERTAS */
        .timer-security { color: #dc2626 !important; font-weight: 900; font-size: 4em; text-align: center; border: 2px solid #dc2626; border-radius: 15px; background: #fff5f5; padding: 10px; }
        
        /* 7. RESPONSIVIDAD DINÁMICA MÓVIL / TABLET / TV */
        @media (max-width: 768px) {
            .glass-panel { padding: 20px; border-width: 4px; }
            .stTabs [data-baseweb="tab"] { font-size: 1.1em !important; padding: 15px !important; font-weight: 800 !important; }
            .muni-title { font-size: 2.2em !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. MÓDULO I: NODO CIUDADANO (WELCOME & REGISTRO QR)
# ==================================================================================================

def view_citizen_node():
    # RECEPCIÓN INSTITUCIONAL CON ESCUDO
    st.markdown(f"<div style='text-align:center;'><img src='{URL_ESCUDO}' width='150'></div>", unsafe_allow_html=True)
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#1e3a8a;'>¡Bienvenidos!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.1em;'>Portal de Atención y Registro Ciudadano</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token_v24')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Iniciar Solicitud de Ingreso")
        # FIX FORM_SUBMIT: Garantizar flujo de datos
        with st.form("form_reg_v24", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                recinto = st.selectbox("Edificio Municipal donde se encuentra:", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos:")
                rut = st.text_input("RUT / Identificación:")
            with col2:
                perfil = st.selectbox("Categoría de Visitante:", PERFILES_SGAAC)
                depto = st.selectbox("Departamento / Oficina de Destino:", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("Motivo de su Visita:")
            
            submit = st.form_submit_button("SOLICITAR AUTORIZACIÓN")
            if submit:
                if nombre and rut:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(), "assisted": assisted,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_token_v24 = uid
                    st.session_state.audit_logs.insert(0, f"SOLICITUD QR: {nombre} en {recinto}")
                    st.rerun()
                else: st.error("⚠️ Complete todos los campos obligatorios.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud en **{info['recinto']}** está siendo procesada")
            # MARKETING TERRITORIAL CON ALTO CONTRASTE
            st.markdown(f"<div style='background:#1e3a8a; color:white; padding:25px; border-radius:15px; font-weight:700; margin:20px 0;'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: st.write("Diríjase al control del Guardia para validar su entrada física.")
            else:
                if st.button("YA INGRESÉ AL ÁREA DE REUNIÓN"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    st.rerun()
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **VISITA EN CURSO**")
            if st.button("FINALIZAR Y EVALUAR ATENCIÓN"):
                st.session_state.waiting_room[token]['estado'] = "COMPLETADO"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
        elif info['estado'] == "COMPLETADO":
            st.balloons()
            st.success("¡Gracias por visitarnos!")
            st.write("La Serena es Innovación de Clase Mundial al servicio de la gente.")
            del st.session_state.citizen_token_v24
            time.sleep(3)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. MÓDULO II: MONITOR CONTROL TOTAL (TV / COMMAND CENTER GRID)
# ==================================================================================================

def view_total_monitor():
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Visión estratégica en tiempo real de la Red Territorial | La Serena</p>", unsafe_allow_html=True)
    
    # Cuadrícula responsiva (4 columnas en TV/Desktop, 1 en Móvil)
    cols = st.columns(4)
    recintos = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r in enumerate(recintos):
        with cols[i % 4]:
            esperas = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'COORDINANDO']
            activos = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'EN_REUNION']
            
            border_color = "#dc2626" if esperas else "#1e3a8a"
            st.markdown(f"""
                <div style='background:white; border-radius:12px; padding:20px; border-top:10px solid {border_color}; box-shadow: 0 8px 15px rgba(0,0,0,0.1); margin-bottom:15px; text-align:center;'>
                    <h3 style="margin:0; font-size:1em; color:#1e3a8a;">{INFRAESTRUCTURA_IMLS[r]['icono']} {r[:20]}...</h3>
                    <hr style="border:1px solid #f1f5f9;">
                    <p style="font-size:1.8em; margin:0; color:#dc2626; font-weight:900;">{len(esperas)} <small style="font-size:0.4em; color:gray;">ESPERA</small></p>
                    <p style="font-size:1.2em; margin:0; color:#1e3a8a; font-weight:800;">{len(activos)} <small style="font-size:0.4em; color:gray;">ACTIVOS</small></p>
                    <p style="font-size:0.6em; color:gray; margin-top:5px;">Zona: {INFRAESTRUCTURA_IMLS[r]['zona']}</p>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. MÓDULO III: TACTICAL HUB (GUARDIA & SECRETARÍAS)
# ==================================================================================================

def view_tactical_hub():
    st.markdown("<h2 class='muni-title'>COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🛡️ Terminal Guardia", "🔔 Panel Secretarías"])
    
    with t1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Visor de Gestiones en Tiempo Real")
        coord = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord:
            df_v = pd.DataFrame([{"Vecino": v['nombre'], "Perfil": v['perfil'], "Hacia": v['depto'], "Edificio": v['recinto']} for v in coord.values()])
            st.table(df_v)
        else: st.caption("Sin solicitudes pendientes en la red.")
        
        st.divider()
        st.subheader("Validación de Ingresos")
        aut = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        for uid, info in aut.items():
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
        pend = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend: st.success("Sin visitas esperando respuesta de oficina.")
        for uid, info in pend.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})\n\n📍 Recinto: {info['recinto']} | Depto: {info['depto']}")
                c1, c2 = st.columns(2)
                if c1.button("✅ AUTORIZAR", key=f"s_ok_{uid}"):
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
    
    # Protocolo de Expiración Automática 180s
    now = datetime.now()
    expired = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    with st.sidebar:
        st.image(URL_ESCUDO, width=180)
        st.divider()
        view_mode = st.radio("MÓDULO DE OPERACIÓN SGAAC:", [
            "1. Ciudadano (Modo QR)", 
            "2. Monitor Control Total", 
            "3. Tactical Hub (Guardia/Sec)", 
            "4. Analítica Big Data", 
            "5. Gestión CRM / BD",
            "6. Auditoría Interna"
        ])
        st.divider()
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    # SISTEMA DE NAVEGACIÓN POR PESTAÑAS UNIVERSALES
    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Monitor" in view_mode: view_total_monitor()
    elif "3. Tactical" in view_mode: view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<h2 class='muni-title'>ANÁLISIS DE GESTIÓN TERRITORIAL</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.metric("Total Registros Big Data", f"{len(st.session_state.db_master):,}")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Edición Estratégica de Fichas Ciudadanas")
        search_id = st.text_input("ID de Visita para completar perfil (ej: VIS-100XXX):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_v24"):
                    tel = st.text_input("WhatsApp / Contacto", st.session_state.db_master.at[i, 'Telefono'])
                    mail = st.text_input("Email de Seguimiento", st.session_state.db_master.at[i, 'Email'])
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
