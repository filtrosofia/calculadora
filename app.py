import streamlit as st
import urllib.parse
from datetime import datetime
from styles import aplicar_estilos
from data_loader import cargar_tasas

# Configurar página con favicon
st.set_page_config(
    page_title="Calculadora Wallet Cambios", 
    layout="centered",
    page_icon="https://raw.githubusercontent.com/filtrosofia/calculadora/main/output-onlinepngtools.png"
)

# Aplicar estilos
aplicar_estilos()

# Cargar tasas
tasas = cargar_tasas()

# Número de WhatsApp
WHATSAPP_NUMBER = "584146108166"

# Inicializar session state para montos rápidos
for i in range(1, 11):
    if f'monto_calc{i}' not in st.session_state:
        st.session_state[f'monto_calc{i}'] = 0.0
    if f'monto_calc{i}b' not in st.session_state:
        st.session_state[f'monto_calc{i}b'] = 0.0

# Función para crear enlace de WhatsApp con mensaje personalizado
def crear_enlace_whatsapp(mensaje):
    mensaje_encoded = urllib.parse.quote(mensaje)
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={mensaje_encoded}"

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
        <strong>⏰ Horario de atención:</strong> Lunes a Sábados 8:00 AM - 6:00 PM | Domingos 9:00 AM - 1:00 PM
    </div>
""", unsafe_allow_html=True)

# ==================== MAPA DE ACCESOS RÁPIDOS ====================
st.markdown("""
    <div id='mapa-calculadoras' class='mapa-container'>
        <h3 class='mapa-titulo'>🧭 Acceso Rápido a Calculadoras</h3>
        <div class='mapa-grid'>
            <a href='#efectivo' class='mapa-link'>💵 Efectivo</a>
            <a href='#usd-bs' class='mapa-link'>USD ➜ Bs</a>
            <a href='#usd-cop' class='mapa-link'>USD ➜ COP</a>
            <a href='#cop-usd' class='mapa-link'>COP ➜ USD</a>
            <a href='#cop-bs' class='mapa-link'>COP ➜ Bs</a>
            <a href='#bs-cop' class='mapa-link'>Bs ➜ COP</a>
            <a href='#clp-bs' class='mapa-link'>CLP ➜ Bs</a>
            <a href='#clp-cop' class='mapa-link'>CLP ➜ COP</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ==================== CALCULADORA DE EFECTIVO ====================
st.markdown("<div id='efectivo'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>💵 Calculadora de Efectivo</h2>", unsafe_allow_html=True)
st.markdown("<p class='texto-info'>Comisión del <strong>5%</strong> aplicada</p>", unsafe_allow_html=True)
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("$50", key="rapido_50_calc1"):
        st.session_state.monto_calc1 = 50.0
        st.rerun()
with col2:
    if st.button("$100", key="rapido_100_calc1"):
        st.session_state.monto_calc1 = 100.0
        st.rerun()
with col3:
    if st.button("$200", key="rapido_200_calc1"):
        st.session_state.monto_calc1 = 200.0
        st.rerun()
with col4:
    if st.button("$300", key="rapido_300_calc1"):
        st.session_state.monto_calc1 = 300.0
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuánto deseas recibir en efectivo?</div>", unsafe_allow_html=True)
recibir = st.number_input("", min_value=0.0, step=1.0, key="recibir", value=st.session_state.monto_calc1, label_visibility="collapsed")

if recibir != st.session_state.monto_calc1:
    st.session_state.monto_calc1 = recibir

if recibir > 0:
    total_enviar = recibir / (1 - 0.05)
    comision = total_enviar - recibir
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💰 Debes enviar: ${total_enviar:.2f} USD</div>
            <div class='resultado-secundario'>Comisión: ${comision:.2f} | Recibirás: ${recibir:.2f}</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${total_enviar:.2f} para recibir ${recibir:.2f} en efectivo"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 2
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("$50", key="rapido_50_calc2"):
        st.session_state.monto_calc2 = 50.0
        st.rerun()
with col2:
    if st.button("$100", key="rapido_100_calc2"):
        st.session_state.monto_calc2 = 100.0
        st.rerun()
with col3:
    if st.button("$200", key="rapido_200_calc2"):
        st.session_state.monto_calc2 = 200.0
        st.rerun()
with col4:
    if st.button("$300", key="rapido_300_calc2"):
        st.session_state.monto_calc2 = 300.0
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuánto vas a enviar?</div>", unsafe_allow_html=True)
enviados = st.number_input("", min_value=0.0, step=1.0, key="enviados_manual", value=st.session_state.monto_calc2, label_visibility="collapsed")

if enviados != st.session_state.monto_calc2:
    st.session_state.monto_calc2 = enviados

if enviados > 0:
    recibir_estimado = enviados * (1 - 0.05)
    comision_enviados = enviados - recibir_estimado
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💵 Recibirás: ${recibir_estimado:.2f} USD</div>
            <div class='resultado-secundario'>Monto enviado: ${enviados:.2f} | Comisión: ${comision_enviados:.2f}</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${enviados:.2f} para recibir ${recibir_estimado:.2f}"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== USD A BOLÍVARES ====================
st.markdown("---")
st.markdown("<div id='usd-bs'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇻🇪 Calculadora USD a Bolívares</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_bs']:.2f} Bs/USD</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 3
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$20", key="rapido_20_calc3"):
        st.session_state.monto_calc3 = 20.0
        st.rerun()
with col2:
    if st.button("$50", key="rapido_50_calc3"):
        st.session_state.monto_calc3 = 50.0
        st.rerun()
with col3:
    if st.button("$100", key="rapido_100_calc3"):
        st.session_state.monto_calc3 = 100.0
        st.rerun()
with col4:
    if st.button("$200", key="rapido_200_calc3"):
        st.session_state.monto_calc3 = 200.0
        st.rerun()
with col5:
    if st.button("$500", key="rapido_500_calc3"):
        st.session_state.monto_calc3 = 500.0
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuántos USD vas a enviar?</div>", unsafe_allow_html=True)
usd_enviar_bs = st.number_input("", min_value=0.0, step=1.0, key="usd_enviar_bs", value=st.session_state.monto_calc3, label_visibility="collapsed")

if usd_enviar_bs != st.session_state.monto_calc3:
    st.session_state.monto_calc3 = usd_enviar_bs

if usd_enviar_bs > 0:
    bs_recibir = usd_enviar_bs * tasas['tasa_bs']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇻🇪 Recibirás: {bs_recibir:,.2f} Bs</div>
            <div class='resultado-secundario'>Envías: ${usd_enviar_bs:.2f} USD | Tasa: {tasas['tasa_bs']:.2f} Bs/USD</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar_bs:.2f} para recibir {bs_recibir:.2f} Bs"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 4
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (Bs):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
montos_bs = [20 * tasas['tasa_bs'], 50 * tasas['tasa_bs'], 100 * tasas['tasa_bs'], 200 * tasas['tasa_bs'], 500 * tasas['tasa_bs']]

with col1:
    if st.button(f"{montos_bs[0]:,.0f} Bs", key="rapido_bs1_calc4"):
        st.session_state.monto_calc4 = montos_bs[0]
        st.rerun()
with col2:
    if st.button(f"{montos_bs[1]:,.0f} Bs", key="rapido_bs2_calc4"):
        st.session_state.monto_calc4 = montos_bs[1]
        st.rerun()
with col3:
    if st.button(f"{montos_bs[2]:,.0f} Bs", key="rapido_bs3_calc4"):
        st.session_state.monto_calc4 = montos_bs[2]
        st.rerun()
with col4:
    if st.button(f"{montos_bs[3]:,.0f} Bs", key="rapido_bs4_calc4"):
        st.session_state.monto_calc4 = montos_bs[3]
        st.rerun()
with col5:
    if st.button(f"{montos_bs[4]:,.0f} Bs", key="rapido_bs5_calc4"):
        st.session_state.monto_calc4 = montos_bs[4]
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos Bolívares quieres recibir?</div>", unsafe_allow_html=True)
bs_deseado = st.number_input("", min_value=0.0, step=100.0, key="bs_deseado", value=st.session_state.monto_calc4, label_visibility="collapsed")

if bs_deseado != st.session_state.monto_calc4:
    st.session_state.monto_calc4 = bs_deseado

if bs_deseado > 0:
    usd_necesarios = bs_deseado / tasas['tasa_bs']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💵 Debes enviar: ${usd_necesarios:.2f} USD</div>
            <div class='resultado-secundario'>Recibirás: {bs_deseado:,.2f} Bs | Tasa: {tasas['tasa_bs']:.2f} Bs/USD</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${usd_necesarios:.2f} para recibir {bs_deseado:.2f} Bs"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== USD A COP ====================
st.markdown("---")
st.markdown("<div id='usd-cop'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇨🇴 Calculadora USD a COP</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_usd_cop_compra']:,.2f} COP/USD</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 5A
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos:</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$20", key="rapido_20_calc5"):
        st.session_state.monto_calc5 = 20.0
        st.rerun()
with col2:
    if st.button("$50", key="rapido_50_calc5"):
        st.session_state.monto_calc5 = 50.0
        st.rerun()
with col3:
    if st.button("$100", key="rapido_100_calc5"):
        st.session_state.monto_calc5 = 100.0
        st.rerun()
with col4:
    if st.button("$200", key="rapido_200_calc5"):
        st.session_state.monto_calc5 = 200.0
        st.rerun()
with col5:
    if st.button("$500", key="rapido_500_calc5"):
        st.session_state.monto_calc5 = 500.0
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuántos USD vas a enviar?</div>", unsafe_allow_html=True)
usd_enviar_cop = st.number_input("", min_value=0.0, step=1.0, key="usd_enviar_cop", value=st.session_state.monto_calc5, label_visibility="collapsed")

if usd_enviar_cop != st.session_state.monto_calc5:
    st.session_state.monto_calc5 = usd_enviar_cop

if usd_enviar_cop > 0:
    cop_recibir = usd_enviar_cop * tasas['tasa_usd_cop_compra']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇴 Recibirás: ${cop_recibir:,.2f} COP</div>
            <div class='resultado-secundario'>Envías: ${usd_enviar_cop:.2f} USD | Tasa: {tasas['tasa_usd_cop_compra']:,.2f} COP/USD</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${usd_enviar_cop:.2f} USD para recibir ${cop_recibir:,.2f} COP"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 5B
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$20K", key="rapido_20k_calc5b"):
        st.session_state.monto_calc5b = 20000.0
        st.rerun()
with col2:
    if st.button("$50K", key="rapido_50k_calc5b"):
        st.session_state.monto_calc5b = 50000.0
        st.rerun()
with col3:
    if st.button("$100K", key="rapido_100k_calc5b"):
        st.session_state.monto_calc5b = 100000.0
        st.rerun()
with col4:
    if st.button("$200K", key="rapido_200k_calc5b"):
        st.session_state.monto_calc5b = 200000.0
        st.rerun()
with col5:
    if st.button("$400K", key="rapido_400k_calc5b"):
        st.session_state.monto_calc5b = 400000.0
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos COP quieres recibir?</div>", unsafe_allow_html=True)
cop_deseado = st.number_input("", min_value=0.0, step=1000.0, key="cop_deseado", value=st.session_state.monto_calc5b, label_visibility="collapsed")

if cop_deseado != st.session_state.monto_calc5b:
    st.session_state.monto_calc5b = cop_deseado

if cop_deseado > 0:
    usd_necesarios_cop = cop_deseado / tasas['tasa_usd_cop_compra']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💵 Debes enviar: ${usd_necesarios_cop:.2f} USD</div>
            <div class='resultado-secundario'>Recibirás: ${cop_deseado:,.2f} COP | Tasa: {tasas['tasa_usd_cop_compra']:,.2f} COP/USD</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${usd_necesarios_cop:.2f} USD para recibir ${cop_deseado:,.2f} COP"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== COP A USD ====================
st.markdown("---")
st.markdown("<div id='cop-usd'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇨🇴 Calculadora COP a USD</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_cop_usd_venta']:,.2f} COP/USD</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 6A
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$100K", key="rapido_100k_calc6"):
        st.session_state.monto_calc6 = 100000.0
        st.rerun()
with col2:
    if st.button("$200K", key="rapido_200k_calc6"):
        st.session_state.monto_calc6 = 200000.0
        st.rerun()
with col3:
    if st.button("$300K", key="rapido_300k_calc6"):
        st.session_state.monto_calc6 = 300000.0
        st.rerun()
with col4:
    if st.button("$400K", key="rapido_400k_calc6"):
        st.session_state.monto_calc6 = 400000.0
        st.rerun()
with col5:
    if st.button("$500K", key="rapido_500k_calc6"):
        st.session_state.monto_calc6 = 500000.0
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos Pesos Colombianos vas a enviar?</div>", unsafe_allow_html=True)
cop_enviar_usd = st.number_input("", min_value=0.0, step=1000.0, key="cop_enviar_usd", value=st.session_state.monto_calc6, label_visibility="collapsed")

if cop_enviar_usd != st.session_state.monto_calc6:
    st.session_state.monto_calc6 = cop_enviar_usd

if cop_enviar_usd > 0:
    usd_recibir = cop_enviar_usd / tasas['tasa_cop_usd_venta']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>💵 Recibirás: ${usd_recibir:.2f} USD</div>
            <div class='resultado-secundario'>Envías: ${cop_enviar_usd:,.2f} COP | Tasa: {tasas['tasa_cop_usd_venta']:,.2f} COP/USD</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${cop_enviar_usd:,.2f} COP para recibir ${usd_recibir:.2f} USD"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 6B
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (USD):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$20", key="rapido_20_calc6b"):
        st.session_state.monto_calc6b = 20.0
        st.rerun()
with col2:
    if st.button("$50", key="rapido_50_calc6b"):
        st.session_state.monto_calc6b = 50.0
        st.rerun()
with col3:
    if st.button("$100", key="rapido_100_calc6b"):
        st.session_state.monto_calc6b = 100.0
        st.rerun()
with col4:
    if st.button("$200", key="rapido_200_calc6b"):
        st.session_state.monto_calc6b = 200.0
        st.rerun()
with col5:
    if st.button("$500", key="rapido_500_calc6b"):
        st.session_state.monto_calc6b = 500.0
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos USD quieres recibir?</div>", unsafe_allow_html=True)
usd_deseado = st.number_input("", min_value=0.0, step=1.0, key="usd_deseado", value=st.session_state.monto_calc6b, label_visibility="collapsed")

if usd_deseado != st.session_state.monto_calc6b:
    st.session_state.monto_calc6b = usd_deseado

if usd_deseado > 0:
    cop_necesarios = usd_deseado * tasas['tasa_cop_usd_venta']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇴 Debes enviar: ${cop_necesarios:,.2f} COP</div>
            <div class='resultado-secundario'>Recibirás: ${usd_deseado:.2f} USD | Tasa: {tasas['tasa_cop_usd_venta']:,.2f} COP/USD</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${cop_necesarios:,.2f} COP para recibir ${usd_deseado:.2f} USD"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== COP A BS ====================
st.markdown("---")
st.markdown("<div id='cop-bs'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇨🇴➡️🇻🇪 Calculadora COP a Bolívares</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_cop_bs']:,.2f} COP/Bs</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 7A
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$100K", key="rapido_100k_calc7"):
        st.session_state.monto_calc7 = 100000.0
        st.rerun()
with col2:
    if st.button("$200K", key="rapido_200k_calc7"):
        st.session_state.monto_calc7 = 200000.0
        st.rerun()
with col3:
    if st.button("$300K", key="rapido_300k_calc7"):
        st.session_state.monto_calc7 = 300000.0
        st.rerun()
with col4:
    if st.button("$400K", key="rapido_400k_calc7"):
        st.session_state.monto_calc7 = 400000.0
        st.rerun()
with col5:
    if st.button("$500K", key="rapido_500k_calc7"):
        st.session_state.monto_calc7 = 500000.0
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuántos COP vas a enviar?</div>", unsafe_allow_html=True)
cop_enviar_bs = st.number_input("", min_value=0.0, step=1000.0, key="cop_enviar_bs", value=st.session_state.monto_calc7, label_visibility="collapsed")

if cop_enviar_bs != st.session_state.monto_calc7:
    st.session_state.monto_calc7 = cop_enviar_bs

if cop_enviar_bs > 0:
    bs_recibir_cop = cop_enviar_bs / tasas['tasa_cop_bs']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇻🇪 Recibirás: {bs_recibir_cop:,.2f} Bs</div>
            <div class='resultado-secundario'>Envías: ${cop_enviar_bs:,.2f} COP | Tasa: {tasas['tasa_cop_bs']:,.2f} COP/Bs</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${cop_enviar_bs:,.2f} COP para recibir {bs_recibir_cop:,.2f} Bs"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 7B
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (Bs):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
montos_bs_calc7b = [20 * tasas['tasa_bs'], 50 * tasas['tasa_bs'], 100 * tasas['tasa_bs'], 200 * tasas['tasa_bs'], 500 * tasas['tasa_bs']]

with col1:
    if st.button(f"{montos_bs_calc7b[0]:,.0f} Bs", key="rapido_bs1_calc7b"):
        st.session_state.monto_calc7b = montos_bs_calc7b[0]
        st.rerun()
with col2:
    if st.button(f"{montos_bs_calc7b[1]:,.0f} Bs", key="rapido_bs2_calc7b"):
        st.session_state.monto_calc7b = montos_bs_calc7b[1]
        st.rerun()
with col3:
    if st.button(f"{montos_bs_calc7b[2]:,.0f} Bs", key="rapido_bs3_calc7b"):
        st.session_state.monto_calc7b = montos_bs_calc7b[2]
        st.rerun()
with col4:
    if st.button(f"{montos_bs_calc7b[3]:,.0f} Bs", key="rapido_bs4_calc7b"):
        st.session_state.monto_calc7b = montos_bs_calc7b[3]
        st.rerun()
with col5:
    if st.button(f"{montos_bs_calc7b[4]:,.0f} Bs", key="rapido_bs5_calc7b"):
        st.session_state.monto_calc7b = montos_bs_calc7b[4]
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos Bs quieres recibir?</div>", unsafe_allow_html=True)
bs_deseado_cop = st.number_input("", min_value=0.0, step=100.0, key="bs_deseado_cop", value=st.session_state.monto_calc7b, label_visibility="collapsed")

if bs_deseado_cop != st.session_state.monto_calc7b:
    st.session_state.monto_calc7b = bs_deseado_cop

if bs_deseado_cop > 0:
    cop_necesarios_bs = bs_deseado_cop * tasas['tasa_cop_bs']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇴 Debes enviar: ${cop_necesarios_bs:,.2f} COP</div>
            <div class='resultado-secundario'>Recibirás: {bs_deseado_cop:,.2f} Bs | Tasa: {tasas['tasa_cop_bs']:,.2f} COP/Bs</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${cop_necesarios_bs:,.2f} COP para recibir {bs_deseado_cop:,.2f} Bs"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== BS A COP ====================
st.markdown("---")
st.markdown("<div id='bs-cop'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇻🇪➡️🇨🇴 Calculadora Bolívares a COP</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_bs_cop']:,.2f} Bs/COP</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 8A
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (Bs):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
montos_bs_calc8 = [20 * tasas['tasa_bs'], 50 * tasas['tasa_bs'], 100 * tasas['tasa_bs'], 200 * tasas['tasa_bs'], 500 * tasas['tasa_bs']]

with col1:
    if st.button(f"{montos_bs_calc8[0]:,.0f} Bs", key="rapido_bs1_calc8"):
        st.session_state.monto_calc8 = montos_bs_calc8[0]
        st.rerun()
with col2:
    if st.button(f"{montos_bs_calc8[1]:,.0f} Bs", key="rapido_bs2_calc8"):
        st.session_state.monto_calc8 = montos_bs_calc8[1]
        st.rerun()
with col3:
    if st.button(f"{montos_bs_calc8[2]:,.0f} Bs", key="rapido_bs3_calc8"):
        st.session_state.monto_calc8 = montos_bs_calc8[2]
        st.rerun()
with col4:
    if st.button(f"{montos_bs_calc8[3]:,.0f} Bs", key="rapido_bs4_calc8"):
        st.session_state.monto_calc8 = montos_bs_calc8[3]
        st.rerun()
with col5:
    if st.button(f"{montos_bs_calc8[4]:,.0f} Bs", key="rapido_bs5_calc8"):
        st.session_state.monto_calc8 = montos_bs_calc8[4]
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuántos Bs vas a enviar?</div>", unsafe_allow_html=True)
bs_enviar_cop = st.number_input("", min_value=0.0, step=100.0, key="bs_enviar_cop", value=st.session_state.monto_calc8, label_visibility="collapsed")

if bs_enviar_cop != st.session_state.monto_calc8:
    st.session_state.monto_calc8 = bs_enviar_cop

if bs_enviar_cop > 0:
    cop_recibir_bs = bs_enviar_cop * tasas['tasa_bs_cop']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇴 Recibirás: ${cop_recibir_bs:,.2f} COP</div>
            <div class='resultado-secundario'>Envías: {bs_enviar_cop:,.2f} Bs | Tasa: {tasas['tasa_bs_cop']:,.2f} Bs/COP</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar {bs_enviar_cop:,.2f} Bs para recibir ${cop_recibir_bs:,.2f} COP"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 8B
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$100K", key="rapido_100k_calc8b"):
        st.session_state.monto_calc8b = 100000.0
        st.rerun()
with col2:
    if st.button("$200K", key="rapido_200k_calc8b"):
        st.session_state.monto_calc8b = 200000.0
        st.rerun()
with col3:
    if st.button("$300K", key="rapido_300k_calc8b"):
        st.session_state.monto_calc8b = 300000.0
        st.rerun()
with col4:
    if st.button("$400K", key="rapido_400k_calc8b"):
        st.session_state.monto_calc8b = 400000.0
        st.rerun()
with col5:
    if st.button("$500K", key="rapido_500k_calc8b"):
        st.session_state.monto_calc8b = 500000.0
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos COP quieres recibir?</div>", unsafe_allow_html=True)
cop_deseado_bs = st.number_input("", min_value=0.0, step=1000.0, key="cop_deseado_bs", value=st.session_state.monto_calc8b, label_visibility="collapsed")

if cop_deseado_bs != st.session_state.monto_calc8b:
    st.session_state.monto_calc8b = cop_deseado_bs

if cop_deseado_bs > 0:
    bs_necesarios = cop_deseado_bs / tasas['tasa_bs_cop']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇻🇪 Debes enviar: {bs_necesarios:,.2f} Bs</div>
            <div class='resultado-secundario'>Recibirás: ${cop_deseado_bs:,.2f} COP | Tasa: {tasas['tasa_bs_cop']:,.2f} Bs/COP</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar {bs_necesarios:,.2f} Bs para recibir ${cop_deseado_bs:,.2f} COP"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== CLP A BS ====================
st.markdown("---")
st.markdown("<div id='clp-bs'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇨🇱➡️🇻🇪 Calculadora CLP a Bolívares</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_clp_bs']:,.2f} CLP/Bs</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 9A
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (CLP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("5.000", key="rapido_5k_calc9"):
        st.session_state.monto_calc9 = 5000.0
        st.rerun()
with col2:
    if st.button("10.000", key="rapido_10k_calc9"):
        st.session_state.monto_calc9 = 10000.0
        st.rerun()
with col3:
    if st.button("20.000", key="rapido_20k_calc9"):
        st.session_state.monto_calc9 = 20000.0
        st.rerun()
with col4:
    if st.button("50.000", key="rapido_50k_calc9"):
        st.session_state.monto_calc9 = 50000.0
        st.rerun()
with col5:
    if st.button("100.000", key="rapido_100k_calc9"):
        st.session_state.monto_calc9 = 100000.0
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuántos CLP vas a enviar?</div>", unsafe_allow_html=True)
clp_enviar_bs = st.number_input("", min_value=0.0, step=1000.0, key="clp_enviar_bs", value=st.session_state.monto_calc9, label_visibility="collapsed")

if clp_enviar_bs != st.session_state.monto_calc9:
    st.session_state.monto_calc9 = clp_enviar_bs

if clp_enviar_bs > 0:
    bs_recibir_clp = clp_enviar_bs * tasas['tasa_clp_bs']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇻🇪 Recibirás: {bs_recibir_clp:,.2f} Bs</div>
            <div class='resultado-secundario'>Envías: ${clp_enviar_bs:,.0f} CLP | Tasa: {tasas['tasa_clp_bs']:,.2f} CLP/Bs</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${clp_enviar_bs:,.0f} CLP para recibir {bs_recibir_clp:,.2f} Bs"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 9B
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (Bs):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
montos_bs_calc9b = [20 * tasas['tasa_bs'], 50 * tasas['tasa_bs'], 100 * tasas['tasa_bs'], 200 * tasas['tasa_bs'], 500 * tasas['tasa_bs']]

with col1:
    if st.button(f"{montos_bs_calc9b[0]:,.0f} Bs", key="rapido_bs1_calc9b"):
        st.session_state.monto_calc9b = montos_bs_calc9b[0]
        st.rerun()
with col2:
    if st.button(f"{montos_bs_calc9b[1]:,.0f} Bs", key="rapido_bs2_calc9b"):
        st.session_state.monto_calc9b = montos_bs_calc9b[1]
        st.rerun()
with col3:
    if st.button(f"{montos_bs_calc9b[2]:,.0f} Bs", key="rapido_bs3_calc9b"):
        st.session_state.monto_calc9b = montos_bs_calc9b[2]
        st.rerun()
with col4:
    if st.button(f"{montos_bs_calc9b[3]:,.0f} Bs", key="rapido_bs4_calc9b"):
        st.session_state.monto_calc9b = montos_bs_calc9b[3]
        st.rerun()
with col5:
    if st.button(f"{montos_bs_calc9b[4]:,.0f} Bs", key="rapido_bs5_calc9b"):
        st.session_state.monto_calc9b = montos_bs_calc9b[4]
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos Bs quieres recibir?</div>", unsafe_allow_html=True)
bs_deseado_clp = st.number_input("", min_value=0.0, step=100.0, key="bs_deseado_clp", value=st.session_state.monto_calc9b, label_visibility="collapsed")

if bs_deseado_clp != st.session_state.monto_calc9b:
    st.session_state.monto_calc9b = bs_deseado_clp

if bs_deseado_clp > 0:
    clp_necesarios = bs_deseado_clp / tasas['tasa_clp_bs']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇱 Debes enviar: ${clp_necesarios:,.0f} CLP</div>
            <div class='resultado-secundario'>Recibirás: {bs_deseado_clp:,.2f} Bs | Tasa: {tasas['tasa_clp_bs']:,.2f} CLP/Bs</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${clp_necesarios:,.0f} CLP para recibir {bs_deseado_clp:,.2f} Bs"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# ==================== CLP A COP ====================
st.markdown("---")
st.markdown("<div id='clp-cop'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitulo-calculadora'>🇨🇱➡️🇨🇴 Calculadora CLP a COP</h2>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='tasa-box'>
        <div class='tasa-principal'>📊 Tasa actual: <span style='color: #F36B2D;'>{tasas['tasa_clp_cop']:,.2f} CLP/COP</span></div>
        <div class='tasa-secundaria'>Actualizado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</div>
    </div>
""", unsafe_allow_html=True)

# CALC 10A
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (CLP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("5.000", key="rapido_5k_calc10"):
        st.session_state.monto_calc10 = 5000.0
        st.rerun()
with col2:
    if st.button("10.000", key="rapido_10k_calc10"):
        st.session_state.monto_calc10 = 10000.0
        st.rerun()
with col3:
    if st.button("20.000", key="rapido_20k_calc10"):
        st.session_state.monto_calc10 = 20000.0
        st.rerun()
with col4:
    if st.button("50.000", key="rapido_50k_calc10"):
        st.session_state.monto_calc10 = 50000.0
        st.rerun()
with col5:
    if st.button("100.000", key="rapido_100k_calc10"):
        st.session_state.monto_calc10 = 100000.0
        st.rerun()

st.markdown("<div class='label-campo'>📤 ¿Cuántos CLP vas a enviar?</div>", unsafe_allow_html=True)
clp_enviar_cop = st.number_input("", min_value=0.0, step=1000.0, key="clp_enviar_cop", value=st.session_state.monto_calc10, label_visibility="collapsed")

if clp_enviar_cop != st.session_state.monto_calc10:
    st.session_state.monto_calc10 = clp_enviar_cop

if clp_enviar_cop > 0:
    cop_recibir_clp = clp_enviar_cop * tasas['tasa_clp_cop']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇴 Recibirás: ${cop_recibir_clp:,.2f} COP</div>
            <div class='resultado-secundario'>Envías: ${clp_enviar_cop:,.0f} CLP | Tasa: {tasas['tasa_clp_cop']:,.2f} CLP/COP</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${clp_enviar_cop:,.0f} CLP para recibir ${cop_recibir_clp:,.2f} COP"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

st.markdown("---")

# CALC 10B
st.markdown("<div class='montos-rapidos-label'>⚡ Montos rápidos (COP):</div>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("$100K", key="rapido_100k_calc10b"):
        st.session_state.monto_calc10b = 100000.0
        st.rerun()
with col2:
    if st.button("$200K", key="rapido_200k_calc10b"):
        st.session_state.monto_calc10b = 200000.0
        st.rerun()
with col3:
    if st.button("$300K", key="rapido_300k_calc10b"):
        st.session_state.monto_calc10b = 300000.0
        st.rerun()
with col4:
    if st.button("$400K", key="rapido_400k_calc10b"):
        st.session_state.monto_calc10b = 400000.0
        st.rerun()
with col5:
    if st.button("$500K", key="rapido_500k_calc10b"):
        st.session_state.monto_calc10b = 500000.0
        st.rerun()

st.markdown("<div class='label-campo'>📥 ¿Cuántos COP quieres recibir?</div>", unsafe_allow_html=True)
cop_deseado_clp = st.number_input("", min_value=0.0, step=1000.0, key="cop_deseado_clp", value=st.session_state.monto_calc10b, label_visibility="collapsed")

if cop_deseado_clp != st.session_state.monto_calc10b:
    st.session_state.monto_calc10b = cop_deseado_clp

if cop_deseado_clp > 0:
    clp_necesarios_cop = cop_deseado_clp / tasas['tasa_clp_cop']
    st.markdown(f"""
        <div class='resultado-container'>
            <div class='resultado-principal'>🇨🇱 Debes enviar: ${clp_necesarios_cop:,.0f} CLP</div>
            <div class='resultado-secundario'>Recibirás: ${cop_deseado_clp:,.2f} COP | Tasa: {tasas['tasa_clp_cop']:,.2f} CLP/COP</div>
        </div>
    """, unsafe_allow_html=True)
    mensaje_whatsapp = f"Hola, necesito enviar ${clp_necesarios_cop:,.0f} CLP para recibir ${cop_deseado_clp:,.2f} COP"
    st.markdown(f"""<a href="{crear_enlace_whatsapp(mensaje_whatsapp)}" target="_blank" class="whatsapp-btn"><span style="font-size: 1.5rem;">💬</span> Realiza el cambio ahora</a>""", unsafe_allow_html=True)

# Botón volver arriba
st.markdown("""
    <a href='#mapa-calculadoras' class='volver-arriba'>
        ⬆️ Volver arriba
    </a>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div class='footer'>
        <p><strong>Wallet Cambios</strong> · La solución a tu problema cambiario</p>
    </div>
""", unsafe_allow_html=True)
