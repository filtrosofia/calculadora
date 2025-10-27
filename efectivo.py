import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# Configurar página con favicon

st.set_page_config(
page_title=“Calculadora Wallet Cambios”,
layout=“centered”,
page_icon=“https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png”
)

# Número de WhatsApp

WHATSAPP_NUMBER = “584146108166”

# Inicializar session state para montos rápidos

if ‘monto_calc1’ not in st.session_state:
st.session_state.monto_calc1 = 0.0
if ‘monto_calc2’ not in st.session_state:
st.session_state.monto_calc2 = 0.0
if ‘monto_calc3’ not in st.session_state:
st.session_state.monto_calc3 = 0.0
if ‘monto_calc4’ not in st.session_state:
st.session_state.monto_calc4 = 0.0
if ‘monto_calc5’ not in st.session_state:
st.session_state.monto_calc5 = 0.0
if ‘monto_calc5b’ not in st.session_state:
st.session_state.monto_calc5b = 0.0
if ‘monto_calc6’ not in st.session_state:
st.session_state.monto_calc6 = 0.0
if ‘monto_calc6b’ not in st.session_state:
st.session_state.monto_calc6b = 0.0

# Función para crear enlace de WhatsApp con mensaje personalizado

def crear_enlace_whatsapp(mensaje):
mensaje_encoded = urllib.parse.quote(mensaje)
return f”https://wa.me/{WHATSAPP_NUMBER}?text={mensaje_encoded}”

# CSS personalizado - Modo oscuro permanente

st.markdown(”””
<style>
@import url(‘https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@300;400;600&display=swap’);

```
    /* Variables de color - Modo oscuro */
    :root {
        --bg-primary: #0f1419;
        --bg-secondary: #1a2332;
        --bg-card: #253142;
        --text-primary: #ffffff;
        --text-secondary: #b8c5d6;
        --text-muted: #8b98a8;
        --shadow-color: rgba(0,0,0,0.5);
        --azul-brillante: #4BA9C3;
        --azul-medio: #3D9FC2;
        --azul-profundo: #2881AB;
        --naranja-energia: #F36B2D;
        --amarillo-calido: #FFC542;
        --verde-whatsapp: #25D366;
    }
    
    /* Reset Streamlit */
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a2332 100%);
        font-family: 'Open Sans', sans-serif;
        color: var(--text-primary);
    }
    
    /* Logo container */
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    .logo-container img {
        width: clamp(90px, 15vw, 140px);
        filter: drop-shadow(0 4px 8px var(--shadow-color));
        transition: transform 0.3s ease;
    }
    
    .logo-container img:hover {
        transform: scale(1.05);
    }
    
    /* Títulos con jerarquía */
    .titulo-principal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: clamp(1.8rem, 4vw, 2.5rem);
        text-align: center;
        color: var(--azul-brillante);
        margin-bottom: 0.5rem;
        animation: fadeInUp 0.8s ease-out;
        text-shadow: 0 2px 4px var(--shadow-color);
    }
    
    .subtitulo-calculadora {
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: clamp(1.3rem, 3vw, 1.8rem);
        text-align: center;
        color: #4BA9C3;
        margin: 2rem 0 1rem 0;
        padding: 1rem;
        background: rgba(75, 169, 195, 0.15);
        border-radius: 12px;
        border: 2px solid var(--azul-brillante);
    }
    
    .label-campo {
        font-family: 'Open Sans', sans-serif;
        font-weight: 600;
        font-size: clamp(1rem, 2vw, 1.15rem);
        color: var(--text-primary);
        margin: 1.5rem 0 0.5rem 0;
    }
    
    .texto-info {
        text-align: center;
        color: var(--text-secondary);
        font-size: clamp(0.9rem, 1.8vw, 1rem);
        margin: 0.5rem 0;
    }
    
    /* Inputs mejorados */
    .stNumberInput > div > div > input {
        border: 2px solid var(--azul-brillante);
        border-radius: 10px;
        padding: 0.75rem;
        font-size: clamp(1rem, 2vw, 1.1rem);
        transition: all 0.3s ease;
        font-family: 'Open Sans', sans-serif;
        background: var(--bg-card);
        color: var(--text-primary);
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: var(--naranja-energia);
        box-shadow: 0 0 0 3px rgba(243, 107, 45, 0.2);
        outline: none;
    }
    
    /* Resultados con animación */
    .resultado-container {
        background: linear-gradient(135deg, #4BA9C3 0%, #2881AB 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 8px 20px rgba(40, 129, 171, 0.4);
        animation: slideInUp 0.5s ease-out;
    }
    
    .resultado-principal {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: clamp(1.3rem, 3vw, 1.6rem);
        margin-bottom: 0.5rem;
        color: #ffffff;
    }
    
    .resultado-secundario {
        font-family: 'Open Sans', sans-serif;
        font-size: clamp(0.95rem, 2vw, 1.1rem);
        opacity: 0.95;
        color: #ffffff;
    }
    
    /* Botones de monto rápido */
    .montos-rapidos-container {
        text-align: center;
        margin: 1.5rem 0;
    }
    
    .montos-rapidos-label {
        color: var(--text-primary);
        font-weight: 600;
        font-size: clamp(0.9rem, 1.8vw, 1rem);
        margin-bottom: 0.75rem;
        display: block;
    }
    
    /* Información adicional */
    .info-box {
        background: rgba(255, 197, 66, 0.2);
        border-left: 4px solid var(--amarillo-calido);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-family: 'Open Sans', sans-serif;
        font-size: clamp(0.9rem, 1.8vw, 1rem);
        color: var(--text-primary);
    }
    
    .tasa-box {
        text-align: center;
        background: rgba(75, 169, 195, 0.2);
        padding: 1.2rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 2px solid var(--azul-brillante);
    }
    
    .tasa-principal {
        font-size: clamp(1.1rem, 2.5vw, 1.4rem);
        font-weight: 600;
        color: var(--azul-brillante);
        margin-bottom: 0.3rem;
    }
    
    .tasa-secundaria {
        font-size: clamp(0.8rem, 1.5vw, 0.9rem);
        color: var(--text-muted);
    }
    
    /* Botón WhatsApp mejorado */
    .whatsapp-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, #25D366 0%, #20BA5A 100%);
        color: white;
        padding: clamp(0.9rem, 2vw, 1.1rem) clamp(1.5rem, 3vw, 2rem);
        text-align: center;
        text-decoration: none;
        border-radius: 12px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        margin: 1.5rem auto;
        max-width: 350px;
        box-shadow: 0 6px 15px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
        font-size: clamp(0.95rem, 2vw, 1.1rem);
    }
    
    .whatsapp-btn:hover {
        background: linear-gradient(135deg, #20BA5A 0%, #1EA952 100%);
        color: white;
        text-decoration: none;
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(37, 211, 102, 0.5);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: var(--text-muted);
        font-size: clamp(0.9rem, 1.8vw, 1rem);
        padding: 3rem 0 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid rgba(255,255,255,0.1);
    }
    
    .footer strong {
        color: var(--azul-brillante);
    }
    
    /* Animaciones */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Responsive */
    @media screen and (max-width: 1024px) {
        .resultado-container {
            padding: 1.2rem;
        }
    }
    
    @media screen and (max-width: 375px) {
        .logo-container img {
            width: 80px;
        }
        
        .whatsapp-btn {
            padding: 0.7rem 1.2rem;
        }
    }
    
    @media (orientation: landscape) and (max-height: 500px) {
        .logo-container {
            margin-bottom: 1rem;
        }
        
        .subtitulo-calculadora {
            margin: 1rem 0 0.5rem 0;
            padding: 0.5rem;
        }
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilo para botones de Streamlit */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        border: 2px solid var(--azul-brillante);
        background: rgba(75, 169, 195, 0.15);
        color: var(--text-primary);
        font-weight: 600;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
        font-family: 'Montserrat', sans-serif;
    }
    
    .stButton > button:hover {
        background: var(--azul-brillante);
        color: white;
        border-color: var(--azul-brillante);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Forzar que las columnas se mantengan horizontales en móvil */
    [data-testid="column"] {
        flex: 1 1 auto !important;
        min-width: 0 !important;
    }
    
    [data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        gap: 0.5rem !important;
    }
    
    /* Ajustar tamaño de botones en móvil */
    @media screen and (max-width: 640px) {
        .stButton > button {
            padding: 0.5rem 0.3rem;
            font-size: 0.85rem;
        }
    }
</style>
```

“””, unsafe_allow_html=True)

# Logo

st.markdown(”””
<div class="logo-container">
<img src="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png" alt="Wallet Cambios Logo">
</div>
“””, unsafe_allow_html=True)

# Título principal

st.markdown(”<h1 class='titulo-principal'>Calculadora Wallet Cambios</h1>”, unsafe_allow_html=True)

# Info de horario

st.markdown(”””
<div class='info-box'>
<strong>⏰ Horario de atención:</strong> Lunes a Viernes 8:00 AM - 6:00 PM | Sábados 9:00 AM - 1:00 PM
</div>
“””, unsafe_allow_html=True)

# ==================== CALCULADORA DE EFECTIVO ====================

st.markdown(”<h2 class='subtitulo-calculadora'>💵 Calculadora de Efectivo</h2>”, unsafe_allow_html=True)
st.markdown(”<p class='texto-info'>Comisión del <strong>5%</strong> aplicada</p>”, unsafe_allow_html=True)

# Campo 1: Para recibir (USD)

st.markdown(”<div class='label-campo'>📥 ¿Cuánto deseas recibir en efectivo?</div>”, unsafe_allow_html=True)

# Botones de monto rápido para efectivo - CALCULADORA 1

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>”, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
if st.button(”$50”, key=“rapido_50_calc1”):
st.session_state.monto_calc1 = 50.0
st.rerun()
with col2:
if st.button(”$100”, key=“rapido_100_calc1”):
st.session_state.monto_calc1 = 100.0
st.rerun()
with col3:
if st.button(”$200”, key=“rapido_200_calc1”):
st.session_state.monto_calc1 = 200.0
st.rerun()
with col4:
if st.button(”$300”, key=“rapido_300_calc1”):
st.session_state.monto_calc1 = 300.0
st.rerun()

recibir = st.number_input(
“”,
min_value=0.0,
step=1.0,
key=“recibir”,
value=st.session_state.monto_calc1,
help=“Ingresa la cantidad en USD que deseas recibir”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if recibir != st.session_state.monto_calc1:
st.session_state.monto_calc1 = recibir

if recibir > 0:
total_enviar = recibir / (1 - 0.05)
comision = total_enviar - recibir

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>💰 Debes enviar: ${total_enviar:.2f} USD</div>
        <div class='resultado-secundario'>Comisión: ${comision:.2f} | Recibirás: ${recibir:.2f}</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Si envías ${total_enviar:.2f}, recibirás ${recibir:.2f} en efectivo
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${total_enviar:.2f} para recibir ${recibir:.2f} en efectivo"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif recibir < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0”)

st.markdown(”—”)

# Campo 2: Si se envían (USD)

st.markdown(”<div class='label-campo'>📤 ¿Cuánto vas a enviar?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 2

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>”, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
if st.button(”$50”, key=“rapido_50_calc2”):
st.session_state.monto_calc2 = 50.0
st.rerun()
with col2:
if st.button(”$100”, key=“rapido_100_calc2”):
st.session_state.monto_calc2 = 100.0
st.rerun()
with col3:
if st.button(”$200”, key=“rapido_200_calc2”):
st.session_state.monto_calc2 = 200.0
st.rerun()
with col4:
if st.button(”$300”, key=“rapido_300_calc2”):
st.session_state.monto_calc2 = 300.0
st.rerun()

enviados = st.number_input(
“”,
min_value=0.0,
step=1.0,
key=“enviados_manual”,
value=st.session_state.monto_calc2,
help=“Ingresa la cantidad en USD que vas a enviar”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if enviados != st.session_state.monto_calc2:
st.session_state.monto_calc2 = enviados

if enviados > 0:
recibir_estimado = enviados * (1 - 0.05)
comision_enviados = enviados - recibir_estimado

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>💵 Recibirás: ${recibir_estimado:.2f} USD</div>
        <div class='resultado-secundario'>Monto enviado: ${enviados:.2f} | Comisión: ${comision_enviados:.2f}</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Para recibir ${recibir_estimado:.2f}, debes enviar ${enviados:.2f}
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${enviados:.2f} para recibir ${recibir_estimado:.2f}"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif enviados < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0”)

# ==================== CALCULADORA USD A BOLÍVARES ====================

st.markdown(”—”)
st.markdown(”<h2 class='subtitulo-calculadora'>🇻🇪 Calculadora USD a Bolívares</h2>”, unsafe_allow_html=True)

# Cargar tasas desde Google Sheets pública con timeout

sheet_url = “https://docs.google.com/spreadsheets/d/1ig4ihkUIeP7kaaR6yZeyOLF7j38Y_peytGKG6tgkqbw/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN”

try:
df = pd.read_csv(sheet_url, header=None)
tasa_bs = float(df.iloc[1, 12])  # Celda M2 - Tasa Bolívares (fila 2, columna M)
tasa_usd_cop_compra = float(df.iloc[3, 12])  # Celda M4 - Tasa USD a COP COMPRA (fila 4, columna M)
tasa_cop_usd_venta = float(df.iloc[3, 13])  # Celda N4 - Tasa para COP a USD VENTA (fila 4, columna N)

```
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>
            📊 Tasa actual: <span style='color: #F36B2D;'>{tasa_bs:.2f} Bs/USD</span>
        </div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)
```

except Exception as e:
st.error(“⚠️ No pudimos cargar la tasa actual desde nuestro sistema. Por favor, intenta nuevamente en unos momentos o contáctanos directamente por WhatsApp.”)
st.stop()

# Modo 1: De USD a Bs

st.markdown(”<div class='label-campo'>📤 ¿Cuántos USD vas a enviar?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 3

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>”, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
if st.button(”$20”, key=“rapido_20_calc3”):
st.session_state.monto_calc3 = 20.0
st.rerun()
with col2:
if st.button(”$50”, key=“rapido_50_calc3”):
st.session_state.monto_calc3 = 50.0
st.rerun()
with col3:
if st.button(”$100”, key=“rapido_100_calc3”):
st.session_state.monto_calc3 = 100.0
st.rerun()
with col4:
if st.button(”$200”, key=“rapido_200_calc3”):
st.session_state.monto_calc3 = 200.0
st.rerun()
with col5:
if st.button(”$500”, key=“rapido_500_calc3”):
st.session_state.monto_calc3 = 500.0
st.rerun()

usd_enviar2 = st.number_input(
“”,
min_value=0.0,
step=1.0,
key=“usd_enviar”,
value=st.session_state.monto_calc3,
help=“Ingresa la cantidad en USD que vas a enviar”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if usd_enviar2 != st.session_state.monto_calc3:
st.session_state.monto_calc3 = usd_enviar2

if usd_enviar2 > 0:
bs_recibir2 = usd_enviar2 * tasa_bs

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>🇻🇪 Recibirás: {bs_recibir2:,.2f} Bs</div>
        <div class='resultado-secundario'>Envías: ${usd_enviar2:.2f} USD | Tasa: {tasa_bs:.2f} Bs/USD</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Para recibir {bs_recibir2:,.2f} Bs, debes enviar ${usd_enviar2:.2f} USD
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar2:.2f} para recibir {bs_recibir2:.2f} Bs"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif usd_enviar2 < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0”)

st.markdown(”—”)

# Modo 2: De Bs a USD

st.markdown(”<div class='label-campo'>📥 ¿Cuántos Bolívares quieres recibir?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 4

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos (Bs):</div>”, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

# Convertir montos USD a Bs para los botones

montos_bs = [20 * tasa_bs, 50 * tasa_bs, 100 * tasa_bs, 200 * tasa_bs, 500 * tasa_bs]

with col1:
if st.button(f”{montos_bs[0]:,.0f} Bs”, key=“rapido_bs1_calc4”):
st.session_state.monto_calc4 = montos_bs[0]
st.rerun()
with col2:
if st.button(f”{montos_bs[1]:,.0f} Bs”, key=“rapido_bs2_calc4”):
st.session_state.monto_calc4 = montos_bs[1]
st.rerun()
with col3:
if st.button(f”{montos_bs[2]:,.0f} Bs”, key=“rapido_bs3_calc4”):
st.session_state.monto_calc4 = montos_bs[2]
st.rerun()
with col4:
if st.button(f”{montos_bs[3]:,.0f} Bs”, key=“rapido_bs4_calc4”):
st.session_state.monto_calc4 = montos_bs[3]
st.rerun()
with col5:
if st.button(f”{montos_bs[4]:,.0f} Bs”, key=“rapido_bs5_calc4”):
st.session_state.monto_calc4 = montos_bs[4]
st.rerun()

bs_recibir = st.number_input(
“”,
min_value=0.0,
step=100.0,
key=“bs_recibir”,
value=st.session_state.monto_calc4,
help=“Ingresa la cantidad en Bolívares que deseas recibir”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if bs_recibir != st.session_state.monto_calc4:
st.session_state.monto_calc4 = bs_recibir

if bs_recibir > 0:
usd_enviar = bs_recibir / tasa_bs

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>💵 Debes enviar: ${usd_enviar:.2f} USD</div>
        <div class='resultado-secundario'>Recibirás: {bs_recibir:,.2f} Bs | Tasa: {tasa_bs:.2f} Bs/USD</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Si envías ${usd_enviar:.2f} USD, recibirás {bs_recibir:,.2f} Bs
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar:.2f} para recibir {bs_recibir:.2f} Bs"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif bs_recibir < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a 0 Bs”)

# ==================== CALCULADORA USD A COP ====================

st.markdown(”—”)
st.markdown(”<h2 class='subtitulo-calculadora'>🇨🇴 Calculadora USD a COP</h2>”, unsafe_allow_html=True)

# Mostrar tasa USD a COP

st.markdown(f”””
<div class='tasa-box'>
<div class='tasa-principal'>
📊 Tasa actual: <span style='color: #F36B2D;'>{tasa_usd_cop_compra:,.2f} COP/USD</span>
</div>
<div class='tasa-secundaria'>Actualizado: {datetime.now().strftime(’%d/%m/%Y %H:%M’)}</div>
</div>
“””, unsafe_allow_html=True)

# Campo: USD a COP

st.markdown(”<div class='label-campo'>📤 ¿Cuántos USD vas a enviar?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 5A

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>”, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
if st.button(”$20”, key=“rapido_20_calc5”):
st.session_state.monto_calc5 = 20.0
st.rerun()
with col2:
if st.button(”$50”, key=“rapido_50_calc5”):
st.session_state.monto_calc5 = 50.0
st.rerun()
with col3:
if st.button(”$100”, key=“rapido_100_calc5”):
st.session_state.monto_calc5 = 100.0
st.rerun()
with col4:
if st.button(”$200”, key=“rapido_200_calc5”):
st.session_state.monto_calc5 = 200.0
st.rerun()
with col5:
if st.button(”$500”, key=“rapido_500_calc5”):
st.session_state.monto_calc5 = 500.0
st.rerun()

usd_enviar_cop = st.number_input(
“”,
min_value=0.0,
step=1.0,
key=“usd_enviar_cop”,
value=st.session_state.monto_calc5,
help=“Ingresa la cantidad en USD que vas a enviar”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if usd_enviar_cop != st.session_state.monto_calc5:
st.session_state.monto_calc5 = usd_enviar_cop

if usd_enviar_cop > 0:
cop_recibir = usd_enviar_cop * tasa_usd_cop_compra

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>🇨🇴 Recibirás: ${cop_recibir:,.2f} COP</div>
        <div class='resultado-secundario'>Envías: ${usd_enviar_cop:.2f} USD | Tasa: {tasa_usd_cop_compra:,.2f} COP/USD</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Para recibir ${cop_recibir:,.2f} COP, debes enviar ${usd_enviar_cop:.2f} USD
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar_cop:.2f} USD para recibir ${cop_recibir:,.2f} COP"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif usd_enviar_cop < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0”)

st.markdown(”—”)

# ==================== CALCULADORA 5B: COP DESEADO -> USD A ENVIAR ====================

# Campo: COP deseado

st.markdown(”<div class='label-campo'>📥 ¿Cuántos COP quieres recibir?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 5B

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>”, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
if st.button(”$20K”, key=“rapido_20k_calc5b”):
st.session_state.monto_calc5b = 20000.0
st.rerun()
with col2:
if st.button(”$50K”, key=“rapido_50k_calc5b”):
st.session_state.monto_calc5b = 50000.0
st.rerun()
with col3:
if st.button(”$100K”, key=“rapido_100k_calc5b”):
st.session_state.monto_calc5b = 100000.0
st.rerun()
with col4:
if st.button(”$200K”, key=“rapido_200k_calc5b”):
st.session_state.monto_calc5b = 200000.0
st.rerun()
with col5:
if st.button(”$400K”, key=“rapido_400k_calc5b”):
st.session_state.monto_calc5b = 400000.0
st.rerun()

cop_deseado = st.number_input(
“”,
min_value=0.0,
step=1000.0,
key=“cop_deseado”,
value=st.session_state.monto_calc5b,
help=“Ingresa la cantidad en Pesos Colombianos que deseas recibir”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if cop_deseado != st.session_state.monto_calc5b:
st.session_state.monto_calc5b = cop_deseado

if cop_deseado > 0:
usd_necesarios = cop_deseado / tasa_usd_cop_compra

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>💵 Debes enviar: ${usd_necesarios:.2f} USD</div>
        <div class='resultado-secundario'>Recibirás: ${cop_deseado:,.2f} COP | Tasa: {tasa_usd_cop_compra:,.2f} COP/USD</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Si envías ${usd_necesarios:.2f} USD, recibirás ${cop_deseado:,.2f} COP
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${usd_necesarios:.2f} USD para recibir ${cop_deseado:,.2f} COP"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif cop_deseado < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0 COP”)

# ==================== CALCULADORA COP A USD ====================

st.markdown(”—”)
st.markdown(”<h2 class='subtitulo-calculadora'>🇨🇴 Calculadora COP a USD</h2>”, unsafe_allow_html=True)

# Mostrar tasa COP a USD

st.markdown(f”””
<div class='tasa-box'>
<div class='tasa-principal'>
📊 Tasa actual: <span style='color: #F36B2D;'>{tasa_cop_usd_venta:,.2f} COP/USD</span>
</div>
<div class='tasa-secundaria'>Actualizado: {datetime.now().strftime(’%d/%m/%Y %H:%M’)}</div>
</div>
“””, unsafe_allow_html=True)

# Campo: COP a USD

st.markdown(”<div class='label-campo'>📥 ¿Cuántos Pesos Colombianos vas a enviar?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 6A

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>”, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
if st.button(”$100K”, key=“rapido_100k_calc6”):
st.session_state.monto_calc6 = 100000.0
st.rerun()
with col2:
if st.button(”$200K”, key=“rapido_200k_calc6”):
st.session_state.monto_calc6 = 200000.0
st.rerun()
with col3:
if st.button(”$300K”, key=“rapido_300k_calc6”):
st.session_state.monto_calc6 = 300000.0
st.rerun()
with col4:
if st.button(”$400K”, key=“rapido_400k_calc6”):
st.session_state.monto_calc6 = 400000.0
st.rerun()
with col5:
if st.button(”$500K”, key=“rapido_500k_calc6”):
st.session_state.monto_calc6 = 500000.0
st.rerun()

cop_enviar = st.number_input(
“”,
min_value=0.0,
step=1000.0,
key=“cop_enviar”,
value=st.session_state.monto_calc6,
help=“Ingresa la cantidad en Pesos Colombianos que vas a enviar”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if cop_enviar != st.session_state.monto_calc6:
st.session_state.monto_calc6 = cop_enviar

if cop_enviar > 0:
usd_recibir = cop_enviar / tasa_cop_usd_venta

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>💵 Recibirás: ${usd_recibir:.2f} USD</div>
        <div class='resultado-secundario'>Envías: ${cop_enviar:,.2f} COP | Tasa: {tasa_cop_usd_venta:,.2f} COP/USD</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Para recibir ${usd_recibir:.2f} USD, debes enviar ${cop_enviar:,.2f} COP
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${cop_enviar:,.2f} COP para recibir ${usd_recibir:.2f} USD"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif cop_enviar < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0 COP”)

st.markdown(”—”)

# ==================== CALCULADORA 6B: USD DESEADO -> COP A ENVIAR ====================

# Campo: USD deseado

st.markdown(”<div class='label-campo'>📥 ¿Cuántos USD quieres recibir?</div>”, unsafe_allow_html=True)

# Botones de monto rápido - CALCULADORA 6B

st.markdown(”<div class='montos-rapidos-label'>⚡ Montos rápidos (USD):</div>”, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
if st.button(”$20”, key=“rapido_20_calc6b”):
st.session_state.monto_calc6b = 20.0
st.rerun()
with col2:
if st.button(”$50”, key=“rapido_50_calc6b”):
st.session_state.monto_calc6b = 50.0
st.rerun()
with col3:
if st.button(”$100”, key=“rapido_100_calc6b”):
st.session_state.monto_calc6b = 100.0
st.rerun()
with col4:
if st.button(”$200”, key=“rapido_200_calc6b”):
st.session_state.monto_calc6b = 200.0
st.rerun()
with col5:
if st.button(”$500”, key=“rapido_500_calc6b”):
st.session_state.monto_calc6b = 500.0
st.rerun()

usd_deseado = st.number_input(
“”,
min_value=0.0,
step=1.0,
key=“usd_deseado”,
value=st.session_state.monto_calc6b,
help=“Ingresa la cantidad en USD que deseas recibir”,
label_visibility=“collapsed”
)

# Actualizar el session state si el usuario cambia manualmente el valor

if usd_deseado != st.session_state.monto_calc6b:
st.session_state.monto_calc6b = usd_deseado

if usd_deseado > 0:
cop_necesarios = usd_deseado * tasa_cop_usd_venta

```
st.markdown(f"""
    <div class='resultado-container'>
        <div class='resultado-principal'>🇨🇴 Debes enviar: ${cop_necesarios:,.2f} COP</div>
        <div class='resultado-secundario'>Recibirás: ${usd_deseado:.2f} USD | Tasa: {tasa_cop_usd_venta:,.2f} COP/USD</div>
        <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.9;'>
            ℹ️ Cálculo inverso: Si envías ${cop_necesarios:,.2f} COP, recibirás ${usd_deseado:.2f} USD
        </div>
    </div>
""", unsafe_allow_html=True)

mensaje_whatsapp = f"Hola, necesito enviar ${cop_necesarios:,.2f} COP para recibir ${usd_deseado:.2f} USD"
st.markdown(f"""
    <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
        <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
    </a>
""", unsafe_allow_html=True)
```

elif usd_deseado < 0:
st.error(“⚠️ Por favor ingresa un monto válido mayor a $0”)

# Footer simple

st.markdown(”—”)
st.markdown(”””
<div class='footer'>
<p><strong>Wallet Cambios</strong> · La solución a tu problema cambiario</p>
</div>
“””, unsafe_allow_html=True)
