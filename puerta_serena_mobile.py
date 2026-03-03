import streamlit as st
import pandas as pd
from datetime import datetime
import time
import firebase_admin
from firebase_admin import credentials, firestore

# ==========================================
# 0. CONEXIÓN BLINDADA (Limpieza de Byte 9)
# ==========================================
@st.cache_resource
def iniciar_conexion():
    if not firebase_admin._apps:
        try:
            cred_dict = dict(st.secrets["firebase"])
            # Limpieza quirúrgica: eliminamos tabulaciones y espacios accidentales
            limpia_key = cred_dict["private_key"].replace("\t", "").replace(" ", "")
            cred_dict["private_key"] = limpia_key.replace("\\n", "\n")
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.error(f"Error de seguridad: {e}")
            return None
    return firestore.client()

db = iniciar_conexion()

# ==========================================
# 1. CONFIGURACIÓN VISUAL MUNICIPAL
# ==========================================
st.set_page_config(page_title="Puerta Serena Smart", page_icon="🚪", layout="centered")

primary_color = "#FFD700" 
st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFFFFF; color: #333333; }}
    div.stButton > button:first-child {{
        background-color: {primary_color}; border: none; border-radius: 10px; font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. ENTORNO VISUAL
# ==========================================
try:
    st.image("serenito_anfitrion.png", width=150)
except Exception:
    st.markdown(f'<div style="width:100px;height:100px;background-color:{primary_color};border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:40px;margin:auto;">🟡</div>', unsafe_allow_html=True)
    st.caption("Conectando entorno visual Smart...")

st.markdown("<h1 style='text-align: center;'>Puerta Serena</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555555;'>Modernización Real · Costo $0</h3>", unsafe_allow_html=True)
st.divider()

# ==========================================
# 3. REGISTRO DE TRAZABILIDAD
# ==========================================
rut_vecino = st.text_input("Ingresa tu RUT para anunciarte", key="rut_input")

if rut_vecino:
    nombre_vecino = st.text_input("Nombre Completo")
    depto_destino = st.selectbox("Departamento de destino", ["DIDECO", "Obras (DOM)", "Rentas", "Alcaldía"])
    motivo_visita = st.text_input("Motivo breve de la atención")

    if st.button("🚪 Solicitar Acceso Smart"):
        if db and motivo_visita and nombre_vecino:
            with st.spinner("Registrando visita..."):
                datos = {
                    "rut": rut_vecino, "nombre": nombre_vecino, "departamento": depto_destino,
                    "motivo": motivo_visita, "fecha_ingreso": datetime.now()
                }
                try:
                    db.collection("historico_visitas").add(datos)
                    st.success(f"¡Listo! Tu visita a {depto_destino} ha sido registrada.")
                except Exception as e:
                    st.error(f"Error al guardar: {e}")
        else:
            st.warning("Director, asegúrese de completar todos los campos.")

st.divider()
st.caption("© 2026 Ilustre Municipalidad de La Serena. | Austeridad Inteligente.")
