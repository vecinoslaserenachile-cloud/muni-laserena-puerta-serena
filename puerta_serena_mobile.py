import streamlit as st
from datetime import datetime
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore

# ==========================================
# PROTOCOLO DE SEGURIDAD INSTITUCIONAL IMLS
# ==========================================
@st.cache_resource
def iniciar_sistema_seguridad():
    if not firebase_admin._apps:
        try:
            # 1. Obtenemos el secreto blindado
            b64_data = st.secrets["CLAVE_MAESTRA"]
            
            # 2. Decodificación y LIMPIEZA TOTAL de caracteres de control (Byte 9)
            # El strip() y replace('\t','') eliminan el ruido del servidor
            json_texto = base64.b64decode(b64_data).decode('utf-8-sig').replace('\t', '').strip()
            
            # 3. Reconstrucción del diccionario de credenciales
            cred_dict = json.loads(json_texto)
            if "private_key" in cred_dict:
                # Aseguramos que los saltos de línea sean reales para el formato PEM
                cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.error(f"FALLA CRÍTICA EN PROTOCOLO DE SEGURIDAD: {e}")
            return None
    return firestore.client()

db = iniciar_sistema_seguridad()

# ==========================================
# INTERFAZ EDIFICIO CONSISTORIAL
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
    .main-header { text-align: center; color: #333333; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Símbolo de Seguridad Institucional
st.markdown('<div style="width:80px;height:80px;background-color:#FFD700;border-radius:15%;display:flex;align-items:center;justify-content:center;font-size:40px;margin:auto;box-shadow: 0 4px 8px rgba(0,0,0,0.1);">🏛️</div>', unsafe_allow_html=True)

st.markdown("<h2 class='main-header'>Seguridad al Acceso Recinto Municipal</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #666666;'>Edificio Consistorial IMLS</h4>", unsafe_allow_html=True)
st.divider()

# ==========================================
# BITÁCORA DE CONTROL DE INGRESO
# ==========================================
with st.form("registro_consistorial"):
    col1, col2 = st.columns(2)
    with col1:
        rut = st.text_input("RUT del Visitante", placeholder="Ej: 12.345.678-9")
    with col2:
        nombre = st.text_input("Nombre Completo")
    
    depto = st.selectbox("Departamento de Destino", 
                         ["Alcaldía", "Secretaría Municipal", "DIDECO", "Obras (DOM)", "Rentas", "Jurídico", "Control"])
    
    motivo = st.text_area("Motivo de la Visita / Referencia de Oficina")
    
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
            st.warning("ATENCIÓN: Debe completar el protocolo de seguridad para autorizar el ingreso.")

st.divider()
st.caption("Sistema de Trazabilidad Institucional | Ilustre Municipalidad de La Serena")
