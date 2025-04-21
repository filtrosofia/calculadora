import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora Wallet Cambios", layout="centered")

# Centrar el logo y hacerlo más pequeño usando HTML
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png" width="120"/>
    </div>
    """,
    unsafe_allow_html=True
)

# Título centrado usando HTML
st.markdown(
    """
    <h1 style='text-align: center;'>🧮 Calculadora de efectivo de Wallet Cambios</h1>
    """,
    unsafe_allow_html=True
)

st.markdown("Las comisiones son del **5%**.")
st.markdown("Ingresa el monto y verás el resultado automáticamente.")

# Entrada
recibir = st.number_input("Monto que deseas recibir (USD):", min_value=0.0, step=1.0)

# Cálculo
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.write(f"**Comisión estimada:** ${comision:.2f}")
    st.write(f"**Debes enviar:** ${total_enviar:.2f}")
