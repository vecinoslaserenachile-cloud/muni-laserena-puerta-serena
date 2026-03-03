import streamlit as st
from datetime import datetime
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore

# ==========================================
# 1. CONFIGURACIÓN VISUAL GENERAL (CON FAVICON)
# ==========================================
st.set_page_config(page_title="Control de Acceso | I.M. La Serena", page_icon="🏛️", layout="wide", initial_sidebar_state="expanded")

# CSS Ajustado para móviles: Fuerza textos oscuros en los inputs y etiquetas
st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    
    /* Forzar color de texto oscuro en etiquetas y campos para evitar el bug del modo oscuro en móviles */
    label, .stTextInput label, .stSelectbox label, .stTextArea label { color: #333333 !important; font-weight: bold !important; }
    input, select, textarea { color: #111111 !important; background-color: #FFFFFF !important; }
    
    .tarjeta-visita {
        background-color: white; padding: 15px; border-radius: 8px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px; border-left: 4px solid #FFD700;
    }
    .nombre-visita { font-weight: bold; font-size: 1.1em; color: #333; margin-bottom: 2px;}
    .depto-visita { color: #555; font-size: 0.9em; }
    .tabla-historico { width: 100%; border-collapse: collapse; background-color: white; box-shadow: 0 2px 4px rgba(0,0,0,0.1); color: #333; }
    .tabla-historico th { background-color: #333; color: white; padding: 10px; text-align: left; }
    .tabla-historico td { padding: 10px; border-bottom: 1px solid #ddd; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. PROTOCOLO DE SEGURIDAD INSTITUCIONAL
# ==========================================
@st.cache_resource
def iniciar_sistema_seguridad():
    if not firebase_admin._apps:
        try:
            b64_data = st.secrets["CLAVE_MAESTRA"]
            json_texto = base64.b64decode(b64_data).decode('utf-8-sig').replace('\t', '').strip()
            cred_dict = json.loads(json_texto)
            if "private_key" in cred_dict:
                cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.error(f"FALLA CRÍTICA EN PROTOCOLO: {e}")
            return None
    return firestore.client()

db = iniciar_sistema_seguridad()

# ==========================================
# 3. MANEJO DE SESIÓN DE GUARDIA
# ==========================================
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# ==========================================
# 4. ENRUTADOR Y SEGURIDAD (MENÚ LATERAL)
# ==========================================
st.sidebar.markdown("<div style='text-align: center; font-size: 70px; margin-bottom: -10px;'>🏛️</div>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: center;'>Sistema Smart IMLS</h3>", unsafe_allow_html=True)

modo_vista = st.sidebar.radio("Navegación del Sistema", ["🖥️ Tótem de Visitas (Público)", "🛡️ Panel de Control (Guardia)"])
st.sidebar.divider()

# ==========================================
# 5. MODO 1: TÓTEM PÚBLICO (ACCESO DIRECTO POR QR)
# ==========================================
if modo_vista == "🖥️ Tótem de Visitas (Público)":
    
    col_vacia1, col_centro, col_vacia2 = st.columns([1, 2, 1])
    
    with col_centro:
        st.markdown('<div style="text-align: center; font-size: 50px; margin-bottom: -20px;">🏛️</div>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #333;'>Registro de Visitas</h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: #666; margin-top: -10px;'>Edificio Consistorial IMLS</h5>", unsafe_allow_html=True)
        st.divider()

        with st.form("registro_consistorial"):
            # Ajuste de RUT chileno
            rut = st.text_input("RUT del Visitante (Sin puntos y con guion)", placeholder="Ej: 12345678-9", max_chars=10)
            nombre = st.text_input("Nombre Completo del Visitante")
            
            # Listado de departamentos ampliado
            depto = st.selectbox("Departamento o Unidad de Destino", [
                "Alcaldía", "Administración Municipal", "Gabinete", "Oficina de Partes", 
                "Comunicaciones", "Prensa", "Relaciones Públicas", "Eventos", "Patrocinios",
                "Secretaría Municipal", "DIDECO", "Obras (DOM)", "Rentas", "Jurídico", "Control"
            ])
            
            motivo = st.text_area("Motivo de la Visita o Funcionario a contactar", max_chars=150)
            
            submit = st.form_submit_button("VALIDAR Y ANUNCIAR LLEGADA", use_container_width=True)

            if submit:
                if db and rut and nombre and motivo:
                    with st.spinner("Anunciando su llegada a recepción..."):
                        try:
                            db.collection("bitacora_consistorial").add({
                                "rut": rut, "nombre": nombre, "departamento": depto,
                                "motivo": motivo, "fecha_hora": datetime.now(),
                                "estado": "En Recepción" 
                            })
                            st.success("✅ **REGISTRO INGRESADO CORRECTAMENTE.**")
                            st.info("🛋️ **Sala de Espera Virtual:** Por favor, tome asiento. Recepción está gestionando su ingreso al edificio.")
                        except Exception as e:
                            st.error(f"Error de sistema: {e}")
                else:
                    st.warning("⚠️ Complete todos los campos solicitados para poder anunciarlo.")

# ==========================================
# 6. MODO 2: PANEL DE CONTROL (RESTRINGIDO)
# ==========================================
elif modo_vista == "🛡️ Panel de Control (Guardia)":
    
    if not st.session_state["autenticado"]:
        st.sidebar.markdown("#### 🔒 Ingreso Operadores")
        usuario = st.sidebar.text_input("Usuario", placeholder="Ej: guardia")
        clave = st.sidebar.text_input("Contraseña", type="password")
        
        if st.sidebar.button("Ingresar al Sistema", use_container_width=True):
            if usuario == "guardia" and clave == "IMLS2026":
                st.session_state["autenticado"] = True
                st.rerun()
            else:
                st.sidebar.error("❌ Credenciales incorrectas")
        
        st.warning("🔒 **Acceso Restringido.** Por favor, ingrese sus credenciales institucionales en el menú lateral para operar el Panel de Control.")

    else:
        st.sidebar.success(f"✅ Sesión Activa: Guardia IMLS")
        if st.sidebar.button("Cerrar Sesión", use_container_width=True):
            st.session_state["autenticado"] = False
            st.rerun()

        col_titulo, col_boton = st.columns([4, 1])
        col_titulo.markdown("## 🛡️ Central de Coordinación y Control")
        if col_boton.button("🔄 Actualizar Panel"):
            st.rerun()
        st.divider()

        col_espera, col_coord, col_adentro, col_rechazo = st.columns(4)
        
        col_espera.markdown("### 🛋️ En Recepción")
        col_coord.markdown("### ⏳ Coordinando")
        col_adentro.markdown("### ✅ Adentro")
        col_rechazo.markdown("### 🚫 Rechazado")

        if db:
            try:
                visitas_ref = db.collection("bitacora_consistorial").order_by("fecha_hora", direction=firestore.Query.DESCENDING).limit(100).stream()
                historico_visitas = []

                for doc in visitas_ref:
                    visita = doc.to_dict()
                    id_doc = doc.id
                    estado = visita.get("estado", "En Recepción")
                    hora_ingreso = visita["fecha_hora"].strftime("%H:%M") if "fecha_hora" in visita else "--:--"
                    
                    tarjeta_html = f"""
                    <div class="tarjeta-visita">
                        <div class="nombre-visita">{visita.get('nombre', 'Sin Nombre')}</div>
                        <div class="depto-visita">🏢 {visita.get('departamento', '')} | Ingreso: {hora_ingreso}</div>
                        <div class="depto-visita" style="margin-top:5px; font-style:italic;">"{visita.get('motivo', '')}"</div>
                    </div>
                    """

                    if estado == "En Recepción":
                        with col_espera:
                            st.markdown(tarjeta_html, unsafe_allow_html=True)
                            c1, c2 = st.columns(2)
                            if c1.button("Coordinar", key=f"coord_{id_doc}", type="secondary", use_container_width=True):
                                db.collection("bitacora_consistorial").document(id_doc).update({"estado": "Coordinando"})
                                st.rerun()
                            if c2.button("Rechazar", key=f"rech_{id_doc}", type="primary", use_container_width=True):
                                db.collection("bitacora_consistorial").document(id_doc).update({"estado": "Rechazado"})
                                st.rerun()
                                
                    elif estado == "Coordinando":
                        with col_coord:
                            st.markdown(tarjeta_html, unsafe_allow_html=True)
                            if st.button("Autorizar Ingreso", key=f"aut_{id_doc}", type="primary", use_container_width=True):
                                db.collection("bitacora_consistorial").document(id_doc).update({"estado": "Adentro"})
                                st.rerun()

                    elif estado == "Adentro":
                        with col_adentro:
                            st.markdown(tarjeta_html, unsafe_allow_html=True)
                            if st.button("Marcar Salida", key=f"salida_{id_doc}", use_container_width=True):
                                db.collection("bitacora_consistorial").document(id_doc).update({
                                    "estado": "Finalizado",
                                    "hora_salida": datetime.now()
                                })
                                st.rerun()

                    elif estado == "Rechazado":
                        with col_rechazo:
                            st.markdown(tarjeta_html, unsafe_allow_html=True)
                            st.caption("Debe agendar cita digital.")
                            
                    elif estado == "Finalizado":
                        historico_visitas.append(visita)

                st.write("")
                st.divider()
                st.markdown("### 📋 Bitácora de Visitas Finalizadas (Histórico)")
                
                if historico_visitas:
                    tabla_html = "<table class='tabla-historico'><tr><th>Nombre Visitante</th><th>RUT</th><th>Departamento</th><th>Hora Ingreso</th><th>Hora Salida</th></tr>"
                    for v in historico_visitas:
                        h_in = v["fecha_hora"].strftime("%H:%M") if "fecha_hora" in v else "--:--"
                        h_out = v["hora_salida"].strftime("%H:%M") if "hora_salida" in v else "Sin registro"
                        tabla_html += f"<tr><td>{v.get('nombre','')}</td><td>{v.get('rut','')}</td><td>{v.get('departamento','')}</td><td>{h_in}</td><td>{h_out}</td></tr>"
                    tabla_html += "</table>"
                    st.markdown(tabla_html, unsafe_allow_html=True)
                else:
                    st.info("Aún no hay visitas finalizadas en la jornada.")

            except Exception as e:
                st.error(f"Error al cargar el panel: {e}")
