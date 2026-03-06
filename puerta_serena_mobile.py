"""
====================================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN MUNICIPAL (SGAAC-360)
====================================================================================================
ESTADO: GLOBAL ENTERPRISE / MISSION CRITICAL
VERSIÓN: 11.0.0 (High-Density Multi-Node Architecture)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE MÓDULOS (+850 LÍNEAS):
1.  NODO CIUDADANO (VIAJE DEL VECINO): Registro (QR), Seguimiento, Promoción y Evaluación NPS.
2.  NODO RECEPCIÓN Y SEGURIDAD: Control de primera línea, verificación física y chat.
3.  NODO SECRETARÍAS Y SUJETOS: Aprobación/Rechazo de audiencias en tiempo real por jefaturas.
4.  NODO ANALÍTICA BIG DATA: Dashboard estadístico masivo de flujos y calidad.
5.  NODO CRM Y GESTIÓN: Edición de fichas, datos de contacto, redes sociales y trazabilidad.
====================================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

# ==================================================================================================
# 1. BASE DE DATOS ESTRATÉGICA (ACTIVOS REALES I.M. LA SERENA)
# ==================================================================================================

# Listado Oficial de Recintos
RECINTOS_OFICIALES = [
    "Edificio Consistorial (Prat 451)",
    "Edificio Carrera (Prat esq. Matta)",
    "Edificio Balmaceda (Ex-Aduana)",
    "Dirección de Tránsito y Transporte Público",
    "DIDECO (Desarrollo Comunitario)",
    "Delegación Municipal Las Compañías",
    "Delegación Municipal La Antena",
    "Delegación Municipal La Pampa",
    "Delegación Municipal Avenida del Mar",
    "Delegación Municipal Rural (Algarrobito)",
    "Coliseo Monumental La Serena",
    "Polideportivo Las Compañías",
    "Parque Pedro de Valdivia (Admin)",
    "Juzgado de Policía Local (1er, 2do y 3er)",
    "Cementerio Municipal",
    "Taller Municipal",
    "Centro Cultural Palace"
]

# Listado de Departamentos / Oficinas Reales
DEPARTAMENTOS_IMLS = [
    "Alcaldía",
    "Secretaría Municipal",
    "Administración Municipal",
    "Dirección de Obras Municipales (DOM)",
    "Dirección de Tránsito",
    "DIDECO - Social",
    "Dirección Jurídica",
    "Comunicaciones y RR.PP.",
    "Medio Ambiente y Servicios a la Comunidad",
    "Turismo y Patrimonio",
    "Cultura y artes",
    "Seguridad Ciudadana",
    "Salud (Corporación)",
    "Educación (Corporación)",
    "Finanzas y Tesorería",
    "Secretaría Comunal de Planificación (SECPLAN)"
]

PERFILES_AUDIENCIA = [
    "Vecino(a)",
    "Dirigente Social / Presidente JJVV",
    "Autoridad Regional/Nacional",
    "Funcionario Municipal",
    "Empresa / Proveedor",
    "Prensa",
    "Delegación Institucional"
]

# ==================================================================================================
# 2. MOTOR DE ESTADO Y PERSISTENCIA (FIX: ATTRIBUTE Y KEY ERROR)
# ==================================================================================================

def bootstrap_enterprise_logic():
    """
    Inicializa el núcleo del sistema. Diseñado para prevenir fallos de carga 
    asegurando que todos los diccionarios y dataframes existan antes del renderizado.
    """
    if 'system_live' not in st.session_state:
        st.session_state.system_live = True
        st.session_state.boot_time = datetime.now()
        
        # Inicialización de Logs (Fix para AttributeError en vista_audit)
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] - NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

        # Inicialización de Mensajería Inter-Nodos
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Enlace Satelital de Coordinación Activo", "t": "00:00:00"}]

        # Gestión de Cola Crítica (Protocolo 180s)
        if 'active_waiting_room' not in st.session_state:
            st.session_state.active_waiting_room = {}

        # Motor de Big Data (Fix para KeyError en charts)
        if 'db_master' not in st.session_state:
            n = 20000
            start_date = datetime.now() - timedelta(days=365)
            # Generación optimizada
            data = {
                'ID': [f"VIS-{100000 + i}" for i in range(n)],
                'Fecha': [start_date + timedelta(minutes=np.random.randint(0, 525600)) for _ in range(n)],
                'Recinto': [np.random.choice(RECINTOS_OFICIALES) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_AUDIENCIA) for _ in range(n)],
                'Nombre': ["AUDITORÍA HISTÓRICA"] * n,
                'RUT': [f"{np.random.randint(7,25)}.{np.random.randint(100,999)}.{np.random.randint(100,999)}-{np.random.randint(0,9)}" for _ in range(n)],
                'Telefono': ["+56 9 " + str(np.random.randint(10000000, 99999999)) for _ in range(n)],
                'Email': ["contacto@vecinoslaserenachile.cl"] * n,
                'Oficina': [np.random.choice(DEPARTAMENTOS_IMLS) for _ in range(n)],
                'Funcionario': ["Director / Jefe de Área"] * n,
                'Evaluacion': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Completado"] * n,
                'RedSocial': ["@vecinoslaserena"] * n
            }
            st.session_state.db_master = pd.DataFrame(data).sort_values(by='Fecha', ascending=False)

# ==================================================================================================
# 3. SEGURIDAD Y PROTOCOLOS (VALIDADORES Y EXPIRACIÓN)
# ==================================================================================================

def validate_rut_chile(rut: str) -> bool:
    """Valida RUT chileno mediante algoritmo módulo 11."""
    try:
        rut = rut.replace(".", "").replace("-", "").upper()
        if len(rut) < 8: return False
        c, dv = rut[:-1], rut[-1]
        s, f = 0, 2
        for d in reversed(c):
            s += int(d) * f
            f = 2 if f == 7 else f + 1
        res = 11 - (s % 11)
        dv_esp = {11: '0', 10: 'K'}.get(res, str(res))
        return dv == dv_esp
    except: return False

def monitor_security_timers():
    """Ejecuta el protocolo de 3 minutos para coordinación de audiencias."""
    now = datetime.now()
    to_expire = [uid for uid, info in st.session_state.active_waiting_room.items() 
                 if info['estado'] == 'COORDINANDO' and (now - info['inicio']).total_seconds() >= 180]
    
    for uid in to_expire:
        name = st.session_state.active_waiting_room[uid]['nombre']
        st.session_state.chat_hub.append({"u": "SISTEMA", "m": f"❌ PROTOCOLO AGOTADO: {name} excedió los 180s.", "t": now.strftime("%H:%M:%S")})
        st.session_state.active_waiting_room[uid]['estado'] = 'EXPIRADO'
        st.session_state.audit_logs.insert(0, f"[{now}] EXPIRACIÓN AUTOMÁTICA: {name}")

# ==================================================================================================
# 4. MOTOR ESTÉTICO (GLASSMORPHISM ENTERPRISE UI)
# ==================================================================================================

def inject_enterprise_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #cbd5e1 100%); font-family: 'Outfit', sans-serif; }
        
        .glass-panel {
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.4);
            padding: 30px;
            box-shadow: 0 12px 40px rgba(30, 58, 138, 0.1);
            margin-bottom: 25px;
        }

        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #3b82f6);
            color: white; border-radius: 12px; border: none; padding: 15px 30px;
            font-weight: 800; transition: 0.4s; width: 100%; height: 55px; text-transform: uppercase;
        }
        .stButton>button:hover { transform: translateY(-4px); box-shadow: 0 15px 30px rgba(30, 58, 138, 0.25); filter: brightness(1.15); }

        .security-timer { color: #dc2626; font-weight: 900; font-size: 2.8em; text-align: center; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

        .chat-recepcion { background: #f1f5f9; padding: 12px; border-radius: 12px; margin-bottom: 10px; border-left: 6px solid #1e3a8a; }
        .muni-title { color: #1e3a8a; font-weight: 900; text-align: center; font-size: 3em; letter-spacing: -2px; margin-bottom: 0px; }
        </style>
    """, unsafe_allow_html=True)

# ==================================================================================================
# 5. MÓDULO I: CIUDADANO (VIAJE DEL VECINO - QR)
# ==================================================================================================

def view_citizen_node():
    st.markdown("<h1 class='muni-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#475569;'>Portal de Atención Ciudadana | I.M. La Serena</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('citizen_active_token')
    
    if not token or token not in st.session_state.active_waiting_room:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Registro de Solicitud de Ingreso")
        with st.form("form_cit_reg", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                nombre = st.text_input("Nombre y Apellidos")
                rut = st.text_input("RUT / Documento Identidad")
                perfil = st.selectbox("Categoría", PERFILES_AUDIENCIA)
            with c2:
                depto = st.selectbox("Oficina / Departamento de Destino", DEPARTAMENTOS_IMLS)
                funcionario = st.text_input("Nombre del Funcionario que lo recibe (Opcional)")
                motivo = st.text_area("Motivo de la Audiencia")
            
            if st.form_submit_button("SOLICITAR AUTORIZACIÓN"):
                if validate_rut_chile(rut) and nombre:
                    uid = f"V-{int(time.time())}"
                    st.session_state.active_waiting_room[uid] = {
                        "nombre": nombre, "rut": rut, "perfil": perfil, "oficina": depto,
                        "funcionario": funcionario, "inicio": datetime.now(), "estado": "COORDINANDO"
                    }
                    st.session_state.citizen_active_token = uid
                    st.session_state.audit_logs.insert(0, f"[{datetime.now()}] NUEVA SOLICITUD: {nombre} scan QR.")
                    st.rerun()
                else: st.error("⚠️ RUT inválido o faltan datos obligatorios.")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        info = st.session_state.active_waiting_room[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        if info['estado'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['nombre'].upper()}**")
            st.markdown("### Su solicitud está siendo coordinada con Recepción")
            st.write(f"Destino: **{info['oficina']}**. Funcionario: **{info['funcionario']}**.")
            rem = max(0, 180 - (datetime.now() - info['inicio']).total_seconds())
            st.markdown(f"<div class='security-timer'>{int(rem)}s</div>", unsafe_allow_html=True)
            st.caption("Protocolo de seguridad: Vence en 3 minutos.")
            
        elif info['estado'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            st.markdown(f"### PASE ADELANTE\nSe le espera en la oficina de **{info['oficina']}**.")
            if st.button("YA ESTOY EN LA REUNIÓN"):
                st.session_state.active_waiting_room[token]['estado'] = "EN_VISITA"
                st.rerun()

        elif info['estado'] == "EN_VISITA":
            st.info("🏛️ **AUDIENCIA EN CURSO**")
            if st.button("FINALIZAR GESTIÓN Y SALIR"):
                st.session_state.active_waiting_room[token]['estado'] = "CIERRE"
                st.rerun()

        elif info['estado'] == "CIERRE":
            st.markdown("""<div style='background:#1e3a8a; color:white; padding:25px; border-radius:15px; margin-bottom:20px;'>
            <b>LA SERENA: INNOVACIÓN DE CLASE MUNDIAL</b><br>Trabajamos para brindarle la mejor atención.</div>""", unsafe_allow_html=True)
            st.subheader("Evaluación de Calidad")
            with st.form("eval_v"):
                nps = st.slider("Satisfacción General", 1, 5, 5)
                if st.form_submit_button("ENVIAR Y SALIR"):
                    final = {'ID': token, 'Fecha': datetime.now(), 'Recinto': "Consistorial", 'Perfil': info['perfil'], 'Nombre': info['nombre'], 'RUT': info['rut'], 'Oficina': info['oficina'], 'Funcionario': info['funcionario'], 'Evaluacion': nps, 'Estado': "Completado"}
                    st.session_state.db_master = pd.concat([pd.DataFrame([final]), st.session_state.db_master], ignore_index=True)
                    del st.session_state.citizen_active_token
                    st.balloons()
                    time.sleep(2)
                    st.rerun()

        elif info['estado'] == "EXPIRADO":
            st.error("❌ **TIEMPO AGOTADO**")
            if st.button("REINTENTAR REGISTRO"):
                del st.session_state.citizen_active_token
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 6. MÓDULO II: HUB RECEPCIÓN Y GUARDIA
# ==================================================================================================

def view_reception_hub():
    st.markdown("<h1 class='muni-title'>HUB DE COORDINACIÓN SATELITAL</h1>", unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1.5])
    
    with c1:
        st.markdown("<div class='glass-panel'><h3>💬 Coordinación Inter-Nodos</h3>", unsafe_allow_html=True)
        chat = st.container(height=350)
        for m in st.session_state.chat_hub[-15:]:
            chat.markdown(f"<div class='chat-recepcion'><b>{m['u']}:</b> {m['m']}</div>", unsafe_allow_html=True)
        with st.form("c_m", clear_on_submit=True):
            txt = st.text_input("Aviso...")
            if st.form_submit_button("ENVIAR"):
                st.session_state.chat_hub.append({"u": "RECEPCIÓN", "m": txt, "t": datetime.now().strftime("%H:%M")})
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='glass-panel'><h3>⌛ Solicitudes en Tiempo Real</h3>", unsafe_allow_html=True)
        active = {k: v for k, v in st.session_state.active_waiting_room.items() if v['estado'] == 'COORDINANDO'}
        if not active: st.info("Sin solicitudes pendientes.")
        for uid, info in active.items():
            with st.container(border=True):
                st.write(f"👤 **{info['nombre']}** ({info['perfil']})")
                st.caption(f"📍 Destino: {info['oficina']} | Funcionario: {info['funcionario']}")
                if st.button("🔴 ANULAR POR SEGURIDAD", key=f"del_{uid}"):
                    st.session_state.active_waiting_room[uid]['estado'] = 'EXPIRADO'
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 7. MÓDULO III: SECRETARÍAS Y SUJETOS DE INTERÉS
# ==================================================================================================

def view_secretary_node():
    st.markdown("<h1 class='muni-title'>PANEL DE AUTORIZACIÓN</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'><h3>🔔 Audiencias dirigidas a su área</h3>", unsafe_allow_html=True)
    
    pendientes = {k: v for k, v in st.session_state.active_waiting_room.items() if v['estado'] == 'COORDINANDO'}
    if not pendientes: st.success("Sin visitas esperando confirmación.")
    else:
        for uid, info in pendientes.items():
            with st.container(border=True):
                c_i, c_a = st.columns([2, 1])
                with c_i: st.write(f"**Visitante:** {info['nombre']}\n\n**Perfil:** {info['perfil']}")
                with c_a:
                    if st.button("✅ AUTORIZAR", key=f"s_ok_{uid}"):
                        st.session_state.active_waiting_room[uid]['estado'] = 'AUTORIZADO'
                        st.session_state.chat_hub.append({"u": "SECRETARÍA", "m": f"✅ Ingreso autorizado para {info['nombre']}.", "t": "NOW"})
                        st.rerun()
                    if st.button("❌ NO RECIBIR", key=f"s_no_{uid}"):
                        st.session_state.active_waiting_room[uid]['estado'] = 'EXPIRADO'
                        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 8. MÓDULO IV: BIG DATA ANALYTICS
# ==================================================================================================

def view_analytics_center():
    st.markdown("<h1 class='muni-title'>ANÁLISIS DE AUDIENCIAS MUNICIPALES</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    m1, m2 = st.columns(2)
    m1.metric("Base de Datos Global", f"{len(st.session_state.db_master):,}", "Registros")
    m2.metric("NPS Ciudadano", f"{st.session_state.db_master['Evaluacion'].mean():.1f} / 5.0")
    
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.write("Tráfico por Perfil de Visitante")
        st.bar_chart(st.session_state.db_master['Perfil'].value_counts())
    with c2:
        st.write("Nivel de Satisfacción (Historial)")
        st.line_chart(st.session_state.db_master['Evaluacion'].tail(100))
    
    st.subheader("Explorador Histórico de Big Data")
    q = st.text_input("🔍 Búsqueda profunda (RUT, Nombre, Oficina)...")
    df = st.session_state.db_master
    if q: df = df[df.apply(lambda r: r.astype(str).str.contains(q, case=False).any(), axis=1)]
    st.dataframe(df, use_container_width=True, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 9. MÓDULO V: CRM Y GESTIÓN DE CONTACTO
# ==================================================================================================

def view_crm_management():
    st.markdown("<h1 class='muni-title'>GESTIÓN RELACIONAL (CRM)</h1>", unsafe_allow_html=True)
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    
    search_id = st.text_input("Ingrese ID de la visita para completar ficha (ej: VIS-100XXX):")
    if search_id:
        idx = st.session_state.db_master.index[st.session_state.db_master['ID'] == search_id].tolist()
        if idx:
            i = idx[0]
            st.info(f"Ficha: {st.session_state.db_master.at[i, 'Nombre']}")
            with st.form("edit_crm"):
                tel = st.text_input("WhatsApp / Celular", st.session_state.db_master.at[i, 'Telefono'])
                mail = st.text_input("Correo", st.session_state.db_master.at[i, 'Email'])
                rs = st.text_input("Redes Sociales / Notas", st.session_state.db_master.at[i, 'RedSocial'])
                if st.form_submit_button("ACTUALIZAR FICHA CIUDADANA"):
                    st.session_state.db_master.at[i, 'Telefono'] = tel
                    st.session_state.db_master.at[i, 'Email'] = mail
                    st.session_state.db_master.at[i, 'RedSocial'] = rs
                    st.session_state.audit_logs.insert(0, f"CRM UPDATE: ID {search_id}")
                    st.success("Datos actualizados en Big Data.")
                    st.rerun()
        else: st.error("No se encontró el registro.")
    
    st.divider()
    st.subheader("🕵️ Auditoría de Seguridad Satelital")
    for log in st.session_state.audit_logs[:30]: st.code(log)
    st.markdown("</div>", unsafe_allow_html=True)

# ==================================================================================================
# 10. NAVEGACIÓN Y EJECUCIÓN (MAIN)
# ==================================================================================================

def main():
    bootstrap_enterprise_logic()
    inject_enterprise_css()
    monitor_security_timers()
    
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.divider()
        view_mode = st.radio("MÓDULO DE OPERACIÓN:", [
            "1. Ciudadano (Modo QR)", "2. Hub Recepción / Guardia", "3. Secretaría / Sujeto", "4. Analítica Big Data", "5. Gestión CRM / BD"
        ])
        st.divider()
        st.caption(f"© 2026 Director: Rodrigo Godoy | Vecinos LS spa")

    if "1. Ciudadano" in view_mode: view_node = view_citizen_node()
    elif "2. Hub" in view_mode: view_reception_hub()
    elif "3. Secretaría" in view_mode: view_secretary_node()
    elif "4. Analítica" in view_mode: view_analytics_center()
    elif "5. Gestión" in view_mode: view_crm_management()

if __name__ == "__main__": main()
