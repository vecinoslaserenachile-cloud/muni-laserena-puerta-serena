"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / SMART CITY EDITION / MISIÓN CRÍTICA / ULTRA-LEGIBILIDAD
VERSIÓN: 42.0.0 (High-Density Modular Architecture - EXTEND MODE +1000 LINES)
PROPIEDAD: Ilustre Municipalidad de La Serena - Proyecto Smart City Chile

ARQUITECTURA MODULAR DE 8 NODOS ESTRATÉGICOS:
1.  NODO CIUDADANO (QR): Recepción, Doble Logo HTML (con fijación de bordes), QR Compartible.
2.  NODO ANTI-DARK MODE: Vacuna CSS radical de forzado de contraste para legibilidad en móviles.
3.  NODO TÁCTICO GUARDIA: Monitor en tiempo real, validación EPP y control de flujos físicos.
4.  NODO PANEL SECRETARÍAS: Hub de toma de decisiones, autorización y reagendamiento.
5.  NODO MONITOR CONTROL TOTAL: Visión 360° (Grid) para Command Center y monitores de TV.
6.  NODO ANALÍTICA BIG DATA: Motor de procesamiento masivo (+60,000 registros históricos).
7.  NODO GESTIÓN CRM: Edición, búsqueda y trazabilidad profunda de fichas ciudadanas.
8.  NODO AUDITORÍA SATELITAL: Registro inmutable de transacciones del sistema.

INNOVACIONES TÉCNICAS Sgaac-360 v42.0:
- Favicon Activo: Portón (🚪) configurado nativamente.
- HTML Header: Logos institucionales servidos vía HTML img con padding inferior blindado (anti-recorte).
- CSS DOM Forced Light: Anulación absoluta del Modo Oscuro nativo de iOS/Android en inputs y textos.
- Zero Branding Externo: Propiedad visual 100% Smart City La Serena.
====================================================================================================
"""

import streamlit as st

# ==================================================================================================
# 0. CONFIGURACIÓN INICIAL DE LA PÁGINA (FAVICON PORTÓN Y METADATOS)
# ==================================================================================================
# Debe ejecutarse antes de cualquier otra importación o comando de Streamlit.
st.set_page_config(
    page_title="Puerta Serena | SGAAC-360 Smart City Chile",
    page_icon="🚪", # Favicon Tipo Portón/Puerta Abierta Activo
    layout="wide",
    initial_sidebar_state="collapsed" # Maximizar espacio útil en móviles
)

import pandas as pd
import numpy as np
import time
import io
import base64
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union, NoReturn

# ==================================================================================================
# 1. CONSTANTES INSTITUCIONALES, IDENTIDAD Y MAPA TERRITORIAL
# ==================================================================================================

# RECURSOS GRÁFICOS INSTITUCIONALES (Gama Alta)
# Logo de la I. Municipalidad de La Serena
URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"
# URL de despliegue final (Ajustar cuando esté productivo)
URL_APP_DEPLOY = "https://puertaserena.laserena.cl"
# Generador dinámico de QR de alta resolución para compartir acceso en fila
URL_QR_COMPARTIR = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={URL_APP_DEPLOY}"

# DICCIONARIO ESTRUCTURAL: INFRAESTRUCTURA DE RED Terrritorial
# Incluye metadata crítica: Flag de dotación física (asistido/autónomo), Icono, Zona, ID Único y Capacidad.
# Esta base de datos estructura el Monitor Central y la Analítica Big Data.
INFRAESTRUCTURA_IMLS: Dict[str, Dict[str, Any]] = {
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

LISTADO_DEPARTAMENTOS: List[str] = [
    "Alcaldía", "Secretaría Municipal", "Administración Municipal",
    "Dirección de Obras (DOM)", "Dirección de Tránsito", "DIDECO - Social",
    "Dirección Jurídica", "Comunicaciones y RR.PP.", "Turismo y Patrimonio",
    "Cultura y Artes", "Seguridad Ciudadana", "Finanzas y Tesorería",
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda", "Departamento de Salud",
    "Educación Corporación", "Oficina de la Juventud", "Oficina de la Mujer", "Adulto Mayor"
]

PERFILES_SGAAC: List[str] = [
    "Vecino(a) de La Serena", "Dirigente Social / JJVV", "Autoridad Pública", 
    "Funcionario Municipal", "Proveedor Externo", "Prensa / Medios", "Delegación Institucional"
]

# MARKETING TERRITORIAL ROTATIVO (Promoción Smart City)
AVISOS_PROMO: List[str] = [
    "🏛️ Mientras coordinamos su ingreso, admire nuestro Casco Histórico, Patrimonio Nacional.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del urbanismo serenense.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "⛪ La Serena es la 'Ciudad de los Campanarios'. Descubra nuestra historia.",
    "🛍️ La Recova está a pocos pasos; artesanía, papaya y sabores únicos de nuestra tierra.",
    "🌊 Recuerde visitar la Avenida del Mar, el polo turístico más importante del norte."
]

# INSTRUCCIONES SENIOR-FRIENDLY HTML (Formato XL para pantallas táctiles)
TEXTO_INSTRUCCIONES_HTML = """
<ul style="font-size:1.35em; font-weight:800; color:#001F3F !important; line-height:1.6; margin-top:10px;">
    <li>Seleccione el edificio municipal en el que se encuentra ahora.</li>
    <li>Escriba su Nombre Completo y su RUT.</li>
    <li>Elija la oficina que desea visitar.</li>
    <li>Presione el <b style="color:#1e3a8a;">BOTÓN AZUL GRANDE</b> al final.</li>
</ul>
"""

# ==================================================================================================
# 2. MOTOR CORE DE DATOS E HISTÓRICOS (INTELIGENCIA TERRITORIAL BIG DATA)
# ==================================================================================================

class SmartCityDataEngine:
    """Clase para la generación masiva de datos Mock y gestión de la persistencia Big Data."""
    
    @staticmethod
    def generate_stress_data(num_records: int = 60000) -> pd.DataFrame:
        """
        Genera un DataFrame histórico robusto para stress-test del sistema Analítico.
        Simula flujos reales de 3 años de operación municipal territoral.
        """
        st.cache_data.clear() # Limpiar cache previo
        start_date = datetime.now() - timedelta(days=1095)
        
        # Generación vectorizada (Alto rendimiento en Python)
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

def bootstrap_enterprise_logic() -> NoReturn:
    """Motor de inicialización absoluta de Session State. Previene AttributeErrors y KeyErrors."""
    # Uso de flag específico de versión para forzar recarga en actualizaciones de estructura de datos
    FLAG_VERSION = 'sgaac_initialized_v42'
    
    if FLAG_VERSION not in st.session_state:
        st.session_state[FLAG_VERSION] = True
        st.session_state.boot_time = datetime.now()
        
        # Subsistema de Auditoría (Inmutable en front-end)
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SGAAC-360 MISIÓN CRÍTICA ACTIVO - I.M. LA SERENA"]

        # Subsistema de Transacciones Activas (Cola de espera en memoria)
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # Subsistema CRM / Inteligencia Ciudadana (Caching temporal)
        if 'crm_cache' not in st.session_state:
            st.session_state.crm_cache = {}

        # Subsistema Big Data Histórico (60,000 registros vectorizados)
        if 'db_master' not in st.session_state:
            with st.spinner("Inicializando Motor Big Data Municipal (+60,000 registros)..."):
                st.session_state.db_master = SmartCityDataEngine.generate_stress_data(60000)
                registrar_auditoria("BIG DATA: Base de datos histórica de 60,000 registros precargada vectorialmente.")

def registrar_auditoria(mensaje: str) -> None:
    """Inyecta un log inmutable en el sistema con timestamp preciso para fiscalización."""
    # Blindaje contra AttributeErrors si el motor no se ha bootstrapeado
    if 'audit_logs' not in st.session_state:
        st.session_state.audit_logs = []
        
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.audit_logs.insert(0, f"[{stamp}] {mensaje}")
    # Limpieza cíclica del log para preservar rendimiento de la app
    if len(st.session_state.audit_logs) > 2000:
        st.session_state.audit_logs = st.session_state.audit_logs[:2000]

# ==================================================================================================
# 3. NODO II: MOTOR ESTÉTICO BLINDADO (DOM OVERRIDE: ANTI-DARK MODE & ALTA LEGIBILIDAD)
# ==================================================================================================

def inject_smartcity_sovereign_css() -> None:
    """
    CSS QUIRÚRGICO DE MISIÓN CRÍTICA:
    1. Page Config Override: Fuerza el esquema de color claro a nivel de navegador.
    2. DOM Forced Legibility: Ataca selectores nativos de Streamlit para anular Modo Oscuro nativo de iOS/Android.
    3. Input Injection: Fuerza fondos blancos y textos Azul Marino en todos los inputs (Text, Textarea, Selectbox).
    4. Stealth Mode: Erradicación visual de GitHub, Deploy y Streamlit UI.
    """
    
    # DEFINICIÓN DE PALETA SMART CITY LA SERENA
    COLOR_BG_PURE = "#FFFFFF"     # Blanco Puro Nieve
    COLOR_NAVY_IMPERIAL = "#001F3F" # Azul Marino Profundo (Legibilidad Máxima)
    COLOR_MUNI_BLUE = "#1e3a8a"   # Azul Municipal Institucional (Botones)
    COLOR_MUNI_ALERT = "#dc2626"  # Rojo Alerta Municipal (Semaforización)
    COLOR_TEXT_SOFT = "#64748b"   # Gris Suave (Subtítulos/Captions)

    st.markdown(f"""
        <style>
        /* ==========================================================================
           1. STEALTH MODE PRO (ERADICACIÓN DE IDENTIDAD DE PLATAFORMA BASE)
           ========================================================================== */
        /* Ocultar menú de hamburguesa native de Streamlit */
        #MainMenu {{visibility: hidden !important; display: none !important;}}
        /* Ocultar cabecera transparente nativa */
        header[data-testid="stHeader"] {{display: none !important;}}
        /* Ocultar footer nativo */
        footer {{visibility: hidden !important; display: none !important;}}
        /* Ocultar botón 'Deploy' de la barra superior */
        .stDeployButton {{display:none !important;}}
        /* Ocultar barra de herramientas de widgets */
        [data-testid="stToolbar"] {{display: none !important;}}
        /* Ocultar estado de carga (Running widget) */
        [data-testid="stStatusWidget"] {{display: none !important;}}
        /* Ocultar línea de decoración de Streamlit */
        [data-testid="stDecoration"] {{display: none !important;}}
        
        /* ==========================================================================
           2. VACUNA ANTI-DARK MODE (FORZADO DE CONTRASTE A NIVEL DOM)
           ========================================================================== */
        /* Forzar explícitamente el esquema de color claro en el navegador del móvil */
        :root {{
            color-scheme: light !important;
        }}
        
        /* Forzar el fondo de toda la aplicación a blanco absoluto y tipografía Outfit */
        html, body, [class*="st-"], .stApp, [data-testid="stAppViewContainer"], .main {{ 
            background-color: {COLOR_BG_PURE} !important; 
            font-family: 'Outfit', sans-serif; 
        }
        
        /* Imponer Azul Marino Profundo (#001F3F) en TODAS las etiquetas y textos genéricos */
        p, span, div, li, h1, h2, h3, h4, h5, table, .stMarkdown, strong {{ 
            color: {COLOR_NAVY_IMPERIAL} !important; 
            font-weight: 600 !important; 
        }
        
        /* Asegurar legibilidad XL de subtítulosinstitucionales */
        h2 {{ 
            color: {COLOR_NAVY_IMPERIAL} !important; 
            font-weight: 900 !important; 
            font-size: 1.8em !important;
        }

        /* ==========================================================================
           3. REPARACIÓN ABSOLUTA DE INPUTS, LABELS Y SELECTBOX (ELIMINACIÓN CAJAS NEGRAS)
           ========================================================================== */
        /* Títulos de los campos (Widget Labels) - Deben ser Azul Marino y Ultra-Visibles */
        label[data-testid="stWidgetLabel"] p, label[data-testid="stWidgetLabel"] div, label p {{
            color: {COLOR_NAVY_IMPERIAL} !important;
            font-weight: 900 !important;
            font-size: 1.15em !important;
            -webkit-text-fill-color: {COLOR_NAVY_IMPERIAL} !important;
        }

        /* Blindaje de Cajas de texto y Textareas (Anti-Dark Mode Android/iOS) */
        div[data-baseweb="input"] {{
            background-color: {COLOR_BG_PURE} !important;
            border: 2.5px solid {COLOR_MUNI_BLUE} !important;
            border-radius: 10px !important;
        }
        div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {{
            background-color: {COLOR_BG_PURE} !important;
            color: {COLOR_NAVY_IMPERIAL} !important;
            -webkit-text-fill-color: {COLOR_NAVY_IMPERIAL} !important; /* Fuerza el color en iOS Safari Forced Dark */
            font-weight: 800 !important;
            font-size: 1.1em !important;
            padding: 15px !important;
        }
        
        div[data-baseweb="textarea"] {{
            background-color: {COLOR_BG_PURE} !important;
            border: 2.5px solid {COLOR_MUNI_BLUE} !important;
            border-radius: 10px !important;
        }

        /* Asegurar que el placeholder no sea blanco sobre blanco en móviles */
        .stTextInput input::placeholder, .stTextArea textarea::placeholder {{
            color: {COLOR_TEXT_SOFT} !important;
            -webkit-text-fill-color: {COLOR_TEXT_SOFT} !important;
            font-weight: 500 !important;
            opacity: 1 !important;
        }

        /* Menús Desplegables (Selectbox / Listbox) */
        div[data-baseweb="select"] > div {{
            background-color: #F8FAFC !important; /* Crema suave para inputs no editables */
            color: {COLOR_NAVY_IMPERIAL} !important;
            border: 2.5px solid {COLOR_MUNI_BLUE} !important;
            font-weight: 800 !important;
            height: 60px !important;
        }
        
        /* El texto seleccionado dentro de la caja del selectbox */
        div[data-baseweb="select"] span {{
            color: {COLOR_NAVY_IMPERIAL} !important;
            -webkit-text-fill-color: {COLOR_NAVY_IMPERIAL} !important;
        }

        /* El contenedor de las opciones (Drop-down list) */
        ul[data-baseweb="listbox"] {{ 
            background-color: {COLOR_BG_PURE} !important; 
            border: 2.5px solid {COLOR_MUNI_BLUE} !important; 
        }
        /* Las opciones individuales dentro de la lista */
        ul[data-baseweb="listbox"] li {{ 
            color: {COLOR_NAVY_IMPERIAL} !important; 
            font-weight: 800 !important; 
            background-color: {COLOR_BG_PURE} !important;
            font-size: 1.1em !important;
        }
        /* Estilo de la opción al pasar el mouse (hover) */
        ul[data-baseweb="listbox"] li:hover {{ 
            background-color: {COLOR_MUNI_BLUE} !important; 
            color: {COLOR_BG_PURE} !important; 
        }

        /* ==========================================================================
           4. WRAP-TABS (Navegación Móvil Táctica Adaptativa)
           ========================================================================== */
        div[data-baseweb="tab-list"] {{
            flex-wrap: wrap !important;
            gap: 12px;
            justify-content: center;
            background-color: {COLOR_BG_PURE} !important;
            border-bottom: none !important;
            padding-bottom: 20px;
            padding-top: 10px;
        }
        div[data-baseweb="tab"] {{
            flex-grow: 1;
            min-width: 150px;
            background-color: #F0F7FF !important; /* Azul muy suave para inactivos */
            border: 2.5px solid {COLOR_MUNI_BLUE} !important;
            border-radius: 12px !important;
            padding: 15px 10px !important;
            text-align: center;
            font-weight: 900 !important;
            color: {COLOR_MUNI_BLUE} !important;
            font-size: 1.05em !important;
        }
        /* Pestaña activa (Asegurar contraste máximo Navy/White) */
        div[data-baseweb="tab"][aria-selected="true"] {{
            background-color: {COLOR_MUNI_BLUE} !important;
            color: {COLOR_BG_PURE} !important;
            border: 2.5px solid {COLOR_NAVY_IMPERIAL} !important;
            box-shadow: 0 4px 12px rgba(30, 58, 138, 0.4);
        }
        div[data-baseweb="tab"]:hover {{
            background-color: #e2e8f0 !important;
        }

        /* ==========================================================================
           5. PANELES INSTITUCIONALES Y RECUADROS DE INSTRUCCIONES
           ========================================================================== */
        .glass-panel {{
            background: {COLOR_BG_PURE} !important; 
            border-radius: 15px;
            border: 4px solid {COLOR_MUNI_BLUE} !important; 
            padding: 35px 25px;
            box-shadow: 0 10px 45px rgba(0, 31, 63, 0.18);
            margin-bottom: 40px;
            margin-top: 15px;
        }

        .instruction-box {{
            background-color: #F8FAFC !important;
            border-left: 15px solid {COLOR_MUNI_BLUE} !important;
            padding: 30px;
            border-radius: 12px;
            margin: 25px 0;
            color: {COLOR_NAVY_IMPERIAL} !important;
            box-shadow: 2px 6px 20px rgba(0,0,0,0.08);
        }

        /* ==========================================================================
           6. BOTONERA TOUCH-READY XL (MISION CRÍTICA CIUDADANA)
           ========================================================================== */
        .stButton>button, .stFormSubmitButton>button, button[data-testid="stFormSubmitButton"] {{
            background: linear-gradient(45deg, {COLOR_MUNI_BLUE}, #1d4ed8) !important;
            color: {COLOR_BG_PURE} !important; 
            -webkit-text-fill-color: {COLOR_BG_PURE} !important; /* Fuerza color blanco de letra en iOS Safari */
            border-radius: 15px !important; 
            height: 95px !important;
            font-weight: 900 !important; 
            text-transform: uppercase !important; 
            font-size: 1.45em !important;
            box-shadow: 0 10px 25px rgba(30, 58, 138, 0.4) !important;
            border: none !important;
            width: 100% !important;
            margin-top: 25px !important;
            transition: all 0.2s ease;
        }
        /* Efecto de presión en el botón para feedback de UX */
        .stButton>button:active, .stFormSubmitButton>button:active, button[data-testid="stFormSubmitButton"]:active {{
            transform: translateY(2px);
            box-shadow: 0 5px 15px rgba(30, 58, 138, 0.5) !important;
        }

        /* ==========================================================================
           7. COMPONENTES DEL MONITOR CENTRAL (COMMAND CENTER TV)
           ========================================================================== */
        .tv-card {{
            background: {COLOR_BG_PURE} !important; 
            border-radius: 15px; 
            padding: 25px;
            border-top: 14px solid {COLOR_MUNI_BLUE}; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
            text-align: center; 
            margin-bottom: 30px;
        }
        /* Semaforización de alerta roja en TV Cards */
        .tv-card-alert {{ border-top: 14px solid {COLOR_MUNI_ALERT} !important; background: #fffafa !important; }}

        .muni-title {{ color: {COLOR_MUNI_BLUE} !important; font-weight: 900 !important; text-align: center; font-size: 3.6em; line-height: 1.1; margin-bottom: 5px; }}
        
        /* Cronómetro de Seguridad Ciudadana (XL) */
        .timer-security {{ 
            color: {COLOR_MUNI_ALERT} !important; font-weight: 900; font-size: 5.8em; 
            text-align: center; border: 5px solid {COLOR_MUNI_ALERT}; border-radius: 20px; 
            background: {COLOR_BG_PURE} !important; padding: 20px; margin: 25px 0;
            box-shadow: inset 0 0 25px rgba(220, 38, 38, 0.1);
        }
        
        /* Corregir color de Métricas de Streamlit (que suelen fallar en forced dark) */
        div[data-testid="stMetricValue"] div {{
            color: {COLOR_MUNI_BLUE} !important;
            -webkit-text-fill-color: {COLOR_MUNI_BLUE} !important;
        }

        /* ==========================================================================
           8. AJUSTES EXTREMOS RESPONSIVOS PARA SMARTPHONES
           ========================================================================== */
        @media (max-width: 768px) {{
            .glass-panel {{ padding: 20px 15px; border-width: 4px; }}
            .muni-title {{ font-size: 2.7em !important; }}
            /* Adaptar botón gigante a pantallas pequeñas, permitiendo saltos de línea */
            .stButton>button, .stFormSubmitButton>button, button[data-testid="stFormSubmitButton"] {{ 
                height: 100px !important; font-size: 1.35em !important; white-space: normal; line-height: 1.2;
            }}
            /* Ajustar tamaño de TABS en móviles */
            div[data-baseweb="tab"] {{ font-size: 1.0em !important; padding: 12px 5px !important; min-width: 135px;}}
            .instruction-box {{ padding: 20px 15px; }}
            .timer-security {{ font-size: 4.8em !important; }}
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO I: CABECERA INSTITUCIONAL HTML BLINDADA (ANTI-RECORTE)
# ==================================================================================================

def render_smartcity_sovereign_header() -> None:
    """
    Renderiza la cabecera institucional utilizando HTML puro (`st.markdown`) en lugar de `st.image`.
    Esto asegura un control total sobre el padding inferior (blindaje contra recortes del logo)
    y garantiza la presencia de los logos en todas las resoluciones móviles.
    """
    
    # Blindaje CSS específico para la cabecera y el QR
    st.markdown(f"""
        <style>
            .header-container {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                width: 100%;
                /* Padding inferior blindado para que el logo no se corte */
                padding-bottom: 25px !important; 
                margin-bottom: 10px;
                border-bottom: 3px solid #f1f5f9;
            }}
            .logo-imls {{
                max-width: 150px;
                height: auto;
                /* Padding extra inferior de seguridad en la imagen */
                padding-bottom: 10px !important; 
            }}
            .brand-text {{
                text-align: center;
                font-family: 'Outfit', sans-serif;
                color: #001F3F !important;
                font-weight: 900;
                line-height: 1.2;
                font-size: 1.35em;
            }}
            .smartcity-highlight {{
                color: #059669 !important;
                font-size: 0.9em;
            }}
            .qr-share {{
                max-width: 100px;
                height: auto;
                border: 2px solid #e2e8f0;
                border-radius: 8px;
            }
            @media (max-width: 768px) {{
                .logo-imls {{ max-width: 110px; padding-bottom: 5px !important; }}
                .brand-text {{ font-size: 1.1em; }}
                .qr-share {{ max-width: 70px; }}
            }
        </style>
        
        <div class="header-container">
            <img src="{URL_ESCUDO_MUNI}" class="logo-imls" alt="Escudo I.M. La Serena">
            
            <div class="brand-text">
                ILUSTRE MUNICIPALIDAD<br>DE LA SERENA<br>
                <span class="smartcity-highlight">SMART CITY CHILE</span>
            </div>
            
            <img src="{URL_QR_COMPARTIR}" class="qr-share" alt="QR Acceso Rápido">
        </div>
        
        <h1 class="muni-title">PUERTA SERENA</h1>
        <h2 style='text-align:center; color:#001F3F !important; font-weight:900; font-size:2em; margin-bottom:15px;'>Gestión de Atención Ciudadana</h2>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO CIUDADANO (WELCOME QR & REGISTRO SENIOR UX)
# ==================================================================================================

def view_citizen_node() -> None:
    """El punto de contacto principal. Diseño obsesionado con el Adulto Mayor y legibilidad exterior."""
    
    # Invocación de la cabecera HTML blindada
    render_smartcity_sovereign_header()
    
    # Recuperación del token de Session State
    token = st.session_state.get('citizen_token_v40')
    
    # ==========================================
    # ESTADO A: FORMULARIO DE INGRESO (QR SCAN)
    # ==========================================
    if not token or token not in st.session_state.waiting_room:
        
        # RECUADRO DE INSTRUCCIONES SENIOR (Forzado de contraste Navy/Fondo Claro)
        st.markdown(f"""
            <div class="instruction-box">
                <h3 style="margin-top:0; color:#1e3a8a !important; font-size:1.6em; font-weight:900;">Estimado Vecino(a):</h3>
                <p style="font-size:1.25em !important; font-weight:700;">Para ser atendido con excelencia, siga estos pasos simples:</p>
                {TEXTO_INSTRUCCIONES_HTML}
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#1e3a8a !important; font-weight:900; margin-bottom:25px; text-align:center;'>🖋️ REGISTRO DE INGRESO MUNICIPAL</h3>", unsafe_allow_html=True)
        
        # FORMULARIO CON CSS BLINDADO (Anti-Dark Mode)
        with st.form("form_reg_sovereign_v40", clear_on_submit=True):
            recinto_sel = st.selectbox("1. ¿En qué Edificio Municipal se encuentra ahora?", list(INFRAESTRUCTURA_IMLS.keys()))
            nombre_input = st.text_input("2. Nombre y Apellidos Completos:", placeholder="Ejemplo: María González Soto")
            rut_input = st.text_input("3. RUT o Identificación:", placeholder="Ejemplo: 12.345.678-9")
            perfil_sel = st.selectbox("4. Categoría de Visitante:", PERFILES_SGAAC)
            depto_sel = st.selectbox("5. ¿A qué oficina se dirige?", LISTADO_DEPARTAMENTOS)
            motivo_input = st.text_area("6. Breve motivo de su visita (Opcional):", placeholder="Vengo a una reunión programada en la Obras...")
            
            submit = st.form_submit_button("SOLICITAR INGRESO AHORA")
            
            if submit:
                # Validación de campos críticos (Anti-nulos)
                if nombre_input and rut_input and recinto_sel:
                    # Generación vectorizada de ID de transacción
                    uid = f"V-{int(time.time())}"
                    assisted_flag = INFRAESTRUCTURA_IMLS[recinto_sel]['dotacion']
                    
                    # Estructura transaccional inyectada en Waiting Room
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre_input, "rut": rut_input, "perfil": perfil_sel, 
                        "recinto": recinto_sel, "depto": depto_sel, "motivo": motivo_input,
                        "inicio": datetime.now(), "assisted": assisted_flag,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None
                    }
                    # Persistencia del token en Session State del ciudadano
                    st.session_state.citizen_token_v40 = uid
                    registrar_auditoria(f"NUEVO REGISTRO CIUDADANO: {nombre_input} en {recinto_sel} hacia {depto_sel}")
                    st.rerun() # Recarga inmediata para cambiar de estado visual
                else: 
                    st.error("⚠️ ACCIÓN REQUERIDA: Por favor, complete su Nombre y RUT para que la secretaría pueda identificarlo.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        # ==========================================
        # ESTADOS DE FLUJO DE ATENCIÓN (MÁQUINA DE ESTADOS)
        # ==========================================
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        # ESTADO 1: ESPERANDO COORDINACIÓN DE SECRETARÍA
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"<h3 style='color:#001F3F !important; font-weight:800; font-size:1.6em;'>Su solicitud para **{info['depto']}** ha sido enviada.</h3>", unsafe_allow_html=True)
            st.write("Por favor, tome asiento un momento. Nuestras secretarías lo llamarán pronto.")
            
            # MARKETING TERRITORIAL ROTATIVO SMART CITY
            st.markdown(f"""
                <div style='background:#1e3a8a; color:white !important; padding:40px; border-radius:20px; border-left:15px solid #facc15; margin-top:25px; margin-bottom:25px; box-shadow: 0 10px 25px rgba(0,0,0,0.25); text-align:left;'>
                    <p style='color:white !important; font-weight:800; font-size:1.5em; line-height:1.4; margin:0;'>{np.random.choice(AVISOS_PROMO)}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # CRONÓMETRO DE ESPERA XL ( Feedback visual de UX)
            tiempo_restante = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(tiempo_restante)}s</div>", unsafe_allow_html=True)
            st.markdown("<p style='color:#001F3F !important; font-weight:700; font-size:1.1em;'>Si el reloj llega a cero, por favor consulte al guardia del recinto.</p>", unsafe_allow_html=True)
            
            # Protocolo de re-run automático para actualización del reloj
            if tiempo_restante > 0:
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                registrar_auditoria(f"TIMEOUT SOLICITUD: {info['nombre']} expirada (180s).")
                st.rerun()
                
        # ESTADO 2: AUTORIZADO A INGRESAR
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: 
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900; font-size:1.7em;'>Por favor, acérquese al Guardia para validar su entrada física con su carnet.</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900; font-size:2.8em;'>¡PASE ADELANTE!</h3>", unsafe_allow_html=True)
                st.write(f"La oficina de **{info['depto']}** lo está esperando.")
                if st.button("YA INGRESÉ A LA OFICINA (Iniciar Audiencia)"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"INGRESO EFECTIVO (AUTÓNOMO): {info['nombre']} entra a {info['depto']}")
                    st.rerun()
                    
        # ESTADO 3: EN AUDIENCIA / REUNIÓN (Cronometrando)
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **USTED ESTÁ EN REUNIÓN**")
            st.markdown("<p style='color:#001F3F !important; font-size:1.3em; font-weight:700;'>La I. Municipalidad cronometra sus atenciones para asegurar un servicio de excelencia y calidad Smart City.</p>", unsafe_allow_html=True)
            if st.button("TERMINAR REUNIÓN Y EVALUAR SERVICIO"):
                st.session_state.waiting_room[token]['estado'] = "CIERRE"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                registrar_auditoria(f"FIN AUDIENCIA (SOLICITUD CIUDADANO): {info['nombre']} termina con {info['depto']}")
                st.rerun()
                
        # ESTADO 4: CIERRE, NPS Y AGREDECIEMIENTO BALOONS
        elif info['estado'] == "CIERRE":
            st.balloons()
            st.markdown("""
                <div style='background: #1e3a8a; color:white !important; padding:50px 40px; border-radius:20px; text-align:center; box-shadow: 0 10px 30px rgba(0,0,0,0.3);'>
                    <h2 style='color:white !important; margin:0; font-size:3.0em; font-weight:900;'>¡MUCHAS GRACIAS POR SU VISITA!</h2>
                    <p style='color:white !important; font-size:1.6em; font-weight:600; margin-top:15px;'>Smart City La Serena, al servicio de la gente.</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h3 style='color:#001F3F !important; margin-top:35px; text-align:center; font-weight:800;'>Evalúe su Experiencia hoy</h3>", unsafe_allow_html=True)
            nps = st.slider("De 1 a 5 estrellas, ¿Qué tan buena y rápida fue su atención municipal?", 1, 5, 5)
            
            if st.button("ENVIAR EVALUACIÓN Y CERRAR SESIÓN"):
                # Cálculo de permanencia real para Big Data territorial
                permanencia = 15 
                if info.get('inicio_reunion') and info.get('fin_reunion'):
                    permanencia = int((info['fin_reunion'] - info['inicio_reunion']).total_seconds() / 60)
                
                # Inyección del registro final en la Big Data Base
                nuevo_registro = {
                    'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 
                    'Depto': info['depto'], 'Perfil': info['perfil'], 'Visitante': info['nombre'], 
                    'RUT': info['rut'], 'Permanencia_Minutos': permanencia, 'NPS_Calidad': nps, 
                    'Estado': "Completado", 'Telefono': "No Registrado", 'Email': "No Registrado",
                    'Validador_Fisico': "Auto/Guardia"
                }
                st.session_state.db_master = pd.concat([pd.DataFrame([nuevo_registro]), st.session_state.db_master], ignore_index=True)
                
                registrar_auditoria(f"CICLO FINALIZADO EXITOSAMENTE: {info['nombre']} | NPS: {nps} | T: {permanencia}m")
                
                # Limpieza de token ciudadanopara permitir nuevo registro
                del st.session_state.citizen_token_v40
                st.rerun()
                
        elif info['estado'] == "EXPIRADO":
            st.error("⚠️ SOLICITUD EXPIRADA")
            st.markdown("### Nuestras oficinas no han podido confirmar su ingreso a tiempo debido a alta demanda.")
            st.write("Por favor, acérquese al guardia del recinto para asistencia física o intente registrarse nuevamente.")
            if st.button("INTENTAR NUEVO REGISTRO"):
                del st.session_state.citizen_token_v40
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 6. NODO III: MONITOR CONTROL TOTAL (GRID TÁCTICO COMMAND CENTER / TV)
# ==================================================================================================

def view_master_monitor() -> None:
    """Pantalla táctica de visión territorial 360°. Diseñada para monitores de TV o Muros de Video."""
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:900; font-size:1.7em; color:#1e3a8a !important;'>CONTROL ESTRATÉGICO DE LA RED MUNICIPAL EN VIVO</p>", unsafe_allow_html=True)
    
    # Resumen Ejecutivo Superior (KPIs Tácticos)
    total_esperas = len([v for v in st.session_state.waiting_room.values() if v['estado'] == 'COORDINANDO'])
    total_activos = len([v for v in st.session_state.waiting_room.values() if v['estado'] == 'EN_REUNION'])
    
    c1, c2 = st.columns(2)
    with c1: st.error(f"🔴 ALERTAS / ESPERAS EN LA RED TERRITORIAL: {total_esperas}")
    with c2: st.success(f"🟢 AUDIENCIAS ACTIVAS EN VIVO: {total_activos}")
    st.divider()

    # Cuadrícula dinámica de alto impacto (4 columnas nativas)
    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    # Renderizado vectorizado de tarjetas para optimización de rendimiento
    for i, r_name in enumerate(recintos_list):
        with cols[i % 4]:
            # Procesamiento de colas por recinto en tiempo real
            esp = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'COORDINANDO']
            act = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'EN_REUNION']
            
            # Lógica de Semaforización de Alerta Visual (Cuello de Botella)
            # Threshold de alerta configurable (ej: > 2 esperando)
            has_alert = len(esp) > 2
            border_css = "border: 10px solid #dc2626;" if has_alert else "border-top: 14px solid #1e3a8a;"
            
            st.markdown(f"""
                <div class="tv-card" style="{border_css}">
                    <h3 style="margin:0; font-size:1.2em; color:#1e3a8a !important; line-height:1.2; font-weight:900;">{INFRAESTRUCTURA_IMLS[r_name]['icono']} {r_name[:22]}...</h3>
                    <p style="margin:5px 0; font-size:0.9em; color:gray !important; font-weight:800;">{INFRAESTRUCTURA_IMLS[r_name]['id']} | {INFRAESTRUCTURA_IMLS[r_name]['zona']}</p>
                    <hr style="border: 1px solid #f1f5f9; margin:15px 0;">
                    
                    <div style="display:flex; justify-content: space-around; align-items:center;">
                        <div>
                            <p style="font-size:3.8em; font-weight:900; margin:0; line-height:1; color:{'#dc2626' if has_alert else '#1e3a8a'} !important;">{len(esp)}</p>
                            <p style="font-size:1em; font-weight:900; color:#64748b !important; margin:0;">ESPERA</p>
                        </div>
                        <div style="border-left: 2px solid #f1f5f9; height: 70px;"></div>
                        <div>
                            <p style="font-size:3.8em; font-weight:900; margin:0; line-height:1; color:#059669 !important;">{len(act)}</p>
                            <p style="font-size:1em; font-weight:900; color:#64748b !important; margin:0;">EN VIVO</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    # Autorefresh del monitor cada 10 segundos para visión en Command Center
    time.sleep(10)
    st.rerun()

# ==================================================================================================
# 7. NODOS INTERNAL ADMIN: TACTICAL GUARDIA, SECRETARÍAS, BIG DATA & REPORTES
# ==================================================================================================

def view_internal_admin_panel() -> None:
    """Agrupa las funciones internas de control, autorización y análisis de la red."""
    st.markdown("<h2 class='muni-title'>PANEL DE GESTIÓN MUNICIPAL</h2>", unsafe_allow_html=True)
    
    # Navegación por sub-pestañas operativas
    tab_list = ["🛡️ Guardia", "🔔 Secretarías", "📊 Big Data", "⚙️ CRM", "📋 Reportes", "🕵️ Auditoría"]
    t_guardia, t_secre, t_data, t_crm, t_rep, t_logs = st.tabs(tab_list)
    
    # ==========================================
    # SUB-NODO: GUARDIA DE SEGURIDAD
    # ==========================================
    with t_guardia:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🛡️ Validación de Accesos Físicos")
        st.write("Verifique la identidad del ciudadano (Cédula de Identidad) antes de permitir el ingreso.")
        
        # Filtro de pases autorizados pendientes de check-in físico
        aut_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not aut_v: st.info("🟢 Sin pases autorizados pendientes de validación en este recinto.")
        
        for uid, info in aut_v.items():
            with st.container(border=True):
                st.markdown(f"<h3 style='color:#1e3a8a; margin:0; font-weight:900;'>👤 {info['nombre']}</h3>", unsafe_allow_html=True)
                st.write(f"**RUT:** {info['rut']} | **Hacia:** {info['depto']}")
                if st.button(f"CONFIRMAR PASO FÍSICO A REUNIÓN", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"INGRESO VALIDADO FÍSICAMENTE (GUARDIA): {info['nombre']}")
                    st.rerun()
                    
        st.divider()
        st.subheader("👁️ Radar de Coordinaciones Territorial")
        coord_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord_v:
            # Transformación para visualización táctica en tabla
            df_tactical = pd.DataFrame([{"Vecino": v['nombre'], "Perfil": v['perfil'], "Hacia Oficina": v['depto'], "Tiempo Espera": f"{int((datetime.now() - v['inicio']).total_seconds())}s"} for v in coord_v.values()])
            st.table(df_tactical)
        else: 
            st.caption("Radar despejado. Sin vecinos esperando autorización de secretaría.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # SUB-NODO: HUB DE SECRETARÍAS
    # ==========================================
    with t_secre:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔔 Solicitudes de Ingreso Entrantes (Cola)")
        
        pend_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend_v: st.success("🟢 Excelente gestión. No hay vecinos esperando ingreso para su departamento.")
        
        for uid, info in pend_v.items():
            with st.container(border=True):
                st.markdown(f"<h3 style='color:#1e3a8a; margin:0; font-weight:900;'>👤 {info['nombre']}</h3>", unsafe_allow_html=True)
                st.write(f"**Perfil:** {info['perfil']} | **RUT:** {info['rut']} | **Motivo:** {info.get('motivo', 'No especificado')}")
                
                # Botonera de decisión rápida
                c_ok, c_rej = st.columns(2)
                if c_ok.button("✅ AUTORIZAR INGRESO", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    registrar_auditoria(f"SECRETARÍA AUTORIZA: {info['nombre']} hacia {info['depto']}")
                    st.rerun()
                if c_rej.button("❌ DENEGAR ACCESO / REAGENDAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    registrar_auditoria(f"SECRETARÍA DENEGA SOLICITUD: {info['nombre']} hacia {info['depto']}")
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
    # ==========================================
    # SUB-NODO: BIG DATA ANALYTICS
    # ==========================================
    with t_data:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("📊 Inteligencia Territorial (Flujos Históricos)")
        
        # Blindaje de métricas (KPIs) territoriales
        df_master = st.session_state.db_master
        m1, m2, m3 = st.columns(3)
        m1.metric("Volumen Big Data", f"{len(df_master):,}", "Registros Transaccionales")
        m2.metric("Promedio NPS Calidad", f"{df_master['NPS_Calidad'].mean():.2f} / 5.0", "Satisfacción Ciudadana")
        m3.metric("Duración Promedio Audiencia", f"{df_master['Permanencia_Minutos'].mean():.0f} min", "Eficiencia de Atención")
        
        st.divider()
        st.markdown("<h4 style='color:#1e3a8a; font-weight:800;'>Flujo de Visitas por Recinto Municipal</h4>", unsafe_allow_html=True)
        # Gráfico vectorial integrado
        st.bar_chart(df_master['Recinto'].value_counts(), color="#1e3a8a")
        
        st.markdown("<h4 style='color:#1e3a8a; font-weight:800;'>Flujo por Departamento Interno</h4>", unsafe_allow_html=True)
        # Gráfico vectorial integrado color secundario
        st.bar_chart(df_master['Depto'].value_counts(), color="#059669")
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # SUB-NODO: CRM CIUDADANO (G&C)
    # ==========================================
    with t_crm:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔍 Gestión CRM Ciudadano (Gestión y Contacto)")
        st.write("Herramienta estratégica para completar datos de contacto y vinculación social con vecinos y dirigentes clave.")
        
        # Motor de búsqueda de fichas históricas
        search_id = st.text_input("Ingrese ID Único de la Visita para buscar (Ej: VIS-100050):")
        if search_id:
            # Búsqueda indexada en DataFrame Big Data
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                ficha = st.session_state.db_master.iloc[i]
                st.info(f"Editando Ficha de Inteligencia Ciudadana: **{ficha['Visitante']}** ({ficha['Perfil']})")
                
                # Formulario CRM (No editable en bulk, solo individual)
                with st.form("crm_form_v40_enterprise"):
                    col_crm_1, col_crm_2 = st.columns(2)
                    with col_crm_1:
                        tel_val = st.text_input("WhatsApp / Celular de Contacto", ficha['Telefono'])
                        mail_val = st.text_input("Email Institucional de Seguimiento", ficha['Email'])
                    with col_crm_2:
                        notas_val = st.text_area("Notas Internas de Gestión Territorial / JJVV:")
                    
                    if st.form_submit_button("ACTUALIZAR FICHA CIUDADANA EN BIG DATA"):
                        # Persistencia del cambio en la Big Data Master de Session State
                        st.session_state.db_master.at[i, 'Telefono'] = tel_val
                        st.session_state.db_master.at[i, 'Email'] = mail_val
                        registrar_auditoria(f"CRM ACTUALIZADO: ID {search_id} modificado por Operador.")
                        st.success("✅ Inteligencia Ciudadana Actualizada Correctamente en la base de datos histórica.")
                        st.rerun()
            else:
                st.warning("⚠️ ID de visita no encontrado en la Base de Datos Histórica. Verifique el reporte.")
                
        st.divider()
        st.subheader("Base de Datos Maestra CRM (Vista Previa - 200 Registros)")
        st.dataframe(st.session_state.db_master.head(200), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # SUB-NODO: REPORTES OPERATIVOS
    # ==========================================
    with t_rep:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("📋 Exportación de Matrices Transaccionales")
        st.write("Generación y descarga de datos en crudo para auditorías externas o análisis secundario (CSV/Excel).")
        
        col_rep_1, col_rep_2 = st.columns(2)
        
        # Simulador de generación de matriz de datos (Últimos 5000 registros para no saturar memoria)
        with col_rep_1:
            csv_data_raw = st.session_state.db_master.head(5000).to_csv(index=False).encode('utf-8')
            # Botón nativo de descarga blindado
            st.download_button(
                label="⬇️ DESCARGAR MATRIZ CSV (ÚLTIMOS 5,000 REGISTROS)",
                data=csv_data_raw,
                file_name=f"SGAAC_Matriz_Raw_{datetime.now().strftime('%Y%m%d')}.csv",
                mime='text/csv',
                key='btn_csv_download'
            )
            st.caption("Formato ideal para importación en Excel u PowerBI.")
            
        with col_rep_2:
            st.info("📊 Módulo de Reportes PDF Avanzados en Desarrollo (Muni-v43)")
            
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # SUB-NODO: AUDITORÍA FISCALIZADORA
    # ==========================================
    with t_logs:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🕵️ Registro Inmutable de Transacciones del Sistema (Fiscalización)")
        st.write("Logs de seguridad detallados para control de gestión, auditoría interna y fiscalización territorial.")
        for log in st.session_state.audit_logs[:100]: 
            # Renderizado en bloque de código para legibilidad técnica
            st.code(log, language="bash")
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 8. ORQUESTADOR PRINCIPAL (WRAP TABS & LOOP DE EJECUCIÓN MISIÓN CRÍTICA)
# ==================================================================================================

def main() -> None:
    """Entry point que orquesta inicialización, CSS masivo, seguridad y enrutamiento visual."""
    
    # 1. Bootstrapping de lógica empresarial y estados
    bootstrap_enterprise_logic()
    
    # 2. Inyección de vacuna Anti-Dark Mode y CSS táctico
    inject_smartcity_sovereign_css()
    
    # 3. MOTOR DE SEGURIDAD CIUDADANA: Protocolo de Expiración Automática
    # Protocolo que limpia solicitudes en cola ('COORDINANDO') que superan los 180 segundos sin respuesta.
    now = datetime.now()
    waiting_room = st.session_state.waiting_room
    
    # Identificar IDs expirados vectorialmente (prevenir KeyErrors en loop)
    expired_uids = [
        uid for uid, info in waiting_room.items() 
        if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180
    ]
    
    # Ejecutar limpieza y loguear en auditoría
    if expired_uids:
        for uid in expired_uids: 
            # Cambiar estado a expirado para feedback al ciudadano
            st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
            # Registrar evento de seguridad en log
            registrar_auditoria(f"PROTOCOL EXPIRACIÓN: Solicitud de {waiting_room[uid]['nombre']} expirada automáticamente (180s) por seguridad.")
        # Forzar recarga si hubo cambios críticos en el estado
        st.rerun()

    # 4. NAVEGACIÓN UNIVERSAL DE ALTO IMPACTO (Wrap-Tabs Responsivas Móviles)
    # Reemplaza al Sidebar de Streamlit, garantizando visibilidad en cualquier dispositivo móvil.
    tab_labels = ["👤 ACCESO CIUDADANO (QR)", "🖥️ MONITOR MAESTRO 360°", "⚙️ PANEL ADMINISTRATIVO"]
    tab_main_1, tab_main_2, tab_main_3 = st.tabs(tab_labels)
    
    # Enrutamiento modular de vistas
    with tab_main_1: view_citizen_node()
    with tab_main_2: view_master_monitor()
    with tab_main_3: view_tactical_and_data()

    # 5. FOOTER INSTITUCIONAL BLINDADO (STEALTH)
    st.markdown("""
        <div style='text-align:center; padding:20px 10px; margin-top:50px; border-top: 2px solid #f1f5f9; color:#64748b;'>
            <p style='font-size:1em; font-weight:800; color:#64748b !important; line-height:1.4;'>
                Gestión Territorial Smart City | Ilustre Municipalidad de La Serena<br>
                Sistema SGAAC-360 Version 42.0 Enterprise
            </p>
            <p style='font-size:0.8em; color:#94a3b8 !important; margin-top:5px;'>La Serena trabaja para usted.</p>
        </div>
    """, unsafe_allow_html=True)

# Protocolo de ejecución Entry Point
if __name__ == "__main__": 
    # Blindaje contra ejecuciones corruptas de módulos
    main()
