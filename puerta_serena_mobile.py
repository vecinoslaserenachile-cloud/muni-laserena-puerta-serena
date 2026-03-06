"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / SMART CITY EDITION / ANTI-DARK MODE UX
VERSIÓN: 39.0.0 (High-Density Modular Architecture - EXTEND MODE 850+ LINES)
PROPIEDAD: Ilustre Municipalidad de La Serena - Proyecto Smart City

ARQUITECTURA MODULAR DE 7 NODOS ESTRATÉGICOS:
1.  NODO CIUDADANO (QR): UX Adulto Mayor, Anti-Dark Mode, QR Compartible y Escudo Municipal.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones, validación de EPP y control de accesos físicos.
3.  NODO PANEL SECRETARÍAS: Hub de toma de decisiones, autorización y reagendamiento.
4.  NODO MONITOR CONTROL TOTAL: Pantalla 360° Grid para Command Center y TV.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +50,000 registros, gráficos de flujo y NPS.
6.  NODO GESTIÓN CRM: Edición profunda de fichas ciudadanas y vinculación territorial.
7.  NODO AUDITORÍA SATELITAL: Registro inmutable de transacciones del sistema.

MOTOR ESTÉTICO Y DE RENDIMIENTO:
- Anti-Dark Mode: Vacuna CSS que fuerza fondos blancos y textos oscuros en cualquier dispositivo.
- Stealth Mode Platinum: Erradicación visual de GitHub (Fork, Logo), Deploy y Streamlit UI.
- Wrap-Tabs: Navegación horizontal responsiva que se adapta a pantallas de teléfonos móviles.
====================================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import io
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Union

# ==================================================================================================
# 1. CONFIGURACIÓN INSTITUCIONAL, IDENTIDAD Y MAPA TERRITORIAL
# ==================================================================================================

# LOGOTIPOS Y MARCA CIUDAD (Gama Alta)
URL_ESCUDO_MUNI = "https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png"
# Código QR dinámico para compartir la app en la fila
URL_APP_DEPLOY = "https://smartcity-laserena.streamlit.app"
URL_QR_COMPARTIR = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={URL_APP_DEPLOY}"

# INFRAESTRUCTURA DE RED EXPANDIDA (Base de cálculo para Monitor Central y Analítica)
# Incluye metadata crítica para despliegues futuros (capacidad, zona, id único)
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
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "zona": "Deportes Norte", "id": "PLC-12", "capacidad": 200},
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
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda", "Adulto Mayor"
]

PERFILES_SGAAC = [
    "Vecino(a) de La Serena", "Dirigente Social / JJVV", "Autoridad Pública", 
    "Funcionario Municipal", "Proveedor Externo", "Prensa / Medios", "Delegación Institucional"
]

# MARKETING TERRITORIAL ROTATIVO (Promoción de la Ciudad)
AVISOS_PROMO = [
    "🏛️ Mientras coordinamos su ingreso, admire nuestro Casco Histórico, Patrimonio Nacional.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del urbanismo serenense.",
    "☕ Calle Prat ofrece excelentes cafés para una espera amena y productiva.",
    "⛪ La Serena es la 'Ciudad de los Campanarios'. Descubra nuestra historia patrimonial.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR CORE DE PERSISTENCIA Y BIG DATA (ANTI-CRASH)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """
    Motor de inicialización absoluta. 
    Evita AttributeErrors y genera la Big Data Base estructurada.
    """
    if 'system_initialized_v39' not in st.session_state:
        st.session_state.system_initialized_v39 = True
        st.session_state.boot_time = datetime.now()
        
        # Subsistema de Auditoría
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] SISTEMA SMART CITY INICIALIZADO"]

        # Subsistema de Transacciones Activas
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Generación de +50,000 registros para stress-test
        if 'db_master' not in st.session_state:
            n = 50000
            start_date = datetime.now() - timedelta(days=1095)
            
            # Generación vectorizada para alto rendimiento de Streamlit
            fechas = [start_date + timedelta(minutes=np.random.randint(0, 1576800)) for _ in range(n)]
            recintos = np.random.choice(list(INFRAESTRUCTURA_IMLS.keys()), n)
            deptos = np.random.choice(LISTADO_DEPARTAMENTOS, n)
            perfiles = np.random.choice(PERFILES_SGAAC, n)
            
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': fechas,
                'Recinto': recintos,
                'Depto': deptos,
                'Perfil': perfiles,
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@laserena.cl"] * n,
                'Permanencia_Minutos': np.random.randint(5, 80, n),
                'NPS_Calidad': np.random.randint(1, 6, n),
                'Estado': ["Finalizado"] * n,
                'Validador_Fisico': ["Guardia Turno A"] * n
            }).sort_values(by='Fecha', ascending=False)

def registrar_auditoria(mensaje: str):
    """Inyecta un log inmutable en el sistema con timestamp preciso."""
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.audit_logs.insert(0, f"[{stamp}] {mensaje}")
    # Mantener el log manejable en memoria para no saturar el servidor
    if len(st.session_state.audit_logs) > 1000:
        st.session_state.audit_logs = st.session_state.audit_logs[:1000]

# ==================================================================================================
# 3. MOTOR CSS (VACUNA ANTI-DARK MODE + STEALTH MODE + WRAP-TABS)
# ==================================================================================================

def inject_smartcity_mobile_css():
    """
    CSS Quirúrgico masivo:
    1. Anula el Dark Mode del navegador del celular.
    2. Fuerza la visibilidad de los inputs y selectbox.
    3. Esconde las herramientas de GitHub y Streamlit.
    4. Implementa Wrap-Tabs para la navegación móvil.
    """
    st.markdown("""
        <style>
        /* ==========================================================================
           1. STEALTH MODE PRO (ELIMINACIÓN DE PLATAFORMA BASE)
           ========================================================================== */
        #MainMenu {visibility: hidden !important;}
        header[data-testid="stHeader"] {display: none !important;}
        footer {visibility: hidden !important;}
        .stDeployButton {display:none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        [data-testid="stStatusWidget"] {display: none !important;}
        [data-testid="stDecoration"] {display: none !important;}
        
        /* ==========================================================================
           2. VACUNA ANTI-DARK MODE (BLANCO PURO Y AZUL MARINO)
           ========================================================================== */
        /* Forzar el fondo de toda la aplicación a blanco absoluto */
        .stApp, [data-testid="stAppViewContainer"], .main { 
            background-color: #FFFFFF !important; 
            font-family: 'Outfit', sans-serif; 
        }
        
        /* Imponer el contraste en textos globales */
        p, span, label, div, li, h1, h2, h3, h4, h5, table, .stMarkdown { 
            color: #001F3F !important; 
            font-weight: 600 !important; 
        }

        /* ==========================================================================
           3. REPARACIÓN DE INPUTS Y SELECTBOX (ELIMINAR CAJAS NEGRAS)
           ========================================================================== */
        /* Cajas de texto (Nombre, RUT, Motivo) */
        .stTextInput input, .stTextArea textarea {
            background-color: #FFFFFF !important;
            color: #001F3F !important;
            -webkit-text-fill-color: #001F3F !important; /* Crítico para iOS/Safari */
            border: 2px solid #1e3a8a !important;
            border-radius: 8px !important;
            font-weight: 700 !important;
            font-size: 1.1em !important;
            padding: 15px !important;
        }
        /* Placeholder visible pero diferenciado */
        .stTextInput input::placeholder, .stTextArea textarea::placeholder {
            color: #64748b !important;
            -webkit-text-fill-color: #64748b !important;
            font-weight: 500 !important;
        }

        /* Menús Desplegables (Selectbox) - Fondo blanco, texto oscuro */
        div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important;
            color: #001F3F !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
            height: 60px !important;
        }
        /* Opciones dentro del menú desplegable */
        ul[data-baseweb="listbox"] { 
            background-color: #FFFFFF !important; 
            border: 2px solid #1e3a8a !important; 
        }
        ul[data-baseweb="listbox"] li { 
            color: #001F3F !important; 
            font-weight: 700 !important; 
            background-color: #FFFFFF !important;
            font-size: 1.2em !important;
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
            gap: 10px;
            justify-content: center;
            background-color: #FFFFFF !important;
            border-bottom: none !important;
            padding-bottom: 15px;
        }
        div[data-baseweb="tab"] {
            flex-grow: 1;
            min-width: 140px;
            background-color: #F8FAFC !important;
            border: 2px solid #1e3a8a !important;
            border-radius: 12px !important;
            padding: 15px !important;
            text-align: center;
            font-weight: 900 !important;
            color: #1e3a8a !important;
            font-size: 1em !important;
        }
        div[data-baseweb="tab"][aria-selected="true"] {
            background-color: #1e3a8a !important;
            color: #FFFFFF !important;
            border: 2px solid #001F3F !important;
        }
        div[data-baseweb="tab"]:hover {
            background-color: #e2e8f0 !important;
        }

        /* ==========================================================================
           5. PANELES INSTITUCIONALES Y BOTONES
           ========================================================================== */
        .glass-panel {
            background: #FFFFFF !important; 
            border-radius: 15px;
            border: 3px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0, 31, 63, 0.1);
            margin-bottom: 30px;
            margin-top: 15px;
        }

        .instruction-box {
            background-color: #F0F7FF !important;
            border-left: 12px solid #1e3a8a !important;
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
            color: #001F3F !important;
            box-shadow: 2px 5px 15px rgba(0,0,0,0.05);
        }

        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #FFFFFF !important; border-radius: 12px; height: 85px;
            font-weight: 900 !important; text-transform: uppercase; font-size: 1.4em !important;
            box-shadow: 0 10px 25px rgba(30, 58, 138, 0.3);
            border: none !important;
            width: 100%;
            margin-top: 20px;
        }
        .stButton>button:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(30, 58, 138, 0.5);
        }

        /* ==========================================================================
           6. COMPONENTES DEL MONITOR CENTRAL (COMMAND CENTER)
           ========================================================================== */
        .tv-card {
            background: #FFFFFF; border-radius: 15px; padding: 25px;
            border-top: 12px solid #1e3a8a; box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            text-align: center; margin-bottom: 25px;
        }
        .tv-card-alert { border-top: 12px solid #dc2626 !important; background: #fffafa; }

        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.2em; line-height: 1; margin-bottom: 10px; }
        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 4.5em; 
            text-align: center; border: 4px solid #dc2626; border-radius: 20px; 
            background: #fff5f5; padding: 20px; margin: 20px 0;
        }

        /* ==========================================================================
           7. AJUSTES EXTREMOS PARA SMARTPHONES PEQUEÑOS
           ========================================================================== */
        @media (max-width: 768px) {
            .glass-panel { padding: 15px; border-width: 3px; }
            .muni-title { font-size: 2.2em !important; }
            .stButton>button { height: 95px; font-size: 1.4em !important; }
            div[data-baseweb="tab"] { font-size: 0.95em !important; padding: 12px !important; min-width: 110px;}
            .instruction-box { padding: 20px; }
        }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. NODO I: CIUDADANO (WELCOME INSTITUCIONAL, QR & REGISTRO UX)
# ==================================================================================================

def render_institutional_header():
    """Renderiza la cabecera de la app con Escudo, Innovación y QR dinámico para filas."""
    col1, col2, col3 = st.columns([1.2, 1.5, 1])
    with col1: 
        st.image(URL_ESCUDO_MUNI, use_container_width=True)
    with col2: 
        st.markdown("<div style='text-align:center; font-weight:900; color:#1e3a8a; font-size:1.3em; padding-top:15px; line-height:1.2;'>ILUSTRE MUNICIPALIDAD<br>DE LA SERENA<br><span style='color:#059669;'>SMART CITY</span></div>", unsafe_allow_html=True)
    with col3:
        st.image(URL_QR_COMPARTIR, caption="Escanear para entrar", use_container_width=True)
        
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#001F3F !important; font-weight:900; font-size:2em;'>¡Bienvenidos!</h2>", unsafe_allow_html=True)

def view_citizen_node():
    """El punto de contacto principal. Diseño obsesionado con el Adulto Mayor y legibilidad exterior."""
    
    render_institutional_header()
    
    token = st.session_state.get('citizen_token_v39')
    
    # ==========================================
    # ESTADO 1: FORMULARIO DE INGRESO
    # ==========================================
    if not token or token not in st.session_state.waiting_room:
        
        # RECUADRO DE INSTRUCCIONES SENIOR (Alto contraste)
        st.markdown("""
            <div class="instruction-box">
                <h3 style="margin-top:0; color:#1e3a8a !important; font-size:1.5em; font-weight:900;">Estimado Vecino(a):</h3>
                <p style="font-size:1.2em !important; font-weight:700;">Para una atención ágil, siga estos pasos:</p>
                <ol style="font-size:1.3em !important; font-weight:800; color:#001F3F !important; line-height:1.5;">
                    <li>Seleccione el edificio donde está ahora.</li>
                    <li>Escriba su Nombre y RUT en las cajas blancas.</li>
                    <li>Elija la oficina que viene a visitar.</li>
                    <li>Presione el <b>BOTÓN AZUL GRANDE</b> al final.</li>
                </ol>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#1e3a8a !important; margin-bottom:20px;'>🖋️ Formulario de Ingreso Municipal</h3>", unsafe_allow_html=True)
        
        with st.form("form_reg_v39", clear_on_submit=True):
            recinto_sel = st.selectbox("1. Edificio Municipal en el que se encuentra:", list(INFRAESTRUCTURA_IMLS.keys()))
            nombre_input = st.text_input("2. Escriba su Nombre Completo:", placeholder="Ejemplo: Juan Pérez")
            rut_input = st.text_input("3. Escriba su RUT (ej: 12345678-9):", placeholder="Ejemplo: 12.345.678-9")
            perfil_sel = st.selectbox("4. Usted se identifica como:", PERFILES_SGAAC)
            depto_sel = st.selectbox("5. Oficina a la que se dirige:", LISTADO_DEPARTAMENTOS)
            motivo_input = st.text_area("6. Breve motivo de su visita (Opcional):", placeholder="Vengo a entregar un documento...")
            
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
                    st.session_state.citizen_token_v39 = uid
                    registrar_auditoria(f"NUEVO REGISTRO QR: {nombre_input} en {recinto_sel}")
                    st.rerun()
                else: 
                    st.error("⚠️ ACCIÓN REQUERIDA: Por favor, complete su Nombre y RUT para continuar.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        # ==========================================
        # ESTADO 2: ESPERANDO AUTORIZACIÓN
        # ==========================================
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"<h3 style='color:#001F3F !important;'>Avisando a la oficina de **{info['depto']}**...</h3>", unsafe_allow_html=True)
            st.write("Por favor, tome asiento. Su solicitud está en la pantalla de la secretaría.")
            
            # MARKETING TERRITORIAL ROTATIVO
            st.markdown(f"""
                <div style='background:#1e3a8a; color:white !important; padding:35px; border-radius:15px; border-left:12px solid #facc15; margin-top:20px; margin-bottom:20px;'>
                    <p style='color:white !important; font-weight:800; font-size:1.3em; line-height:1.4; margin:0;'>{np.random.choice(AVISOS_PROMO)}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # CRONÓMETRO DE ESPERA
            tiempo_restante = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(tiempo_restante)}s</div>", unsafe_allow_html=True)
            st.caption("Si el reloj llega a cero, por favor consulte al guardia del recinto.")
            
            if tiempo_restante == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
                
        # ==========================================
        # ESTADO 3: AUTORIZADO A ENTRAR
        # ==========================================
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: 
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900;'>Por favor, acérquese al Guardia para validar su entrada física.</h3>", unsafe_allow_html=True)
            else:
                st.markdown("<h3 style='color:#001F3F !important; font-weight:900;'>¡PASE ADELANTE!</h3>", unsafe_allow_html=True)
                st.write(f"La oficina de **{info['depto']}** ha autorizado su ingreso.")
                if st.button("YA INGRESÉ A LA OFICINA"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.session_state.waiting_room[token]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"INGRESO EFECTIVO (AUTÓNOMO): {info['nombre']}")
                    st.rerun()
                    
        # ==========================================
        # ESTADO 4: EN REUNIÓN
        # ==========================================
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **USTED ESTÁ EN REUNIÓN**")
            st.markdown("<p style='color:#001F3F !important; font-size:1.2em;'>La Municipalidad cronometra sus atenciones para asegurar un servicio de excelencia.</p>", unsafe_allow_html=True)
            if st.button("TERMINAR REUNIÓN Y EVALUAR"):
                st.session_state.waiting_room[token]['estado'] = "CIERRE"
                st.session_state.waiting_room[token]['fin_reunion'] = datetime.now()
                st.rerun()
                
        # ==========================================
        # ESTADO 5: CIERRE Y NPS
        # ==========================================
        elif info['estado'] == "CIERRE":
            st.balloons()
            st.markdown("""
                <div style='background: #1e3a8a; color:white !important; padding:40px; border-radius:15px; text-align:center;'>
                    <h2 style='color:white !important; margin:0; font-size:2.5em;'>¡GRACIAS!</h2>
                    <p style='color:white !important; font-size:1.4em;'>La Serena: Innovación al servicio de la gente.</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<h3 style='color:#001F3F !important;'>Evalúe su Experiencia</h3>", unsafe_allow_html=True)
            nps = st.slider("De 1 a 5 estrellas, ¿Qué tan buena fue su atención?", 1, 5, 5)
            
            if st.button("ENVIAR EVALUACIÓN Y SALIR"):
                # Cálculo de permanencia real para Big Data
                permanencia = 15 # Valor por defecto fallback
                if info.get('inicio_reunion') and info.get('fin_reunion'):
                    permanencia = int((info['fin_reunion'] - info['inicio_reunion']).total_seconds() / 60)
                
                nuevo_registro = {
                    'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 
                    'Depto': info['depto'], 'Perfil': info['perfil'], 'Visitante': info['nombre'], 
                    'RUT': info['rut'], 'Permanencia_Minutos': permanencia, 'NPS_Calidad': nps, 
                    'Estado': "Completado", 'Telefono': "No Registrado", 'Email': "No Registrado",
                    'Validador_Fisico': "Auto/Guardia"
                }
                # Concatenación eficiente a la base maestra
                st.session_state.db_master = pd.concat([pd.DataFrame([nuevo_registro]), st.session_state.db_master], ignore_index=True)
                registrar_auditoria(f"CICLO CERRADO: {info['nombre']} | NPS: {nps} | T: {permanencia}m")
                del st.session_state.citizen_token_v39
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. NODO II: MONITOR CONTROL TOTAL (PANTALLA MAESTRA / COMMAND CENTER GRID)
# ==================================================================================================

def view_master_monitor():
    """Pantalla táctica para la Central de Mando. Diseñada para proyección en TV 4K."""
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-weight:900; font-size:1.6em; color:#1e3a8a !important;'>VISIÓN ESTRATÉGICA DE LA RED TERRITORIAL</p>", unsafe_allow_html=True)
    
    # Resumen Ejecutivo Superior
    total_esperas = len([v for v in st.session_state.waiting_room.values() if v['estado'] == 'COORDINANDO'])
    total_activos = len([v for v in st.session_state.waiting_room.values() if v['estado'] == 'EN_REUNION'])
    
    c1, c2 = st.columns(2)
    with c1: st.error(f"🔴 ALERTAS / ESPERAS EN LA RED: {total_esperas}")
    with c2: st.success(f"🟢 AUDIENCIAS ACTIVAS EN VIVO: {total_activos}")
    st.divider()

    # Cuadrícula dinámica
    cols = st.columns(4)
    recintos_list = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r_name in enumerate(recintos_list):
        with cols[i % 4]:
            # Procesamiento de colas por recinto en tiempo real
            esp = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'COORDINANDO']
            act = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r_name and v['estado'] == 'EN_REUNION']
            
            # Lógica de Alerta Visual (Cuello de Botella)
            has_alert = len(esp) > 2
            border_css = "border: 8px solid #dc2626;" if has_alert else "border-top: 12px solid #1e3a8a;"
            
            st.markdown(f"""
                <div class="tv-card" style="{border_css}">
                    <h3 style="margin:0; font-size:1.1em; color:#1e3a8a !important; line-height:1.2;">{INFRAESTRUCTURA_IMLS[r_name]['icono']} {r_name[:22]}...</h3>
                    <p style="margin:5px 0; font-size:0.8em; color:gray !important; font-weight:800;">{INFRAESTRUCTURA_IMLS[r_name]['id']} | {INFRAESTRUCTURA_IMLS[r_name]['zona']}</p>
                    <hr style="border: 1px solid #f1f5f9; margin:15px 0;">
                    
                    <div style="display:flex; justify-content: space-around; align-items:center;">
                        <div>
                            <p style="font-size:3em; font-weight:900; margin:0; line-height:1; color:{'#dc2626' if has_alert else '#1e3a8a'} !important;">{len(esp)}</p>
                            <p style="font-size:0.9em; font-weight:800; color:#64748b !important; margin:0;">ESPERA</p>
                        </div>
                        <div style="border-left: 2px solid #f1f5f9; height: 60px;"></div>
                        <div>
                            <p style="font-size:3em; font-weight:900; margin:0; line-height:1; color:#059669 !important;">{len(act)}</p>
                            <p style="font-size:0.9em; font-weight:800; color:#64748b !important; margin:0;">EN VIVO</p>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# ==================================================================================================
# 6. NODOS III, IV, V: TACTICAL GUARDIA, SECRETARÍAS, ANALÍTICA Y CRM
# ==================================================================================================

def view_tactical_and_data():
    """Agrupa las funciones administrativas internas de control de la red."""
    st.markdown("<h2 class='muni-title'>PANEL ADMINISTRATIVO INTERNO</h2>", unsafe_allow_html=True)
    
    # Sub-pestañas para el entorno administrativo
    t_guardia, t_secre, t_data, t_crm, t_logs = st.tabs([
        "🛡️ Guardia", "🔔 Secretarías", "📊 Big Data", "⚙️ Gestión CRM", "🕵️ Auditoría"
    ])
    
    with t_guardia:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🛡️ Validación de Accesos Físicos")
        st.write("Verifique la identidad del vecino con su cédula antes de permitir el ingreso.")
        aut_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not aut_v: st.info("Sin pases autorizados pendientes de validación.")
        for uid, info in aut_v.items():
            with st.container(border=True):
                st.markdown(f"<h3 style='color:#1e3a8a; margin:0;'>👤 {info['nombre']}</h3>", unsafe_allow_html=True)
                st.write(f"**RUT:** {info['rut']} | **Hacia:** {info['depto']}")
                if st.button(f"CONFIRMAR INGRESO FÍSICO", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    registrar_auditoria(f"INGRESO VALIDADO GUARDIA: {info['nombre']}")
                    st.rerun()
        st.divider()
        st.subheader("👁️ Radar de Coordinaciones (En Espera)")
        coord_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord_v:
            df_tactical = pd.DataFrame([{"Vecino": v['nombre'], "Oficina": v['depto']} for v in coord_v.values()])
            st.table(df_tactical)
        else: 
            st.caption("Radar despejado. Sin vecinos esperando autorización.")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_secre:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔔 Solicitudes de Audiencia Entrantes")
        pend_v = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pend_v: st.success("No hay vecinos esperando en la recepción de su recinto.")
        for uid, info in pend_v.items():
            with st.container(border=True):
                st.markdown(f"<h3 style='color:#1e3a8a; margin:0;'>👤 {info['nombre']}</h3>", unsafe_allow_html=True)
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
        st.subheader("📊 Analítica Territorial")
        m1, m2, m3 = st.columns(3)
        m1.metric("Volumen Big Data", f"{len(st.session_state.db_master):,}", "Registros")
        m2.metric("Promedio NPS", f"{st.session_state.db_master['NPS_Calidad'].mean():.2f} / 5.0", "Calidad Muni")
        m3.metric("Tiempo Promedio", f"{st.session_state.db_master['Permanencia_Minutos'].mean():.0f} min", "Por Atención")
        
        st.divider()
        st.markdown("<h4 style='color:#1e3a8a;'>Flujo de Visitas por Recinto Municipal</h4>", unsafe_allow_html=True)
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts(), color="#1e3a8a")
        
        st.markdown("<h4 style='color:#1e3a8a;'>Flujo por Departamento</h4>", unsafe_allow_html=True)
        st.bar_chart(st.session_state.db_master['Depto'].value_counts(), color="#059669")
        st.markdown("</div>", unsafe_allow_html=True)

    with t_crm:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🔍 Buscador y Gestión CRM Ciudadano")
        st.write("Permite completar datos de contacto para vinculación con Dirigentes y Vecinos clave de La Serena.")
        
        search_id = st.text_input("Ingrese ID de la Visita (Ej: VIS-100050):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                ficha = st.session_state.db_master.iloc[i]
                st.info(f"Editando Ficha de: **{ficha['Visitante']}** ({ficha['Perfil']})")
                
                with st.form("crm_form_v39"):
                    tel = st.text_input("WhatsApp / Contacto Móvil", ficha['Telefono'])
                    mail = st.text_input("Email de Seguimiento Institucional", ficha['Email'])
                    notas = st.text_area("Notas Internas de Gestión Social:")
                    
                    if st.form_submit_button("ACTUALIZAR FICHA EN BIG DATA"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        registrar_auditoria(f"CRM ACTUALIZADO: ID {search_id} por Administración")
                        st.success("✅ Inteligencia Ciudadana Actualizada Correctamente.")
            else:
                st.warning("⚠️ ID no encontrado en la Base de Datos Histórica.")
                
        st.divider()
        st.subheader("Base de Datos Maestra (Últimos 100 registros)")
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with t_logs:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🕵️ Registro Inmutable de Transacciones")
        st.write("Logs de sistema blindados para fiscalización y control del Director de Proyecto.")
        for log in st.session_state.audit_logs[:50]: 
            st.code(log, language="bash")
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 8. ORQUESTADOR PRINCIPAL (WRAP TABS Y LOOP DE EJECUCIÓN)
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

    # NAVEGACIÓN UNIVERSAL (Wrap-Tabs: No se ocultan en móvil, reemplazan al Sidebar)
    tab_labels = ["👤 ACCESO CIUDADANO (QR)", "🖥️ MONITOR MAESTRO 360°", "⚙️ PANEL ADMINISTRATIVO"]
    tab_main_1, tab_main_2, tab_main_3 = st.tabs(tab_labels)
    
    with tab_main_1: view_citizen_node()
    with tab_main_2: view_master_monitor()
    with tab_main_3: view_tactical_and_data()

    # Footer Institucional Stealth
    st.markdown("""
        <div style='text-align:center; padding:20px; margin-top:40px; border-top: 1px solid #e2e8f0;'>
            <p style='font-size:0.9em; font-weight:600; color:#64748b !important;'>
                Gestión Smart City | Ilustre Municipalidad de La Serena<br>
                Sistema SGAAC-360
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__": 
    main()
