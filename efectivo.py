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

# 🧮 Calculadora de efectivo
st.markdown("<h3 class='titulo'>🧮 Calculadora de efectivo</h3>", unsafe_allow_html=True)
st.markdown("Las comisiones son del **5%**.")
st.markdown("Ingresa el monto y verás el resultado automáticamente.")

# Campo: Para recibir (USD)
recibir = st.number_input("📤 Para recibir (USD):", min_value=0.0, step=1.0, key="recibir")
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.markdown(f"**Comisión estimada:** ${comision:.2f}")
    st.markdown(f"**Debes enviar:** ${total_enviar:.2f}")

# Campo: Si se envían (USD)
st.markdown("---")
enviados = st.number_input("📤 Si se envían (USD):", min_value=0.0, step=1.0, key="enviados_manual")
if enviados > 0:
    recibir_estimado = enviados * (1 - 0.05)
    st.markdown(f"**Recibirás en efectivo:** ${recibir_estimado:.2f}")

# 💱 Calculadora USD a Bs
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

st.markdown("### 📤 Si se envían (USD):", unsafe_allow_html=True)
usd_enviar2 = st.number_input("", min_value=0.0, step=1.0, key="usd_enviar")
if usd_enviar2 > 0:
    bs_recibir2 = usd_enviar2 * tasa
    st.markdown(f"<div class='resultado'>Se reciben: {bs_recibir2:.2f} Bs</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📤 Para recibir (Bs):", unsafe_allow_html=True)
bs_recibir = st.number_input("", min_value=0.0, step=1.0, key="bs_recibir")
if bs_recibir > 0:
    usd_enviar = bs_recibir / tasa
    st.markdown(f"<div class='resultado'>Hay que enviar: ${usd_enviar:.2f} USD</div>", unsafe_allow_html=True)

# 🇻🇪 Venezuela → Colombia
st.markdown("---")
st.markdown("<h3 class='titulo'>🇻🇪 Calculadora Venezuela → Colombia 🇨🇴</h3>", unsafe_allow_html=True)
sheet_veco_url = "https://docs.google.com/spreadsheets/d/1T5fq8FLpLHDmtiADlAa70E8xkA9st1rs/gviz/tq?tqx=out:csv&sheet=TASAS%20AL%20MAYOR"

try:
    df_veco = pd.read_csv(sheet_veco_url, header=None)
    raw_val_veco = df_veco.iloc[24, 1]  # Celda B25
    tasa_veco = float(str(raw_val_veco).replace(",", ".").replace("$", "").strip())
    st.markdown(f"Tasa actual: **{tasa_veco:.2f} COP/Bs**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except Exception as e:
    st.error("No se pudo obtener la tasa de VENEZUELA a COLOMBIA.")
    st.stop()

st.markdown("### 📤 Si se envían (Bs):", unsafe_allow_html=True)
bs_ve = st.number_input("", min_value=0.0, step=1.0, key="bs_ve")
if bs_ve > 0:
    cop_recibidos = bs_ve * tasa_veco
    st.markdown(f"<div class='resultado'>Recibirás: {cop_recibidos:.2f} COP</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📤 Para recibir (COP):", unsafe_allow_html=True)
cop_deseado = st.number_input("", min_value=0.0, step=1.0, key="cop_deseado")
if cop_deseado > 0:
    bs_necesarios = cop_deseado / tasa_veco
    st.markdown(f"<div class='resultado'>Debes enviar: {bs_necesarios:.2f} Bs</div>", unsafe_allow_html=True)

# 🇨🇴 Colombia → Venezuela
st.markdown("---")
st.markdown("<h3 class='titulo'>🇨🇴 Calculadora Colombia → Venezuela 🇻🇪</h3>", unsafe_allow_html=True)

try:
    df_covene = pd.read_csv(sheet_veco_url, header=None)
    raw_val_covene = df_covene.iloc[25, 1]  # Celda B26
    tasa_covene = float(str(raw_val_covene).replace(",", ".").replace("$", "").strip())
    st.markdown(f"Tasa actual: **{tasa_covene:.2f} Bs/COP**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except Exception as e:
    st.error("No se pudo obtener la tasa de COLOMBIA a VENEZUELA.")
    st.stop()

st.markdown("### 📤 Si se envían (COP):", unsafe_allow_html=True)
cop_cv = st.number_input("", min_value=0.0, step=1.0, key="cop_cv")
if cop_cv > 0:
    bs_cv = cop_cv * tasa_covene
    st.markdown(f"<div class='resultado'>Recibirás: {bs_cv:.2f} Bs</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📤 Para recibir (Bs):", unsafe_allow_html=True)
bs_objetivo = st.number_input("", min_value=0.0, step=1.0, key="bs_objetivo")
if bs_objetivo > 0:
    cop_requerido = bs_objetivo / tasa_covene
    st.markdown(f"<div class='resultado'>Debes enviar: {cop_requerido:.2f} COP</div>", unsafe_allow_html=True)

