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

# Título principal
st.markdown("<h2 class='titulo'>Calculadoras de Wallet Cambios </h2>", unsafe_allow_html=True)

# ──────────────────────────────
# Calculadora de efectivo
st.markdown("<h3 class='titulo'>🧮 Calculadora de efectivo</h3>", unsafe_allow_html=True)
st.markdown("Las comisiones son del **5%**.")
st.markdown("Ingresa el monto y verás el resultado automáticamente.")

recibir = st.number_input("📤 Para recibir (USD):", min_value=0.0, step=1.0, key="recibir")
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.markdown(f"**Comisión estimada:** ${comision:.2f}")
    st.markdown(f"**Debes enviar:** ${total_enviar:.2f}")

st.markdown("---")

enviados = st.number_input("📤 Si se envían (USD):", min_value=0.0, step=1.0, key="enviados_manual")
if enviados > 0:
    recibir_estimado = enviados * (1 - 0.05)
    st.markdown(f"**Recibirás en efectivo:** ${recibir_estimado:.2f}")

# ──────────────────────────────
# Calculadora USD ↔ Bs
st.markdown("---")
st.markdown("### 💱 Calculadora USD a Bolívares 🇻🇪")

sheet_url = "https://docs.google.com/spreadsheets/d/1T5fq8FLpLHDmtiADlAa70E8xkA9st1rs/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"

try:
    df = pd.read_csv(sheet_url, header=None)
    tasa = float(df.iloc[1, 12])  # Celda M2
    st.markdown(f"Tasa actual: **{tasa} Bs/USD**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except Exception as e:
    st.error("No se pudo obtener la tasa de VENEZUELA desde Google Sheets.")
    st.stop()

st.markdown("<h3 class='destacado'>📤 Si se envían (USD):</h3>", unsafe_allow_html=True)
usd_enviar2 = st.number_input("", min_value=0.0, step=1.0, key="usd_enviar")
if usd_enviar2 > 0:
    bs_recibir2 = usd_enviar2 * tasa
    st.markdown(f"<div class='resultado'>Se reciben: {bs_recibir2:.2f} Bs</div>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h3 class='destacado'>📤 Para recibir (Bs):</h3>", unsafe_allow_html=True)
bs_recibir = st.number_input("", min_value=0.0, step=1.0, key="bs_recibir")
if bs_recibir > 0:
    usd_enviar = bs_recibir / tasa
    st.markdown(f"<div class='resultado'>Hay que enviar: ${usd_enviar:.2f} USD</div>", unsafe_allow_html=True)

# ──────────────────────────────
# Calculadora Venezuela → Colombia
st.markdown("---")
st.markdown("### 🇻🇪 Calculadora Venezuela → Colombia 🇨🇴")

try:
    tasa_vzla_col = float(df.iloc[3, 1])  # Celda B4
    st.markdown(f"Tasa actual: **{tasa_vzla_col} COP/Bs**")
except:
    st.error("No se pudo obtener la tasa de VENEZUELA a COLOMBIA.")
    st.stop()

bs_vzla_col = st.number_input("📤 Si se envían (Bs):", min_value=0.0, step=1.0, key="bs_vzla_col")
if bs_vzla_col > 0:
    cop_recibido = bs_vzla_col * tasa_vzla_col
    st.markdown(f"<div class='resultado'>Recibirás: {cop_recibido:.2f} COP</div>", unsafe_allow_html=True)

st.markdown("---")

cop_deseado = st.number_input("📤 Para recibir (COP):", min_value=0.0, step=1.0, key="cop_deseado")
if cop_deseado > 0:
    bs_necesarios = cop_deseado / tasa_vzla_col
    st.markdown(f"<div class='resultado'>Debes enviar: {bs_necesarios:.2f} Bs</div>", unsafe_allow_html=True)

# ──────────────────────────────
# Calculadora Colombia → Venezuela
st.markdown("---")
st.markdown("### 🇨🇴 Calculadora Colombia → Venezuela 🇻🇪")

try:
    tasa_col_vzla = float(df.iloc[8, 5])  # Celda F9
    st.markdown(f"Tasa actual: **{tasa_col_vzla} Bs/COP**")
except:
    st.error("No se pudo obtener la tasa de COLOMBIA a VENEZUELA.")
    st.stop()

cop_col_vzla = st.number_input("📤 Si se envían (COP):", min_value=0.0, step=1.0, key="cop_col_vzla")
if cop_col_vzla > 0:
    bs_recibidos = cop_col_vzla * tasa_col_vzla
    st.markdown(f"<div class='resultado'>Recibirás: {bs_recibidos:.2f} Bs</div>", unsafe_allow_html=True)

st.markdown("---")

bs_deseados = st.number_input("📤 Para recibir (Bs):", min_value=0.0, step=1.0, key="bs_deseados")
if bs_deseados > 0:
    cop_requeridos = bs_deseados / tasa_col_vzla
    st.markdown(f"<div class='resultado'>Debes enviar: {cop_requeridos:.2f} COP</div>", unsafe_allow_html=True)
