import streamlit as st

st.set_page_config(page_title="Calculadora PayPal", layout="centered")

st.title("🧮 Calculadora de Comisiones PayPal")
st.markdown("Las comisiones son del **5% + $0**.")

# Input
recibir = st.number_input("Monto que deseas recibir (USD):", min_value=0.0, step=1.0)

# Cálculo inverso
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.write(f"**Comisión estimada:** ${comision:.2f}")
    st.write(f"**Debes enviar:** ${total_enviar:.2f}")
