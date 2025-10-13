import streamlit as st
import pandas as pd
import urllib.parse

# Configurar página
st.set_page_config(page_title="Calculadora Wallet Cambios", layout="centered")

# Número de WhatsApp
WHATSAPP_NUMBER = "584146108166"
WHATSAPP_MESSAGE = "Hola, quiero hacer un cambio"

# Función para crear enlace de WhatsApp
def crear_enlace_whatsapp():
    mensaje_encoded = urllib.parse.quote(WHATSAPP_MESSAGE)
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={mensaje_encoded}"

# CSS personalizado
st.markdown("""
    <style>
        .logo-container img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 120px;
        }
        .titulo {
            text-align: center;
            font-size: 2em;
        }
        .destacado {
            font-size: 1.2em !important;
            font-weight: bold;
        }
        .resultado {
            font-size: 1.3em !important;
            font-weight: bold;
        }
        .whatsapp-btn {
            display: block;
            background-color: #25D366;
            color: white;
            padding: 12px 24px;
            text-align: center;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            margin: 15px auto;
            max-width: 300px;
            transition: background-color 0.3s;
        }
        .whatsapp-btn:hover {
            background-color: #20BA5A;
            color: white;
            text-decoration: none;
        }
        h3 {
            font-size: 2em;
            text-align: center;
        }
        @media screen and (max-width: 768px) {
            .logo-container img {
                width: 90px;
            }
            .titulo {
                font-size: 1.4em;
            }
            .destacado {
                font-size: 1.1em !important;
            }
            .resultado {
                font-size: 1.2em !important;
            }
            .whatsapp-btn {
                padding: 10px 20px;
                font-size: 0.9em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Logo
st.markdown("""
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png">
    </div>
""", unsafe_allow_html=True)

# Título
st.markdown("<h2 class='titulo'>Calculadoras de Wallet Cambios </h2>", unsafe_allow_html=True)
st.markdown("<h3 class='titulo'>🧮 Calculadora de efectivo</h3>", unsafe_allow_html=True)
st.markdown("Las comisiones son del **5%**.")
st.markdown("Ingresa el monto y verás el resultado automáticamente.")

# Campo 1: Para recibir (USD)
st.markdown("<h3 class='destacado'>📤 Para recibir (USD):</h3>", unsafe_allow_html=True)
recibir = st.number_input("", min_value=0.0, step=1.0, key="recibir")

if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.markdown(f"**Comisión estimada:** ${comision:.2f}")
    st.markdown(f"**Debes enviar:** ${total_enviar:.2f}")
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp()}" target="_blank" class="whatsapp-btn">
            💬 Realiza el cambio con nosotros ahora
        </a>
    """, unsafe_allow_html=True)

# Campo 2: Si se envían (USD)
st.markdown("<h3 class='destacado'>📤 Si se envían (USD):</h3>", unsafe_allow_html=True)
enviados = st.number_input("", min_value=0.0, step=1.0, key="enviados_manual")

if enviados > 0:
    recibir_estimado = enviados * (1 - 0.05)
    st.markdown(f"**Recibirás en efectivo:** ${recibir_estimado:.2f}")
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp()}" target="_blank" class="whatsapp-btn">
            💬 Realiza el cambio con nosotros ahora
        </a>
    """, unsafe_allow_html=True)

# Separador
st.markdown("---")
st.markdown("### 💱 Calculadora USD a Bolívares 🇻🇪")

# Cargar tasa desde Google Sheets pública
sheet_url = "https://docs.google.com/spreadsheets/d/1ig4ihkUIeP7kaaR6yZeyOLF7j38Y_peytGKG6tgkqbw/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"

try:
    df = pd.read_csv(sheet_url, header=None)
    tasa = float(df.iloc[1, 12])  # Celda M2
    st.markdown(f"Tasa actual: **{tasa} Bs/USD**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except Exception as e:
    st.error("No se pudo obtener la tasa de VENEZUELA desde Google Sheets.")
    st.stop()

# Modo 1: De USD a Bs
st.markdown("<h3 class='destacado'>📤 Si se envían (USD):</h3>", unsafe_allow_html=True)
usd_enviar2 = st.number_input("", min_value=0.0, step=1.0, key="usd_enviar")

if usd_enviar2 > 0:
    bs_recibir2 = usd_enviar2 * tasa
    st.markdown(f"<div class='resultado'>Se reciben: {bs_recibir2:.2f} Bs</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp()}" target="_blank" class="whatsapp-btn">
            💬 Realiza el cambio con nosotros ahora
        </a>
    """, unsafe_allow_html=True)

# Divider
st.markdown("---")

# Modo 2: De Bs a USD
st.markdown("<h3 class='destacado'>📤 Para recibir (Bs):</h3>", unsafe_allow_html=True)
bs_recibir = st.number_input("", min_value=0.0, step=1.0, key="bs_recibir")

if bs_recibir > 0:
    usd_enviar = bs_recibir / tasa
    st.markdown(f"<div class='resultado'>Hay que enviar: ${usd_enviar:.2f} USD</div>", unsafe_allow_html=True)
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp()}" target="_blank" class="whatsapp-btn">
            💬 Realiza el cambio con nosotros ahora
        </a>
    """, unsafe_allow_html=True)

