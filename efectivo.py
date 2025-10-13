import streamlit as st
import pandas as pd
import urllib.parse
from datetime import datetime

# Configurar página con favicon
st.set_page_config(
    page_title="Calculadora Wallet Cambios", 
    layout="centered",
    page_icon="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png"
)

# Número de WhatsApp
WHATSAPP_NUMBER = "584146108166"

# Función para crear enlace de WhatsApp con mensaje personalizado
def crear_enlace_whatsapp(mensaje):
    mensaje_encoded = urllib.parse.quote(mensaje)
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={mensaje_encoded}"

# CSS personalizado con guía de marca
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@300;400;600&display=swap');
        
        /* Variables de color de marca */
        :root {
            --azul-brillante: #4BA9C3;
            --azul-medio: #3D9FC2;
            --azul-turquesa: #399BC0;
            --azul-profundo: #2881AB;
            --naranja-energia: #F36B2D;
            --amarillo-calido: #FFC542;
            --gris-claro: #F5F7FA;
            --gris-medio: #A0A7AF;
            --texto-principal: #3A3A3A;
        }
        
        /* Modo oscuro */
        [data-theme="dark"] {
            --bg-primary: #1a1a2e;
            --bg-secondary: #16213e;
            --text-primary: #ffffff;
            --text-secondary: #a0a7af;
        }
        
        /* Reset Streamlit */
        .stApp {
            background: linear-gradient(135deg, #E9F5FA 0%, #FFFFFF 100%);
            font-family: 'Open Sans', sans-serif;
        }
        
        /* Logo container */
        .logo-container {
            text-align: center;
            margin-bottom: 2rem;
            animation: fadeInDown 0.8s ease-out;
        }
        
        .logo-container img {
            width: clamp(90px, 15vw, 140px);
            filter: drop-shadow(0 4px 8px rgba(40, 129, 171, 0.2));
            transition: transform 0.3s ease;
        }
        
        .logo-container img:hover {
            transform: scale(1.05);
        }
        
        /* Títulos con jerarquía */
        .titulo-principal {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: clamp(1.8rem, 4vw, 2.5rem);
            text-align: center;
            color: var(--azul-profundo);
            margin-bottom: 0.5rem;
            animation: fadeInUp 0.8s ease-out;
        }
        
        .subtitulo-calculadora {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: clamp(1.3rem, 3vw, 1.8rem);
            text-align: center;
            color: var(--azul-medio);
            margin: 2rem 0 1rem 0;
            padding: 1rem;
            background: linear-gradient(90deg, transparent, rgba(75, 169, 195, 0.1), transparent);
            border-radius: 8px;
        }
        
        .label-campo {
            font-family: 'Open Sans', sans-serif;
            font-weight: 600;
            font-size: clamp(1rem, 2vw, 1.15rem);
            color: var(--azul-profundo);
            margin: 1.5rem 0 0.5rem 0;
        }
        
        /* Inputs mejorados */
        .stNumberInput > div > div > input {
            border: 2px solid var(--azul-brillante);
            border-radius: 8px;
            padding: 0.75rem;
            font-size: clamp(1rem, 2vw, 1.1rem);
            transition: all 0.3s ease;
            font-family: 'Open Sans', sans-serif;
        }
        
        .stNumberInput > div > div > input:focus {
            border-color: var(--naranja-energia);
            box-shadow: 0 0 0 3px rgba(243, 107, 45, 0.2);
            outline: none;
        }
        
        /* Resultados con animación */
        .resultado-container {
            background: linear-gradient(135deg, #4BA9C3 0%, #2881AB 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            margin: 1rem 0;
            box-shadow: 0 8px 20px rgba(40, 129, 171, 0.3);
            animation: slideInUp 0.5s ease-out;
        }
        
        .resultado-principal {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
            font-size: clamp(1.3rem, 3vw, 1.6rem);
            margin-bottom: 0.5rem;
        }
        
        .resultado-secundario {
            font-family: 'Open Sans', sans-serif;
            font-size: clamp(0.95rem, 2vw, 1.1rem);
            opacity: 0.95;
        }
        
        /* Botones de monto rápido */
        .montos-rapidos {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            margin: 1rem 0;
            justify-content: center;
        }
        
        .btn-monto-rapido {
            background: var(--gris-claro);
            border: 2px solid var(--azul-brillante);
            color: var(--azul-profundo);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: clamp(0.85rem, 1.5vw, 0.95rem);
        }
        
        .btn-monto-rapido:hover {
            background: var(--azul-brillante);
            color: white;
            transform: translateY(-2px);
        }
        
        /* Botón WhatsApp mejorado */
        .whatsapp-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            background: linear-gradient(135deg, #25D366 0%, #20BA5A 100%);
            color: white;
            padding: clamp(0.8rem, 2vw, 1rem) clamp(1.5rem, 3vw, 2rem);
            text-align: center;
            text-decoration: none;
            border-radius: 12px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            margin: 1.5rem auto;
            max-width: 350px;
            box-shadow: 0 6px 15px rgba(37, 211, 102, 0.4);
            transition: all 0.3s ease;
            font-size: clamp(0.95rem, 2vw, 1.1rem);
        }
        
        .whatsapp-btn:hover {
            background: linear-gradient(135deg, #20BA5A 0%, #1EA952 100%);
            color: white;
            text-decoration: none;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(37, 211, 102, 0.5);
        }
        
        /* Información adicional */
        .info-box {
            background: rgba(255, 197, 66, 0.15);
            border-left: 4px solid var(--amarillo-calido);
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            font-family: 'Open Sans', sans-serif;
            font-size: clamp(0.9rem, 1.8vw, 1rem);
        }
        
        /* Toggle dark mode */
        .dark-mode-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 999;
            background: var(--azul-profundo);
            color: white;
            border: none;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            font-size: 1.5rem;
        }
        
        /* Animaciones */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Responsive */
        @media screen and (max-width: 1024px) {
            .resultado-container {
                padding: 1.2rem;
            }
        }
        
        @media screen and (max-width: 768px) {
            .montos-rapidos {
                gap: 0.3rem;
            }
            
            .btn-monto-rapido {
                padding: 0.4rem 0.8rem;
            }
        }
        
        @media screen and (max-width: 375px) {
            .logo-container img {
                width: 80px;
            }
            
            .whatsapp-btn {
                padding: 0.7rem 1.2rem;
            }
        }
        
        @media (orientation: landscape) and (max-height: 500px) {
            .logo-container {
                margin-bottom: 1rem;
            }
            
            .subtitulo-calculadora {
                margin: 1rem 0 0.5rem 0;
                padding: 0.5rem;
            }
        }
        
        /* Ocultar elementos de Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Logo
st.markdown("""
    <div class="logo-container">
        <img src="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png" alt="Wallet Cambios Logo">
    </div>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='titulo-principal'>Calculadora Wallet Cambios</h1>", unsafe_allow_html=True)

# Info de horario
st.markdown("""
    <div class='info-box'>
        <strong>⏰ Horario de atención:</strong> Lunes a Viernes 8:00 AM - 6:00 PM | Sábados 9:00 AM - 1:00 PM
    </div>
""", unsafe_allow_html=True)

# ==================== CALCULADORA DE EFECTIVO ====================
st.markdown("<h2 class='subtitulo-calculadora'>💵 Calculadora de Efectivo</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #3A3A3A;'>Comisión del <strong>5%</strong> aplicada</p>", unsafe_allow_html=True)

# Botones de monto rápido para efectivo
st.markdown("""
    <div class='montos-rapidos'>
        <span style='color: #2881AB; font-weight: 600; margin-right: 0.5rem;'>Montos rápidos:</span>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
monto_rapido_efectivo = None

with col1:
    if st.button("$50", key="rapido_50_efectivo"):
        monto_rapido_efectivo = 50.0
with col2:
    if st.button("$100", key="rapido_100_efectivo"):
        monto_rapido_efectivo = 100.0
with col3:
    if st.button("$500", key="rapido_500_efectivo"):
        monto_rapido_efectivo = 500.0
with col4:
    if st.button("$1000", key="rapido_1000_efectivo"):
        monto_rapido_efectivo = 1000.0

# Campo 1: Para recibir (USD)
st.markdown("<div class='label-campo'>📥 ¿Cuánto deseas recibir en efectivo?</div>", unsafe_allow_html=True)
recibir = st.number_input(
    "",
    min_value=0.0,
    step=1.0,
    key="recibir",
    value=monto_rapido_efectivo if monto_rapido_efectivo else 0.0,
    help="Ingresa la cantidad en USD que deseas recibir",
    label_visibility="collapsed"
)

if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💰 Debes enviar: ${total_enviar:.2f} USD</div>
            <div class='resultado-secundario'>Comisión: ${comision:.2f} | Recibirás: ${recibir:.2f}</div>
            <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.8;'>
                ℹ️ Cálculo inverso: Si envías ${total_enviar:.2f}, recibirás ${recibir:.2f} en efectivo
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    mensaje_whatsapp = f"Hola, necesito enviar ${total_enviar:.2f} para recibir ${recibir:.2f} en efectivo"
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
            <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
        </a>
    """, unsafe_allow_html=True)
elif recibir < 0:
    st.error("⚠️ Por favor ingresa un monto válido mayor a $0")

st.markdown("---")

# Campo 2: Si se envían (USD)
st.markdown("<div class='label-campo'>📤 ¿Cuánto vas a enviar?</div>", unsafe_allow_html=True)
enviados = st.number_input(
    "",
    min_value=0.0,
    step=1.0,
    key="enviados_manual",
    help="Ingresa la cantidad en USD que vas a enviar",
    label_visibility="collapsed"
)

if enviados > 0:
    recibir_estimado = enviados * (1 - 0.05)
    comision_enviados = enviados - recibir_estimado
    
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💵 Recibirás: ${recibir_estimado:.2f} USD</div>
            <div class='resultado-secundario'>Monto enviado: ${enviados:.2f} | Comisión: ${comision_enviados:.2f}</div>
            <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.8;'>
                ℹ️ Cálculo inverso: Para recibir ${recibir_estimado:.2f}, debes enviar ${enviados:.2f}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    mensaje_whatsapp = f"Hola, necesito enviar ${enviados:.2f} para recibir ${recibir_estimado:.2f}"
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
            <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
        </a>
    """, unsafe_allow_html=True)
elif enviados < 0:
    st.error("⚠️ Por favor ingresa un monto válido mayor a $0")

# ==================== CALCULADORA USD A BOLÍVARES ====================
st.markdown("---")
st.markdown("<h2 class='subtitulo-calculadora'>🇻🇪 Calculadora USD a Bolívares</h2>", unsafe_allow_html=True)

# Cargar tasa desde Google Sheets pública con timeout
sheet_url = "https://docs.google.com/spreadsheets/d/1ig4ihkUIeP7kaaR6yZeyOLF7j38Y_peytGKG6tgkqbw/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"

try:
    df = pd.read_csv(sheet_url, header=None)
    tasa = float(df.iloc[1, 12])  # Celda M2
    
    st.markdown(f"""
        <div style='text-align: center; background: rgba(75, 169, 195, 0.15); padding: 1rem; border-radius: 8px; margin: 1rem 0;'>
            <span style='font-size: 1.2rem; font-weight: 600; color: #2881AB;'>
                📊 Tasa actual: <span style='color: #F36B2D;'>{tasa:.2f} Bs/USD</span>
            </span>
            <br>
            <span style='font-size: 0.85rem; color: #A0A7AF;'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</span>
        </div>
    """, unsafe_allow_html=True)
    
except Exception as e:
    st.error("⚠️ No pudimos cargar la tasa actual desde nuestro sistema. Por favor, intenta nuevamente en unos momentos o contáctanos directamente por WhatsApp.")
    st.stop()

# Botones de monto rápido para bolívares
st.markdown("""
    <div class='montos-rapidos'>
        <span style='color: #2881AB; font-weight: 600; margin-right: 0.5rem;'>Montos rápidos:</span>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
monto_rapido_bs = None

with col1:
    if st.button("$50", key="rapido_50_bs"):
        monto_rapido_bs = 50.0
with col2:
    if st.button("$100", key="rapido_100_bs"):
        monto_rapido_bs = 100.0
with col3:
    if st.button("$500", key="rapido_500_bs"):
        monto_rapido_bs = 500.0
with col4:
    if st.button("$1000", key="rapido_1000_bs"):
        monto_rapido_bs = 1000.0

# Modo 1: De USD a Bs
st.markdown("<div class='label-campo'>📤 ¿Cuántos USD vas a enviar?</div>", unsafe_allow_html=True)
usd_enviar2 = st.number_input(
    "",
    min_value=0.0,
    step=1.0,
    key="usd_enviar",
    value=monto_rapido_bs if monto_rapido_bs else 0.0,
    help="Ingresa la cantidad en USD que vas a enviar",
    label_visibility="collapsed"
)

if usd_enviar2 > 0:
    bs_recibir2 = usd_enviar2 * tasa
    
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇻🇪 Recibirás: {bs_recibir2:,.2f} Bs</div>
            <div class='resultado-secundario'>Envías: ${usd_enviar2:.2f} USD | Tasa: {tasa:.2f} Bs/USD</div>
            <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.8;'>
                ℹ️ Cálculo inverso: Para recibir {bs_recibir2:,.2f} Bs, debes enviar ${usd_enviar2:.2f} USD
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar2:.2f} para recibir {bs_recibir2:.2f} Bs"
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
            <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
        </a>
    """, unsafe_allow_html=True)
elif usd_enviar2 < 0:
    st.error("⚠️ Por favor ingresa un monto válido mayor a $0")

st.markdown("---")

# Modo 2: De Bs a USD
st.markdown("<div class='label-campo'>📥 ¿Cuántos Bolívares quieres recibir?</div>", unsafe_allow_html=True)
bs_recibir = st.number_input(
    "",
    min_value=0.0,
    step=100.0,
    key="bs_recibir",
    help="Ingresa la cantidad en Bolívares que deseas recibir",
    label_visibility="collapsed"
)

if bs_recibir > 0:
    usd_enviar = bs_recibir / tasa
    
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💵 Debes enviar: ${usd_enviar:.2f} USD</div>
            <div class='resultado-secundario'>Recibirás: {bs_recibir:,.2f} Bs | Tasa: {tasa:.2f} Bs/USD</div>
            <div class='resultado-secundario' style='margin-top: 0.5rem; opacity: 0.8;'>
                ℹ️ Cálculo inverso: Si envías ${usd_enviar:.2f} USD, recibirás {bs_recibir:,.2f} Bs
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar:.2f} para recibir {bs_recibir:.2f} Bs"
    st.markdown(f"""
        <a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn">
            <span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora
        </a>
    """, unsafe_allow_html=True)
elif bs_recibir < 0:
    st.error("⚠️ Por favor ingresa un monto válido mayor a 0 Bs")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #A0A7AF; font-size: 0.9rem; padding: 2rem 0;'>
        <p><strong style='color: #2881AB;'>Wallet Cambios</strong> - Tu aliado en transferencias internacionales</p>
        <p>💬 ¿Tienes dudas? Contáctanos por WhatsApp</p>
    </div>
""", unsafe_allow_html=True)
