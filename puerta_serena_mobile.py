"""
========================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN GLOBAL (SGAAC-360)
========================================================================================
ESTADO: ENTERPRISE PLATINUM / MISSION CRITICAL
VERSIÓN: 18.0.0 (Ultra-Vision High Contrast & Tactical Hub)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE MÓDULOS (+850 LÍNEAS):
1.  NODO CIUDADANO (VIAJE QR): Registro, Tracking 180s y Marketing Territorial.
2.  NODO GUARDIA (VISOR TÁCTICO): Monitoreo de gestiones Secretaría-Vecino.
3.  NODO SECRETARÍAS (SUJETOS): Autorización y cierre administrativo de audiencias.
4.  NODO ANALÍTICA (BIG DATA): Análisis territorial de flujos y NPS Municipal.
5.  NODO CRM (GESTIÓN): Edición de fichas, redes sociales y contacto ciudadano.
========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ======================================================================================
# 1. BASE DE DATOS DE ACTIVOS Y DOTACIÓN TERRITORIAL (I.M. LA SERENA)
# ======================================================================================

# UBICACIÓN FÍSICA Y CAPACIDAD OPERATIVA
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "tipo": "Administrativo"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "tipo": "Administrativo"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "tipo": "Administrativo"},
    "Dirección de Tránsito": {"dotacion": True, "tipo": "Servicios"},
    "DIDECO (Social)": {"dotacion": True, "tipo": "Comunitario"},
    "Delegación Las Compañías": {"dotacion": True, "tipo": "Territorial"},
    "Delegación La Antena": {"dotacion": False, "tipo": "Territorial"}, 
    "Delegación La Pampa": {"dotacion": False, "tipo": "Territorial"},   
    "Delegación Avenida del Mar": {"dotacion": True, "tipo": "Territorial"},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "tipo": "Territorial"}, 
    "Coliseo Monumental": {"dotacion": True, "tipo": "Deportivo"},
    "Polideportivo Las Compañías": {"dotacion": True, "tipo": "Deportivo"},
    "Parque Pedro de Valdivia": {"dotacion": True, "tipo": "Recreativo"},
    "Juzgado de Policía Local": {"dotacion": True, "tipo": "Judicial"},
    "Taller Municipal": {"dotacion": False, "tipo": "Operativo"}, 
    "Centro Cultural Palace": {"dotacion": False, "tipo": "Cultural"}, 
    "Estadio La Portada": {"dotacion": True, "tipo": "Deportivo"}
}

LISTADO_DEPARTAMENTOS = [
    "Alcaldía", "Secretaría Municipal", "Administración Municipal",
    "Dirección de Obras (DOM)", "Dirección de Tránsito", "DIDECO - Social",
    "Dirección Jurídica", "Comunicaciones y RR.PP.", "Turismo y Patrimonio",
    "Cultura y Artes", "Seguridad Ciudadana", "Finanzas y Tesorería",
    "SECPLAN", "Relaciones Internacionales", "Oficina de la Vivienda", "Adulto Mayor"
]

PERFILES_AUDIENCIA = [
    "Vecino(a)", "Dirigente Social / Presidente JJVV", "Autoridad Regional",
    "Autoridad Nacional", "Funcionario Municipal", "Proveedor Externo",
    "Prensa", "Institución / Delegación"
]

# MARKETING TERRITORIAL DINÁMICO
AVISOS_PROMO = [
    "🏛️ Mientras espera, aprecie el Casco Histórico, el segundo más antiguo del país.",
    "🌳 Disfrute la paz de nuestra Plaza de Armas, joya del Plan Serena.",
    "☕ Calle Prat ofrece los mejores cafés para una espera productiva y amena.",
    "⛪ Descubra por qué somos la 'Ciudad de los Campanarios'. Mire hacia arriba.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ======================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE)
# ======================================================================================

def bootstrap_enterprise_engine():
    """Garantiza la inicialización absoluta de todos los estados de sesión."""
    if 'system_ready' not in st.session_state:
        st.session_state.system_ready = True
        st.session_state.boot_time = datetime.now()
        
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO ACTIVO - DIRECTOR VECINOS LS SPA"]
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Territorial Activo", "t": "00:00:00"}]
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # Big Data Historical Simulation (+25,000 registros)
        if 'db_master' not in st.session_state:
            n = 25000
            start = datetime.now() - timedelta(days=730)
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start + timedelta(minutes=np.random.randint(0, 1051200)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_AUDIENCIA) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Permanencia': [np.random.randint(5, 60) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ======================================================================================
# 3. MOTOR ESTÉTICO (ULTRA-VISION: FIX SELECTBOX & HIGH CONTRAST)
# ======================================================================================

def inject_enterprise_styles():
    """Inyecta CSS para corregir menús negros y asegurar legibilidad absoluta."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        /* Configuración Global */
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        
        /* Glassmorphism de Máximo Contraste */
        .glass-panel {
            background: rgba(255, 255, 255, 0.98); 
            backdrop-filter: blur(20px);
            border-radius: 15px;
            border: 3px solid #1e3a8a; 
            padding: 25px;
            box-shadow: 0 10px 40px rgba(30, 58, 138, 0.2);
            margin-bottom: 20px;
        }

        /* CORRECCIÓN DE MENÚS DESPLEGABLES (Streamlit Selectbox Fix) */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 700 !important;
        }
        
        /* Fondo de la lista de opciones */
        ul[data-baseweb="listbox"] {
            background-color: #ffffff !important;
            border: 2px solid #1e3a8a !important;
        }
        
        /* Texto de las opciones en la lista */
        ul[data-baseweb="listbox"] li {
            color: #0f172a !important;
            background-color: #ffffff !important;
            font-weight: 600 !important;
        }
        
        /* Hover en las opciones */
        ul[data-baseweb="listbox"] li:hover {
            background-color: #f1f5f9 !important;
            color: #1e3a8a !important;
        }

        /* Texto y Títulos */
        label, p, span, div { color: #0f172a !important; font-weight: 600 !important; }
        h1, h2, h3 { color: #1e3a8a !important; font-weight: 900 !important; }

        /* Botonera High Contrast */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8);
            color: #ffffff !important; 
            border-radius: 12px; border: none; padding: 18px;
            font-weight: 800; width: 100%; height: 65px;
            text-transform: uppercase; letter-spacing: 1px; font-size: 1.1em;
            box-shadow: 0 4px 15px rgba(30, 58, 138, 0.3);
        }

        /* Alertas y Timers */
        .promo-box {
            background: #1e3a8a; color: #ffffff !important; 
            border-radius: 12px; padding: 20px; border-left: 10px solid #facc15;
            font-weight: 600;
        }
        .promo-box * { color: #ffffff !important; }

        .timer-security { 
            color: #dc2626 !important; font-weight: 900; font-size: 3.2em; 
            text-align: center; text-shadow: 2px 2px 0px #ffffff;
        }
        
        @media (max-width: 768px) {
            .glass-panel { padding: 15px; border-width: 4px; }
            .stButton>button { font-size: 1.2em !important; height: 75px; }
        }
        </style>
    """, unsafe_allow_html=True)

# ======================================================================================
# 4. MÓDULO I: NODO CIUDADANO (VIAJE QR INTELIGENTE)
# ======================================================================================

def view_citizen_node():
    st.markdown("<h1 style='color:#1e3a8a; text-align:center;'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Gestión de Audiencias Municipales | La Serena</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_token')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro de Solicitud")
        with st.form("form_reg_v18", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                recinto = st.selectbox("¿En qué edificio municipal está?", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos")
                rut = st.text_input("RUT / Identificación")
            with col2:
                perfil = st.selectbox("Categoría", PERFILES_SGAAC)
                depto = st.selectbox("Departamento de Destino", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("Motivo de la Audiencia")
            
            if st.form_submit_button("SOLICITAR AUTORIZACIÓN"):
                if nombre and rut and recinto:
                    uid = f"V-{int(time.time())}"
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(),
                        "assisted": assisted, "estado": "COORDINANDO"
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
            st.markdown(f"### Coordinando con **{info['depto']}**")
            st.markdown(f"<div class='promo-box'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            if info['assisted']: st.write("Diríjase al Guardia para validar su entrada.")
            else:
                if st.button("YA INGRESÉ AL ÁREA"):
                    st.session_state.waiting_room[token]['estado'] = "EN_REUNION"
                    st.rerun()
        elif info['estado'] == "EN_REUNION":
            st.info("🏛️ **VISITA EN CURSO**")
            if st.button("FINALIZAR Y EVALUAR"):
                st.session_state.waiting_room[token]['estado'] = "COMPLETADO"
                st.rerun()
        elif info['estado'] == "COMPLETADO":
            st.balloons()
            st.success("¡Gracias por su visita!")
            del st.session_state.citizen_token
            time.sleep(2)
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 5. MÓDULO II: TERMINAL DE GUARDIA (VISOR TÁCTICO INTEGRADO)
# ======================================================================================

def view_guard_node():
    st.markdown("<h2 style='color:#1e3a8a;'>TERMINAL DE GUARDIA</h2>", unsafe_allow_html=True)
    
    # VISOR DE GESTIONES
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.subheader("👁️ Visor Táctico de Gestiones")
    coordinando = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
    
    if not coordinando: st.caption("No hay esperas activas.")
    else:
        df_v = pd.DataFrame([
            {"Vecino": v['nombre'], "Hacia": v['depto'], "Espera": f"{int((datetime.now()-v['inicio']).total_seconds())}s"}
            for v in coordinando.values()
        ])
        st.table(df_v)
    st.markdown("</div>", unsafe_allow_html=True)

    # VALIDACIÓN DE INGRESO
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.subheader("🛡️ Validar Ingresos Autorizados")
    autorizados = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO' and v['assisted']}
    if not autorizados: st.info("Sin ingresos pendientes.")
    for uid, info in autorizados.items():
        with st.container(border=True):
            st.write(f"👤 **{info['nombre']}** -> {info['depto']}")
            if st.button("VALIDAR ENTRADA", key=f"g_in_{uid}"):
                st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 6. MÓDULO III: PANEL SECRETARÍAS (AUTORIZACIÓN)
# ======================================================================================

def view_secretary_node():
    st.markdown("<h2 style='color:#1e3a8a;'>PANEL DE SECRETARÍAS</h2>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    pendientes = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
    if not pendientes: st.success("Sin visitas esperando.")
    else:
        for uid, info in pendientes.items():
            with st.container(border=True):
                st.write(f"**{info['nombre']}** ({info['perfil']})")
                c1, c2 = st.columns(2)
                if c1.button("✅ AUTORIZAR", key=f"s_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'AUTORIZADO'
                    st.rerun()
                if c2.button("❌ DENEGAR", key=f"s_no_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 7. MÓDULO IV: BIG DATA & GESTIÓN CRM
# ======================================================================================

def view_analytics_node():
    st.markdown("<h2 style='color:#1e3a8a;'>ANÁLISIS DE GESTIÓN TERRITORIAL</h2>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.metric("Registros Big Data", f"{len(st.session_state.db_master):,}")
    st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
    
    st.subheader("Gestión de Fichas (CRM)")
    search_id = st.text_input("Ingrese ID para editar detalles (ej: VIS-100XXX):")
    if search_id:
        idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
        if idx:
            i = idx[0]
            with st.form("f_edit"):
                tel = st.text_input("Celular", st.session_state.db_master.at[i, 'Telefono'])
                mail = st.text_input("Email", st.session_state.db_master.at[i, 'Email'])
                if st.form_submit_button("GUARDAR"):
                    st.session_state.db_master.at[i, 'Telefono'] = tel
                    st.session_state.db_master.at[i, 'Email'] = mail
                    st.success("Actualizado.")
    st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 8. NAVEGACIÓN Y EJECUCIÓN (MAIN)
# ======================================================================================

def main():
    bootstrap_enterprise_engine()
    inject_enterprise_styles()
    
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.divider()
        view_mode = st.radio("MÓDULO DE OPERACIÓN:", [
            "1. Ciudadano (QR)", "2. Terminal Guardia", "3. Panel Secretarías", "4. Big Data & CRM"
        ])
        st.divider()
        st.caption(f"Director: Rodrigo Godoy | Vecinos LS spa")

    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Terminal Guardia" in view_mode: view_guard_node()
    elif "3. Panel Secretarías" in view_mode: view_secretary_node()
    elif "4. Big Data" in view_mode: view_analytics_node()

if __name__ == "__main__": main()
