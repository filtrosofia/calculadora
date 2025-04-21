import streamlit as st

import streamlit as st

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

# Logo centrado y escalable
st.markdown(
    """
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png">
    </div>
    """,
    unsafe_allow_html=True
)

# Título centrado y adaptable
st.markdown(
    "<h1 class='titulo'>🧮 Calculadora de efectivo de Wallet Cambios</h1>",
    unsafe_allow_html=True
)

# Subtítulo + entrada
st.markdown("Las comisiones son del **5% + $0**.")
st.markdown("Ingresa el monto y verás el resultado automáticamente.")

recibir = st.number_input("Monto que deseas recibir (USD):", min_value=0.0, step=1.0)

# Cálculo
if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.write(f"**Comisión estimada:** ${comision:.2f}")
    st.write(f"**Debes enviar:** ${total_enviar:.2f}")

