import streamlit as st
from datetime import datetime
import pytz
import json
import base64
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import numpy as np

# ==========================================
# 1. CONFIGURACIÓN GENERAL Y HORA CHILE
# ==========================================
st.set_page_config(page_title="Control Acceso Visitas | IMLS", page_icon="🏛️", layout="wide", initial_sidebar_state="expanded")

tz_chile = pytz.timezone('America/Santiago')

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
    .kpi-card { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); text-align: center; border-bottom: 3px solid #2B6CB0; }
    </style>
""", unsafe_allow_html=True)

RECINTOS_IMLS = [
    "Edificio Consistorial (Prat 451)", "Edificio O'Higgins / Ex CCU (Balmaceda)",
    "Delegación Municipal Las Compañías", "Delegación Municipal La Antena",
    "Delegación Municipal La Pampa", "Delegación Municipal Centro",
    "Delegación Municipal Avenida del Mar", "Delegación Municipal Rural",
    "Dirección de Tránsito", "Juzgados de Policía Local", "Centro Comunitario / Coliseo Monumental"
]

# ==========================================
# 2. PROTOCOLO DE SEGURIDAD (CONEXIÓN BD)
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
if "autenticado" not in st.session_state: st.session_state["autenticado"] = False
if "mi_visita_id" not in st.session_state: st.session_state["mi_visita_id"] = None

# ==========================================
# 4. ENRUTADOR (MENÚ LATERAL)
# ==========================================
st.sidebar.markdown("<div style='text-align: center; font-size: 70px; margin-bottom: -10px;'>🏛️</div>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: center; font-size: 1.3em;'>Control Accesos IMLS</h3>", unsafe_allow_html=True)

modo_vista = st.sidebar.radio("Navegación del Sistema", 
                              ["📱 Acceso Ciudadano (QR)", "🛡️ Panel de Guardia", "📊 Big Data & Inteligencia"])
st.sidebar.divider()

# ==========================================
# 5. MODO 1: TÓTEM / CAPTURA ENRIQUECIDA
# ==========================================
if modo_vista == "📱 Acceso Ciudadano (QR)":
    col_v1, col_centro, col_v2 = st.columns([1, 2, 1])
    with col_centro:
        st.markdown('<div style="text-align: center; font-size: 50px; margin-bottom: -20px;">🏛️</div>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #333;'>Control Acceso Visitas</h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: #666; margin-top: -10px;'>Red de Recintos Municipales | I.M. La Serena</h5>", unsafe_allow_html=True)
        st.divider()

        if st.session_state["mi_visita_id"] is None:
            with st.form("registro_consistorial"):
                st.info("💡 **Sistema SmartCity:** Por favor, registre sus datos para coordinar su ingreso.")
                
                # DATOS DUROS
                col_rut, col_serie = st.columns(2)
                with col_rut: rut = st.text_input("RUT (Sin puntos y con guion)", max_chars=10)
                with col_serie: num_serie = st.text_input("Nº de Documento (Serie)", max_chars=15)
                nombre = st.text_input("Nombre Completo")
                
                # DATA ENRIQUECIDA PARA BIG DATA
                st.markdown("#### 🏢 Perfil del Visitante")
                col_perfil, col_empresa = st.columns(2)
                with col_perfil:
                    perfil_visitante = st.selectbox("Tipo de Visita", ["Ciudadano / Vecino", "Empresa / Proveedor", "Organización Social / ONG", "Institución Pública / Autoridad"])
                with col_empresa:
                    empresa_inst = st.text_input("Organización o Empresa (Opcional)", placeholder="Ej: Constructora XYZ, Junta Vecinal N°4")
                
                # DESTINO
                recinto_seleccionado = st.selectbox("Recinto Municipal a Visitar", RECINTOS_IMLS)
                depto = st.selectbox("Unidad / Departamento de Destino", [
                    "Alcaldía", "Administración Municipal", "Gabinete", "Oficina de Partes", 
                    "Comunicaciones / Prensa", "Relaciones Públicas / Eventos", "DIDECO", 
                    "Obras (DOM)", "Rentas y Patentes", "Jurídico", "Control", 
                    "Dirección de Tránsito", "Seguridad Ciudadana", "Atención a Público General"
                ])
                motivo = st.text_area("Motivo de la Visita", max_chars=150)
                
                submit = st.form_submit_button("VALIDAR Y ANUNCIAR LLEGADA", use_container_width=True)

                if submit:
                    if db and rut and nombre and motivo:
                        with st.spinner("Registrando datos en la red municipal..."):
                            try:
                                ahora_chile = datetime.now(tz_chile)
                                chat_inicial = [{"role": "assistant", "content": f"👋 Hola {nombre.split()[0]}. Soy la Asistencia Virtual IMLS. Notificando a seguridad..."}]
                                
                                update_time, doc_ref = db.collection("bitacora_consistorial").add({
                                    "rut": rut, "numero_serie": num_serie, "nombre": nombre, 
                                    "perfil_visitante": perfil_visitante, "empresa_institucion": empresa_inst,
                                    "recinto": recinto_seleccionado, "departamento": depto,
                                    "motivo": motivo, "fecha_hora": ahora_chile, "estado": "En Recepción",
                                    "chat": chat_inicial
                                })
                                st.session_state["mi_visita_id"] = doc_ref.id
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error de conexión: {e}")
                    else:
                        st.warning("⚠️ Complete los campos obligatorios (RUT, Nombre y Motivo).")

        else:
            if db:
                doc_ref = db.collection("bitacora_consistorial").document(st.session_state["mi_visita_id"])
                doc_actual = doc_ref.get()
                if doc_actual.exists:
                    datos = doc_actual.to_dict()
                    estado_actual = datos.get("estado", "En Recepción")

                    if estado_actual in ["En Recepción", "Coordinando"]:
                        st.info("⏳ **En proceso de coordinación.** Aguarde la confirmación de su reunión.")
                    elif estado_actual == "Adentro":
                        st.error("🚨 **ACCESO AUTORIZADO:** Tiene 2 minutos para llegar a la oficina.", icon="✅")
                    elif estado_actual == "Rechazado":
                        st.error("❌ **ATENCIÓN NO DISPONIBLE:** Agende su visita para otra jornada.")
                    elif estado_actual == "Finalizado":
                        st.success("✅ Su visita ha concluido. Gracias por visitar la IMLS.")

                    if st.button("🔄 Actualizar / Finalizar Visita", use_container_width=True):
                        if estado_actual in ["Rechazado", "Finalizado"]: st.session_state["mi_visita_id"] = None
                        st.rerun()

# ==========================================
# 6. MODO 2: PANEL DE GUARDIA
# ==========================================
elif modo_vista == "🛡️ Panel de Guardia":
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
    else:
        st.sidebar.success("✅ Sesión Activa")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state["autenticado"] = False
            st.rerun()

        col_t, col_b = st.columns([3, 1])
        col_t.markdown("## 🛡️ Central de Coordinación y Acceso")
        if col_b.button("🔄 Actualizar Panel", use_container_width=True): st.rerun()
        
        recinto_filtro = st.selectbox("📍 Filtrar por Recinto", ["TODOS LA SERENA"] + RECINTOS_IMLS)
        st.divider()

        c_esp, c_coo, c_ade, c_rec = st.columns(4)
        c_esp.markdown("### 🛋️ Solicitudes")
        c_coo.markdown("### ⏳ Coordinando")
        c_ade.markdown("### ✅ Adentro")
        c_rec.markdown("### 🚫 Rechazado")

        if db:
            docs = db.collection("bitacora_consistorial").order_by("fecha_hora", direction=firestore.Query.DESCENDING).limit(100).stream()
            for doc in docs:
                v = doc.to_dict()
                id_d = doc.id
                est = v.get("estado", "En Recepción")
                recinto_actual = v.get("recinto", "Registro Antiguo")
                
                if recinto_filtro != "TODOS LA SERENA" and recinto_actual != recinto_filtro and recinto_actual != "Registro Antiguo": 
                    continue
                
                perfil = v.get("perfil_visitante", "Ciudadano")
                empresa_tag = f"<br><small style='color:#2B6CB0;'>🏢 {v.get('empresa_institucion')}</small>" if v.get("empresa_institucion") else ""
                
                try: h_in = v["fecha_hora"].astimezone(tz_chile).strftime("%H:%M")
                except: h_in = "--:--"
                
                t_html = f'<div class="tarjeta-visita"><b>{v.get("nombre","")}</b> <span style="font-size:0.8em; color:gray;">({perfil})</span>{empresa_tag}<br><small>📍 {recinto_actual}</small><br><small>🎯 {v.get("departamento","")} | Ingreso: 🕒 {h_in}</small></div>'
                
                if est == "En Recepción":
                    with c_esp:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Coordinar", key=f"c_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Coordinando"}); st.rerun()
                elif est == "Coordinando":
                    with c_coo:
                        st.markdown(t_html, unsafe_allow_html=True)
                        c1, c2 = st.columns(2)
                        if c1.button("Autorizar", key=f"a_{id_d}", type="primary"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Adentro", "hora_autorizacion": datetime.now(tz_chile)}); st.rerun()
                        if c2.button("Rechazar", key=f"r_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Rechazado", "hora_salida": datetime.now(tz_chile)}); st.rerun()
                elif est == "Adentro":
                    with c_ade:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Marcar Salida", key=f"s_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Finalizado", "hora_salida": datetime.now(tz_chile)}); st.rerun()
                elif est == "Rechazado":
                    with c_rec: st.markdown(t_html, unsafe_allow_html=True)

# ==========================================
# 7. MODO 3: BIG DATA & INTELIGENCIA (BI ENRIQUECIDO)
# ==========================================
elif modo_vista == "📊 Big Data & Inteligencia":
    st.markdown("## 📊 Centro de Inteligencia y Big Data IMLS")
    st.markdown("Análisis avanzado del comportamiento de visitas, tiempos de respuesta y mapeo institucional de La Serena.")
    
    if db:
        with st.spinner("Procesando matriz de datos municipales..."):
            docs = db.collection("bitacora_consistorial").stream()
            lista_v = [d.to_dict() for d in docs]
            
            if lista_v:
                df = pd.DataFrame(lista_v)
                
                # --- ESCUDO DE NORMALIZACIÓN DE DATOS ANTIGUOS ---
                # Previene colapsos si hay registros guardados antes de la actualización
                columnas_nuevas = ['recinto', 'perfil_visitante', 'empresa_institucion', 'departamento', 'estado', 'nombre']
                for col in columnas_nuevas:
                    if col not in df.columns:
                        df[col] = "Registro Antiguo"
                # --------------------------------------------------
                
                # Limpieza y preparación de Timestamps
                if 'fecha_hora' in df.columns: df['fecha_hora'] = pd.to_datetime(df['fecha_hora'], utc=True).dt.tz_convert(tz_chile)
                if 'hora_autorizacion' in df.columns: df['hora_autorizacion'] = pd.to_datetime(df['hora_autorizacion'], utc=True).dt.tz_convert(tz_chile)
                if 'hora_salida' in df.columns: df['hora_salida'] = pd.to_datetime(df['hora_salida'], utc=True).dt.tz_convert(tz_chile)
                
                # Cálculos de Inteligencia de Tiempos
                if 'hora_autorizacion' in df.columns and 'fecha_hora' in df.columns:
                    df['espera_lobby_min'] = (df['hora_autorizacion'] - df['fecha_hora']).dt.total_seconds() / 60.0
                else: df['espera_lobby_min'] = np.nan
                
                if 'hora_salida' in df.columns and 'hora_autorizacion' in df.columns:
                    df['reunion_efectiva_min'] = (df['hora_salida'] - df['hora_autorizacion']).dt.total_seconds() / 60.0
                else: df['reunion_efectiva_min'] = np.nan
                
                # Extracción de la hora para mapa de calor
                if 'fecha_hora' in df.columns:
                    df['hora_del_dia'] = df['fecha_hora'].dt.hour
                else:
                    df['hora_del_dia'] = 0
                
                df_finalizados = df[df['estado'] == 'Finalizado'].copy()
                
                # TABS DE NAVEGACIÓN ANALÍTICA
                tab1, tab2, tab3 = st.tabs(["📈 Visión General y Flujo", "🏢 Inteligencia Organizacional", "⏱️ Rendimiento de Tiempos (SLA)"])
                
                with tab1:
                    st.markdown("### 🚦 Flujo Integral de Recintos")
                    k1, k2, k3, k4 = st.columns(4)
                    k1.markdown(f"<div class='kpi-card'><h3>{len(df)}</h3><p>Total Registros Históricos</p></div>", unsafe_allow_html=True)
                    k2.markdown(f"<div class='kpi-card'><h3>{len(df[df['estado'] == 'Adentro'])}</h3><p>Personas Adentro Ahora</p></div>", unsafe_allow_html=True)
                    tasa_rec = (len(df[df['estado'] == 'Rechazado']) / len(df)) * 100 if len(df)>0 else 0
                    k3.markdown(f"<div class='kpi-card'><h3>{tasa_rec:.1f}%</h3><p>Tasa de Rechazo</p></div>", unsafe_allow_html=True)
                    
                    # Cálculo seguro del TOP 1
                    if not df['recinto'].empty and len(df['recinto'].dropna()) > 0:
                        top_recinto = df['recinto'].mode()[0]
                    else:
                        top_recinto = "N/A"
                    
                    k4.markdown(f"<div class='kpi-card'><h3>Top 1</h3><p>{top_recinto}</p></div>", unsafe_allow_html=True)
                    
                    st.write("")
                    c1, c2 = st.columns([2,1])
                    with c1:
                        st.markdown("#### 🔥 Horas Punta de Visitas (Mapa de Demanda)")
                        flujo_hora = df['hora_del_dia'].value_counts().sort_index()
                        st.line_chart(flujo_hora)
                    with c2:
                        st.markdown("#### 🏢 Tráfico por Recinto")
                        st.bar_chart(df['recinto'].value_counts(), color="#DD6B20")

                with tab2:
                    st.markdown("### 🧬 Análisis de Perfil de Visitantes y Relaciones (CRM)")
                    c3, c4 = st.columns(2)
                    with c3:
                        st.markdown("#### Distribución de Perfiles")
                        st.bar_chart(df['perfil_visitante'].value_counts(), color="#319795")
                    with c4:
                        st.markdown("#### 🏢 Top Instituciones / Empresas Frecuentes")
                        empresas_limpias = df[(df['empresa_institucion'].notna()) & (df['empresa_institucion'] != "") & (df['empresa_institucion'] != "Registro Antiguo")]
                        top_empresas = empresas_limpias['empresa_institucion'].value_counts().head(10)
                        if not top_empresas.empty:
                            st.dataframe(top_empresas.rename("Visitas Generadas"), use_container_width=True)
                        else:
                            st.info("No hay registros de empresas aún.")
                    
                    st.divider()
                    st.markdown("#### Demanda por Unidad/Departamento Destino")
                    st.bar_chart(df['departamento'].value_counts(), color="#805AD5")

                with tab3:
                    st.markdown("### ⏱️ Control de SLAs y Eficiencia de Atención")
                    st.caption("Métricas basadas únicamente en visitas procesadas y finalizadas.")
                    
                    if not df_finalizados.empty and 'espera_lobby_min' in df_finalizados.columns and not df_finalizados['espera_lobby_min'].isna().all():
                        espera_promedio = df_finalizados['espera_lobby_min'].mean()
                        reunion_promedio = df_finalizados['reunion_efectiva_min'].mean()
                        
                        col_sla1, col_sla2 = st.columns(2)
                        col_sla1.metric("⏳ Promedio de Espera en Lobby", f"{espera_promedio:.1f} minutos", "Recepción a Autorización", delta_color="off")
                        col_sla2.metric("🤝 Promedio de Reunión Efectiva", f"{reunion_promedio:.1f} minutos", "Autorización a Salida", delta_color="off")
                        
                        st.write("")
                        st.markdown("#### ⌛ Cuellos de botella: Departamentos que más hacen esperar en Lobby")
                        espera_deptos = df_finalizados.groupby('departamento')['espera_lobby_min'].mean().sort_values(ascending=False)
                        st.bar_chart(espera_deptos, color="#E53E3E")
                    else:
                        st.info("Se requiere procesar ciclos completos de visitas (Autorizar -> Finalizar) para medir la inteligencia de tiempos.")
            else:
                st.info("La matriz de Big Data se encenderá cuando ingrese el primer registro en el sistema.")
