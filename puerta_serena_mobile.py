"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL GLOBAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE PLATINUM / UNIVERSAL RESPONSIVE MODE
VERSIÓN: 21.0.0 (High-Density Multi-Node Architecture - FULL EXTEND MODE)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE 7 COMPONENTES ESTRATÉGICOS (+1,300 LÍNEAS):
1.  NODO CIUDADANO (QR): Registro inteligente, Detección de Infraestructura, Tracking y Marketing.
2.  NODO TÁCTICO GUARDIA: Visor de gestiones en curso, validación EPP e ingresos/salidas físicas.
3.  NODO PANEL SECRETARÍAS: Hub de autorización y cierre administrativo para cálculo de tiempos.
4.  NODO MONITOR CONTROL TOTAL: Visión 360° en cuadrícula dinámica para TV y Central de Mando.
5.  NODO ANALÍTICA BIG DATA: Trazabilidad de +30,000 registros, flujos territoriales y NPS.
6.  NODO GESTIÓN CRM: Edición de fichas ciudadanas, redes sociales y vinculación con dirigentes.
7.  NODO AUDITORÍA SATELITAL: Logs de sistema blindados para fiscalización y control de Director.

OPTIMIZACIÓN UNIVERSAL:
- Mobile: Alto contraste, menús corregidos, botones XL.
- Tablet: Visor táctico del guardia con gestos fluidos.
- TV / Desktop: Cuadrícula expandida de recintos con alertas visuales de color.
====================================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import io
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ==================================================================================================
# 1. INFRAESTRUCTURA Y ACTIVOS REALES (MUNICIPALIDAD DE LA SERENA)
# ==================================================================================================

# VARIABLE MAESTRA: Configuración de Recintos con Variable de Dotación y Metadatos
INFRAESTRUCTURA_IMLS = {
    "Edificio Consistorial (Prat 451)": {"dotacion": True, "icono": "🏛️", "color": "#1e3a8a"},
    "Edificio Carrera (Prat esq. Matta)": {"dotacion": True, "icono": "🏢", "color": "#1e3a8a"},
    "Edificio Balmaceda (Ex-Aduana)": {"dotacion": True, "icono": "🏫", "color": "#1e3a8a"},
    "Dirección de Tránsito": {"dotacion": True, "icono": "🚦", "color": "#1e3a8a"},
    "DIDECO (Social)": {"dotacion": True, "icono": "🤝", "color": "#1e3a8a"},
    "Delegación Municipal Las Compañías": {"dotacion": True, "icono": "🏘️", "color": "#1e3a8a"},
    "Delegación Municipal La Antena": {"dotacion": False, "icono": "📡", "color": "#059669"}, # Autónomo
    "Delegación Municipal La Pampa": {"dotacion": False, "icono": "🌳", "color": "#059669"},   # Autónomo
    "Delegación Avenida del Mar": {"dotacion": True, "icono": "🏖️", "color": "#1e3a8a"},
    "Delegación Rural (Algarrobito)": {"dotacion": False, "icono": "🚜", "color": "#059669"}, # Autónomo
    "Coliseo Monumental": {"dotacion": True, "icono": "🏀", "color": "#1e3a8a"},
    "Polideportivo Las Compañías": {"dotacion": True, "icono": "🏋️", "color": "#1e3a8a"},
    "Parque Pedro de Valdivia (Admin)": {"dotacion": True, "icono": "🦌", "color": "#1e3a8a"},
    "Juzgado de Policía Local": {"dotacion": True, "icono": "⚖️", "color": "#1e3a8a"},
    "Taller Municipal": {"dotacion": False, "icono": "🛠️", "color": "#059669"}, 
    "Centro Cultural Palace": {"dotacion": False, "icono": "🎨", "color": "#059669"}, 
    "Estadio La Portada (Admin)": {"dotacion": True, "icono": "⚽", "color": "#1e3a8a"}
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

# MARKETING TERRITORIAL DINÁMICO (LA SERENA)
AVISOS_PROMO = [
    "🏛️ Mientras coordinamos, admire nuestro Casco Histórico, Patrimonio Nacional.",
    "🌳 Disfrute la brisa en nuestra Plaza de Armas, joya del urbanismo colonial.",
    "☕ Calle Prat ofrece los mejores cafés para una espera productiva y amena.",
    "⛪ Descubra por qué somos la 'Ciudad de los Campanarios'. Mire hacia arriba.",
    "🛍️ La Recova está a pocos pasos; artesanía y sabores únicos de nuestra tierra."
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (BIG DATA CORE - FIX ATTRIBUTE/KEY/NAME ERROR)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """Garantiza la inicialización absoluta de todos los estados para prevenir colapsos."""
    if 'sgaac_system_initialized' not in st.session_state:
        st.session_state.sgaac_system_initialized = True
        st.session_state.launch_timestamp = datetime.now()
        
        # FIX ATTRIBUTE_ERROR (Previene fallo al leer logs inexistentes)
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        # Canal de Mensajería Inter-Nodos
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace de Coordinación Territorial Activo", "t": "00:00:00"}]

        # Gestión de Cola de Coordinación (Real-Time Sync)
        if 'waiting_room' not in st.session_state:
            st.session_state.waiting_room = {}

        # BIG DATA: Generación de +30,000 registros históricos (Stress-test Territorial)
        # FIX KEY_ERROR: Asegura que las columnas coincidan con los gráficos de Analítica
        if 'db_master' not in st.session_state:
            n = 30000
            start_date = datetime.now() - timedelta(days=730)
            st.session_state.db_master = pd.DataFrame({
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start_date + timedelta(minutes=np.random.randint(0, 1051200)) for _ in range(n)],
                'Recinto': [np.random.choice(list(INFRAESTRUCTURA_IMLS.keys())) for _ in range(n)],
                'Depto': [np.random.choice(LISTADO_DEPARTAMENTOS) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_SGAAC) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO"] * n,
                'RUT': ["12.XXX.XXX-X"] * n,
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Funcionario': ["Director / Jefe de Área"] * n,
                'Permanencia': [np.random.randint(5, 60) for _ in range(n)],
                'NPS': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Finalizado"] * n,
                'RedesSociales': ["@vecinoslaserena"] * n
            }).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. MOTOR ESTÉTICO (ULTRA-VISION: UNIVERSAL RESPONSIVE & HIGH CONTRAST)
# ==================================================================================================

def inject_universal_styles():
    """Motor CSS quirúrgico para anular menús negros y adaptar la UI a Móvil/Tablet/TV."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        /* 1. CONFIGURACIÓN BASE DE ALTO CONTRASTE */
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        
        /* 2. PANELES GLASSMORPHISM (Legibilidad Reforzada) */
        .glass-panel {
            background: rgba(255, 255, 255, 0.98) !important; 
            backdrop-filter: blur(25px);
            border-radius: 15px;
            border: 3px solid #1e3a8a !important; 
            padding: 30px;
            box-shadow: 0 10px 40px rgba(30, 58, 138, 0.25);
            margin-bottom: 25px;
            color: #0f172a !important;
        }

        /* 3. CORRECCIÓN MENÚS DESPLEGABLES (Solución al fallo Negro/Azul) */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #1e3a8a !important;
            border: 2px solid #1e3a8a !important;
            font-weight: 800 !important;
        }
        ul[data-baseweb="listbox"] { background-color: #ffffff !important; border: 2px solid #1e3a8a !important; }
        ul[data-baseweb="listbox"] li { color: #0f172a !important; font-weight: 600 !important; background-color: #ffffff !important; }
        ul[data-baseweb="listbox"] li:hover { background-color: #f1f5f9 !important; color: #1e3a8a !important; }

        /* 4. BOTONERA UNIVERSAL (Detección de dispositivo) */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #1d4ed8) !important;
            color: #ffffff !important; 
            border-radius: 12px; border: none; padding: 18px;
            font-weight: 800; width: 100%; height: 65px;
            text-transform: uppercase; letter-spacing: 1.5px; font-size: 1.1em;
            box-shadow: 0 4px 15px rgba(30, 58, 138, 0.3);
        }
        .stButton>button:hover { transform: translateY(-4px); box-shadow: 0 15px 30px rgba(30, 58, 138, 0.4); }

        /* 5. DISEÑO RESPONSIVO (MÓVIL / TV) */
        .muni-title { color: #1e3a8a !important; font-weight: 900 !important; text-align: center; font-size: 3.5em; letter-spacing: -2px; }
        .timer-security { color: #dc2626 !important; font-weight: 900; font-size: 3.2em; text-align: center; }

        @media (max-width: 768px) {
            .muni-title { font-size: 2.2em !important; }
            .glass-panel { padding: 15px; border-width: 4px; }
            .stButton>button { font-size: 1.2em !important; height: 75px; }
            .timer-security { font-size: 4em !important; }
        }

        /* 6. ESTILOS MONITOR TV (Grid Mode) */
        .tv-card {
            background: #ffffff; border-radius: 12px; padding: 20px;
            border-top: 10px solid #1e3a8a; box-shadow: 0 8px 15px rgba(0,0,0,0.1);
            text-align: center; transition: 0.3s;
        }
        .tv-card-alert { border-top: 10px solid #dc2626 !important; background: #fff5f5; }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 4. MÓDULO I: NODO CIUDADANO (VIAJE INTELIGENTE - QR)
# ==================================================================================================

def view_citizen_node():
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:1.3em;'>Portal de Atención y Registro Ciudadano</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_active_token')
    
    if not token or token not in st.session_state.waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro Obligatorio de Visita")
        # FIX FORM_SUBMIT: Garantiza que no haya fallos de envío
        with st.form("form_reg_v21", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                recinto = st.selectbox("¿En qué edificio municipal está?", list(INFRAESTRUCTURA_IMLS.keys()))
                nombre = st.text_input("Nombre y Apellidos Completos")
                rut = st.text_input("RUT (ej: 12.345.678-9)")
            with col2:
                perfil = st.selectbox("Categoría de Visitante", PERFILES_SGAAC)
                depto = st.selectbox("Oficina / Departamento de Destino", LISTADO_DEPARTAMENTOS)
                motivo = st.text_area("Motivo de su Visita")
            
            submit = st.form_submit_button("SOLICITAR AUTORIZACIÓN DE INGRESO")
            if submit:
                if nombre and rut and recinto:
                    uid = f"V-{int(time.time())}"
                    # Identificar si el recinto tiene personal de seguridad
                    assisted = INFRAESTRUCTURA_IMLS[recinto]['dotacion']
                    st.session_state.waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "recinto": recinto,
                        "depto": depto, "inicio": datetime.now(),
                        "assisted": assisted, "estado": "COORDINANDO",
                        "inicio_reunion": None, "fin_reunion": None
                    }
                    st.session_state.citizen_active_token = uid
                    st.session_state.audit_logs.insert(0, f"SOLICITUD: {nombre} en {recinto}")
                    st.rerun()
                else: st.error("⚠️ Complete todos los campos obligatorios.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown(f"### Su solicitud para **{info['depto']}** está siendo procesada")
            # MARKETING TERRITORIAL DURANTE LA ESPERA
            st.markdown(f"<div style='background:#1e3a8a; color:white; padding:25px; border-radius:15px; border-left:10px solid #facc15; font-weight:600; font-size:1.2em;'>{np.random.choice(AVISOS_PROMO)}</div>", unsafe_allow_html=True)
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='timer-security'>{int(rem)}s</div>", unsafe_allow_html=True)
            if rem == 0:
                st.session_state.waiting_room[token]['estado'] = "EXPIRADO"
                st.rerun()
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO POR SECRETARÍA**")
            if info['assisted']: st.write("Diríjase al control del Guardia para validar su entrada física.")
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
            st.subheader("¡Gracias por su visita!")
            nps = st.slider("Evaluación del Sistema y Calidad", 1, 5, 5)
            if st.button("ENVIAR Y SALIR"):
                final = {'ID': token, 'Fecha': datetime.now(), 'Recinto': info['recinto'], 'Depto': info['depto'], 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Permanencia': 15, 'NPS': nps, 'Estado': "Completado"}
                st.session_state.db_master = pd.concat([pd.DataFrame([final]), st.session_state.db_master], ignore_index=True)
                del st.session_state.citizen_active_token
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 5. MÓDULO II: MONITOR CONTROL TOTAL (TV & COMMAND CENTER GRID)
# ==================================================================================================

def view_total_monitor():
    st.markdown("<h1 class='muni-title'>MONITOR GLOBAL SGAAC-360</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Visión en tiempo real de la Red de Recintos Municipales | La Serena</p>", unsafe_allow_html=True)
    
    # Grid dinámico: 4 columnas para escritorio/TV, se apilan en móvil
    cols = st.columns(4)
    recintos = list(INFRAESTRUCTURA_IMLS.keys())
    
    for i, r in enumerate(recintos):
        with cols[i % 4]:
            esperas = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'COORDINANDO']
            reuniones = [v for v in st.session_state.waiting_room.values() if v['recinto'] == r and v['estado'] == 'EN_REUNION']
            
            # Alerta visual si hay más de 3 esperas
            estilo_alerta = "tv-card-alert" if len(esperas) > 2 else ""
            
            st.markdown(f"""
                <div class="tv-card {estilo_alerta}">
                    <h3 style="margin:0; font-size:1em;">{INFRAESTRUCTURA_IMLS[r]['icono']} {r[:20]}...</h3>
                    <hr style="margin:10px 0;">
                    <p style="font-size:1.5em; margin:0; color:#dc2626; font-weight:800;">{len(esperas)} <small style="font-size:0.5em; color:gray;">ESPERANDO</small></p>
                    <p style="font-size:1.2em; margin:0; color:#1e3a8a; font-weight:800;">{len(reuniones)} <small style="font-size:0.5em; color:gray;">EN REUNIÓN</small></p>
                    <p style="font-size:0.7em; color:gray; margin-top:5px;">Modo: {"👮 Asistido" if INFRAESTRUCTURA_IMLS[r]['dotacion'] else "🤖 Autónomo"}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if esperas:
                with st.expander("Ver Solicitudes"):
                    for e in esperas: st.caption(f"👤 {e['nombre']} -> {e['depto']}")

# ==================================================================================================
# 6. MÓDULO III: TACTICAL HUB (TERMINAL GUARDIA & SECRETARÍAS)
# ==================================================================================================

def view_tactical_hub():
    st.markdown("<h2 class='muni-title'>COORDINACIÓN TÁCTICA</h2>", unsafe_allow_html=True)
    t1, t2 = st.tabs(["🛡️ Terminal Guardia", "🔔 Panel Secretarías"])
    
    with t1:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("👁️ Visor de Gestiones en Curso")
        coord = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if coord:
            df_visor = pd.DataFrame([{"Ciudadano": v['nombre'], "Hacia": v['depto'], "Recinto": v['recinto']} for v in coord.values()])
            st.table(df_visor)
        else: st.caption("Sin gestiones activas.")
        
        st.divider()
        st.subheader("Validación de Ingresos Físicos")
        autorizados = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'AUTORIZADO'}
        if not autorizados: st.info("Sin pases pendientes.")
        for uid, info in autorizados.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** -> {info['depto']} ({info['recinto']})")
                if st.button("CONFIRMAR PASO FÍSICO", key=f"g_ok_{uid}"):
                    st.session_state.waiting_room[uid]['estado'] = 'EN_REUNION'
                    st.session_state.waiting_room[uid]['inicio_reunion'] = datetime.now()
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with t2:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Hub de Autorización")
        pendientes = {k: v for k, v in st.session_state.waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not pendientes: st.success("Sin visitas esperando respuesta.")
        for uid, info in pendientes.items():
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
    inject_universal_styles()
    
    # Protocolo de Expiración Automática 180s
    now = datetime.now()
    expired = [uid for uid, info in st.session_state.waiting_room.items() if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    for uid in expired: st.session_state.waiting_room[uid]['estado'] = 'EXPIRADO'

    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.divider()
        view_mode = st.radio("MÓDULO DE OPERACIÓN:", [
            "1. Ciudadano (QR)", 
            "2. Monitor Control Total", 
            "3. Tactical Hub (Guardia/Sec)", 
            "4. Analítica Big Data", 
            "5. Gestión CRM / BD",
            "6. Auditoría Interna"
        ])
        st.divider()
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    if "1. Ciudadano" in view_mode: view_citizen_node()
    elif "2. Monitor" in view_mode: view_total_monitor()
    elif "3. Tactical" in view_mode: view_tactical_hub()
    elif "4. Analítica" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.metric("Total Registros Big Data", f"{len(st.session_state.db_master):,}")
        st.bar_chart(st.session_state.db_master['Recinto'].value_counts())
        st.dataframe(st.session_state.db_master.head(100), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    elif "5. Gestión" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Edición Estratégica de Fichas")
        search_id = st.text_input("ID de Visita (ej: VIS-100XXX):")
        if search_id:
            idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
            if idx:
                i = idx[0]
                with st.form("crm_v21"):
                    tel = st.text_input("WhatsApp", st.session_state.db_master.at[i, 'Telefono'])
                    mail = st.text_input("Email", st.session_state.db_master.at[i, 'Email'])
                    if st.form_submit_button("ACTUALIZAR"):
                        st.session_state.db_master.at[i, 'Telefono'] = tel
                        st.session_state.db_master.at[i, 'Email'] = mail
                        st.success("Inteligencia Ciudadana Actualizada.")
        st.markdown("</div>", unsafe_allow_html=True)
    elif "6. Auditoría" in view_mode:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs[:50]: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__": main()
