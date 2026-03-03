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
            # Decodificación de la Clave Maestra enviada por el Director
            b64_data = st.secrets["CLAVE_MAESTRA"]
            # El decodificador ignora cualquier deformación del servidor
            json_data = base64.b64decode(b64_data).decode('utf-8-sig')
            
            # Limpieza de posibles etiquetas TOML si se incluyeron en el encode
            if "private_key =" in json_data:
                # Si el encode incluyó formato TOML, lo procesamos como tal
                import tomllib
                cred_dict = tomllib.loads(json_data)["firebase"]
                cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
            else:
                # Si es JSON puro
                cred_dict = json.loads(json_data)
            
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
        height: 3.5em; width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Seguridad al Acceso Recinto Municipal</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666666;'>Edificio Consistorial IMLS</h4>", unsafe_allow_html=True)
st.divider()

# ==========================================
# REGISTRO DE CONTROL DE INGRESO
# ==========================================
with st.form("registro_consistorial"):
    rut = st.text_input("RUT del Visitante", placeholder="Ej: 12.345.678-9")
    nombre = st.text_input("Nombre Completo")
    depto = st.selectbox("Departamento de Destino", 
                         ["Alcaldía", "Secretaría Municipal", "DIDECO", "Obras (DOM)", "Rentas", "Jurídico", "Control"])
    motivo = st.text_area("Motivo de la Visita")
    
    submit = st.form_submit_button("VALIDAR Y REGISTRAR INGRESO")

    if submit:
        if db and rut and nombre and motivo:
            try:
                db.collection("bitacora_consistorial").add({
                    "rut": rut, "nombre": nombre, "departamento": depto,
                    "motivo": motivo, "fecha_hora": datetime.now()
                })
                st.success(f"REGISTRO EXITOSO: Visitante autorizado para {depto}.")
            except Exception as e:
                st.error(f"ERROR DE SISTEMA: {e}")
        else:
            st.warning("ATENCIÓN: Debe completar el protocolo de seguridad para autorizar el ingreso.")

st.divider()
st.caption("Sistema de Trazabilidad Institucional | Ilustre Municipalidad de La Serena")
