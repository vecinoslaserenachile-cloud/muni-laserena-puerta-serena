import streamlit as st
from datetime import datetime
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd # Para el análisis de datos

# ==========================================
# 1. CONFIGURACIÓN VISUAL GENERAL
# ==========================================
st.set_page_config(page_title="Control de Acceso | I.M. La Serena", page_icon="🏛️", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp { background-color: #F8F9FA; }
    label, .stTextInput label, .stSelectbox label, .stTextArea label { color: #333333 !important; font-weight: bold !important; }
    input, select, textarea { color: #111111 !important; background-color: #FFFFFF !important; }
    .tarjeta-visita {
        background-color: white; padding: 15px; border-radius: 8px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px; border-left: 4px solid #FFD700;
    }
    .nombre-visita { font-weight: bold; font-size: 1.1em; color: #333; margin-bottom: 2px;}
    .depto-visita { color: #555; font-size: 0.9em; }
    .tabla-historico { width: 100%; border-collapse: collapse; background-color: white; color: #333; }
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
# 3. MANEJO DE SESIÓN
# ==========================================
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

# ==========================================
# 4. ENRUTADOR (MENÚ LATERAL)
# ==========================================
st.sidebar.markdown("<div style='text-align: center; font-size: 70px; margin-bottom: -10px;'>🏛️</div>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: center;'>Sistema Smart IMLS</h3>", unsafe_allow_html=True)

modo_vista = st.sidebar.radio("Navegación del Sistema", 
                              ["🖥️ Tótem de Visitas (Público)", "🛡️ Panel de Control (Guardia)", "📊 Reportes Institucionales"])
st.sidebar.divider()

# ==========================================
# 5. MODO 1: TÓTEM PÚBLICO
# ==========================================
if modo_vista == "🖥️ Tótem de Visitas (Público)":
    col_v1, col_centro, col_v2 = st.columns([1, 2, 1])
    with col_centro:
        st.markdown('<div style="text-align: center; font-size: 50px; margin-bottom: -20px;">🏛️</div>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #333;'>Registro de Visitas</h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: #666; margin-top: -10px;'>Edificio Consistorial IMLS</h5>", unsafe_allow_html=True)
        st.divider()

        with st.form("registro_consistorial"):
            rut = st.text_input("RUT del Visitante (Sin puntos y con guion)", placeholder="Ej: 12345678-9", max_chars=10)
            nombre = st.text_input("Nombre Completo")
            depto = st.selectbox("Unidad de Destino", [
                "Alcaldía", "Administración Municipal", "Gabinete", "Oficina de Partes", 
                "Comunicaciones", "Prensa", "Relaciones Públicas", "Eventos", "Patrocinios",
                "Secretaría Municipal", "DIDECO", "Obras (DOM)", "Rentas", "Jurídico", "Control"
            ])
            motivo = st.text_area("Motivo de la Visita", max_chars=150)
            submit = st.form_submit_button("VALIDAR Y ANUNCIAR LLEGADA", use_container_width=True)

            if submit:
                if db and rut and nombre and motivo:
                    try:
                        db.collection("bitacora_consistorial").add({
                            "rut": rut, "nombre": nombre, "departamento": depto,
                            "motivo": motivo, "fecha_hora": datetime.now(),
                            "estado": "En Recepción" 
                        })
                        st.success("✅ **REGISTRO INGRESADO.**")
                        st.info("🛋️ **Sala de Espera Virtual:** Recepción gestionará su ingreso.")
                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.warning("⚠️ Complete todos los campos.")

# ==========================================
# 6. MODO 2 Y 3: PANEL Y REPORTES (CON LOGIN)
# ==========================================
else:
    if not st.session_state["autenticado"]:
        st.sidebar.markdown("#### 🔒 Ingreso Operadores")
        usuario = st.sidebar.text_input("Usuario")
        clave = st.sidebar.text_input("Contraseña", type="password")
        if st.sidebar.button("Ingresar"):
            if usuario == "guardia" and clave == "IMLS2026":
                st.session_state["autenticado"] = True
                st.rerun()
            else:
                st.sidebar.error("❌ Credenciales incorrectas")
        st.warning("🔒 Ingrese sus credenciales en el menú lateral.")

    elif modo_vista == "🛡️ Panel de Control (Guardia)":
        st.sidebar.success("✅ Sesión Activa")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state["autenticado"] = False
            st.rerun()

        col_t, col_b = st.columns([4, 1])
        col_t.markdown("## 🛡️ Central de Coordinación")
        if col_b.button("🔄 Actualizar"): st.rerun()
        st.divider()

        c_esp, c_coo, c_ade, c_rec = st.columns(4)
        c_esp.markdown("### 🛋️ Recepción")
        c_coo.markdown("### ⏳ Coordinando")
        c_ade.markdown("### ✅ Adentro")
        c_rec.markdown("### 🚫 Rechazado")

        if db:
            docs = db.collection("bitacora_consistorial").order_by("fecha_hora", direction=firestore.Query.DESCENDING).limit(50).stream()
            historico = []
            for doc in docs:
                v = doc.to_dict()
                id_d = doc.id
                est = v.get("estado", "En Recepción")
                h_in = v["fecha_hora"].strftime("%H:%M") if "fecha_hora" in v else "--:--"
                
                t_html = f'<div class="tarjeta-visita"><b>{v.get("nombre","")}</b><br><small>🏢 {v.get("departamento","")} | 🕒 {h_in}</small></div>'
                
                if est == "En Recepción":
                    with c_esp:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Coordinar", key=f"c_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Coordinando"}); st.rerun()
                elif est == "Coordinando":
                    with c_coo:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Autorizar", key=f"a_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Adentro"}); st.rerun()
                elif est == "Adentro":
                    with c_ade:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Salida", key=f"s_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Finalizado", "hora_salida": datetime.now()}); st.rerun()
                elif est == "Finalizado": historico.append(v)
            
            st.divider()
            st.markdown("### 📋 Bitácora de Salidas")
            if historico: st.table(pd.DataFrame(historico)[["nombre", "rut", "departamento", "fecha_hora"]].rename(columns={"fecha_hora":"Hora Ingreso"}))

    # ==========================================
    # 7. MODO 3: REPORTES (NUEVA PESTAÑA)
    # ==========================================
    elif modo_vista == "📊 Reportes Institucionales":
        st.markdown("## 📊 Inteligencia de Datos: Flujo de Ciudadanos")
        st.divider()
        
        if db:
            with st.spinner("Analizando histórico de visitas..."):
                docs = db.collection("bitacora_consistorial").stream()
                lista_v = [d.to_dict() for d in docs]
                
                if lista_v:
                    df = pd.DataFrame(lista_v)
                    df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])
                    
                    # KPIs Superiores
                    kpi1, kpi2, kpi3 = st.columns(3)
                    kpi1.metric("Total Visitas Acumuladas", len(df))
                    kpi2.metric("Departamentos Atendiendo", df['departamento'].nunique())
                    kpi3.metric("Ciudadanos Únicos (RUT)", df['rut'].nunique())
                    
                    st.write("")
                    
                    col_g1, col_g2 = st.columns(2)
                    
                    with col_g1:
                        st.markdown("#### 🏢 Visitas por Departamento")
                        # Gráfico de barras de departamentos
                        conteo_depto = df['departamento'].value_counts()
                        st.bar_chart(conteo_depto)
                        st.caption("Distribución del flujo de personas por oficina municipal.")
                    
                    with col_g2:
                        st.markdown("#### 👤 Top 10 Visitantes Recurrentes")
                        # Frecuencia por persona (RUT/Nombre)
                        top_visitantes = df.groupby(['rut', 'nombre']).size().reset_index(name='Visitas').sort_values(by='Visitas', ascending=False).head(10)
                        st.dataframe(top_visitantes, use_container_width=True)
                        st.caption("Identificación de ciudadanos con alta frecuencia de asistencia presencial.")

                    st.divider()
                    st.markdown("#### 📈 Tendencia de Ingresos")
                    # Agrupar por fecha para ver tendencia
                    df['fecha'] = df['fecha_hora'].dt.date
                    tendencia = df.groupby('fecha').size()
                    st.line_chart(tendencia)
                else:
                    st.info("No hay datos suficientes para generar reportes aún.")
