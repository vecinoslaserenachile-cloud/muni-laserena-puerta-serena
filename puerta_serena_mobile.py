import streamlit as st
from datetime import datetime
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore

# ==========================================
# PROTOCOLO DE SEGURIDAD INSTITUCIONAL
# ==========================================
@st.cache_resource
def iniciar_sistema_seguridad():
    if not firebase_admin._apps:
        try:
            # Decodificación blindada para evitar errores de PEM / MalformedFraming
            b64_data = st.secrets["CLAVE_MAESTRA"]
            json_data = base64.b64decode(b64_data).decode('utf-8-sig')
            cred_dict = json.loads(json_data)
            
            # Limpieza de saltos de línea para la llave privada
            if "private_key" in cred_dict:
                cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.error(f"FALLA CRÍTICA DE ACCESO: {e}")
            return None
    return firestore.client()

db = iniciar_sistema_seguridad()

# ==========================================
# INTERFAZ EDIFICIO CONSISTORIAL IMLS
# ==========================================
st.set_page_config(page_title="Seguridad de Acceso | I.M. La Serena", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    div.stButton > button {
        background-color: #FFD700 !important; color: #000000 !important;
        font-weight: bold; border-radius: 4px; border: 1px solid #B89600;
        height: 3.5em; width: 100%; font-size: 1.1em;
    }
    .main-header { text-align: center; color: #333333; margin-bottom: 5px; font-weight: bold; }
    .sub-header { text-align: center; color: #666666; margin-top: 0px; font-weight: normal; font-size: 1.2em; }
    </style>
""", unsafe_allow_html=True)

# Icono Institucional de Seguridad
st.markdown('<div style="width:80px;height:80px;background-color:#FFD700;border-radius:15%;display:flex;align-items:center;justify-content:center;font-size:40px;margin:auto;box-shadow: 0 4px 8px rgba(0,0,0,0.1);">🏛️</div>', unsafe_allow_html=True)

st.markdown("<h2 class='main-header'>Seguridad al Acceso Recinto Municipal</h2>", unsafe_allow_html=True)
st.markdown("<h4 class='sub-header'>Edificio Consistorial IMLS</h4>", unsafe_allow_html=True)
st.divider()

# ==========================================
# FORMULARIO DE CONTROL DE ACCESO
# ==========================================
with st.form("registro_consistorial"):
    col1, col2 = st.columns(2)
    with col1:
        rut = st.text_input("RUT del Visitante", placeholder="Ej: 12.345.678-9")
    with col2:
        nombre = st.text_input("Nombre Completo")
    
    depto = st.selectbox("Departamento de Destino", 
                         ["Alcaldía", "Secretaría Municipal", "DIDECO", "Obras (DOM)", "Rentas", "Jurídico", "Control"])
    
    motivo = st.text_area("Motivo de la Visita / Oficina de Referencia")
    
    submit = st.form_submit_button("VALIDAR Y REGISTRAR INGRESO")

    if submit:
        if db and rut and nombre and motivo:
            with st.spinner("Procesando registro en bitácora digital..."):
                try:
                    db.collection("bitacora_consistorial").add({
                        "rut": rut,
                        "nombre": nombre,
                        "departamento": depto,
                        "motivo": motivo,
                        "fecha_hora": datetime.now()
                    })
                    st.success(f"REGISTRO EXITOSO: Visitante autorizado para {depto}.")
                except Exception as e:
                    st.error(f"ERROR DE SISTEMA: {e}")
        else:
            st.warning("ATENCIÓN: Debe completar todos los campos del protocolo de seguridad.")

st.divider()
st.caption("Ilustre Municipalidad de La Serena | Sistema de Control de Acceso")
