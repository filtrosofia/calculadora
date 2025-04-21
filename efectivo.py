import streamlit as st

st.set_page_config(page_title="Calculadora PayPal", layout="centered")

# Mostrar el logo desde GitHub (versión cruda)
st.image("https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png", width=200)

# Título e instrucciones
st.title("🧮 Calculadora de efectivo de Wallet Cambios")
st.markdown("Las comisiones son del **5% + $0**.")
st.caption("Ingresa el monto y verás el resultado automáticamente.")

# Input
recibir = st.number_input("Monto que deseas recibir (USD):", min_value=0.0, step=1.0)

# Cálculo inverso
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.write(f"**Comisión estimada:** ${comision:.2f}")
    st.write(f"**Debes enviar:** ${total_enviar:.2f}")
