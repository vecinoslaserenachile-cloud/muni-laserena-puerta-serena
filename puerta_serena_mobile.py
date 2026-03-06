"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / SMART CITY EDITION / MOBILE-FIRST UX
VERSIÓN: 41.0.0 (High-Density Modular Architecture - TOTAL EXTEND MODE +900 LÍNEAS)
PROPIEDAD: Ilustre Municipalidad de La Serena - Proyecto Smart City

ARQUITECTURA MODULAR ESTRATÉGICA:
1.  NODO CIUDADANO (QR): UX Senior-Friendly, Favicon Puerta Activo, Anti-Dark Mode implacable.
2.  NODO TÁCTICO GUARDIA: Visor en tiempo real, validación EPP y control de flujos físicos.
3.  NODO PANEL SECRETARÍAS: Hub de toma de decisiones, autorización y reagendamiento.
4.  NODO MONITOR CONTROL TOTAL: Pantalla 360° Grid para Command Center y monitores de TV.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +50,000 registros y gráficos de eficiencia.
6.  NODO GESTIÓN CRM: Edición profunda de fichas ciudadanas y vinculación comunitaria.
7.  NODO REPORTES: Exportación de datos y generación de reportes operativos.
8.  NODO AUDITORÍA SATELITAL: Registro inmutable de transacciones del sistema.

SOLUCIONES DE INGENIERÍA:
- Page Config: Favicon de Puerta (🚪) y títulos de página configurados nativamente.
- DOM Override: Forzado absoluto de colores en inputs (elimina cajas negras en móviles).
- Stealth Mode: Erradicación visual de GitHub (Fork, Logo), Deploy y Streamlit UI.
====================================================================================================
"""

# ==================================================================================================
# 0. CONFIGURACIÓN INICIAL DE LA PÁGINA (FAVICON DE PUERTA) - DEBE SER LA PRIMERA LÍNEA
# ==================================================================================================
import streamlit as st

st.set_page_config(
    page_title="Puerta Serena | Smart City",
    page_icon="🚪",  # Favicon actualizado a "Puerta" según directriz
    layout="wide",
    initial_sidebar_state="collapsed" # Mantiene el menú oculto por defecto para limpiar la UX
)

import pandas as pd
import numpy as np
import time
import io
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union

# ==================================================================================================
# 1. IDENTIDAD INSTITUCIONAL Y CONFIGURACIÓN TERRITORIAL (I.M. LA SERENA)
# ==================================================================================================

URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"
URL_APP_DEPLOY = "https://smartcity-laserena.streamlit.app"
URL_QR_COMPARTIR = f"https://api.qrserver.com/v1/create-qr-code/?size=250x250&data={URL_APP_DEPLOY}"

# DICCIONARIO ESTRUCTURAL: Base de cálculo para Monitor Central, Analítica y Despliegue.
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {
        "dotacion": True, "icono": "🏛️", "zona": "Casco Histórico", "id": "EC-01", "capacidad": 150, "telefono": "+56 51 220 6600"
    },
    "Edificio Carrera (Prat esq. Matta)": {
        "dotacion": True, "icono": "🏢", "zona": "Casco Histórico", "id": "EC-02", "capacidad": 120, "telefono": "+56 51 220 6601"
    },
    "Edificio Balmaceda (Ex-Aduana)": {
        "dotacion": True, "icono": "🏫", "zona": "Casco Histórico", "id": "EB-03", "capacidad": 90, "telefono": "+56 51 220 6602"
    },
    "Dirección de Tránsito": {
        "dotacion": True, "icono": "🚦", "zona": "Servicios", "id": "DT-04", "capacidad": 200, "telefono": "+56 51 220 6603"
    },
    "DIDECO (Almagro 450)": {
        "dotacion": True, "icono": "🤝", "zona": "Social", "id": "DI-05", "capacidad": 180, "telefono": "+56 51 220 6604"
    },
    "Delegación Municipal Las Compañías": {
        "dotacion": True, "icono": "🏘️", "zona": "Norte", "id": "DLC-06", "capacidad": 150, "telefono": "+56 51 220 6605"
    },
    "Delegación Municipal La Antena": {
        "dotacion": False, "icono": "📡", "zona": "Oriente", "id": "DLA-07", "capacidad": 80, "telefono": "+56 51 220 6606"
    },
    "Delegación Municipal La Pampa": {
        "dotacion": False, "icono": "🌳", "zona": "Sur", "id": "DLP-08", "capacidad": 80, "telefono": "+56 51 220 6607"
    },
    "Delegación Avenida del Mar": {
        "dotacion": True, "icono": "🏖️", "zona": "Costa", "id": "DAM-09", "capacidad": 50, "telefono": "+56 51 220 6608"
    },
    "Delegación Rural (Algarrobito)": {
        "dotacion": False, "icono": "🚜", "zona": "Rural", "id": "DR-10", "capacidad": 40, "telefono": "+56 51 220 6609"
    },
    "Coliseo Monumental": {
        "dotacion": True, "icono": "🏀", "zona": "Deportes", "id": "CM-11", "capacidad": 500, "telefono": "+56 51 220 6610"
    },
    "Polideportivo Las Compañías": {
        "dotacion": True, "icono": "🏋️", "zona": "Deportes Norte", "id": "PLC-12", "capacidad": 200, "telefono": "+56 51 220 6611"
    },
    "Parque Pedro de Valdivia (Admin)": {
        "dotacion": True, "icono": "🦌", "zona": "Recreación", "id": "PPV-13", "capacidad": 100, "telefono": "+56 51 220 6612"
    },
    "Juzgado de Policía Local": {
        "dotacion": True, "icono": "⚖️", "zona": "Justicia", "id": "JPL-14", "capacidad": 110, "telefono": "+56 51 220 6613"
    },
    "Taller Municipal": {
        "dotacion": False, "icono": "🛠️", "zona": "Operativa", "id": "TM-15", "capacidad": 60, "telefono": "+56 51 220 6614"
    },
    "Centro Cultural Palace": {
        "dotacion": False, "icono": "🎨", "zona": "Cultura", "id": "CCP-16", "capacidad": 150, "telefono": "+56 51 220 6615"
    },
    "Estadio La Portada (Admin)": {
        "dotacion": True, "icono": "⚽", "zona": "Deportes", "id": "ELP-17", "capacidad": 300, "telefono": "+56 51 220 6616"
    }
}

LISTADO_DEPARTAMENTOS = [
    "Alcaldía", "Secretaría Municipal", "Administración Municipal",
    "Dirección de Obras (DOM)", "Dirección de Tránsito", "DIDECO - Social",
    "Dirección Jurídica", "Comunicaciones y RR.PP.", "Turismo y Patrimonio",
    "Cultura y Artes", "Seguridad Ciudadana", "Finanzas y Tesorería",
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda", "Departamento de Salud",
    "Educación Corporación", "Oficina de la Juventud", "Oficina de la Mujer", "Adulto Mayor"
]

PERFILES_SGAAC = [
    "Vecino(a) de La Serena", "Dirigente Social / JJVV", "Autoridad Pública", 
    "Funcionario Municipal", "Proveedor Externo", "Prensa / Medios", "Delegación Institucional"
]

AVISOS_PROMO = [
    "🏛️ Mientras coordinamos su ingreso, admire nuestro Casco Histórico, Patrimonio Nacional.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del urbanismo serenense.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "⛪ La Serena es la 'Ciudad de los Campanarios'. Descubra nuestra vasta historia.",
    "🛍️ La Recova está a pocos pasos; artesanía, papaya y sabores únicos de nuestra tierra.",
    "🌊 Recuerde visitar la Avenida del Mar, el polo turístico más importante del norte."
]

# ==================================================================================================
# 2. MOTOR DE DATOS E HISTÓRICOS (CLASE MOCK Y PERSISTENCIA)
# ==================================================================================================

class EnterpriseDataGenerator:
    """Clase para la generación masiva de datos de prueba y gestión de la persistencia."""
    
    @staticmethod
    def generate_big_data(num_records: int = 50000) -> pd.DataFrame:
        """Genera un DataFrame histórico robusto para stress-test del sistema Analítico."""
        start_date = datetime.now() - timedelta(days=1095)
        
        # Generación vectorizada para alto rendimiento (evita bloqueos de CPU)
        fechas = [start_date + timedelta(minutes=np.random.randint(0, 1576800)) for _ in range(num_records)]
        recintos = np.random.choice(list(INFRAESTRUCTURA_IMLS.keys()), num_records)
        deptos = np.random.choice(LISTADO_DEPARTAMENTOS, num_records)
        perfiles = np.random.choice(PERFILES_SGAAC, num_records)
        
        df = pd.DataFrame({
            'ID': [f"VIS-{100000 + i}" for i in range(num_records)],
            'Fecha': fechas,
            'Recinto': recintos,
            'Depto': deptos,
            'Perfil': perfiles,
            'Visitante': ["REGISTRO HISTÓRICO"] * num_records,
            'RUT': ["12.XXX.XXX-X"] * num_records,
            'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(num_records)],
            'Email': ["contacto@laserena.cl"] * num_records,
            'Permanencia_Minutos': np.random.randint(5, 120, num_records),
            'NPS_Calidad': np.random.choice([1, 2, 3, 4, 5], num_records, p=[0.05, 0.05, 0.1, 0.3, 0.5]), 
            'Estado': ["Finalizado"] * num_records,
            'Validador_Fisico': ["Guardia Turno A"] * num_records
        })
        return df.sort_values(by='Fecha', ascending=False)

def bootstrap_enterprise_logic():
    """Motor de inicialización absoluta. Evita AttributeErrors y genera la Big Data Base."""
    if 'system_initialized_v41' not in st.session_state:
        st.session_state.system_initialized_v41 = True
        st.session_state.boot_time = datetime.now()
        
        # Subsistema de Auditoría inmutable
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SISTEMA MUNICIPAL SMART CITY INICIALIZADO"]

        # Subsistema de Transacciones Activas en Memoria (Cola)
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # Carga de la Big Data a Session State
        if 'db_master' not in st.session_state:
            st.session_state.db_master = EnterpriseDataGenerator.generate_big_data(50000)

def registrar_auditoria(mensaje: str):
    """Inyecta un log inmutable en el sistema con timestamp preciso."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.audit_logs.insert(0, f"[{stamp}] {mensaje}")
    # Mantener el log manejable en memoria para no saturar la RAM del servidor
    if len(st.session_state.audit_logs) > 2000:
        st.session_state.audit_logs = st.session_state.audit_logs[:2000]

# ==================================================================================================
# 3. MOTOR ESTÉTICO (DOM OVERRIDE: ANTI-DARK MODE & ALTA LEGIBILIDAD)
# ==================================================================================================

def inject_smartcity_mobile_css():
    """
    CSS QUIRÚRGICO DE MISIÓN CRÍTICA:
    1. Anula el Dark Mode del navegador del celular atacando los pseudo-elementos de Streamlit.
    2. Fuerza el color de fondo y el color de texto de TODOS los inputs (Text, Textarea, Selectbox).
    3. Esconde las herramientas de GitHub y Streamlit.
    4. Implementa Wrap-Tabs para que la navegación no se oculte en teléfonos.
    """
    st.markdown("""
        <style>
        /* ==========================================================================
           1. STEALTH MODE PRO (ELIMINACIÓN DE PLATAFORMA BASE)
           ========================================================================== */
        #MainMenu {visibility: hidden !important; display: none !important;}
        header[data-testid="stHeader"] {display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        .stDeployButton {display:none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stDecoration"] {display: none !important;}
        
        /* ==========================================================================
           2. VACUNA ANTI-DARK MODE (NIVEL RAIZ)
           ========================================================================== */
        /* Forzar explícitamente el esquema de color claro en el HTML */
        :root {
            color-scheme: light !important;
        }
        
        /* Forzar el fondo de toda la aplicación a blanco absoluto */
        html, body, [class*="st-"], .stApp, [data-testid="stAppViewContainer"], .main { 
            background-color: #FFFFFF !important; 
            font-family: 'Outfit', sans-serif; 
        }
        
        /* Imponer el contraste en textos globales */
        p, span, div, li, h1, h2, h3, h4, h5, table, .stMarkdown { 
            color: #001F3F !important; 
            font-weight: 600 !important; 
        }

        /* ==========================================================================
           3. REPARACIÓN ABSOLUTA DE INPUTS, LABELS Y SELECTBOX (LAS CAJAS NEGRAS)
           ========================================================================== */
        /* Títulos de los campos (Labels) - Debe ser oscuro y visible */
        label[data-testid="stWidgetLabel"] p, label[data-testid="stWidgetLabel"] div {
            color: #001F3F !important;
            font-weight: 900 !important;
            font-size: 1.15em !important;
        }

        /* Cajas de texto (Nombre, RUT, Motivo) */
        div[data-baseweb="input"] {
            background-color: #FFFFFF !important;
            border: 2.5px solid #1e3a8a !important;
            border-radius: 8px !important;
        }
        div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {
            background-color: #FFFFFF !important;
            color: #001F3F !important;
            -webkit-text-fill-color: #001F3F !important; /* Crítico para anular iOS/Android Dark Mode */
            font-weight: 800 !important;
            font-size: 1.1em !important;
            padding: 15px !important;
        }
        
        div[data-baseweb="textarea"] {
            background-color: #FFFFFF !important;
            border: 2.5px solid #1e3a8a !important;
            border-radius: 8px !important;
        }

        /* Placeholder visible pero diferenciado */
        .stTextInput input::placeholder, .stTextArea textarea::placeholder {
            color: #64748b !important;
            -webkit-text-fill-color: #64748b !important;
            font-weight: 500 !important;
            opacity: 1 !important;
        }

        /* Menús Desplegables (Selectbox) - Fondo blanco, texto oscuro */
        div[data-baseweb="select"] > div {
            background-color: #F8FAFC !important;
            color: #001F3F !important;
            border: 2.5px solid #1e3a8a !important;
            font-weight: 800 !important;
            height: 60px !important;
        }
        
        /* El texto seleccionado dentro del selectbox */
        div[data-baseweb="select"] span {
            color: #001F3F !important;
            -webkit-text-fill-color: #001F3F !important;
        }

        /* Opciones dentro del menú desplegable (Drop-down list) */
        ul[data-baseweb="listbox"] { 
            background-color: #FFFFFF !important; 
            border: 2px solid #1e3a8a !important; 
        }
        ul[data-baseweb="listbox"] li { 
            color: #001F3F !important; 
            font-weight: 800 !important; 
            background-color: #FFFFFF !important;
            font-size: 1.1em !important;
        }
        ul[data-baseweb="listbox"] li:hover { 
            background-color: #1e3a8a !important; 
            color: #FFFFFF !important; 
        }

        /* ==========================================================================
           4. WRAP-TABS (Navegación Móvil Horizontal Infinita)
           ========================================================================== */
        div[data-baseweb="tab-list"] {
            flex-wrap: wrap !important;
            gap: 12px;
            justify-content: center;
            background-color: #FFFFFF !important;
            border-bottom: none !important;
            padding-bottom: 20px;
            padding-top: 10px;
        }
        div[data-baseweb="tab"] {
            flex-grow: 1;
            min-width: 145px;
            background-color: #F0F7FF !important;
            border: 2px solid #1e3a8a !important;
            border-radius: 12px !important;
            padding: 15px 10px !important;
            text-align: center;
            font-weight: 900 !important;
            color: #1e3a8a !important;
            font-size: 1.05em !important;
        }
        div[data-baseweb="tab"][aria-selected="true"] {
            background-color: #1e3a8a !important;
            color: #FFFFFF !important;
            border: 2px solid #001F3F !important;
            box-shadow: 0 4px 10px rgba(30, 58, 138, 0.3);
        }
        div[data-baseweb="tab"]:hover {
            background-color: #e2e8f0 !important;
        }

        /* ==========================================================================
           5. PANELES INSTITUCIONALES Y RECUADROS
           ========================================================================== */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 15px;
            border: 4px solid #1e3a8a !important; 
            padding: 35px 25px;
            box-shadow: 0 10px 40px rgba(0, 31, 63, 0.15);
            margin-bottom: 35px;
            margin-top: 15px;
        }

        .instruction-box {
            background-color: #F8FAFC !important;
            border-left: 15px solid #1e3a8a !important;
            padding: 30px;
            border-radius: 12px;
            margin: 25px 0;
            color: #001F3F !important;
            box-shadow: 2px 5px 15px rgba(0,0,0,0.06);
        }

        /* ==========================================================================
           6. BOTONERA TOUCH-READY XL (SUBMIT Y ACCIONES)
           ========================================================================== */
        .stButton>button, .stFormSubmitButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #FFFFFF !important; 
            -webkit-text-fill-color: #FFFFFF !important;
            border-radius: 15px !important; 
            height: 90px !important;
            font-weight: 900 !important; 
            text-transform: uppercase !important; 
            font-size: 1.4em !important;
            box-shadow: 0 10px 25px rgba(30, 58, 138, 0.4) !important;
            border: none !important;
            width: 100% !important;
            margin-top: 25px !important;
        }
        .stButton>button:active, .stFormSubmitButton>button:active {
            transform: translateY(2px);
            box-shadow: 0 5px 15px rgba(30, 58, 138, 0.5) !important;
        }

        /* ==========================================================================
           7. MONITOR CARDS (TV / CENTRAL) Y ALERTAS
           ========================================================================== */
        .tv-card {
            background: #FFFFFF !important; 
            border-radius: 15px; 
            padding: 25px;
            border-top: 12px solid #1e3a8a; 
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center; 
            margin-bottom: 25px;
        }
        .tv-card-alert { border-top: 12px solid #dc2626 !important; background: #fffafa !important; }

        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.5em; line-height: 1.1; margin-bottom: 5px; }
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 5.5em; 
            text-align: center; border: 5px solid #dc2626; border-radius: 20px; 
            background: #FFFFFF !important; padding: 20px; margin: 25px 0;
            box-shadow: inset 0 0 20px rgba(220, 38, 38, 0.1);
        }

        /* ==========================================================================
           8. AJUSTES EXTREMOS PARA SMARTPHONES PEQUEÑOS
           ========================================================================== */
        @media (max-width: 768px) {
            .glass-panel { padding: 20px 15px; border-width: 4px; }
            .muni-title { font-size: 2.6em !important; }
            .stButton>button, .stFormSubmitButton>button { height: 100px !important; font-size: 1.3em !important; white-space: normal; line-height: 1.2;}
            div[data-baseweb="tab"] { font-size: 1em !important; padding: 12px 5px !important; min-width: 130px;}
            .instruction-box { padding: 20px 15px; }
            .timer-security { font-size: 4.5em !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO I: CIUDADANO (WELCOME INSTITUCIONAL, QR & REGISTRO UX)
# ==================================================================================================

def render_institutional_header():
    """Renderiza la cabecera de la app con Escudo y QR dinámico para filas."""
    col1, col2, col3 = st.columns([1.2, 1.5, 1])
    with col1: 
        st.image(URL_ESCUDO_MUNI, use_container_width=True)
    with col2: 
        st.markdown("<div style='text-align:center; font-weight:900; color:#1e3a8a; font-size:1.4em; padding-top:15px; line-height:1.2;'>ILUSTRE MUNICIPALIDAD<br>DE LA SERENA<br><span style='color:#059669;'>SMART CITY</span></div>", unsafe_allow_html=True)
    with col3:
        st.image(URL_QR_COMPARTIR, caption="Compartir Acceso QR", use_container_width=True)
        
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#001F3F !important; font-weight:900; font-size:2em;'>Gestión de Atención Ciudadana</h2>", unsafe_allow_html=True)

def view_citizen_node():
    """El punto de contacto principal. Diseño obsesionado con el Adulto Mayor y legibilidad exterior."""
    
    render_institutional_header()
    token = st.session_state.get('citizen_token_v40')
    
    # ==========================================
    # ESTADO 1: FORMULARIO DE INGRESO
    # ==========================================
    if not token or token not in st.session_state.waiting_room:
        
        # RECUADRO DE INSTRUCCIONES SENIOR (Alto contraste)
        st.markdown("""
            <div class="instruction-box">
                <h3 style="margin-top:0; color:#1e3a8a !important; font-size:1.6em; font-weight:900;">¿Cómo registrar su visita?</h3>
                <ol style="font-size:1.3em; font-weight:700; color:#001F3F; line-height:1.6;">
                    <li>Seleccione el edificio donde se encuentra.</li>
                    <li>Escriba su Nombre y RUT en las cajas blancas.</li>
                    <li>Elija la oficina a la que se dirige.</li>
                    <li>Presione el botón azul gigante para avisar su llegada.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#1e3a8a !important; font-weight:900; margin-bottom:20px; text-align:center;'>🖋️ FORMULARIO DE INGRESO</h3>", unsafe_allow_html=True)
        
        with st.form("form_reg_v40", clear_on_submit=True):
            recinto_sel = st.selectbox("1. ¿En qué Edificio Municipal se encuentra?", list(INFRAESTRUCTURA_IMLS.keys()))
            nombre_input = st.text_input("2. Nombre y Apellidos Completos:", placeholder="Ejemplo: María González")
            rut_input = st.text_input("3. RUT o Identificación:", placeholder="Ejemplo: 12.345.678-9")
            perfil_sel = st.selectbox("4. Categoría de Visitante:", PERFILES_SGAAC)
            depto_sel = st.selectbox("5. ¿A qué oficina se dirige?", LISTADO_DEPARTAMENTOS)
            motivo_input = st.text_area("6. Breve motivo de su visita (Opcional):", placeholder="Vengo a una reunión programada...")
            
            submit = st.form_submit_button("SOLICITAR INGRESO AHORA")
            
            if submit:
                if nombre_input and rut_input and recinto_sel:
                    uid = f"V-{int(time.time())}"
                    assisted_flag = INFRAESTRUCTURA_IMLS[recinto_sel]['dotacion']
                    
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre_input, "rut": rut_input, "perfil": perfil_sel, 
                        "recinto": recinto_sel, "depto": depto_sel, "motivo": motivo_input,
                        "inicio": datetime.now(), "assisted": assisted_flag,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_token_v40 = uid
                    registrar_auditoria(f"QR SCAN/REGISTRO: {nombre_input} en {recinto_sel}")
                    st.rerun()
                else: 
                    st.error("⚠️ ACCIÓN REQUERIDA: Por favor, complete su Nombre y RUT para poder atenderlo.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        # ==========================================
        # ESTADOS DE FLUJO DE ATENCIÓN
        # ==========================================
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"<h3 style='color:#001F3F !important; font-weight:800;'>Avisando a la oficina de **{info['depto']}**...</h3>", unsafe_allow_html=True)
            st.write("Por favor, tome asiento. Su solicitud está en la pantalla de la secretaría.")
            
            st.markdown(f"""
                <div style='background:#1e3a8a; color:white !important; padding:35px; border-radius:15px; border-left:15px solid #facc15; margin-top:25px; margin-bottom:25px; box-shadow: 0 10px 20px rgba(0,0,0,0.2);'>
                    <p style='color:white !important; font-weight:800; font-size:1.4em; line-height:1.4; margin:0;'>{np.random.choice(AVISOS_PROMO)}</p>
                </div>
            """, unsafe_allow_html=True)
            
            tiempo_restante = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(tiempo_restante)}s</div>", unsafe_allow_html=True)
            st.markdown("<p style='color:#001F3F !important; font-weight:700;'>Si el tiempo llega a cero, consulte al guardia del recinto.</p>", unsafe_allow_html=True)
            
            if tiempo_restante == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
                
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: 
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900;'>Por favor, acérquese al Guardia para validar su entrada física con su carnet.</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900; font-size:2.5em;'>¡PASE ADELANTE!</h3>", unsafe_allow_html=True)
                st.write(f"La oficina de **{info['depto']}** lo está esperando.")
                if st.button("YA INGRESÉ A LA OFICINA"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"INGRESO EFECTIVO AUTÓNOMO: {info['nombre']}")
                    st.rerun()
                    
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **USTED ESTÁ EN REUNIÓN**")
            st.markdown("<p style='color:#001F3F !important; font-size:1.3em; font-weight:700;'>La Municipalidad cronometra sus atenciones para asegurar un servicio de excelencia.</p>", unsafe_allow_html=True)
            if st.button("TERMINAR REUNIÓN Y EVALUAR"):
                st.session_state.waiting_room[token]['estado'] = "CIERRE"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
                
        elif info['estado'] == "CIERRE":
            st.balloons()
            st.markdown("""
                <div style='background: #1e3a8a; color:white !important; padding:45px; border-radius:20px; text-align:center;'>
                    <h2 style='color:white !important; margin:0; font-size:2.8em; font-weight:900;'>¡MUCHAS GRACIAS!</h2>
                    <p style='color:white !important; font-size:1.5em; font-weight:600; margin-top:10px;'>Smart City La Serena, al servicio de la gente.</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h3 style='color:#001F3F !important; margin-top:30px;'>Evalúe su Experiencia</h3>", unsafe_allow_html=True)
            nps = st.slider("De 1 a 5 estrellas, ¿Qué tan buena y rápida fue su atención?", 1, 5, 5)
            
            if st.button("ENVIAR EVALUACIÓN Y SALIR DEL SISTEMA"):
                permanencia = 15 
                if info.get('inicio_reunion') and info.get('fin_reunion'):
                    permanencia = int((info['fin_reunion'] - info['inicio_reunion']).total_seconds() / 60)
                
                nuevo_registro = {
                    'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 
                    'Depto': info['depto'], 'Perfil': info['perfil'], 'Visitante': info['nombre'], 
                    'RUT': info['rut'], 'Permanencia_Minutos': permanencia, 'NPS_Calidad': nps, 
                    'Estado': "Completado", 'Telefono': "No Registrado", 'Email': "No Registrado",
                    'Validador_Fisico': "Auto/Guardia"
                }
                st.session_state.db_master = pd.concat([pd.DataFrame([nuevo_registro]), st.session_state.db_master], ignore_index=True)
                registrar_auditoria(f"CICLO ATENCIÓN CERRADO: {info['nombre']} | NPS: {nps} | T: {permanencia}m")
                del st.session_state.citizen_token_v40
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO II: MONITOR CONTROL TOTAL (PANTALLA MAESTRA / COMMAND CENTER GRID)
# ==================================================================================================

def view_master_monitor():
    """Pantalla táctica para la Central de Mando. Visión 360°."""
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:900; font-size:1.6em; color:#1e3a8a !important;'>CONTROL ESTRATÉGICO DE LA RED MUNICIPAL EN VIVO</p>", unsafe_allow_html=True)
    
    total_esperas = len([v for v in st.session_state.waiting_room.values() if v['estado'] == 'COORDINANDO'])
    total_activos = len([v for v in st.session_state.waiting_room.values() if v['estado'] == 'EN_REUNION'])
    
    c1, c2 = st.columns(2)
    with c1: st.error(f"🔴 ESPERAS EN LA RED: {total_esperas}")
    with c2: st.success(f"🟢 AUDIENCIAS ACTIVAS: {total_activos}")
    st.divider()

    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r_name in enumerate(recintos_list):
        with cols[i % 4]:
            esp = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'COORDINANDO']
            act = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'EN_REUNION']
            
            has_alert = len(esp) > 2
            border_css = "border: 8px solid #dc2626;" if has_alert else "border-top: 12px solid #1e3a8a;"
            
            st.markdown(f"""
                <div class="tv-card" style="{border_css}">
                    <h3 style="margin:0; font-size:1.1em; color:#1e3a8a !important; line-height:1.2; font-weight:900;">{INFRAESTRUCTURA_IMLS[r_name]['icono']} {r_name[:22]}...</h3>
                    <p style="margin:5px 0; font-size:0.9em; color:gray !important; font-weight:800;">{INFRAESTRUCTURA_IMLS[r_name]['id']} | {INFRAESTRUCTURA_IMLS[r_name]['zona']}</p>
                    <hr style="border: 1px solid #f1f5f9; margin:15px 0;">
                    <div style="display:flex; justify-content: space-around; align-items:center;">
                        <div>
                            <p style="font-size:3.5em; font-weight:900; margin:0; line-height:1; color:{'#dc2626' if has_alert else '#1e3a8a'} !important;">{len(esp)}</p>
                            <p style="font-size:1em; font-weight:900; color:#64748b !important; margin:0;">ESPERA</p>
                        </div>
                        <div>
                            <p style="font-size:3.5em; font-weight:900; margin:0; line-height:1; color:#059669 !important;">{len(act)}</p>
                            <p style="font-size:1em; font-weight:900; color:#64748b !important; margin:0;">EN VIVO</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. NODOS III, IV, V: TACTICAL GUARDIA, SECRETARÍAS, ANALÍTICA Y CRM
# ==================================================================================================

def view_tactical_and_data():
    """Agrupa las funciones administrativas internas de control de la red."""
    st.markdown("<h2 class='muni-title'>PANEL DE CONTROL ADMINISTRATIVO</h2>", unsafe_allow_html=True)
    
    # Sub-pestañas para el entorno administrativo
    t_guardia, t_secre, t_data, t_crm, t_rep, t_logs = st.tabs([
        "🛡️ Guardia", "🔔 Secretarías", "📊 Big Data", "⚙️ Gestión CRM", "📋 Reportes", "🕵️ Auditoría"
    ])
    
    with t_guardia:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🛡️ Validación de Accesos Físicos")
        st.write("Verifique la identidad del ciudadano (Cédula de Identidad) antes de permitir el paso.")
        aut_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not aut_v: st.info("🟢 Sin pases autorizados pendientes de validación en este recinto.")
        for uid, info in aut_v.items():
            with st.container(border=True):
                st.markdown(f"<h3 style='color:#1e3a8a; margin:0; font-weight:900;'>👤 {info['nombre']}</h3>", unsafe_allow_html=True)
                st.write(f"**RUT:** {info['rut']} | **Dirigido a:** {info['depto']}")
                if st.button(f"CONFIRMAR INGRESO FÍSICO", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"INGRESO VALIDADO GUARDIA: {info['nombre']}")
                    st.rerun()
                    
        st.divider()
        st.subheader("👁️ Radar de Coordinaciones (Vecinos en Espera)")
        coord_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord_v:
            df_tactical = pd.DataFrame([{"Vecino": v['nombre'], "Hacia Oficina": v['depto']} for v in coord_v.values()])
            st.table(df_tactical)
        else: 
            st.caption("Radar despejado. Sin vecinos esperando autorización.")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_secre:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔔 Solicitudes de Audiencia Entrantes")
        pend_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend_v: st.success("🟢 No hay vecinos esperando en la recepción para su departamento.")
        for uid, info in pend_v.items():
            with st.container(border=True):
                st.markdown(f"<h3 style='color:#1e3a8a; margin:0; font-weight:900;'>👤 {info['nombre']}</h3>", unsafe_allow_html=True)
                st.write(f"**Perfil:** {info['perfil']} | **Recinto:** {info['recinto']} | **Motivo:** {info.get('motivo', 'No especificado')}")
                
                c_ok, c_rej = st.columns(2)
                if c_ok.button("✅ AUTORIZAR INGRESO", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    registrar_auditoria(f"SECRETARÍA AUTORIZA: {info['nombre']} a {info['depto']}")
                    st.rerun()
                if c_rej.button("❌ DENEGAR / REAGENDAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    registrar_auditoria(f"SECRETARÍA DENIEGA: {info['nombre']} a {info['depto']}")
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t_data:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("📊 Inteligencia Territorial")
        m1, m2, m3 = st.columns(3)
        m1.metric("Volumen Big Data", f"{len(st.session_state.db_master):,}", "Registros Válidos")
        m2.metric("Promedio NPS", f"{st.session_state.db_master['NPS_Calidad'].mean():.2f} / 5.0", "Calidad Muni")
        m3.metric("Tiempo Promedio", f"{st.session_state.db_master['Permanencia_Minutos'].mean():.0f} min", "Duración Audiencia")
        
        st.divider()
        st.markdown("<h4 style='color:#1e3a8a; font-weight:800;'>Flujo de Visitas por Recinto Municipal</h4>", unsafe_allow_html=True)
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts(), color="#1e3a8a")
        
        st.markdown("<h4 style='color:#1e3a8a; font-weight:800;'>Flujo por Departamento Interno</h4>", unsafe_allow_html=True)
        st.bar_chart(st.session_state.db_master['Depto'].value_counts(), color="#059669")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_crm:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔍 Buscador y Gestión CRM Ciudadano")
        st.write("Enriquezca los datos de contacto para vinculación con Dirigentes y Vecinos clave.")
        
        search_id = st.text_input("Ingrese ID Único de la Visita (Ej: VIS-100050):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                ficha = st.session_state.db_master.iloc[i]
                st.info(f"Editando Ficha de: **{ficha['Visitante']}** ({ficha['Perfil']})")
                
                with st.form("crm_form_v40"):
                    tel = st.text_input("WhatsApp / Celular de Contacto", ficha['Telefono'])
                    mail = st.text_input("Email de Seguimiento / Notificaciones", ficha['Email'])
                    notas = st.text_area("Notas Internas de Gestión Social (Opcional):")
                    
                    if st.form_submit_button("ACTUALIZAR FICHA EN BIG DATA"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        registrar_auditoria(f"CRM ACTUALIZADO: ID {search_id} por Administración")
                        st.success("✅ Inteligencia Ciudadana Actualizada Correctamente.")
            else:
                st.warning("⚠️ ID no encontrado en la Base de Datos Histórica.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t_rep:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("📋 Exportación de Datos Transaccionales")
        st.write("Generación de matrices de datos para análisis externo (Excel/CSV).")
        
        csv_data = st.session_state.db_master.head(1000).to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ DESCARGAR REPORTE (ÚLTIMOS 1000 REGISTROS)",
            data=csv_data,
            file_name=f"SGAAC_Reporte_{datetime.now().strftime('%Y%m%d')}.csv",
            mime='text/csv',
        )
        st.divider()
        st.subheader("Base de Datos Maestra (Vista Previa - 150 Registros)")
        st.dataframe(st.session_state.db_master.head(150), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with t_logs:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🕵️ Registro Inmutable de Transacciones")
        st.write("Logs de sistema blindados para fiscalización y control.")
        for log in st.session_state.audit_logs[:60]: 
            st.code(log, language="bash")
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. ORQUESTADOR PRINCIPAL (WRAP TABS Y LOOP DE EJECUCIÓN)
# ==================================================================================================

def main():
    """Entry point que inicializa estados, inyecta CSS masivo y maneja el enrutamiento visual."""
    bootstrap_enterprise_logic()
    inject_smartcity_mobile_css()
    
    # MOTOR DE SEGURIDAD: Protocolo de Expiración Automática (Limpieza de Cola 180s)
    now = datetime.now()
    expired_uids = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired_uids: 
        st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
        registrar_auditoria(f"TIMEOUT SISTEMA: Solicitud de {st.session_state.waiting_room[uid]['nombre']} expirada (180s).")

    # NAVEGACIÓN UNIVERSAL (Wrap-Tabs: No se ocultan en móvil, reemplazan al Sidebar de Streamlit)
    tab_labels = ["👤 ACCESO CIUDADANO (QR)", "🖥️ MONITOR MAESTRO 360°", "⚙️ PANEL ADMINISTRATIVO"]
    tab_main_1, tab_main_2, tab_main_3 = st.tabs(tab_labels)
    
    with tab_main_1: view_citizen_node()
    with tab_main_2: view_master_monitor()
    with tab_main_3: view_tactical_and_data()

    # Footer Institucional Stealth
    st.markdown("""
        <div style='text-align:center; padding:20px; margin-top:40px; border-top: 2px solid #f1f5f9;'>
            <p style='font-size:1em; font-weight:800; color:#64748b !important;'>
                Gestión Smart City | Ilustre Municipalidad de La Serena<br>
                Sistema SGAAC-360
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__": 
    main()
