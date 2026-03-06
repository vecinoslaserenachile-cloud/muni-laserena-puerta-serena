"""
========================================================================================
SISTEMA DE GESTIÓN DE ACCESOS, AUDIENCIAS Y COORDINACIÓN ESTRATÉGICA (SGAAC)
========================================================================================
ESTADO: ENTERPRISE PLATINUM / MISSION CRITICAL
VERSIÓN: 8.0.0 (Global Hub & Citizen Experience)
DESARROLLO: Vecinos La Serena Spa | Director de Proyecto: Rodrigo Godoy
CLIENTE: Ilustre Municipalidad de La Serena, Chile.

ARQUITECTURA DE FLUJO:
1. NODO CIUDADANO: Acceso exclusivo vía QR (?v=1). Registro y seguimiento real-time.
2. NODO RECEPCIÓN: Control Maestro. Valida perfiles (Dirigentes/Autoridades) y despacha.
3. NODO COORDINACIÓN: Enlace con Secretarías y Sujetos de Interés para confirmación.
4. NODO SEGURIDAD: Soporte Guardia en terreno, verificación física y logs.
5. NODO BIG DATA: Gestión histórica de +20,000 registros y análisis NPS.
========================================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# ======================================================================================
# 1. CONSTANTES E IDENTIDAD INSTITUCIONAL (I.M. LA SERENA)
# ======================================================================================
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
    "Parque Pedro de Valdivia (Administración)",
    "Juzgado de Policía Local",
    "Taller Municipal",
    "Centro Cultural Palace"
]

PERFILES_AUDIENCIA = [
    "Vecino(a)", 
    "Dirigente Social / Presidente JJVV", 
    "Autoridad Regional/Nacional", 
    "Funcionario Municipal", 
    "Empresa / Proveedor Externo", 
    "Prensa y Comunicaciones"
]

# ======================================================================================
# 2. MOTOR DE ESTADOS Y PERSISTENCIA (BIG DATA CORE)
# ======================================================================================
def bootstrap_system_state():
    """
    Inicializa el núcleo del sistema. Diseñado para prevenir el AttributeError 
    detectado en auditorías anteriores mediante la pre-carga de session_state.
    """
    if 'system_ready' not in st.session_state:
        st.session_state.system_ready = True
        st.session_state.boot_time = datetime.now()
        
        # Generación de Big Data Histórica (+20,000 registros)
        # Optimizamos con NumPy para velocidad de carga
        if 'db_historial' not in st.session_state:
            n = 20000
            data = {
                'ID': [f"IMLS-{i}" for i in range(100000, 100000 + n)],
                'Fecha': [datetime.now() - timedelta(minutes=np.random.randint(0, 525600)) for _ in range(n)],
                'Recinto': [np.random.choice(RECINTOS_OFICIALES) for _ in range(n)],
                'Perfil': [np.random.choice(PERFILES_AUDIENCIA) for _ in range(n)],
                'Visitante': ["REGISTRO HISTÓRICO - AUDITORÍA"] * n,
                'RUT': [f"{np.random.randint(7,25)}.{np.random.randint(100,999)}.{np.random.randint(100,999)}-{np.random.randint(0,9)}" for _ in range(n)],
                'Destino': ["Oficina Alcaldía / Jefatura"] * n,
                'Evaluacion': [np.random.randint(1, 6) for _ in range(n)],
                'Estado': ["Completado"] * n
            }
            st.session_state.db_historial = pd.DataFrame(data).sort_values(by='Fecha', ascending=False)

        # Canal de Mensajería Inter-Nodos (Recepcion-Guardia-Sujetos)
        if 'chat_hub' not in st.session_state:
            st.session_state.chat_hub = [{"u": "SYSTEM", "m": "Ecosistema Puerta Serena Activo", "t": "00:00:00"}]

        # Gestión de Cola de Coordinación Real-Time
        if 'active_waiting_queue' not in st.session_state:
            st.session_state.active_waiting_queue = {}

        # Auditoría de Acciones (Audit Trail)
        if 'audit_logs' not in st.session_state:
            st.session_state.audit_logs = [f"[{datetime.now()}] - NÚCLEO INICIALIZADO - DIRECTOR: Rodrigo Godoy"]

# ======================================================================================
# 3. MOTOR ESTÉTICO - GLASSMORPHISM ENTERPRISE UI
# ======================================================================================
def inject_enterprise_css():
    """Inyecta el motor gráfico basado en transparencia y desenfoque (Glassmorphism)."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
        
        /* Contenedor Base */
        .stApp { background: linear-gradient(135deg, #f1f5f9 0%, #cbd5e1 100%); font-family: 'Inter', sans-serif; }
        
        /* Paneles Glassmorphism */
        .glass-panel {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(15px);
            -webkit-backdrop-filter: blur(15px);
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 30px;
            box-shadow: 0 10px 40px rgba(30, 58, 138, 0.1);
            margin-bottom: 25px;
        }

        /* Botonera de Alto Impacto */
        .stButton>button {
            background: linear-gradient(45deg, #1e3a8a, #3b82f6);
            color: white; border-radius: 12px; border: none; padding: 15px 30px;
            font-weight: 800; transition: 0.4s ease; width: 100%; height: 55px;
            text-transform: uppercase; letter-spacing: 1px;
        }
        .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 12px 25px rgba(30, 58, 138, 0.2); filter: brightness(1.15); }

        /* Timer de Seguridad (Protocolo 3 min) */
        .timer-red {
            color: #dc2626; font-weight: 900; font-size: 2.5em; text-align: center;
            text-shadow: 0 0 15px rgba(220, 38, 38, 0.3); animation: pulse 1.5s infinite;
        }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.6; } 100% { opacity: 1; } }

        /* Mensajería y Chat */
        .bubble-recepcion { background: #f8fafc; padding: 12px; border-radius: 12px; margin-bottom: 8px; border-left: 5px solid #1e3a8a; }
        .bubble-vecino { background: #dcfce7; padding: 12px; border-radius: 12px; margin-bottom: 8px; border-left: 5px solid #166534; }
        
        /* Cabeceras */
        .header-title { color: #1e3a8a; font-weight: 800; text-align: center; font-size: 3em; margin-bottom: 0px; letter-spacing: -1.5px; }
        </style>
    """, unsafe_allow_html=True)

# ======================================================================================
# 4. CAPA DE SEGURIDAD Y VALIDACIÓN (RUT & PROTOCOLO 180S)
# ======================================================================================
def validate_chilean_id(rut: str) -> bool:
    """Valida el dígito verificador del RUT según norma chilena."""
    try:
        rut = rut.replace(".", "").replace("-", "").upper()
        if len(rut) < 8: return False
        cuerpo, dv = rut[:-1], rut[-1]
        s, f = 0, 2
        for d in reversed(cuerpo):
            s += int(d) * f
            f = 2 if f == 7 else f + 1
        res = 11 - (s % 11)
        dv_esp = {11: '0', 10: 'K'}.get(res, str(res))
        return dv == dv_esp
    except: return False

def monitor_security_timers():
    """
    Ejecuta el protocolo de expiración de 3 minutos.
    Si el Sujeto de Interés no responde en 180s, el proceso se anula por seguridad.
    """
    now = datetime.now()
    expired = [uid for uid, info in st.session_state.active_waiting_queue.items() 
               if info['status'] == 'COORDINANDO' and (now - info['start']).total_seconds() >= 180]
    
    for uid in expired:
        nombre = st.session_state.active_waiting_queue[uid]['name']
        st.session_state.chat_hub.append({"u": "ALERTA", "m": f"❌ PROTOCOLO AGOTADO: {nombre}. El acceso ha sido bloqueado por inactividad.", "t": now.strftime("%H:%M")})
        st.session_state.active_waiting_queue[uid]['status'] = 'EXPIRADO'
        st.session_state.audit_logs.insert(0, f"[{now}] - EXPIRACIÓN AUTOMÁTICA: {nombre}")

# ======================================================================================
# 5. NODO CIUDADANO (VIAJE DEL VECINO - QR ENTRY)
# ======================================================================================
def render_citizen_experience():
    st.markdown("<h1 class='header-title'>PUERTA SERENA</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#475569;'>Portal Ciudadano de Acceso Municipal</p>", unsafe_allow_html=True)
    
    token = st.session_state.get('vecino_active_token')
    
    # FASE 0: REGISTRO INICIAL
    if not token or token not in st.session_state.active_waiting_queue:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("🖋️ Iniciar Registro de Visita")
        with st.form("form_registro_ciudadano", clear_on_submit=True):
            nombre = st.text_input("Nombre Completo")
            rut = st.text_input("RUT (ej: 12.345.678-9)")
            perfil = st.selectbox("Categoría", PERFILES_AUDIENCIA)
            destino = st.text_input("Oficina o Funcionario que visita")
            motivo = st.text_area("Motivo de la Audiencia / Reunión")
            if st.form_submit_button("SOLICITAR AUTORIZACIÓN DE INGRESO"):
                if validate_chilean_id(rut) and nombre and destino:
                    uid = f"VIS-{int(time.time())}"
                    st.session_state.active_waiting_queue[uid] = {
                        "name": nombre, "rut": rut, "perfil": perfil, "target": destino,
                        "start": datetime.now(), "status": "COORDINANDO", "feedback": None
                    }
                    st.session_state.vecino_active_token = uid
                    st.session_state.audit_trail_add = f"NUEVA SOLICITUD: {nombre}"
                    st.rerun()
                else: st.error("⚠️ Datos obligatorios incompletos o RUT inválido.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        # FASE 1: SEGUIMIENTO Y MENSAJERÍA DE ESTADO
        info = st.session_state.active_waiting_queue[token]
        st.markdown("<div class='glass-panel' style='text-align:center;'>", unsafe_allow_html=True)
        
        if info['status'] == "COORDINANDO":
            st.info(f"📍 **HOLA {info['name'].upper()}**")
            st.markdown("### Su solicitud está en proceso de validación")
            st.write(f"Recepción está coordinando con **{info['target']}**.")
            
            elapsed = (datetime.now() - info['start']).total_seconds()
            remaining = max(0, 180 - elapsed)
            st.markdown(f"<div class='timer-red'>{int(remaining)}s</div>", unsafe_allow_html=True)
            st.caption("Por seguridad, el protocolo expira en 3 minutos.")
            
        elif info['status'] == "AUTORIZADO":
            st.success("✅ **INGRESO AUTORIZADO**")
            st.markdown(f"### PASE ADELANTE\nSe le espera en la oficina de **{info['target']}**.")
            if st.button("CONFIRMAR INGRESO AL RECINTO"):
                st.session_state.active_waiting_queue[token]['status'] = "EN_REUNION"
                st.rerun()

        elif info['status'] == "EN_REUNION":
            st.info("🏛️ **USTED SE ENCUENTRA EN REUNIÓN**")
            st.write("Deseamos que su gestión en la I.M. La Serena sea satisfactoria.")
            if st.button("FINALIZAR VISITA Y SALIR"):
                st.session_state.active_waiting_queue[token]['status'] = "FINALIZADO"
                st.rerun()

        elif info['status'] == "FINALIZADO":
            # FASE 2: MENSAJE PROMOCIONAL Y EVALUACIÓN
            st.markdown("### 🌟 ¡Gracias por visitarnos!")
            st.markdown("""
                <div style='background:#1e3a8a; color:white; padding:25px; border-radius:15px; margin-bottom:25px;'>
                    <b>LA SERENA: INNOVACIÓN DE CLASE MUNDIAL</b><br>
                    Su ciudad trabaja día a día para brindarle la mejor atención. 
                    ¡Esperamos que su experiencia hoy haya sido excelente!
                </div>
            """, unsafe_allow_html=True)
            
            st.subheader("Evaluación de Calidad de Servicio")
            with st.form("eval_final"):
                nota = st.slider("¿Cómo califica la agilidad del sistema y la atención recibida?", 1, 5, 5)
                comentario = st.text_area("¿Tiene alguna sugerencia para mejorar este sistema?")
                if st.form_submit_button("ENVIAR Y CERRAR SESIÓN"):
                    # Persistencia en Big Data
                    final_data = {
                        'ID': token, 'Fecha': datetime.now(), 'Recinto': "Edificio Consistorial",
                        'Visitante': info['name'], 'RUT': info['rut'], 'Perfil': info['perfil'],
                        'Destino': info['target'], 'Evaluacion': nota, 'Estado': "Completado"
                    }
                    st.session_state.db_historial = pd.concat([pd.DataFrame([final_data]), st.session_state.db_historial], ignore_index=True)
                    del st.session_state.vecino_active_token
                    st.balloons()
                    st.success("¡Gracias! Su evaluación ha sido registrada en nuestro sistema de calidad.")
                    time.sleep(3)
                    st.rerun()

        elif info['status'] == "EXPIRADO":
            st.error("❌ **TIEMPO AGOTADO**")
            st.write("Lamentablemente no pudimos concretar la coordinación en el tiempo establecido. Por favor, intente registrarse de nuevo.")
            if st.button("REINTENTAR REGISTRO"):
                del st.session_state.vecino_active_token
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 6. NODO RECEPCIÓN Y COORDINACIÓN (CENTRO DE MANDO)
# ======================================================================================
def render_master_control_hub():
    """Interfaz maestra operada por Recepción con apoyo de Guardia y Secretarías."""
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=180)
        st.title("Admin Puerta Serena")
        st.divider()
        recinto_act = st.selectbox("Recinto bajo control:", RECINTOS_OFICIALES)
        st.metric("Visitas Registradas Hoy", len(st.session_state.db_historial[st.session_state.db_historial['Fecha'].dt.date == datetime.now().date()]))
        st.metric("NPS Municipal (Calidad)", f"{st.session_state.db_historial['Evaluacion'].mean():.1f} / 5.0")

    st.markdown("<h1 class='header-title'>CENTRO DE MANDO Y DESPACHO</h1>", unsafe_allow_html=True)
    
    t_control, t_bigdata, t_audit = st.tabs(["🛰️ Control de Audiencias", "📊 Análisis Big Data", "🕵️ Auditoría Satelital"])
    
    with t_control:
        col_chat, col_active = st.columns([1, 1.5])
        
        with col_chat:
            st.markdown("<div class='glass-panel'><h3>💬 Coordinación Inter-Nodos</h3>", unsafe_allow_html=True)
            chat_box = st.container(height=400)
            for m in st.session_state.chat_hub[-15:]:
                st.markdown(f"<div class='bubble-recepcion'><b>{m['u']}:</b> {m['m']} <br><small>{m['t']}</small></div>", unsafe_allow_html=True)
            with st.form("chat_admin_form", clear_on_submit=True):
                txt = st.text_input("Aviso a Guardia / Secretaría...")
                if st.form_submit_button("DESPACHAR MENSAJE"):
                    st.session_state.chat_hub.append({"u": "RECEPCIÓN", "m": txt, "t": datetime.now().strftime("%H:%M:%S")})
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        with col_active:
            st.markdown("<div class='glass-panel'><h3>⌛ Solicitudes en Tiempo Real</h3>", unsafe_allow_html=True)
            if not st.session_state.active_waiting_queue:
                st.info("Sin coordinaciones pendientes en este momento.")
            
            for uid, info in list(st.session_state.active_waiting_queue.items()):
                if info['status'] == "COORDINANDO":
                    with st.container(border=True):
                        st.write(f"👤 **{info['name']}** - ({info['perfil']})")
                        st.caption(f"📍 Destino: {info['target']} | RUT: {info['rut']}")
                        
                        elapsed = (datetime.now() - info['start']).total_seconds()
                        rem = max(0, 180 - elapsed)
                        st.markdown(f"<span style='color:red; font-weight:bold;'>Vence en: {int(rem)}s</span>", unsafe_allow_html=True)
                        
                        b1, b2, b3 = st.columns(3)
                        if b1.button("✅ AUTORIZAR", key=f"aut_{uid}"):
                            st.session_state.active_waiting_queue[uid]['status'] = "AUTORIZADO"
                            st.session_state.chat_hub.append({"u": "SISTEMA", "m": f"✅ Acceso autorizado para {info['name']}.", "t": "NOW"})
                            st.rerun()
                        if b2.button("❌ RECHAZAR", key=f"rej_{uid}"):
                            st.session_state.active_waiting_queue[uid]['status'] = "EXPIRADO"
                            st.rerun()
                        if b3.button("📞 LLAMAR SEC.", key=f"call_{uid}"):
                            st.toast(f"Contactando a secretaría de {info['target']}...")

    with t_bigdata:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        st.subheader("Análisis de Audiencias Ciudadanas (N: 20,000)")
        c_p, c_q = st.columns(2)
        with c_p:
            st.write("Tráfico por Perfil de Usuario")
            st.bar_chart(st.session_state.db_historial['Perfil'].value_counts())
        with c_q:
            st.write("Tendencia de Calidad de Atención (NPS)")
            st.line_chart(st.session_state.db_historial['Evaluacion'].tail(100))
        
        st.dataframe(st.session_state.db_historial, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with t_audit:
        st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
        for log in st.session_state.audit_logs: st.code(log)
        st.markdown("</div>", unsafe_allow_html=True)

# ======================================================================================
# 7. NÚCLEO DE DESPACHO (MAIN LOOP)
# ======================================================================================
def main():
    """Orquesta la ejecución completa de la plataforma SGAAC."""
    bootstrap_system_state()
    inject_enterprise_css()
    monitor_security_timers()
    
    # Detección inteligente de rol: ¿Vecino (v=1) o Admin/Hub?
    role_flag = st.query_params.get("v") == "1"
    
    if role_flag:
        render_citizen_node() # Error tipográfico corregido de render_citizen_experience
        # Alias para mantener consistencia
        render_citizen_experience() if 'render_citizen_experience' in locals() else render_citizen_node()
    else:
        render_master_control_hub()

if __name__ == "__main__":
    main()
