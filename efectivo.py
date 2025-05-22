import streamlit as st
import pandas as pd

# Configurar página
st.set_page_config(page_title="Calculadora Wallet Cambios", layout="centered")

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
recibir = st.number_input("📤 Para recibir (USD):", min_value=0.0, step=1.0, key="recibir")
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.markdown(f"**Comisión estimada:** ${comision:.2f}")
    st.markdown(f"**Debes enviar:** ${total_enviar:.2f}")

st.markdown("---")

# Campo 2: Si se envían (USD)
enviados = st.number_input("📤 Si se envían (USD):", min_value=0.0, step=1.0, key="enviados_manual")
if enviados > 0:
    recibir_estimado = enviados * (1 - 0.05)
    st.markdown(f"**Recibirás en efectivo:** ${recibir_estimado:.2f}")

# ────────────────────────────────
# Calculadora USD a Bs (tasa M2)
st.markdown("---")
st.markdown("<h3 class='titulo'>💱 Calculadora USD a Bolívares 🇻🇪</h3>", unsafe_allow_html=True)

sheet_url = "https://docs.google.com/spreadsheets/d/1T5fq8FLpLHDmtiADlAa70E8xkA9st1rs/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"

try:
    df = pd.read_csv(sheet_url, header=None)
    tasa = float(df.iloc[1, 12])  # Celda M2
    st.markdown(f"Tasa actual: **{tasa} Bs/USD**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except Exception as e:
    st.error("No se pudo obtener la tasa de VENEZUELA.")
    st.stop()

# Si se envían (USD)
st.markdown("<h3 class='destacado'>📤 Si se envían (USD):</h3>", unsafe_allow_html=True)
usd_envio = st.number_input("", min_value=0.0, step=1.0, key="usd_envio")
if usd_envio > 0:
    st.markdown(f"<div class='resultado'>Se reciben: {usd_envio * tasa:.2f} Bs</div>", unsafe_allow_html=True)

# Divider
st.markdown("---")

# Para recibir (Bs)
st.markdown("<h3 class='destacado'>📤 Para recibir (Bs):</h3>", unsafe_allow_html=True)
bs_recibo = st.number_input("", min_value=0.0, step=1.0, key="bs_recibo")
if bs_recibo > 0:
    st.markdown(f"<div class='resultado'>Hay que enviar: ${bs_recibo / tasa:.2f} USD</div>", unsafe_allow_html=True)

# ────────────────────────────────
# VE -> CO Calculadora (tasa B4)
st.markdown("---")
st.markdown("<h3 class='titulo'>🇻🇪 Calculadora Venezuela → Colombia 🇨🇴</h3>", unsafe_allow_html=True)

try:
    tasa_ve_co = float(df.iloc[3, 1])  # Celda B4
    st.markdown(f"Tasa actual: **{tasa_ve_co} COP/Bs**")
except:
    st.error("No se pudo obtener la tasa de VENEZUELA a COLOMBIA.")
    st.stop()

# Si se envían (Bs)
st.markdown("<h3 class='destacado'>📤 Si se envían (Bs):</h3>", unsafe_allow_html=True)
bs_ve_co = st.number_input("", min_value=0.0, step=1.0, key="bs_ve_co")
if bs_ve_co > 0:
    st.markdown(f"<div class='resultado'>Se reciben: {bs_ve_co * tasa_ve_co:.2f} COP</div>", unsafe_allow_html=True)

# Divider
st.markdown("---")

# Para recibir (COP)
st.markdown("<h3 class='destacado'>📤 Para recibir (COP):</h3>", unsafe_allow_html=True)
cop_deseado = st.number_input("", min_value=0.0, step=1.0, key="cop_deseado")
if cop_deseado > 0:
    st.markdown(f"<div class='resultado'>Hay que enviar: {cop_deseado / tasa_ve_co:.2f} Bs</div>", unsafe_allow_html=True)

# ────────────────────────────────
# CO -> VE Calculadora (tasa F9)
st.markdown("---")
st.markdown("<h3 class='titulo'>🇨🇴 Calculadora Colombia → Venezuela 🇻🇪</h3>", unsafe_allow_html=True)

try:
    tasa_co_ve = float(df.iloc[8, 5])  # Celda F9
    st.markdown(f"Tasa actual: **{tasa_co_ve} Bs/COP**")
except:
    st.error("No se pudo obtener la tasa de COLOMBIA a VENEZUELA.")
    st.stop()

# Si se envían (COP)
st.markdown("<h3 class='destacado'>📤 Si se envían (COP):</h3>", unsafe_allow_html=True)
cop_envio = st.number_input("", min_value=0.0, step=1.0, key="cop_envio")
if cop_envio > 0:
    st.markdown(f"<div class='resultado'>Se reciben: {cop_envio * tasa_co_ve:.2f} Bs</div>", unsafe_allow_html=True)

# Divider
st.markdown("---")

# Para recibir (Bs)
st.markdown("<h3 class='destacado'>📤 Para recibir (Bs):</h3>", unsafe_allow_html=True)
bs_deseado = st.number_input("", min_value=0.0, step=1.0, key="bs_deseado")
if bs_deseado > 0:
    st.markdown(f"<div class='resultado'>Hay que enviar: {bs_deseado / tasa_co_ve:.2f} COP</div>", unsafe_allow_html=True)


