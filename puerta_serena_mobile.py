import streamlit as st
import pandas as pd
from datetime import datetime
import time
import firebase_admin
from firebase_admin import credentials, firestore

# ==========================================
# 0. CONEXIÓN DIRECTA Y SEGURA
# ==========================================
@st.cache_resource
def iniciar_conexion():
    if not firebase_admin._apps:
        try:
            # Leemos el bloque [firebase] de los secretos
            cred_dict = dict(st.secrets["firebase"])
            # Limpieza forzada de la llave para evitar el error MalformedFraming
            cred_dict["private_key"] = cred_dict["private_key"].replace("\\n", "\n")
            
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as e:
            st.error(f"Error de conexión: {e}")
            return None
    return firestore.client()

db = iniciar_conexion()

# ==========================================
# 1. CONFIGURACIÓN VISUAL
# ==========================================
st.set_page_config(page_title="Puerta Serena", page_icon="🚪", layout="centered")

primary_color = "#FFD700" 
st.markdown(f"""
    <style>
    .stApp {{ background-color: #FFFFFF; color: #333333; }}
    div.stButton > button:first-child {{
        background-color: {primary_color}; border-radius: 10px; font-weight: bold;
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. MANEJO SEGURO DE IMAGEN (Línea 92 corregida)
# ==========================================
try:
    # Intentamos cargar la imagen de Serenito
    st.image("serenito_anfitrion.png", width=150)
except Exception:
    # Si falla, mostramos el avatar dorado para que la app no se caiga
    st.markdown(f'<div style="width:100px;height:100px;background-color:{primary_color};border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:40px;margin:auto;">🟡</div>', unsafe_allow_html=True)
    st.caption("Cargando entorno visual...")

st.markdown("<h1 style='text-align: center;'>Puerta Serena</h1>", unsafe_allow_html=True)
st.divider()

# ==========================================
# 3. LÓGICA DE REGISTRO
# ==========================================
rut = st.text_input("Ingresa tu RUT")

if rut:
    nombre = st.text_input("Nombre Completo")
    depto = st.selectbox("Departamento", ["DIDECO", "Obras (DOM)", "Rentas", "Alcaldía"])
    motivo = st.text_input("Motivo de la visita")

    if st.button("🚪 Solicitar Acceso Smart"):
        if db and motivo and nombre:
            with st.spinner("Registrando..."):
                datos = {
                    "rut": rut, "nombre": nombre, "departamento": depto,
                    "motivo": motivo, "fecha": datetime.now()
                }
                try:
                    db.collection("historico_visitas").add(datos)
                    st.success(f"¡Listo! Notificado a {depto}.")
                except Exception as e:
                    st.error(f"Error al guardar: {e}")
        else:
            st.warning("Completa todos los campos.")

st.divider()
st.caption("© 2026 Ilustre Municipalidad de La Serena.")
