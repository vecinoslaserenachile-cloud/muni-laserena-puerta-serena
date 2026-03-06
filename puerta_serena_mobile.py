"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / MISSION CRITICAL / ULTRA-LEGIBILITY / STEALTH MODE
VERSIÓN: 35.0.0 (High-Density Modular Architecture - TOTAL EXTEND MODE)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 NODOS ESTRATÉGICOS:
1.  NODO CIUDADANO (QR): Home de Bienvenida con Doble Logo, Instrucciones Claras y Registro.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones en tiempo real para apoyo en primera línea.
3.  NODO PANEL SECRETARÍAS: Hub de autorización y cierre correlativo de tiempos reales.
4.  NODO MONITOR CONTROL TOTAL: Pantalla maestra 360° en cuadrícula táctica (TV/Mando).
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +50,000 registros, flujos y NPS Municipal.
6.  NODO GESTIÓN CRM: Edición estratégica de fichas de contacto y redes sociales de dirigentes.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización y control del Director.

SOLUCIONES DE DISEÑO:
- High Contrast: Texto Azul Imperial (#002855) sobre Blanco Puro (#FFFFFF).
- Mobile-First: Botones XL, formularios de alta visibilidad y menús simplificados.
- Stealth Mode: Ocultamiento absoluto de GitHub Tools, Fork, Deploy y Streamlit Branding.
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
# 1. IDENTIDAD INSTITUCIONAL Y CONFIGURACIÓN TERRITORIAL (I.M. LA SERENA)
# ==================================================================================================

# RECURSOS GRÁFICOS INSTITUCIONALES
URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"
# Logo conceptual de Innovación diseñado para el Home Ciudadano
URL_INNOVACION = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_smartcity.png"

# VARIABLE MAESTRA: Recintos Reales con Variable de Dotación (Realidad Territorial)
# Es la base para la Pantalla Central de Control Maestro.
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️", "zona": "Casco Histórico", "id": "EC01"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢", "zona": "Casco Histórico", "id": "EC02"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫", "zona": "Casco Histórico", "id": "EB03"},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦", "zona": "Servicios", "id": "DT04"},
    "DIDECO (Almagro 450)": {"dotacion": True, "icono": "🤝", "zona": "Social", "id": "DI05"},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️", "zona": "Norte", "id": "DL06"},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡", "zona": "Oriente", "id": "LA07"},
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳", "zona": "Sur", "id": "LP08"},
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️", "zona": "Costa", "id": "AM09"},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜", "zona": "Rural", "id": "DR10"},
    "Coliseo Monumental": {"dotacion": True, "icono": "🏀", "zona": "Deportes", "id": "CM11"},
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "zona": "Deportes Norte", "id": "PC12"},
    "Parque Pedro de Valdivia (Admin)": {"dotacion": True, "icono": "🦌", "zona": "Recreación", "id": "PV13"},
    "Juzgado de Policía Local": {"dotacion": True, "icono": "⚖️", "zona": "Justicia", "id": "JP14"},
    "Taller Municipal": {"dotacion": False, "icono": "🛠️", "zona": "Operativa", "id": "TM15"},
    "Centro Cultural Palace": {"dotacion": False, "icono": "🎨", "zona": "Cultura", "id": "CP16"},
    "Estadio La Portada (Admin)": {"dotacion": True, "icono": "⚽", "zona": "Deportes", "id": "EP17"}
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

# MENSAJES PROMOCIONALES DINÁMICOS
AVISOS_PROMO = [
    "🏛️ Mientras coordinamos su ingreso, admire nuestro Casco Histórico, Patrimonio Nacional.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del Plan Serena.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "Church ⛪ ¿Sabía que somos la 'Ciudad de los Campanarios'? Descubra su historia.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - ANTI CRASH SYSTEM)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Garantiza la inicialización absoluta de todos los estados para prevenir colapsos."""
    if 'system_initialized_v35' not in st.session_state:
        st.session_state.system_initialized_v35 = True
        st.session_state.boot_time = datetime.now()
        
        # FIX ATTRIBUTE_ERROR: Logs de Auditoría Blindados
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00"}]

        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Simulación masiva de +50,000 registros históricos
        # FIX KEY_ERROR: Columnas estandarizadas para evitar fallos en gráficos
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
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (ULTRA-VISION: DEEP CONTRAST & STEALTH MODE PRO)
# ==================================================================================================

def inject_universal_sovereign_css():
    """Inyecta CSS radical para ocultar herramientas técnicas y asegurar legibilidad absoluta."""
    st.markdown("""
        <style>
        /* 1. STEALTH MODE PRO: OCULTAR GITHUB, FORK, DEPLOY Y STREAMLIT UI */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stDecoration"] {display: none;}
        
        /* 2. CONFIGURACIÓN DE ALTO CONTRASTE (FONDO BLANCO / TEXTO IMPERIAL NAVY #002855) */
        .stApp { background-color: #FFFFFF !important; font-family: 'Outfit', sans-serif; }
        
        /* Forzar texto Azul Marino Profundo en TODA la interfaz para evitar ilegibilidad */
        p, span, label, div, li, h1, h2, h3, h4, h5, table, .stMarkdown { 
            color: #002855 !important; 
            font-weight: 600 !important; 
        }
        
        /* Paneles Institucionales (Eliminación de Recuadros Negros e Ilegibles) */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 12px;
            border: 4px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.12);
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
            border-radius: 12px 12px 0 0 !important;
            padding: 15px 30px !important;
            border: 1px solid #f1f5f9 !important;
            margin-right: 8px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #1e3a8a !important;
            color: #FFFFFF !important;
        }

        /* 4. FIX SELECTBOX (Contraste Máximo para Adulto Mayor) */
        div[data-baseweb="select"] > div {
            background-color: #f8fafc !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
            height: 65px !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 3px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #002855 !important; font-weight: 700 !important; background-color: #ffffff !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #1e3a8a !important; color: #ffffff !important; }

        /* 5. BOTONERA XL INSTITUCIONAL (TOUCH READY) */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #ffffff !important; border-radius: 18px; height: 95px;
            font-weight: 900; text-transform: uppercase; font-size: 1.5em;
            box-shadow: 0 10px 30px rgba(30, 58, 138, 0.45);
            border: none !important;
            margin-top: 25px;
        }

        /* 6. MONITOR CARDS (Diseño Táctico para TV / Command Center) */
        .monitor-card {
            background: #FFFFFF; border-radius: 18px; padding: 25px;
            border-top: 15px solid #1e3a8a; box-shadow: 0 15px 30px rgba(0,0,0,0.15);
            text-align: center; border-left: 1px solid #f1f5f9; border-right: 1px solid #f1f5f9;
            margin-bottom: 25px; min-height: 280px;
        }
        .monitor-card-alert { border-top: 15px solid #dc2626 !important; background: #fffafa; }
        .monitor-stat-big { font-size: 4em !important; font-weight: 950 !important; margin: 0; line-height: 1; }
        .monitor-label { font-size: 1.1em !important; font-weight: 900 !important; text-transform: uppercase; color: #64748b !important; }

        /* 7. RESPONSIVIDAD DINÁMICA MÓVIL EXTREMA */
        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.8em; letter-spacing: -2px; }
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 5em; 
            text-align: center; border: 6px solid #dc2626; border-radius: 25px; 
            background: #fff5f5; padding: 25px; margin: 25px 0;
        }
        
        @media (max-width: 768px) {
            .glass-panel { padding: 20px; border-width: 5px; }
            .muni-title { font-size: 2.5em !important; }
            .stButton>button { height: 110px; font-size: 1.6em !important; }
            .timer-security { font-size: 4.5em !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO I: CIUDADANO (WELCOME QR & REGISTRO SENIOR-FRIENDLY)
# ==================================================================================================

def view_citizen_node():
    """Interfaz diseñada para el vecino: impacto visual y legibilidad absoluta."""
    # CABECERA INSTITUCIONAL: ESCUDO MUNICIPAL + MENSAJE BIENVENIDA
    st.markdown(f"<div style='text-align:center; padding:30px;'><img src='{URL_ESCUDO_MUNI}' width='240'></div>", unsafe_allow_html=True)
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#1e3a8a !important; font-weight:950; font-size:2.5em; margin-bottom:10px;'>¡Bienvenidos!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.6em; font-weight:800; margin-bottom:40px; color:#1e3a8a !important;'>La Serena: Innovación al Servicio de la Gente</p>", unsafe_allow_html=True)
    
    # RECUADRO DE INSTRUCCIONES XL (Contraste Deep Navy sobre Fondo Crema Suave)
    st.markdown(f"""
        <div style="background-color: #F8FAFC; border-left: 15px solid #1e3a8a; padding: 40px; border-radius: 20px; margin-bottom: 40px; box-shadow: 0 8px 20px rgba(0,0,0,0.08);">
            <h3 style="margin-top:0; color:#1e3a8a !important; font-size:1.6em;">Estimado Vecino(a):</h3>
            <p style="font-size:1.4em !important; line-height:1.4; font-weight:700;">Para ser atendido, siga estos pasos simples:</p>
            <ul style="font-size:1.4em !important; font-weight:800; color:#002855 !important; line-height:1.6;">
                <li>Seleccione el edificio municipal donde se encuentra.</li>
                <li>Escriba su Nombre y RUT con calma.</li>
                <li>Elija la oficina y el motivo de su visita.</li>
                <li>Presione el <b>BOTÓN AZUL GRANDE</b> al final.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token_v35')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Iniciar Registro de Visita")
        # FORMULARIO DE ALTA LEGIBILIDAD
        with st.form("form_reg_final_v35", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                recinto = st.selectbox("1. Edificio Municipal donde está ahora:", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("2. Su Nombre y Apellidos Completos:")
                rut = st.text_input("3. Su RUT (ej: 12.345.678-9):")
            with col2:
                perfil = st.selectbox("4. Categoría de Visitante:", PERFILES_SGAAC)
                depto = st.selectbox("5. Oficina de Destino:", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("6. ¿A qué viene hoy? (Motivo):")
            
            submit = st.form_submit_button("PRESIONE AQUÍ PARA SOLICITAR INGRESO")
            if submit:
                if nombre and rut and recinto:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(), "assisted": assisted,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_token_v35 = uid
                    st.session_state.audit_logs.insert(0, f"REGISTRO QR: {nombre} en {recinto}")
                    st.rerun()
                else: st.error("⚠️ Complete todos los campos requeridos para su atención.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud para **{info['depto']}** está siendo procesada")
            # MARKETING TERRITORIAL DINÁMICO
            st.markdown(f"<div style='background:#1e3a8a; color:white !important; padding:45px; border-radius:25px; border-left:15px solid #facc15; font-weight:900; font-size:1.6em; line-height:1.3;'>{np.random.choice(AVISOS_BIENVENIDA)}</div>", unsafe_allow_html=True)
            
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO POR SECRETARÍA**")
            if info['assisted']: st.write("Por favor, diríjase al control del Guardia para validar su entrada física.")
            else:
                st.markdown("### ¡PASE ADELANTE!")
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
            st.markdown("""<div style='background: #1e3a8a; color:white !important; padding:45px; border-radius:25px; text-align:center;'>
            <h2 style='color:white !important; margin:0; font-size:2.2em;'>¡LA SERENA: INNOVACIÓN DE CLASE MUNDIAL!</h2>
            <p style='color:white !important; font-size:1.5em;'>Trabajamos cada día para brindarle la mejor experiencia ciudadana.</p></div>""", unsafe_allow_html=True)
            st.subheader("Calificación del Sistema y Atención Recibida")
            nps = st.slider("¿Cómo evalúa su experiencia hoy?", 1, 5, 5)
            if st.button("ENVIAR EVALUACIÓN Y FINALIZAR"):
                final_entry = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': 20, 'NPS': nps, 'Estado': "Completado"}
                st.session_state.db_master = pd.concat([pd.DataFrame([final_entry]), st.session_state.db_master], ignore_index=True)
                del st.session_state.citizen_token_v35
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO II: MONITOR CONTROL TOTAL (GRID MAESTRO DE ALTA VISIBILIDAD)
# ==================================================================================================

def view_master_monitor():
    """Pantalla central de mando: visión estratégica en tiempo real de los 17 recintos."""
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:900; font-size:1.8em; color:#1e3a8a !important;'>CONTROL ESTRATÉGICO DE LA RED TERRITORIAL | LA SERENA</p>", unsafe_allow_html=True)
    
    # Grid dinámico de alto rendimiento (4 columnas para TV, 1 para móvil)
    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r_name in enumerate(recintos_list):
        with cols[i % 4]:
            # Filtrado en tiempo real de datos vivos
            esp = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'COORDINANDO']
            act = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'EN_REUNION']
            
            # ALERTA VISUAL: Cambio de color si hay ciudadanos esperando
            has_alert = len(esp) > 0
            card_style = "monitor-card-alert" if has_alert else ""
            
            st.markdown(f"""
                <div class="monitor-card {card_style}">
                    <h3 style="margin:0; font-size:1.4em; color:#1e3a8a !important; line-height:1.1;">{INFRAESTRUCTURA_IMLS[r_name]['icono']} {r_name[:25]}...</h3>
                    <p style="margin:5px 0; font-size:1em; color:gray !important; font-weight:800;">ZONA: {INFRAESTRUCTURA_IMLS[r_name]['zona']}</p>
                    <hr style="border: 2px solid #f1f5f9; margin:20px 0;">
                    <div style="display:flex; justify-content: space-around; align-items:center;">
                        <div>
                            <p class="monitor-stat-big" style="color:{'#dc2626' if has_alert else '#1e3a8a'} !important;">{len(esp)}</p>
                            <p class="monitor-label">ESPERA</p>
                        </div>
                        <div style="border-left: 3px solid #f1f5f9; height: 100px;"></div>
                        <div>
                            <p class="monitor-stat-big" style="color:#059669 !important;">{len(act)}</p>
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
    
    # Navegación por Pestañas Universales (Legibilidad Navy on White)
    t_guardia, t_secre = st.tabs(["🛡️ Terminal Guardia (Validación Física)", "🔔 Panel Secretarías (Autorización)"])
    
    with t_guardia:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("👁️ Visor de Gestiones en Curso")
        coord_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord_v:
            df_tactical = pd.DataFrame([{"Vecino": v['nombre'], "Depto": v['depto'], "Edificio": v['recinto']} for v in coord_v.values()])
            st.table(df_tactical)
        else: st.caption("No hay coordinaciones activas en la red municipal en este momento.")
        
        st.divider()
        st.subheader("🛡️ Validación de Ingresos Físicos")
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
    inject_universal_sovereign_css()
    
    # Protocolo de Expiración Automática 180s (Limpieza de Cola Crítica)
    now = datetime.now()
    expired_uids = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired_uids: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    # SIDEBAR INSTITUCIONAL (Stealth Optimized)
    with st.sidebar:
        st.image(URL_ESCUDO_MUNI, width=200)
        st.markdown("<hr style='border:3px solid #1e3a8a;'>", unsafe_allow_html=True)
        # NAVEGACIÓN POR RADIO (FUNCIONALIDAD TOTAL TRASPASADA A MÓVIL)
        view_mode = st.radio("SELECCIONE MÓDULO OPERATIVO:", [
            "1. Ciudadano (Modo QR)", 
            "2. Monitor Control Maestro", 
            "3. Tactical Hub (Guardia/Sec)", 
            "4. Analítica Big Data", 
            "5. Gestión CRM / BD",
            "6. Auditoría de Sistema"
        ])
        st.divider()
        st.caption(f"📅 {datetime.now().strftime('%d/%m/%Y')} | 🕒 {datetime.now().strftime('%H:%M:%S')}")
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    # SISTEMA DE NAVEGACIÓN UNIVERSAL (TODOS LOS MÓDULOS VISIBLES EN MÓVIL/TABLET/TV)
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
        m1.metric("Registros Big Data", f"{len(st.session_state.db_master):,}", "Histórico")
        m2.metric("NPS Satisfacción", f"{st.session_state.db_master['NPS'].mean():.1f} / 5.0")
        st.divider()
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(250), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Edición Estratégica de Fichas Ciudadanas")
        search_id = st.text_input("Ingrese ID de Visita para completar perfil (ej: VIS-100XXX):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_v35"):
                    tel = st.text_input("WhatsApp / Contacto Movil", st.session_state.db_master.at[i, 'Telefono'])
                    mail = st.text_input("Email de Seguimiento Institucional", st.session_state.db_master.at[i, 'Email'])
                    if st.form_submit_button("ACTUALIZAR FICHA CIUDADANA"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        st.success("Inteligencia Ciudadana Actualizada en Big Data.")
        st.markdown("</div>", unsafe_allow_html=True)
    elif "6. Auditoría" in view_mode:
        st.markdown("<h2 class='muni-title'>LOGS DE SISTEMA BLINDADOS</h2>", unsafe_allow_html=True)
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:200]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": 
    main()
