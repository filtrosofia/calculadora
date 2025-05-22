
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

# Separador
st.markdown("---")
st.markdown("<h3 class='titulo'>💱 Calculadora USD a Bolívares 🇻🇪</h3>", unsafe_allow_html=True)

sheet_url = "https://docs.google.com/spreadsheets/d/1T5fq8FLpLHDmtiADlAa70E8xkA9st1rs/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"

try:
    df = pd.read_csv(sheet_url, header=None)
    tasa = float(df.iloc[1, 12])
    st.markdown(f"Tasa actual: **{tasa} Bs/USD**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except:
    st.error("No se pudo obtener la tasa de VENEZUELA desde Google Sheets.")
    st.stop()

# USD a Bs
st.markdown("<h3 class='destacado'>📤 Si se envían (USD):</h3>", unsafe_allow_html=True)
usd_enviar2 = st.number_input("", min_value=0.0, step=1.0, key="usd_enviar")
if usd_enviar2 > 0:
    bs_recibir2 = usd_enviar2 * tasa
    st.markdown(f"<div class='resultado'>Se reciben: {bs_recibir2:.2f} Bs</div>", unsafe_allow_html=True)

st.markdown("---")

# Bs a USD
st.markdown("<h3 class='destacado'>📤 Para recibir (Bs):</h3>", unsafe_allow_html=True)
bs_recibir = st.number_input("", min_value=0.0, step=1.0, key="bs_recibir")
if bs_recibir > 0:
    usd_enviar = bs_recibir / tasa
    st.markdown(f"<div class='resultado'>Hay que enviar: ${usd_enviar:.2f} USD</div>", unsafe_allow_html=True)

# ───────────────────────────────────────────────
# NUEVAS CALCULADORAS ADICIONALES
# ───────────────────────────────────────────────

# Calculadora Venezuela → Colombia
st.markdown("---")
st.markdown("<h3 class='titulo'>🇻🇪 Calculadora Venezuela → Colombia 🇨🇴</h3>", unsafe_allow_html=True)

sheet_veco_url = "https://docs.google.com/spreadsheets/d/1T5fq8FLpLHDmtiADlAa70E8xkA9st1rs/gviz/tq?tqx=out:csv&sheet=TASAS%20AL%20MAYOR"

try:
    df_veco = pd.read_csv(sheet_veco_url, header=None)
    tasa_veco = float(df_veco.iloc[3, 1])
except:
    st.error("No se pudo obtener la tasa de VENEZUELA a COLOMBIA.")
    st.stop()

# Bs a COP
st.markdown("<h3 class='destacado'>📤 Si se envían (Bs):</h3>", unsafe_allow_html=True)
veco_bs = st.number_input("", min_value=0.0, step=1.0, key="veco_bs")
if veco_bs > 0:
    veco_cop = veco_bs * tasa_veco
    st.markdown(f"<div class='resultado'>Recibirás: {veco_cop:.2f} COP</div>", unsafe_allow_html=True)

st.markdown("---")

# COP a Bs
st.markdown("<h3 class='destacado'>📤 Para recibir (COP):</h3>", unsafe_allow_html=True)
veco_cop_rev = st.number_input("", min_value=0.0, step=1.0, key="veco_cop")
if veco_cop_rev > 0:
    veco_bs_rev = veco_cop_rev / tasa_veco
    st.markdown(f"<div class='resultado'>Debes enviar: {veco_bs_rev:.2f} Bs</div>", unsafe_allow_html=True)

# Calculadora Colombia → Venezuela
st.markdown("---")
st.markdown("<h3 class='titulo'>🇨🇴 Calculadora Colombia → Venezuela 🇻🇪</h3>", unsafe_allow_html=True)

try:
    tasa_cove = float(df_veco.iloc[8, 5])
except:
    st.error("No se pudo obtener la tasa de COLOMBIA a VENEZUELA.")
    st.stop()

# COP a Bs
st.markdown("<h3 class='destacado'>📤 Si se envían (COP):</h3>", unsafe_allow_html=True)
cove_cop = st.number_input("", min_value=0.0, step=1.0, key="cove_cop")
if cove_cop > 0:
    cove_bs = cove_cop * tasa_cove
    st.markdown(f"<div class='resultado'>Recibirás: {cove_bs:.2f} Bs</div>", unsafe_allow_html=True)

st.markdown("---")

# Bs a COP
st.markdown("<h3 class='destacado'>📤 Para recibir (Bs):</h3>", unsafe_allow_html=True)
cove_bs_rev = st.number_input("", min_value=0.0, step=1.0, key="cove_bs")
if cove_bs_rev > 0:
    cove_cop_rev = cove_bs_rev / tasa_cove
    st.markdown(f"<div class='resultado'>Debes enviar: {cove_cop_rev:.2f} COP</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='resultado'>Hay que enviar: {bs_deseado / tasa_co_ve:.2f} COP</div>", unsafe_allow_html=True)


