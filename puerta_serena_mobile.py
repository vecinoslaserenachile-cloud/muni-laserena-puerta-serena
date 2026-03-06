"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / SMART CITY / GLOBAL SYNC MULTIPLAYER
VERSIÓN: 46.0.0 (High-Density Modular Architecture - TOTAL EXTEND MODE +1000 LÍNEAS)
PROPIEDAD: Ilustre Municipalidad de La Serena - Proyecto Smart City Chile

====================================================================================================
NUEVO NÚCLEO DE SINCRONIZACIÓN GLOBAL (V46.0):
====================================================================================================
- Global Shared Memory: Se ha implementado `@st.cache_resource` para crear un bloque de memoria 
  único en el servidor. 
- Transaccionalidad Real-Time: La "Sala de Espera" (Waiting Room), la Big Data y los Logs 
  ya no son individuales por dispositivo. Ahora son variables globales. Si un ciudadano en la calle 
  se registra, el Guardia y el Monitor Central lo ven en milisegundos.
- Tokenización Local: Solo el token de sesión (`citizen_token`) se mantiene privado en el móvil 
  del usuario para garantizar que cada vecino solo vea su propia pantalla de seguimiento, 
  mientras la administración ve el panorama completo.

ARQUITECTURA DE NODOS ESTRATÉGICOS:
1.  NODO CIUDADANO (QR): UX Senior-Friendly, Escudos HTML fijos, Anti-Dark Mode, QR Infalible.
2.  NODO MONITOR CONTROL TOTAL: Pantalla 360° Grid para Command Center (TV 4K).
3.  NODO TÁCTICO GUARDIA: Validación de entrada, Visor de Coordinación y Control de Salida.
4.  NODO PANEL SECRETARÍAS: Hub de autorización y Cierre de Audiencias.
5.  NODO ANALÍTICA & CRM: Trazabilidad de +60,000 registros, edición de fichas y métricas.
6.  NODO AUDITORÍA SATELITAL: Registro inmutable de transacciones del sistema.
====================================================================================================
"""

import streamlit as st

# ==================================================================================================
# 0. CONFIGURACIÓN INICIAL (DEBE SER LA PRIMERA LÍNEA DE CÓDIGO)
# ==================================================================================================
st.set_page_config(
    page_title="Puerta Serena | Smart City La Serena",
    page_icon="🚪", 
    layout="wide",
    initial_sidebar_state="collapsed" 
)

import pandas as pd
import numpy as np
import time
import urllib.parse
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union, NoReturn

# ==================================================================================================
# 1. CONSTANTES INSTITUCIONALES Y CONFIGURACIÓN TERRITORIAL
# ==================================================================================================

# RECURSOS GRÁFICOS INSTITUCIONALES (Propiedad Ilustre Municipalidad de La Serena)
URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"

# QR ENCODING: Enlace real del prototipo con URL Encoding para evitar rotura del código QR
URL_APP_DEPLOY = "https://puertaserena.streamlit.app"
URL_ENCODED = urllib.parse.quote(URL_APP_DEPLOY)
URL_QR_COMPARTIR = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={URL_ENCODED}"

# INFRAESTRUCTURA DE RED (17 Recintos Estratégicos de la IMLS)
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️", "zona": "Casco Histórico", "id": "EC-01", "capacidad": 150},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢", "zona": "Casco Histórico", "id": "EC-02", "capacidad": 120},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫", "zona": "Casco Histórico", "id": "EB-03", "capacidad": 90},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦", "zona": "Servicios", "id": "DT-04", "capacidad": 200},
    "DIDECO (Almagro 450)": {"dotacion": True, "icono": "🤝", "zona": "Social", "id": "DI-05", "capacidad": 180},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️", "zona": "Norte", "id": "DLC-06", "capacidad": 150},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡", "zona": "Oriente", "id": "DLA-07", "capacidad": 80},
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳", "zona": "Sur", "id": "DLP-08", "capacidad": 80},
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️", "zona": "Costa", "id": "DAM-09", "capacidad": 50},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜", "zona": "Rural", "id": "DR-10", "capacidad": 40},
    "Coliseo Monumental": {"dotacion": True, "icono": "🏀", "zona": "Deportes", "id": "CM-11", "capacidad": 500},
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "zona": "Deportes", "id": "PLC-12", "capacidad": 200},
    "Parque Pedro de Valdivia (Admin)": {"dotacion": True, "icono": "🦌", "zona": "Recreación", "id": "PPV-13", "capacidad": 100},
    "Juzgado de Policía Local": {"dotacion": True, "icono": "⚖️", "zona": "Justicia", "id": "JPL-14", "capacidad": 110},
    "Taller Municipal": {"dotacion": False, "icono": "🛠️", "zona": "Operativa", "id": "TM-15", "capacidad": 60},
    "Centro Cultural Palace": {"dotacion": False, "icono": "🎨", "zona": "Cultura", "id": "CCP-16", "capacidad": 150},
    "Estadio La Portada (Admin)": {"dotacion": True, "icono": "⚽", "zona": "Deportes", "id": "ELP-17", "capacidad": 300}
}

LISTADO_DEPARTAMENTOS = [
    "Alcaldía", "Secretaría Municipal", "Administración Municipal",
    "Dirección de Obras (DOM)", "Dirección de Tránsito", "DIDECO - Social",
    "Dirección Jurídica", "Comunicaciones y RR.PP.", "Turismo y Patrimonio",
    "Cultura y Artes", "Seguridad Ciudadana", "Finanzas y Tesorería",
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda", "Oficina Adulto Mayor"
]

PERFILES_SGAAC = [
    "Vecino(a) de La Serena", "Dirigente Social / JJVV", "Autoridad Pública", 
    "Funcionario Municipal", "Proveedor Externo", "Prensa / Medios", "Delegación"
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
# 2. MOTOR DE MEMORIA GLOBAL Y PERSISTENCIA (SISTEMA MULTIPLAYER)
# ==================================================================================================

class EnterpriseDataGenerator:
    """Clase para la generación masiva de datos y gestión de la persistencia."""
    @staticmethod
    def generate_stress_data(num_records: int = 60000) -> pd.DataFrame:
        """Genera un DataFrame histórico masivo para stress-test."""
        start_date = datetime.now() - timedelta(days=1095)
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

@st.cache_resource
def get_global_memory():
    """
    EL NÚCLEO DEL SISTEMA: Este diccionario reside en la memoria del servidor.
    TODOS los teléfonos y computadoras conectados acceden y modifican ESTE mismo bloque de datos.
    Esto permite que el guardia vea en tiempo real lo que el ciudadano ingresa en su móvil.
    """
    return {
        'waiting_room': {},
        'audit_logs': [f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SISTEMA SMART CITY: SERVIDOR GLOBAL SINCRONIZADO"],
        'db_master': EnterpriseDataGenerator.generate_stress_data(60000)
    }

# Instanciación de la memoria global
GLOBAL_MEM = get_global_memory()

def registrar_auditoria(mensaje: str):
    """Inyecta un log inmutable en la memoria global del servidor."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    GLOBAL_MEM['audit_logs'].insert(0, f"[{stamp}] {mensaje}")
    if len(GLOBAL_MEM['audit_logs']) > 2000:
        GLOBAL_MEM['audit_logs'] = GLOBAL_MEM['audit_logs'][:2000]

# ==================================================================================================
# 3. MOTOR CSS BLINDADO (ANTI-DARK MODE Y DESTRUCCIÓN DE SIDEBAR)
# ==================================================================================================

def inject_titanium_mobile_css():
    """
    CSS PURO DE MISIÓN CRÍTICA. 
    Fuerza fondo blanco, letras oscuras en inputs (Anti-Dark Mode) y destruye la barra lateral.
    """
    st.markdown("""
        <style>
        /* ==========================================================================
           1. DESTRUCCIÓN DEL MENÚ HAMBURGUESA Y SIDEBAR (Stealth Absoluto)
           ========================================================================== */
        [data-testid="collapsedControl"] { display: none !important; }
        [data-testid="stSidebar"] { display: none !important; width: 0 !important; }
        #MainMenu {visibility: hidden !important; display: none !important;}
        header[data-testid="stHeader"] {display: none !important;}
        footer {visibility: hidden !important; display: none !important;}
        .stDeployButton {display:none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        
        /* ==========================================================================
           2. VACUNA ANTI-DARK MODE (FORZADO ABSOLUTO DE BLANCO Y AZUL)
           ========================================================================== */
        :root { color-scheme: light !important; }
        
        html, body, [class*="st-"], .stApp, [data-testid="stAppViewContainer"], .main { 
            background-color: #FFFFFF !important; 
            font-family: 'Outfit', sans-serif; 
        }
        
        p, span, div, li, h1, h2, h3, h4, h5, table, strong { 
            color: #001F3F !important; 
            font-weight: 600 !important; 
        }

        /* ==========================================================================
           3. REPARACIÓN DE CAJAS DE TEXTO NEGRAS EN MÓVILES (INPUTS Y LABELS)
           ========================================================================== */
        label[data-testid="stWidgetLabel"] p, label[data-testid="stWidgetLabel"] div {
            color: #001F3F !important;
            font-weight: 900 !important;
            font-size: 1.15em !important;
        }

        input, textarea, select {
            background-color: #FFFFFF !important;
            color: #001F3F !important;
            -webkit-text-fill-color: #001F3F !important;
            font-weight: 800 !important;
        }

        div[data-baseweb="input"], div[data-baseweb="textarea"] {
            background-color: #FFFFFF !important;
            border: 2.5px solid #1e3a8a !important;
            border-radius: 10px !important;
        }

        input::placeholder, textarea::placeholder {
            color: #64748b !important;
            -webkit-text-fill-color: #64748b !important;
            font-weight: 500 !important;
            opacity: 1 !important;
        }

        div[data-baseweb="select"] > div {
            background-color: #F8FAFC !important;
            color: #001F3F !important;
            border: 2.5px solid #1e3a8a !important;
            font-weight: 800 !important;
        }
        
        div[data-baseweb="select"] span {
            color: #001F3F !important;
            -webkit-text-fill-color: #001F3F !important;
        }

        ul[data-baseweb="listbox"] { background-color: #FFFFFF !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #001F3F !important; font-weight: 800 !important; background-color: #FFFFFF !important;}
        ul[data-baseweb="listbox"] li:hover { background-color: #1e3a8a !important; color: #FFFFFF !important; }

        /* ==========================================================================
           4. WRAP-TABS (Navegación Móvil Horizontal Adaptativa)
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
            min-width: 150px;
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
        }

        /* ==========================================================================
           5. PANELES INSTITUCIONALES
           ========================================================================== */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 15px;
            border: 4px solid #1e3a8a !important; 
            padding: 35px 25px;
            box-shadow: 0 10px 45px rgba(0, 31, 63, 0.15);
            margin-bottom: 40px;
            margin-top: 15px;
        }

        .instruction-box {
            background-color: #F8FAFC !important;
            border-left: 15px solid #1e3a8a !important;
            padding: 30px;
            border-radius: 12px;
            margin: 25px 0;
            color: #001F3F !important;
            box-shadow: 2px 6px 20px rgba(0,0,0,0.08);
        }

        .stButton>button, .stFormSubmitButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #FFFFFF !important; 
            -webkit-text-fill-color: #FFFFFF !important; 
            border-radius: 15px !important; 
            height: 95px !important;
            font-weight: 900 !important; 
            text-transform: uppercase !important; 
            font-size: 1.45em !important;
            box-shadow: 0 10px 25px rgba(30, 58, 138, 0.4) !important;
            border: none !important;
            width: 100% !important;
            margin-top: 25px !important;
        }

        /* Botones secundarios (Rojos) */
        button[kind="secondary"] {
            background: linear-gradient(45deg, #b91c1c, #ef4444) !important;
        }

        .tv-card {
            background: #FFFFFF !important; 
            border-radius: 15px; 
            padding: 25px;
            border-top: 14px solid #1e3a8a; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
            text-align: center; 
            margin-bottom: 30px;
        }
        .tv-card-alert { border-top: 14px solid #dc2626 !important; background: #fffafa !important; }

        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.6em; line-height: 1.1; margin-bottom: 5px; }
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 5.5em; 
            text-align: center; border: 5px solid #dc2626; border-radius: 20px; 
            background: #FFFFFF !important; padding: 20px; margin: 25px 0;
        }

        @media (max-width: 768px) {
            .glass-panel { padding: 20px 15px; border-width: 4px; }
            .muni-title { font-size: 2.6em !important; }
            .stButton>button, .stFormSubmitButton>button { height: 100px !important; font-size: 1.3em !important; white-space: normal;}
            div[data-baseweb="tab"] { font-size: 1em !important; padding: 12px 5px !important; min-width: 130px;}
            .timer-security { font-size: 4.5em !important; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO I: CIUDADANO (HTML CABECERA Y FLUJO DE REGISTRO)
# ==================================================================================================

def render_smartcity_sovereign_header():
    """Cabecera HTML pura que asegura que los logos no se corten en móviles."""
    st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; padding-bottom: 25px; margin-bottom: 10px; border-bottom: 3px solid #f1f5f9;">
            <img src="{URL_ESCUDO_MUNI}" style="max-width: 130px; height: auto;" alt="Escudo La Serena">
            <div style="text-align: center; font-family: 'Outfit', sans-serif; color: #001F3F !important; font-weight: 900; line-height: 1.2; font-size: 1.2em;">
                ILUSTRE MUNICIPALIDAD<br>DE LA SERENA<br>
                <span style="color: #059669 !important; font-size: 0.9em;">SMART CITY CHILE</span>
            </div>
            <img src="{URL_QR_COMPARTIR}" style="max-width: 80px; height: auto; border: 2px solid #e2e8f0; border-radius: 8px;" alt="QR Compartir">
        </div>
        <h1 class="muni-title">PUERTA SERENA</h1>
        <h2 style='text-align:center; color:#001F3F !important; font-weight:900; font-size:2em; margin-bottom:15px;'>Gestión de Atención Ciudadana</h2>
    """, unsafe_allow_html=True)

def view_citizen_node():
    """El punto de contacto principal para el ciudadano."""
    render_smartcity_sovereign_header()
    
    # El token SIEMPRE debe ser local (st.session_state) para que cada teléfono vea su propio estado.
    token = st.session_state.get('citizen_token_v46')
    
    if not token or token not in GLOBAL_MEM['waiting_room']:
        st.markdown("""
            <div class="instruction-box">
                <h3 style="margin-top:0; color:#1e3a8a !important; font-size:1.6em; font-weight:900;">Estimado Vecino(a):</h3>
                <p style="font-size:1.25em !important; font-weight:700; color:#001F3F !important;">Siga estos pasos para registrarse:</p>
                <ol style="font-size:1.3em !important; font-weight:800; color:#001F3F !important; line-height:1.6;">
                    <li>Seleccione el edificio donde está ahora.</li>
                    <li>Escriba su Nombre y RUT en las cajas blancas.</li>
                    <li>Elija la oficina a la que se dirige.</li>
                    <li>Presione el <b>BOTÓN AZUL</b> al final.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#1e3a8a !important; font-weight:900; margin-bottom:20px; text-align:center;'>🖋️ FORMULARIO DE INGRESO</h3>", unsafe_allow_html=True)
        
        with st.form("form_registro_ciudadano", clear_on_submit=True):
            recinto_sel = st.selectbox("1. ¿En qué Edificio Municipal se encuentra?", list(INFRAESTRUCTURA_IMLS.keys()))
            nombre_input = st.text_input("2. Nombre y Apellidos Completos:")
            rut_input = st.text_input("3. RUT o Identificación:")
            perfil_sel = st.selectbox("4. Categoría de Visitante:", PERFILES_SGAAC)
            depto_sel = st.selectbox("5. ¿A qué oficina se dirige?", LISTADO_DEPARTAMENTOS)
            motivo_input = st.text_area("6. Breve motivo de su visita (Opcional):")
            
            submit = st.form_submit_button("SOLICITAR INGRESO AHORA")
            
            if submit:
                if nombre_input and rut_input and recinto_sel:
                    uid = f"V-{int(time.time())}"
                    assisted_flag = INFRAESTRUCTURA_IMLS[recinto_sel]['dotacion']
                    
                    # INYECCIÓN EN LA MEMORIA GLOBAL DEL SERVIDOR
                    GLOBAL_MEM['waiting_room'][uid] = {
                        "nombre": nombre_input, "rut": rut_input, "perfil": perfil_sel, 
                        "recinto": recinto_sel, "depto": depto_sel, "motivo": motivo_input,
                        "inicio": datetime.now(), "assisted": assisted_flag,
                        "estado": "COORDINANDO", "inicio_reunion": None, "fin_reunion": None,
                        "nps_temp": 5
                    }
                    st.session_state.citizen_token_v46 = uid
                    registrar_auditoria(f"NUEVO INGRESO GLOBAL: {nombre_input} en {recinto_sel}")
                    st.rerun()
                else: 
                    st.error("⚠️ ACCIÓN REQUERIDA: Por favor, escriba su Nombre y RUT.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        # ==========================================
        # LECTURA DEL ESTADO DESDE LA MEMORIA GLOBAL
        # ==========================================
        info = GLOBAL_MEM['waiting_room'][token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"<h3 style='color:#001F3F !important; font-weight:800;'>Avisando a la oficina de **{info['depto']}**...</h3>", unsafe_allow_html=True)
            st.write("Por favor, tome asiento. Le avisaremos por esta pantalla.")
            
            tiempo_restante = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(tiempo_restante)}s</div>", unsafe_allow_html=True)
            
            if tiempo_restante == 0:
                GLOBAL_MEM['waiting_room'][token]['estado'] = "EXPIRADO"
                st.rerun()
                
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: 
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900;'>Por favor, acérquese al Guardia para validar su entrada física.</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900; font-size:2.5em;'>¡PASE ADELANTE!</h3>", unsafe_allow_html=True)
                if st.button("YA INGRESÉ A LA OFICINA"):
                    GLOBAL_MEM['waiting_room'][token]['estado'] = "EN_REUNION"
                    GLOBAL_MEM['waiting_room'][token]['inicio_reunion'] = datetime.now()
                    st.rerun()
                    
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **USTED ESTÁ EN REUNIÓN**")
            st.markdown("<h3 style='color:#001F3F !important;'>La Municipalidad cronometra sus atenciones para asegurar la excelencia.</h3>", unsafe_allow_html=True)
            st.markdown("<p style='color:#dc2626 !important; font-weight:800; font-size:1.2em;'>La secretaría finalizará su atención en el sistema cuando termine.</p>", unsafe_allow_html=True)
                
        elif info['estado'] == "EVALUACION":
            st.balloons()
            st.markdown("""
                <div style='background: #1e3a8a; color:white !important; padding:30px; border-radius:15px; text-align:center;'>
                    <h2 style='color:white !important; margin:0; font-size:2.5em;'>¡REUNIÓN FINALIZADA!</h2>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h3 style='color:#001F3F !important; margin-top:30px;'>Evalúe su Experiencia</h3>", unsafe_allow_html=True)
            nps = st.slider("De 1 a 5 estrellas, ¿Qué tan buena fue su atención?", 1, 5, 5)
            
            if st.button("ENVIAR EVALUACIÓN Y DIRIGIRME A LA SALIDA"):
                GLOBAL_MEM['waiting_room'][token]['nps_temp'] = nps
                GLOBAL_MEM['waiting_room'][token]['estado'] = "SALIDA_PENDIENTE"
                st.rerun()
                
        elif info['estado'] == "SALIDA_PENDIENTE":
            st.success("✅ **EVALUACIÓN RECIBIDA**")
            st.markdown("<h3 style='color:#001F3F !important; font-weight:900;'>Por favor, diríjase a la salida.</h3>", unsafe_allow_html=True)
            st.write("El guardia del recinto verificará su retiro para cerrar el ciclo de seguridad.")
            
            # Auto-cierre si el recinto no tiene dotación de guardia
            if not info['assisted']:
                if st.button("YA SALÍ DEL RECINTO"):
                    permanencia = int((info['fin_reunion'] - info['inicio_reunion']).total_seconds() / 60) if info.get('inicio_reunion') else 15
                    nuevo_registro = {
                        'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 
                        'Perfil': info['perfil'], 'Visitante': info['nombre'], 'RUT': info['rut'], 
                        'Permanencia_Minutos': permanencia, 'NPS_Calidad': info.get('nps_temp', 5), 
                        'Estado': "Completado", 'Telefono': "No Registrado", 'Email': "No Registrado",
                        'Validador_Fisico': "Autónomo"
                    }
                    GLOBAL_MEM['db_master'] = pd.concat([pd.DataFrame([nuevo_registro]), GLOBAL_MEM['db_master']], ignore_index=True)
                    del st.session_state.citizen_token_v46
                    st.rerun()
        
        elif info['estado'] == "EXPIRADO":
            st.error("⚠️ TIEMPO DE ESPERA AGOTADO")
            st.write("Por favor, avise al guardia o intente registrarse nuevamente.")
            if st.button("VOLVER A INTENTAR"):
                del st.session_state.citizen_token_v46
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO II: MONITOR CONTROL TOTAL (LEE DESDE MEMORIA GLOBAL)
# ==================================================================================================

def view_master_monitor():
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:900; font-size:1.6em; color:#1e3a8a !important;'>CONTROL DE RED TERRITORIAL EN VIVO</p>", unsafe_allow_html=True)
    
    total_esperas = len([v for v in GLOBAL_MEM['waiting_room'].values() if v['estado'] == 'COORDINANDO'])
    total_activos = len([v for v in GLOBAL_MEM['waiting_room'].values() if v['estado'] == 'EN_REUNION'])
    
    c1, c2 = st.columns(2)
    with c1: st.error(f"🔴 ESPERAS ACTIVAS EN LA RED: {total_esperas}")
    with c2: st.success(f"🟢 AUDIENCIAS EN VIVO: {total_activos}")
    st.divider()

    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r_name in enumerate(recintos_list):
        with cols[i % 4]:
            esp = [v for v in GLOBAL_MEM['waiting_room'].values() if v['recinto'] == r_name and v['estado'] == 'COORDINANDO']
            act = [v for v in GLOBAL_MEM['waiting_room'].values() if v['recinto'] == r_name and v['estado'] == 'EN_REUNION']
            
            has_alert = len(esp) > 2
            border_css = "border: 10px solid #dc2626;" if has_alert else "border-top: 14px solid #1e3a8a;"
            
            st.markdown(f"""
                <div class="tv-card" style="{border_css}">
                    <h3 style="margin:0; font-size:1.1em; color:#1e3a8a !important; line-height:1.2;">{INFRAESTRUCTURA_IMLS[r_name]['icono']} {r_name[:22]}...</h3>
                    <hr style="border: 1px solid #f1f5f9; margin:15px 0;">
                    <div style="display:flex; justify-content: space-around; align-items:center;">
                        <div>
                            <p style="font-size:3.5em; font-weight:900; margin:0; line-height:1; color:{'#dc2626' if has_alert else '#1e3a8a'} !important;">{len(esp)}</p>
                            <p style="font-size:0.9em; font-weight:900; color:#64748b !important; margin:0;">ESPERA</p>
                        </div>
                        <div>
                            <p style="font-size:3.5em; font-weight:900; margin:0; line-height:1; color:#059669 !important;">{len(act)}</p>
                            <p style="font-size:0.9em; font-weight:900; color:#64748b !important; margin:0;">EN VIVO</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. NODOS INTERNOS: GUARDIA Y SECRETARÍAS (MULTIUSUARIO REAL)
# ==================================================================================================

def view_tactical_and_data():
    st.markdown("<h2 class='muni-title'>PANEL DE GESTIÓN INTERNA</h2>", unsafe_allow_html=True)
    
    t_guardia, t_secre, t_data, t_crm, t_logs = st.tabs([
        "🛡️ Guardia / Control Físico", "🔔 Secretarías (Audiencias)", "📊 Big Data", "⚙️ CRM", "🕵️ Auditoría"
    ])
    
    with t_guardia:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🛡️ 1. Validación de ENTRADA (Filtro Perimetral)")
        aut_v = {k: v for k, v in GLOBAL_MEM['waiting_room'].items() if v['estado'] == 'AUTORIZADO'}
        if not aut_v: st.info("🟢 Sin pases de entrada pendientes en toda la red.")
        for uid, info in aut_v.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** | RUT: {info['rut']} -> Hacia: {info['depto']}")
                if st.button(f"CONFIRMAR ENTRADA FÍSICA", key=f"g_in_{uid}"):
                    GLOBAL_MEM['waiting_room'][uid]['estado'] = 'EN_REUNION'
                    GLOBAL_MEM['waiting_room'][uid]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"ENTRADA VALIDADA POR GUARDIA: {info['nombre']}")
                    st.rerun()
                    
        st.divider()
        st.subheader("🚪 2. Validación de SALIDA (Cierre de Ciclo)")
        sal_v = {k: v for k, v in GLOBAL_MEM['waiting_room'].items() if v['estado'] in ['EVALUACION', 'SALIDA_PENDIENTE']}
        if not sal_v: st.info("🟢 Sin vecinos en proceso de retiro.")
        for uid, info in sal_v.items():
            with st.container(border=True):
                estado_texto = "En Evaluación" if info['estado'] == 'EVALUACION' else "Listo para Salir"
                st.write(f"👤 **{info['nombre']}** | De: {info['depto']} | Estado: {estado_texto}")
                if st.button(f"CONFIRMAR SALIDA DEL RECINTO", key=f"g_out_{uid}"):
                    permanencia = 15 
                    if info.get('inicio_reunion') and info.get('fin_reunion'):
                        permanencia = int((info['fin_reunion'] - info['inicio_reunion']).total_seconds() / 60)
                    
                    nuevo_registro = {
                        'ID': uid, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 
                        'Depto': info['depto'], 'Perfil': info['perfil'], 'Visitante': info['nombre'], 
                        'RUT': info['rut'], 'Permanencia_Minutos': permanencia, 'NPS_Calidad': info.get('nps_temp', 5), 
                        'Estado': "Completado", 'Telefono': "No Registrado", 'Email': "No Registrado",
                        'Validador_Fisico': "Guardia Turno Activo"
                    }
                    GLOBAL_MEM['db_master'] = pd.concat([pd.DataFrame([nuevo_registro]), GLOBAL_MEM['db_master']], ignore_index=True)
                    registrar_auditoria(f"SALIDA CONFIRMADA GUARDIA (CIERRE BD): {info['nombre']}")
                    
                    del GLOBAL_MEM['waiting_room'][uid]
                    st.rerun()

        st.divider()
        st.subheader("👁️ Radar de Esperas Global (Coordinando)")
        coord_v = {k: v for k, v in GLOBAL_MEM['waiting_room'].items() if v['estado'] == 'COORDINANDO'}
        if coord_v:
            df_tactical = pd.DataFrame([{"Vecino": v['nombre'], "Oficina": v['depto'], "Recinto": v['recinto']} for v in coord_v.values()])
            st.table(df_tactical)
        st.markdown("</div>", unsafe_allow_html=True)

    with t_secre:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔔 1. Solicitudes Entrantes (Recepción)")
        pend_v = {k: v for k, v in GLOBAL_MEM['waiting_room'].items() if v['estado'] == 'COORDINANDO'}
        if not pend_v: st.success("🟢 No hay vecinos esperando recepción.")
        for uid, info in pend_v.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** | Perfil: {info['perfil']} | Recinto: {info['recinto']}")
                c_ok, c_rej = st.columns(2)
                if c_ok.button("✅ AUTORIZAR INGRESO", key=f"s_ok_{uid}"):
                    GLOBAL_MEM['waiting_room'][uid]['estado'] = 'AUTORIZADO'
                    registrar_auditoria(f"SECRETARÍA AUTORIZA INGRESO: {info['nombre']}")
                    st.rerun()
                if c_rej.button("❌ DENEGAR", key=f"s_no_{uid}"):
                    GLOBAL_MEM['waiting_room'][uid]['estado'] = 'EXPIRADO'
                    st.rerun()
                    
        st.divider()
        st.subheader("🤝 2. Audiencias en Curso (Control de Tiempos)")
        reuniones = {k: v for k, v in GLOBAL_MEM['waiting_room'].items() if v['estado'] == 'EN_REUNION'}
        if not reuniones: st.info("🟢 No hay audiencias activas en el sistema.")
        for uid, info in reuniones.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** | RUT: {info['rut']}")
                if st.button("🛑 FINALIZAR REUNIÓN (Cerrar Tiempo)", key=f"s_fin_{uid}"):
                    GLOBAL_MEM['waiting_room'][uid]['estado'] = 'EVALUACION'
                    GLOBAL_MEM['waiting_room'][uid]['fin_reunion'] = datetime.now()
                    registrar_auditoria(f"SECRETARÍA FINALIZA AUDIENCIA: {info['nombre']}")
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
    with t_data:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("📊 Inteligencia Territorial (Big Data)")
        st.metric("Volumen Big Data", f"{len(GLOBAL_MEM['db_master']):,}", "Registros Válidos")
        st.bar_chart(GLOBAL_MEM['db_master']['Recinto'].value_counts(), color="#1e3a8a")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_crm:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔍 CRM Ciudadano")
        search_id = st.text_input("Ingrese ID Único de Visita (Ej: VIS-100050):")
        if search_id:
            idx = GLOBAL_MEM['db_master'].index[GLOBAL_MEM['db_master']['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_form"):
                    tel = st.text_input("Contacto", GLOBAL_MEM['db_master'].at[i, 'Telefono'])
                    if st.form_submit_button("ACTUALIZAR FICHA"):
                        GLOBAL_MEM['db_master'].at[i, 'Telefono'] = tel
                        st.success("✅ Ficha Actualizada en Servidor Global.")
        st.dataframe(GLOBAL_MEM['db_master'].head(50), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with t_logs:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🕵️ Auditoría Inmutable del Servidor")
        for log in GLOBAL_MEM['audit_logs'][:60]: 
            st.code(log, language="bash")
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. ORQUESTADOR PRINCIPAL (LOOP MULTIPLAYER)
# ==================================================================================================

def main():
    bootstrap_enterprise_logic()
    inject_titanium_mobile_css()
    
    # Motor de limpieza de la memoria Global
    now = datetime.now()
    expired_uids = [uid for uid, info in GLOBAL_MEM['waiting_room'].items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired_uids: 
        GLOBAL_MEM['waiting_room'][uid]['estado'] = 'EXPIRADO'
        registrar_auditoria(f"SERVIDOR: Timeout automático de {GLOBAL_MEM['waiting_room'][uid]['nombre']}")

    tab_labels = ["👤 CIUDADANO (QR)", "🖥️ MONITOR MAESTRO", "⚙️ PANEL ADMINISTRATIVO"]
    tab_main_1, tab_main_2, tab_main_3 = st.tabs(tab_labels)
    
    with tab_main_1: view_citizen_node()
    with tab_main_2: view_master_monitor()
    with tab_main_3: view_tactical_and_data()

    st.markdown("""
        <div style='text-align:center; padding:20px; border-top: 2px solid #f1f5f9;'>
            <p style='font-size:1em; font-weight:800; color:#64748b !important;'>
                Gestión Smart City | Ilustre Municipalidad de La Serena<br>
                SGAAC-360 Version 46.0 Global Sync
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__": 
    main()
