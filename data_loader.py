import pandas as pd
import streamlit as st

# URLs de Google Sheets
SHEET_URL = "https://docs.google.com/spreadsheets/d/1ig4ihkUIeP7kaaR6yZeyOLF7j38Y_peytGKG6tgkqbw/gviz/tq?tqx=out:csv&sheet=TASAS%20COL%20-%20VEN"
SHEET_URL_TASAS_MAYOR = "https://docs.google.com/spreadsheets/d/1ig4ihkUIeP7kaaR6yZeyOLF7j38Y_peytGKG6tgkqbw/gviz/tq?tqx=out:csv&sheet=Tasas%20al%20mayor"

def limpiar_valor(valor):
    """Limpia valores eliminando $, espacios y comas para convertir a float"""
    return float(str(valor).replace('$', '').replace(',', '').strip())

def cargar_tasas():
    """Carga todas las tasas desde Google Sheets"""
    try:
        # Cargar primera hoja
        df = pd.read_csv(SHEET_URL, header=None)
        tasa_bs = float(df.iloc[1, 12])  # M2
        tasa_usd_cop_compra = float(df.iloc[3, 12])  # M4
        tasa_cop_usd_venta = float(df.iloc[3, 13])  # N4
        
        # Cargar segunda hoja
        df_mayor = pd.read_csv(SHEET_URL_TASAS_MAYOR, header=None, skip_blank_lines=False)
        
        # Buscar las tasas por nombre y limpiar
        tasa_bs_cop = limpiar_valor(df_mayor[df_mayor[0] == 've/cop'][1].values[0])
        tasa_cop_bs = limpiar_valor(df_mayor[df_mayor[0] == 'cop/ves'][1].values[0])
        tasa_clp_bs = limpiar_valor(df_mayor[df_mayor[0] == 'clp/ves'][1].values[0])
        tasa_clp_cop = limpiar_valor(df_mayor[df_mayor[0] == 'clp/cop'][1].values[0])
        
        return {
            'tasa_bs': tasa_bs,
            'tasa_usd_cop_compra': tasa_usd_cop_compra,
            'tasa_cop_usd_venta': tasa_cop_usd_venta,
            'tasa_bs_cop': tasa_bs_cop,
            'tasa_cop_bs': tasa_cop_bs,
            'tasa_clp_bs': tasa_clp_bs,
            'tasa_clp_cop': tasa_clp_cop
        }
        
    except Exception as e:
        st.error("⚠️ No pudimos cargar las tasas desde nuestro sistema. Por favor, intenta nuevamente en unos momentos o contáctanos directamente por WhatsApp.")
        st.stop()