import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# ==========================================
# 0. CONEXIÓN BLINDADA (Austeridad Inteligente)
# ==========================================
@st.cache_resource
def iniciar_conexion():
    if not firebase_admin._apps:
        try:
            # Extraemos los secretos y limpiamos caracteres invisibles
            cred_dict = dict(st.secrets["firebase"])
            # Limpieza quirúrgica de la llave
            raw_key = cred_dict["private_key"].strip().replace("\t", "").replace(" ", "")
            cred_dict["private_key"] = raw_key.replace("\\n", "\n")
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.error(f"Error de seguridad: {e}")
            return None
    return firestore.client()

db = iniciar_conexion()

# ==========================================
# 1. INTERFAZ MUNICIPAL
# ==========================================
st.set_page_config(page_title="Puerta Serena Smart", layout="centered")

# Estética Golden Hour
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    div.stButton > button {
        background-color: #FFD700 !important; color: #333333 !important;
        font-weight: bold; border-radius: 10px; border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Avatar de Resiliencia
st.markdown('<div style="width:100px;height:100px;background-color:#FFD700;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:40px;margin:auto;">🟡</div>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Puerta Serena</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666666;'>Modernización Real · Costo $0</h3>", unsafe_allow_html=True)
st.divider()

# ==========================================
# 2. FORMULARIO DE ACCESO
# ==========================================
rut = st.text_input("Ingresa tu RUT para anunciarte")

if rut:
    nombre = st.text_input("Nombre Completo")
    depto = st.selectbox("Departamento de destino", ["Alcaldía", "DIDECO", "Obras (DOM)", "Rentas"])
    motivo = st.text_input("Motivo de la atención")

    if st.button("🟡 Solicitar Acceso Smart"):
        if db and nombre and motivo:
            with st.spinner("Registrando en SmartLS..."):
                try:
                    db.collection("historico_visitas").add({
                        "rut": rut, "nombre": nombre, "departamento": depto,
                        "motivo": motivo, "fecha": datetime.now()
                    })
                    st.success(f"¡Listo! Notificado a {depto}.")
                except Exception as e:
                    st.error(f"Error de registro: {e}")
        else:
            st.warning("Director, complete todos los campos para el registro.")

st.divider()
st.caption("© 2026 Ilustre Municipalidad de La Serena. | Austeridad Inteligente.")
