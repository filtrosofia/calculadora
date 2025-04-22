import streamlit as st
import pandas as pd

# Configurar página
st.set_page_config(page_title="Calculadora Wallet Cambios", layout="centered")

# CSS para centrar, escalar en móvil y ajustar el diseño
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

        @media screen and (max-width: 768px) {
            .logo-container img {
                width: 90px;
            }
            .titulo {
                font-size: 1.4em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Logo
st.markdown(
    """
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png">
    </div>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h2 class='titulo'>🧮 Calculadora de efectivo de Wallet Cambios</h2>", unsafe_allow_html=True)
st.markdown("Las comisiones son del **5%**.")
st.markdown("Ingresa el monto y verás el resultado automáticamente.")

# Primera calculadora: efectivo + comisiones
recibir = st.number_input("Monto que deseas recibir (USD):", min_value=0.0, step=1.0)
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.write(f"**Comisión estimada:** ${comision:.2f}")
    st.write(f"**Debes enviar:** ${total_enviar:.2f}")

# ────────────────────────────────────────────────
# Segunda calculadora: USD ↔ Bs (con tasa dinámica)
st.markdown("---")
st.markdown("<h2 class='titulo'>💱 Calculadora USD</h2>", unsafe_allow_html=True)

# Cargar tasa desde Google Sheets pública
sheet_url = "https://docs.google.com/spreadsheets/d/1T5fq8FLpLHDmtiADlAa70E8xkA9st1rs/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"
df = pd.read_csv(sheet_url)

# Obtener tasa de compra para VENEZUELA
try:
    venezuela_row = df[df['PAIS'].str.upper() == 'VENEZUELA']
    tasa = float(venezuela_row['COMPRA'].values[0])
    st.markdown(f"Tasa actual: **{tasa} Bs/USD**")
    st.markdown("Ingresa el monto y verás el resultado automáticamente.")
except Exception as e:
    st.error("No se pudo obtener la tasa de VENEZUELA desde Google Sheets.")
    st.stop()

# Modo 1: Para recibir X Bs, ¿cuántos USD enviar?
st.subheader("🔁 De Bolívares a Dólares")
bs_recibir = st.number_input("Para recibir (Bs):", min_value=0.0, step=1.0, key="bs_recibir")
if bs_recibir > 0:
    usd_enviar = bs_recibir / tasa
    st.write(f"**Hay que enviar:** ${usd_enviar:.2f} USD")

# Modo 2: Si se envían X USD, ¿cuántos Bs se reciben?
st.subheader("🔄 De Dólares a Bolívares")
usd_enviar2 = st.number_input("Si se envían (USD):", min_value=0.0, step=1.0, key="usd_enviar")
if usd_enviar2 > 0:
    bs_recibir2 = usd_enviar2 * tasa
    st.write(f"**Se reciben:** {bs_recibir2:.2f} Bs")
