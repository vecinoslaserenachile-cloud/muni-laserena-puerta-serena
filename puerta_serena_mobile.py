import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURACIÓN DEL PORTAL
# ==========================================
st.set_page_config(page_title="La Serena SmartCity", page_icon="🌐", layout="wide")

# ==========================================
# 2. MOTOR GRÁFICO (ELEGANCIA Y RESPONSIVIDAD)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    
    a { text-decoration: none !important; }
    
    .metro-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        /* Altura base mayor y capacidad de expandirse si el texto es muy largo */
        grid-auto-rows: minmax(180px, auto); 
        gap: 18px;
        padding: 20px 0;
    }
    
    .metro-tile {
        color: white !important;
        padding: 22px;
        border-radius: 12px;
        font-family: 'Segoe UI', sans-serif;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.1);
        height: 100%; /* Asegura que usen todo el espacio disponible */
    }
    
    .metro-tile * { text-decoration: none !important; color: white !important; }
    
    a.metro-tile:hover {
        transform: scale(1.02) translateY(-4px);
        box-shadow: 0 15px 25px rgba(0,0,0,0.2);
        filter: brightness(1.1);
    }
    
    /* Baldosas en desarrollo: Más opacas y apagadas */
    .disabled-tile {
        cursor: default;
        opacity: 0.5; 
        filter: grayscale(50%); 
    }
    
    /* TEXTOS AUMENTADOS */
    .tile-icon { font-size: 2.6em; margin-bottom: 5px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2); }
    .tile-title { font-weight: 700; font-size: 1.4em; line-height: 1.2; margin-bottom: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.2); }
    .tile-subtitle { font-size: 0.95em; opacity: 0.95; font-weight: 400; line-height: 1.3; }
    
    .bg-alcaldia { background: linear-gradient(135deg, #1A365D 0%, #2B6CB0 100%); } 
    .bg-radio { background: linear-gradient(135deg, #C53030 0%, #E53E3E 100%); } 
    .bg-turismo { background: linear-gradient(135deg, #C05621 0%, #ED8936 100%); } 
    .bg-educacion { background: linear-gradient(135deg, #2B6CB0 0%, #4299E1 100%); } 
    .bg-transito { background: linear-gradient(135deg, #285E61 0%, #38B2AC 100%); } 
    .bg-vecinos { background: linear-gradient(135deg, #276749 0%, #48BB78 100%); } 
    .bg-orange { background: linear-gradient(135deg, #9C4221 0%, #DD6B20 100%); }
    .bg-purple { background: linear-gradient(135deg, #553C9A 0%, #805AD5 100%); }
    .bg-teal { background: linear-gradient(135deg, #234E52 0%, #319795 100%); }
    .bg-darkred { background: linear-gradient(135deg, #742A2A 0%, #9B2C2C 100%); }
    .bg-eco { background: linear-gradient(135deg, #22543D 0%, #38A169 100%); } 
    .bg-blue-neon { background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%); border: 1px solid #00ffcc;}
    .bg-art { background: linear-gradient(135deg, #D53F8C 0%, #B83280 100%); }
    
    /* REGLAS INTACTAS PARA ESCRITORIO */
    .logo-muni { width: 100%; object-fit: contain; }
    .logo-inno-desktop { width: 100%; object-fit: contain; }
    .logo-inno-mobile { display: none; } 
    .qr-wrapper { display: flex; flex-direction: column; align-items: flex-start; }
    .qr-wrapper img { width: 120px; }
    
    .main-title {
        color: #2D3748; 
        margin-bottom: 0; 
        text-align: center; 
        font-size: 3.2em;
    }

    /* Estabilidad en Tablets */
    @media (max-width: 1024px) {
        .metro-grid { grid-template-columns: repeat(2, 1fr); }
    }
    
    /* CIRUGÍA EXCLUSIVA PARA CELULARES (Móvil) */
    @media (max-width: 768px) {
        .metro-grid { grid-template-columns: 1fr; grid-auto-rows: auto; }
        .metro-tile { min-height: 160px; } 
        
        .logo-muni { width: 45%; display: block; margin: 0 auto; }
        
        .main-title {
            color: #E53E3E !important; 
            font-size: 1.7em !important; 
            white-space: nowrap !important; 
            margin-top: 15px !important;
        }
        
        .logo-inno-desktop { display: none; }
        .logo-inno-mobile { 
            display: block; 
            width: 360px !important; 
            max-width: 90%; 
            margin: 40px auto 20px auto; 
            object-fit: contain; 
        }
        
        .qr-wrapper { align-items: center; margin-top: 10px; margin-bottom: 25px; width: 100%; text-align: center; }
        .qr-wrapper img { width: 170px !important; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. CABECERA: ENLACES RAW CON TRUCO ANTI-CACHÉ (?v=1)
# ==========================================
col_logo1, col_logo2, col_texto, col_qr = st.columns([1.2, 1.2, 6, 1.5])

with col_logo1:
    st.markdown('<img src="https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_muni.png?v=1" class="logo-muni">', unsafe_allow_html=True)

with col_logo2:
    st.markdown('<img src="https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_innovacion.png?v=1" class="logo-inno-desktop">', unsafe_allow_html=True)

with col_texto:
    st.markdown("<h1 class='main-title'>La Serena SmartCity</h1>", unsafe_allow_html=True)
    
    reloj_html = """
    <div id="reloj_smart" style="font-family: 'Segoe UI', sans-serif; font-size: 1.1em; color: #4A5568; text-align: center; font-weight: 500; margin-top: 5px;"></div>
    <script>
    function actualizarReloj() {
        var hoy = new Date();
        var opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
        var fecha = hoy.toLocaleDateString('es-CL', opciones);
        var hora = hoy.toLocaleTimeString('es-CL');
        fecha = fecha.charAt(0).toUpperCase() + fecha.slice(1);
        document.getElementById('reloj_smart').innerHTML = '📍 La Serena | ' + fecha + '<br>🕒 ' + hora;
    }
    setInterval(actualizarReloj, 1000);
    actualizarReloj();
    </script>
    """
    components.html(reloj_html, height=75)

with col_qr:
    qr_html = """
    <div class="qr-wrapper">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https://app-smartcity-imls.streamlit.app/">
        <p style='font-size: 0.85em; color: #4A5568; font-weight: bold; margin-top: 5px; margin-bottom: 0;'>📱 Escanea y Entra</p>
    </div>
    """
    st.markdown(qr_html, unsafe_allow_html=True)

st.divider()

# ==========================================
# 4. CONSTRUCCIÓN DEL MOSAICO HTML
# ==========================================
mosaico_html = """
<div class="metro-grid">

<a href="https://puertaserena.streamlit.app/" target="_blank" class="metro-tile bg-alcaldia">
<div><div class="tile-icon">🏛️</div><div class="tile-title">Control Acceso Visitas</div></div>
<div class="tile-subtitle">Red de Recintos Municipales | I.M. La Serena</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/serenito-app/" target="_blank" class="metro-tile bg-turismo">
<div><div class="tile-icon">🎭</div><div class="tile-title">Eventos y Protocolos</div></div>
<div class="tile-subtitle">Gestión interna de eventos, protocolo y relaciones públicas.</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/RDMLS/" target="_blank" class="metro-tile bg-radio">
<div><div class="tile-icon">📻</div><div class="tile-title">Plataforma RDMLS</div></div>
<div class="tile-subtitle">Portal interactivo de la Radio Digital Municipal La Serena.</div>
</a>

<a href="https://az11.yesstreaming.net/public/radio-digital-municipal-la-serena" target="_blank" class="metro-tile bg-darkred">
<div><div class="tile-icon">🎧</div><div class="tile-title">Señal Radial en Vivo</div></div>
<div class="tile-subtitle">Escucha la transmisión directa de la RDMLS.</div>
</a>

<a href="https://vecinoslaserenachile-cloud.github.io/portal-induccion-imls/" target="_blank" class="metro-tile bg-educacion">
<div><div class="tile-icon">🎓</div><div class="tile-title">Portal de Inducción</div></div>
<div class="tile-subtitle">Capacitación y recursos formativos IMLS.</div>
</a>

<a href="https://honorarios-ls-me.streamlit.app/" target="_blank" class="metro-tile bg-teal">
<div><div class="tile-icon">💼</div><div class="tile-title">Gestión de Honorarios</div></div>
<div class="tile-subtitle">Plataforma administrativa de servicios a honorarios.</div>
</a>

<a href="https://monitor-laserena.streamlit.app/" target="_blank" class="metro-tile bg-purple">
<div><div class="tile-icon">📡</div><div class="tile-title">Sentinel: Monitor Social</div></div>
<div class="tile-subtitle">Escucha digital y tendencias en redes.</div>
</a>

<a href="https://redvecinos-smart-imls.web.app/" target="_blank" class="metro-tile bg-blue-neon">
<div><div class="tile-icon">🛡️</div><div class="tile-title">Acceso Municipal - Fiscalización</div></div>
<div class="tile-subtitle">Portal exclusivo para funcionarios y Centro de Gestión.</div>
</a>

<a href="https://redvecinos-smart-imls.web.app/#/fiscalizacion" target="_blank" class="metro-tile bg-vecinos">
<div><div class="tile-icon">📱</div><div class="tile-title">Nueva Alerta de Seguridad</div></div>
<div class="tile-subtitle">Formulario de reporte in situ para recintos privados.</div>
</a>


<div class="metro-tile bg-orange disabled-tile">
<div><div class="tile-icon">🚧</div><div class="tile-title">Monitor Vial y Tránsito</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 1.05em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Georeferenciación de baches, luminarias y vehículos.</div>
</div>
</div>

<div class="metro-tile bg-eco disabled-tile">
<div><div class="tile-icon">🌱</div><div class="tile-title">Cuidado Ambiental</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 1.05em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Protección de humedales y entorno ecológico.</div>
</div>
</div>

<div class="metro-tile bg-transito disabled-tile">
<div><div class="tile-icon">🚰</div><div class="tile-title">Servicios Básicos</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 1.05em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Control de agua, alcantarillado, redes eléctricas y telecomunicaciones.</div>
</div>
</div>

<div class="metro-tile bg-art disabled-tile">
<div><div class="tile-icon">🎨</div><div class="tile-title">Cultura y Arte Urbano</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 1.05em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Música, artes escénicas, grafiti y expresiones urbanas.</div>
</div>
</div>

<div class="metro-tile bg-turismo disabled-tile">
<div><div class="tile-icon">🧘‍♀️</div><div class="tile-title">Deportes y Bienestar</div></div>
<div>
    <div class="tile-subtitle" style="color: #FFD700 !important; font-weight: bold; font-size: 1.05em;">⏳ Próximamente integrado...</div>
    <div class="tile-subtitle" style="margin-top: 4px;">Plataforma interactiva de yoga, fitness, wellness y actividades deportivas.</div>
</div>
</div>

</div>
"""

st.markdown(mosaico_html, unsafe_allow_html=True)

st.write("")
st.divider()

# ==========================================
# 5. FOOTER: LOGO MÓVIL Y TEXTO
# ==========================================
st.caption("Seleccione un servicio para ingresar. Plataforma centralizada de la Ilustre Municipalidad de La Serena.")

st.markdown('<img src="https://raw.githubusercontent.com/vecinoslaserenachile-cloud/portal-smartcity-imls/main/logo_innovacion.png?v=1" class="logo-inno-mobile">', unsafe_allow_html=True)
