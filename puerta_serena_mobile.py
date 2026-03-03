import streamlit as st
from datetime import datetime
import pytz
import json
import base64
import random
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# ==========================================
# 1. CONFIGURACIÓN GENERAL Y HORA CHILE
# ==========================================
st.set_page_config(page_title="Control de Acceso | I.M. La Serena", page_icon="🏛️", layout="wide", initial_sidebar_state="expanded")

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
                              ["📱 Acceso Ciudadano (QR)", "🛡️ Panel de Guardia", "📊 Reportes Institucionales"])
st.sidebar.divider()

# ==========================================
# 5. MODO 1: TÓTEM PÚBLICO / CELULAR CIUDADANO
# ==========================================
if modo_vista == "📱 Acceso Ciudadano (QR)":
    col_v1, col_centro, col_v2 = st.columns([1, 2, 1])
    with col_centro:
        st.markdown('<div style="text-align: center; font-size: 50px; margin-bottom: -20px;">🏛️</div>', unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: #333;'>Registro de Visitas</h2>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: #666; margin-top: -10px;'>Edificio Consistorial IMLS</h5>", unsafe_allow_html=True)
        st.divider()

        with st.form("registro_consistorial"):
            st.info("💡 **Dato de Seguridad:** Tenga su Cédula de Identidad a mano.")
            
            col_rut, col_serie = st.columns(2)
            with col_rut:
                rut = st.text_input("RUT (Sin puntos y con guion)", placeholder="Ej: 12345678-9", max_chars=10)
            with col_serie:
                num_serie = st.text_input("Nº de Documento (Serie)", placeholder="Ej: A12345678", max_chars=15)
                
            nombre = st.text_input("Nombre Completo")
            depto = st.selectbox("Unidad de Destino", [
                "Alcaldía", "Administración Municipal", "Gabinete", "Oficina de Partes", 
                "Comunicaciones", "Prensa", "Relaciones Públicas", "Eventos", "Patrocinios",
                "Secretaría Municipal", "DIDECO", "Obras (DOM)", "Rentas", "Jurídico", "Control"
            ])
            motivo = st.text_area("Motivo de la Visita", max_chars=150)
            
            submit = st.form_submit_button("VALIDAR Y ANUNCIAR LLEGADA", use_container_width=True)

            if submit:
                if db and rut and num_serie and nombre and motivo:
                    with st.spinner("Anunciando su llegada a recepción..."):
                        try:
                            ahora_chile = datetime.now(tz_chile)
                            db.collection("bitacora_consistorial").add({
                                "rut": rut, 
                                "numero_serie": num_serie,
                                "nombre": nombre, 
                                "departamento": depto,
                                "motivo": motivo, 
                                "fecha_hora": ahora_chile,
                                "estado": "En Recepción" 
                            })
                            
                            # MOTOR DE MENSAJES CÁLIDOS Y ROTATIVOS
                            mensajes_bienvenida = [
                                # Mensaje 1: Plaza de Armas
                                """
                                <div style="background-color: #F0F8FF; padding: 40px; border-radius: 15px; border: 3px solid #FFD700; text-align: center; box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-top: 20px;">
                                    <div style="font-size: 80px; margin-bottom: 10px;">🙋‍♂️</div>
                                    <h2 style="color: #003366; font-size: 34px; margin-bottom: 25px;">¡Registro Exitoso!</h2>
                                    <p style="font-size: 26px; color: #333; line-height: 1.5; font-weight: 500;">
                                        Vecino/a, estamos gestionando su atención. Le rogamos esperar unos momentos mientras confirmamos su ingreso con el departamento.<br><br>
                                        Si dispone de tiempo, le invitamos a contemplar nuestra hermosa <b>Plaza de Armas</b> o realizar algún trámite rápido por el sector.<br><br>
                                        <b style="color: #D32F2F; font-size: 28px;">Eso sí, ¡le pedimos estar muy atento a nuestro aviso en esta pantalla! Muchas gracias por su visita.</b>
                                    </p>
                                </div>
                                """,
                                # Mensaje 2: Casco Histórico
                                """
                                <div style="background-color: #F9FBE7; padding: 40px; border-radius: 15px; border: 3px solid #8BC34A; text-align: center; box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-top: 20px;">
                                    <div style="font-size: 80px; margin-bottom: 10px;">🌳</div>
                                    <h2 style="color: #33691E; font-size: 34px; margin-bottom: 25px;">¡Su llegada ha sido anunciada!</h2>
                                    <p style="font-size: 26px; color: #333; line-height: 1.5; font-weight: 500;">
                                        Nuestro equipo ya está coordinando su atención. La espera podría tomar algunos minutos.<br><br>
                                        Si gusta, puede aprovechar de recorrer el encanto de nuestro <b>Casco Histórico</b> mientras aguarda.<br><br>
                                        <b style="color: #D32F2F; font-size: 28px;">Le notificaremos su autorización por este mismo medio. ¡Agradecemos enormemente su paciencia!</b>
                                    </p>
                                </div>
                                """,
                                # Mensaje 3: Arquitectura / Descanso
                                """
                                <div style="background-color: #FFF3E0; padding: 40px; border-radius: 15px; border: 3px solid #FF9800; text-align: center; box-shadow: 0 8px 16px rgba(0,0,0,0.2); margin-top: 20px;">
                                    <div style="font-size: 80px; margin-bottom: 10px;">🏛️</div>
                                    <h2 style="color: #E65100; font-size: 34px; margin-bottom: 25px;">¡Datos recibidos correctamente!</h2>
                                    <p style="font-size: 26px; color: #333; line-height: 1.5; font-weight: 500;">
                                        Mientras el departamento confirma su disponibilidad, le invitamos a tomar asiento o admirar la bella <b>arquitectura colonial</b> de nuestro recinto.<br><br>
                                        Nos pondremos en contacto con usted a la brevedad.<br><br>
                                        <b style="color: #D32F2F; font-size: 28px;">Por favor, manténgase atento a esta pantalla para su confirmación de acceso. ¡Es un gusto recibirle!</b>
                                    </p>
                                </div>
                                """
                            ]
                            
                            mensaje_elegido = random.choice(mensajes_bienvenida)
                            st.markdown(mensaje_elegido, unsafe_allow_html=True)
                            
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    st.warning("⚠️ Complete todos los campos solicitados, incluyendo el Número de Documento.")

# ==========================================
# 6. MODO 2: PANEL DE GUARDIA (CON LOGIN)
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
        st.warning("🔒 Ingrese sus credenciales institucionales.")

    elif modo_vista == "🛡️ Panel de Guardia":
        st.sidebar.success("✅ Sesión Activa")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state["autenticado"] = False
            st.rerun()

        col_t, col_b = st.columns([4, 1])
        col_t.markdown("## 🛡️ Central de Coordinación y Acceso")
        if col_b.button("🔄 Actualizar Panel"): st.rerun()
        st.divider()

        c_esp, c_coo, c_ade, c_rec = st.columns(4)
        c_esp.markdown("### 🛋️ Solicitudes")
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
                
                if "fecha_hora" in v:
                    try:
                        hora_lectura = v["fecha_hora"].astimezone(tz_chile)
                        h_in = hora_lectura.strftime("%H:%M")
                    except:
                        h_in = v["fecha_hora"].strftime("%H:%M")
                else:
                    h_in = "--:--"
                
                doc_verificado = f"📄 Doc: {v.get('numero_serie', 'N/A')}"
                t_html = f'<div class="tarjeta-visita"><b>{v.get("nombre","")}</b><br><small>🏢 {v.get("departamento","")} | 🕒 {h_in}</small><br><small style="color:green;">{doc_verificado}</small></div>'
                
                if est == "En Recepción":
                    with c_esp:
                        st.markdown(t_html, unsafe_allow_html=True)
                        c1, c2 = st.columns(2)
                        if c1.button("Coordinar", key=f"c_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Coordinando"}); st.rerun()
                        if c2.button("Rechazar", key=f"r_{id_d}", type="primary"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Rechazado", "hora_salida": datetime.now(tz_chile)}); st.rerun()
                            
                elif est == "Coordinando":
                    with c_coo:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Autorizar", key=f"a_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Adentro"}); st.rerun()
                            
                elif est == "Adentro":
                    with c_ade:
                        st.markdown(t_html, unsafe_allow_html=True)
                        if st.button("Salida", key=f"s_{id_d}"):
                            db.collection("bitacora_consistorial").document(id_d).update({"estado":"Finalizado", "hora_salida": datetime.now(tz_chile)}); st.rerun()
                            
                elif est == "Rechazado":
                    with c_rec:
                        st.markdown(t_html, unsafe_allow_html=True)
                        st.caption("Agendar cita digital.")
                        
                elif est == "Finalizado": 
                    registro_seguro = {
                        "nombre": v.get("nombre", "Sin registro"),
                        "rut": v.get("rut", "Sin registro"),
                        "numero_serie": v.get("numero_serie", "N/A"),
                        "departamento": v.get("departamento", "Sin registro"),
                        "hora_ingreso": h_in
                    }
                    historico.append(registro_seguro)
            
            st.divider()
            st.markdown("### 📋 Bitácora de Salidas")
            if historico: 
                df_historico = pd.DataFrame(historico)
                df_mostrar = df_historico[["nombre", "rut", "numero_serie", "departamento", "hora_ingreso"]].copy()
                df_mostrar = df_mostrar.rename(columns={
                    "nombre": "Nombre Completo", "rut": "RUT", "numero_serie": "Nº Doc", "departamento": "Destino", "hora_ingreso": "Hora Ingreso"
                })
                st.dataframe(df_mostrar, use_container_width=True)

    # ==========================================
    # 7. MODO 3: REPORTES CON INTELIGENCIA (BI)
    # ==========================================
    elif modo_vista == "📊 Reportes Institucionales":
        st.sidebar.success("✅ Sesión Activa")
        if st.sidebar.button("Cerrar Sesión"):
            st.session_state["autenticado"] = False
            st.rerun()
            
        st.markdown("## 📊 Inteligencia de Datos: Flujo de Ciudadanos")
        st.markdown("Evaluación de atención basada en SLA global (Service Level Agreement) de la administración pública.")
        st.divider()
        
        if db:
            with st.spinner("Analizando histórico de visitas bajo estándares de Smart City..."):
                docs = db.collection("bitacora_consistorial").stream()
                lista_v = [d.to_dict() for d in docs]
                
                if lista_v:
                    df = pd.DataFrame(lista_v)
                    
                    if 'fecha_hora' in df.columns:
                        df['fecha_hora'] = pd.to_datetime(df['fecha_hora'], utc=True).dt.tz_convert(tz_chile)
                    
                    if 'hora_salida' in df.columns:
                        df['hora_salida'] = pd.to_datetime(df['hora_salida'], utc=True).dt.tz_convert(tz_chile)
                        df['minutos_adentro'] = (df['hora_salida'] - df['fecha_hora']).dt.total_seconds() / 60.0
                    else:
                        df['minutos_adentro'] = pd.NA
                    
                    df_completados = df[df['estado'] == 'Finalizado'].copy()
                    rechazados = len(df[df['estado'] == 'Rechazado'])
                    total_solicitudes = len(df)
                    tasa_rechazo = (rechazados / total_solicitudes) * 100 if total_solicitudes > 0 else 0
                    
                    st.markdown("### ⏱️ Indicadores Clave de Rendimiento (KPIs)")
                    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
                    kpi1.metric("Total Solicitudes", total_solicitudes)
                    kpi2.metric("Tasa de Rechazos", f"{tasa_rechazo:.1f}%", "- Objetivo: < 10%", delta_color="inverse")
                    
                    if not df_completados.empty and 'minutos_adentro' in df_completados.columns:
                        tiempo_promedio = df_completados['minutos_adentro'].mean()
                        kpi3.metric("Tiempo Promedio Atención", f"{tiempo_promedio:.0f} min", "SLA Global: 30 min", delta_color="inverse" if tiempo_promedio > 30 else "normal")
                        max_tiempo = df_completados['minutos_adentro'].max()
                        kpi4.metric("Máximo Tiempo Registrado", f"{max_tiempo:.0f} min")
                    else:
                        kpi3.metric("Tiempo Promedio Atención", "N/A", "Faltan datos de salida")
                        kpi4.metric("Máximo Tiempo Registrado", "N/A")

                    st.write("")
                    st.divider()

                    col_g1, col_g2 = st.columns(2)
                    with col_g1:
                        st.markdown("#### 🚦 Tasa de Aprobación vs Rechazo")
                        if 'estado' in df.columns:
                            distribucion_estado = df['estado'].value_counts()
                            st.bar_chart(distribucion_estado, color="#FFD700")
                        else:
                            st.info("Aún no hay estados definidos.")
                            
                    with col_g2:
                        st.markdown("#### 🏢 Volumen de Visitas por Departamento")
                        if 'departamento' in df.columns:
                            st.bar_chart(df['departamento'].value_counts())
                        else:
                            st.info("Aún no hay datos de departamentos.")
                    
                    st.write("")
                    col_g3, col_g4 = st.columns(2)
                    
                    with col_g3:
                        st.markdown("#### ⏳ Tiempos Promedio por Departamento (Minutos)")
                        if not df_completados.empty and 'minutos_adentro' in df_completados.columns:
                            tiempo_depto = df_completados.groupby('departamento')['minutos_adentro'].mean()
                            st.bar_chart(tiempo_depto)
                        else:
                            st.info("Se requiere marcar salidas ('Finalizado') para calcular tiempos promedios.")

                    with col_g4:
                        st.markdown("#### 🏆 Extremos de Atención (Visitas Finalizadas)")
                        if not df_completados.empty and 'minutos_adentro' in df_completados.columns:
                            df_sorted = df_completados.sort_values(by='minutos_adentro', ascending=False)
                            
                            st.caption("🔴 Visitas más largas (Mayor permanencia)")
                            top_largas = df_sorted[['nombre', 'departamento', 'minutos_adentro']].head(3)
                            top_largas['minutos_adentro'] = top_largas['minutos_adentro'].apply(lambda x: f"{x:.0f} min")
                            st.dataframe(top_largas, use_container_width=True, hide_index=True)
                            
                            st.caption("🟢 Visitas más veloces (Menor permanencia)")
                            top_cortas = df_sorted[['nombre', 'departamento', 'minutos_adentro']].tail(3)
                            top_cortas['minutos_adentro'] = top_cortas['minutos_adentro'].apply(lambda x: f"{x:.0f} min")
                            st.dataframe(top_cortas, use_container_width=True, hide_index=True)
                        else:
                            st.info("Aún no hay visitas finalizadas con hora de salida.")
                            
                else:
                    st.info("No hay datos suficientes para generar reportes aún. Registre visitas y marque salidas.")
