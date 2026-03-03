import streamlit as st
import pandas as pd
from datetime import datetime
import time

# ==========================================
# 1. CONFIGURACIÓN ESTRATÉGICA Y VISUAL
# ==========================================
st.set_page_config(
    page_title="Puerta Serena | Muni La Serena Smart",
    page_icon="🚪",
    layout="centered", # Ideal para móviles
    initial_sidebar_state="collapsed"
)

# Paleta de Colores de Campaña (Golden Hour Accent #FFD700)
primary_color = "#FFD700" 
background_color = "#FFFFFF"
text_color = "#333333"

# Inyección de CSS para estética Transmedia
st.markdown(f"""
    <style>
    /* Fondo y Texto Base */
    .stApp {{
        background-color: {background_color};
        color: {text_color};
    }}
    /* Títulos Principales */
    h1, h2, h3 {{
        color: {text_color} !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }}
    /* Botones de Campaña */
    div.stButton > button:first-child {{
        background-color: {primary_color};
        color: {text_color};
        border: none;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }}
    div.stButton > button:first-child:hover {{
        background-color: #ECC000; # Un tono más oscuro para hover
        color: #000000;
        transform: translateY(-2px);
    }}
    /* Inputs Estilizados */
    .stTextInput>div>div>input {{
        border-radius: 8px;
        border: 1px solid #CCCCCC;
    }}
    /* Glow de Serenito (Golden Hour effect) */
    .serenito-glow {{
        filter: drop-shadow(0 0 10px {primary_color});
    }}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. ENTORNO VISUAL Y NARRATIVA
# ==========================================

# Placeholder para Imagen de Serenito Anfitrión (3D Vinilo texture)
# INSTRUCCIÓN: Subir el render 'serenito_anfitrion.png' al mismo directorio
try:
    # Usamos una imagen local si existe, sino un placeholder
    serenito_img = "serenito_anfitrion.png"
    st.image(serenito_img, width=150, caption="", output_format="PNG")
except FileNotFoundError:
    # Placeholder visual mientras el equipo sube el render real
    st.markdown(f'<div style="width:150px;height:150px;background-color:{primary_color};border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:40px;margin:auto;">🟡</div>', unsafe_allow_html=True)
    st.caption("*[Insertar render 3D Serenito Anfitrión (Textura Vinilo)]*")

st.markdown("<h1 style='text-align: center;'>Puerta Serena</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #555555;'>¡La Serena se levanta con inteligencia territorial!</h3>", unsafe_allow_html=True)
st.divider()

st.markdown("#### ¡Hola! Soy Serenito, tu anfitrión municipal Smart.")
st.markdown("Estamos 'remodelando la casa' para servirte mejor. Por favor, **anúnciate** para agilizar tu atención y reducir tu tiempo de espera.")

# ==========================================
# 3. MÓDULO DE IDENTIFICACIÓN (TRAZABILIDAD $0)
# ==========================================
with st.container():
    st.markdown("##### 1. Identifícate")
    rut_ingresado = st.text_input("Ingresa tu RUT (Ej: 12345678-9)", placeholder="12345678-9", help="Para trazabilidad y seguridad in-house.")

# Simulamos base de datos histórica para autocompletado (En producción: Lee Google Sheets)
visitas_historicas = {
    "12345678-9": {"nombre": "Juan Pérez", "telefono": "+56912345678", "categoria": "Vecino / Dirigente"},
    "8765432-1": {"nombre": "Pedro González (Seremi Vivienda)", "telefono": "+56987654321", "categoria": "Autoridad / Gobierno"}
}

visita_datos = {}

if rut_ingresado:
    st.divider()
    
    # Lógica de Enrolamiento Inteligente
    if rut_ingresado in visitas_historicas:
        visita_datos = visitas_historicas[rut_ingresado]
        st.success(f"¡Bienvenido de vuelta, {visita_datos['nombre']}!")
        st.markdown(f"*Datos autocompletados (Categoría: {visita_datos['categoria']}). Si son incorrectos, por favor avisa en recepción.*")
    else:
        st.info("Es tu primera visita Smart o tu RUT no está registrado. Por favor, completa tu enrolamiento:")
        visita_datos['nombre'] = st.text_input("Nombre Completo (como aparece en CI)")
        visita_datos['telefono'] = st.text_input("Teléfono Celular de Contacto")
        visita_datos['categoria'] = st.selectbox(
            "¿A qué categoría corresponde tu visita?",
            ("Vecino / Dirigente Vecinal", "Autoridad / Gobierno", "Proveedor / Empresa", "Otro")
        )

# ==========================================
# 4. MÓDULO DE DESTINO (CADENA DE VÍNCULOS)
# ==========================================
if rut_ingresado and visita_datos.get('nombre') and visita_datos.get('telefono'):
    st.divider()
    st.markdown("##### 2. ¿A quién vienes a visitar?")
    
    # Datos simulados de la estructura municipal (En producción: Lee Google Sheets)
    estructura_muni = {
        "DIDECO": ["Director DIDECO", "Subdirector Social", "Ficha Protección Social"],
        "Obras (DOM)": ["Director de Obras", "Edificación", "Licitaciones"],
        "Rentas": ["Director Rentas", "Patentes Comerciales"],
        "Alcaldía": ["Alcaldesa Daniela Norambuena", "Jefe de Gabinete", "Secretaría Alcaldía"]
    }
    
    departamento = st.selectbox("Selecciona el Departamento", list(estructura_muni.keys()))
    
    if departamento:
        funcionario = st.selectbox(f"Selecciona el Funcionario/Sección en {departamento}", estructura_muni[departamento])
        motivo = st.text_input("Motivo breve de la visita (Ej: Consulta de patente, reunión agendada)")

    # ==========================================
    # 5. ACCIÓN Y DISPARO DE ALERTAS
    # ==========================================
    st.divider()
    submit_btn = st.button("🚪 Solicitar Acceso Smart")

    if submit_btn:
        if funcionario and motivo:
            # Simulamos el guardado de datos y el disparo de la Cadena de Vínculos
            with st.spinner(f"Anunciando tu visita a {funcionario} en {departamento}..."):
                time.sleep(1.5) # Simulación de delay de API
                
                # Registro exitoso
                timestamp = datetime.now().strftime("%H:%M:%S")
                st.success(f"¡Listo, {visita_datos['nombre']}! Tu visita ha sido notificada instantáneamente.")
                
                # Feedback para el vecino (Reducción de ansiedad)
                st.info(f"El staff de {funcionario} y la recepción ya saben que estás aquí. Por favor, avanza al pórtico de acceso. Registro exitoso a las {timestamp}.")
                
                # Nota Estratégica para el equipo (No visible en producción)
                # st.write(f"*DEVELOPER NOTE: Disparar Email/Webhook a staff de {funcionario} y actualizar Dashboard de Guardia.*")
                
                # Resetear formulario (opcional, redirigir a landing de RDMLS)
                # st.experimental_rerun()
        else:
            st.error("Por favor, selecciona a quién vienes a visitar y el motivo brevemente para poder anunciarte.")

# ==========================================
# 6. FOOTER INSTITUCIONAL ($0 COSTO)
# ==========================================
st.divider()
st.caption(f"""
    © 2024 Ilustre Municipalidad de La Serena. | Administración Alcaldesa Daniela Norambuena. |
    Tecnología Smart City In-House (Austeridad Inteligente). | $0 Costo de Inversión en Software.
""")
