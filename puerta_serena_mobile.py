"""
=============================================================================
SISTEMA DE GESTIÓN DE ACCESO - RED DE RECINTOS MUNICIPALES IMLS
=============================================================================
Cliente: Ilustre Municipalidad de La Serena
Desarrollo: Vecinos La Serena Spa
Versión: 2.5.0 (Robusta / Enterprise)
Descripción: Aplicación para el registro, control y trazabilidad de visitas.
=============================================================================
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import csv
import io

# =============================================================================
# 1. CONFIGURACIÓN DE SEGURIDAD Y ENTORNO
# =============================================================================
st.set_page_config(
    page_title="Control Acceso | I.M. La Serena",
    page_icon="🏛️",
    layout="centered"
)

# Estilos CSS para el "Modo Guardia" (Botones grandes y contraste alto)
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button {
        width: 100%;
        height: 3em;
        font-weight: bold;
        background-color: #1A365D;
        color: white;
        border-radius: 10px;
    }
    .status-box {
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .header-muni {
        text-align: center;
        padding: 10px;
        border-bottom: 3px solid #1A365D;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# 2. LÓGICA DE PERSISTENCIA DE DATOS (DATABASE MOCK)
# =============================================================================
if 'registro_visitas' not in st.session_state:
    # Inicialización del historial en memoria
    st.session_state.registro_visitas = pd.DataFrame(columns=[
        'Fecha', 'Hora', 'Recinto', 'Nombre Completo', 'RUT', 'Motivo Visita', 'Departamento/Oficina', 'Estado'
    ])

# =============================================================================
# 3. COMPONENTES DE LA INTERFAZ
# =============================================================================

def render_header():
    st.markdown("""
        <div class="header-muni">
            <h1 style='color: #1A365D;'>🏛️ Control de Acceso</h1>
            <p style='color: #718096;'>Red de Recintos Municipales | I.M. La Serena</p>
        </div>
    """, unsafe_allow_html=True)

def formulario_ingreso():
    st.subheader("📝 Registro de Nuevo Ingreso")
    
    with st.form("form_visita", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            recinto = st.selectbox("Seleccione Recinto", [
                "Edificio Consistorial", 
                "Dirección de Tránsito", 
                "Desarrollo Comunitario (DIDECO)",
                "Polideportivo Las Compañías",
                "Delegación Av. del Mar"
            ])
            nombre = st.text_input("Nombre Completo del Visitante")
            rut = st.text_input("RUT (ej: 12.345.678-9)")
            
        with col2:
            depto = st.text_input("Departamento / Oficina de destino")
            motivo = st.selectbox("Motivo", [
                "Trámite Administrativo",
                "Reunión Agendada",
                "Entrega de Correspondencia",
                "Mantenimiento/Servicios",
                "Otro"
            ])
            estado = st.radio("Estado Inicial", ["Ingreso Autorizado", "En Espera"], horizontal=True)

        submitted = st.form_submit_button("REGISTRAR INGRESO")
        
        if submitted:
            if nombre and rut:
                nuevo_registro = {
                    'Fecha': datetime.now().strftime("%d/%m/%Y"),
                    'Hora': datetime.now().strftime("%H:%M:%S"),
                    'Recinto': recinto,
                    'Nombre Completo': nombre,
                    'RUT': rut,
                    'Motivo Visita': motivo,
                    'Departamento/Oficina': depto,
                    'Estado': estado
                }
                # Guardar en el estado de la sesión
                st.session_state.registro_visitas = pd.concat([
                    pd.DataFrame([nuevo_registro]), 
                    st.session_state.registro_visitas
                ], ignore_index=True)
                
                st.success(f"✅ Ingreso registrado: {nombre}")
            else:
                st.error("⚠️ Por favor complete Nombre y RUT.")

def visor_historial():
    st.divider()
    st.subheader("📋 Visitas Recientes (Hoy)")
    
    if not st.session_state.registro_visitas.empty:
        # Filtro rápido por recinto
        filtro = st.multiselect("Filtrar por Recinto:", 
                               options=st.session_state.registro_visitas['Recinto'].unique())
        
        df_mostrar = st.session_state.registro_visitas
        if filtro:
            df_mostrar = df_mostrar[df_mostrar['Recinto'].isin(filtro)]
            
        st.dataframe(df_mostrar, use_container_width=True)
        
        # Botón de exportación técnica
        csv_buffer = io.StringIO()
        df_mostrar.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Descargar Reporte (CSV)",
            data=csv_buffer.getvalue(),
            file_name=f"visitas_serena_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("No hay registros de visitas para el día de hoy.")

# =============================================================================
# 4. BUCLE PRINCIPAL
# =============================================================================
def main():
    render_header()
    
    # Menú lateral para administración
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png", width=150)
        st.title("Panel de Control")
        opcion = st.radio("Acciones:", ["Registrar Visita", "Consultar Historial", "Cerrar Turno"])
        
        st.divider()
        st.caption("📍 Sistema Operativo SmartCity")
        st.caption(f"🕒 {datetime.now().strftime('%H:%M:%S')}")

    if opcion == "Registrar Visita":
        formulario_ingreso()
    elif opcion == "Consultar Historial":
        visor_historial()
    elif opcion == "Cerrar Turno":
        st.warning("¿Está seguro que desea cerrar el turno? Se generará un reporte final.")
        if st.button("Confirmar Cierre"):
            st.write("Turno cerrado. Reporte enviado a la central.")

if __name__ == "__main__":
    main()
