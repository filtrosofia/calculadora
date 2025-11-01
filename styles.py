import streamlit as st

def aplicar_estilos():
    """Aplica todos los estilos CSS de la aplicación"""
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@300;400;600&display=swap');
            
            :root {
                --bg-primary: #0f1419;
                --bg-secondary: #1a2332;
                --bg-card: #253142;
                --text-primary: #ffffff;
                --text-secondary: #b8c5d6;
                --text-muted: #8b98a8;
                --shadow-color: rgba(0,0,0,0.5);
                --azul-brillante: #4BA9C3;
                --azul-medio: #3D9FC2;
                --azul-profundo: #2881AB;
                --naranja-energia: #F36B2D;
                --amarillo-calido: #FFC542;
                --verde-whatsapp: #25D366;
            }
            
            .stApp {
                background: linear-gradient(135deg, #0f1419 0%, #1a2332 100%);
                font-family: 'Open Sans', sans-serif;
                color: var(--text-primary);
            }
            
            .logo-container {
                text-align: center;
                margin-bottom: 2rem;
                animation: fadeInDown 0.8s ease-out;
            }
            
            .logo-container img {
                width: clamp(90px, 15vw, 140px);
                filter: drop-shadow(0 4px 8px var(--shadow-color));
                transition: transform 0.3s ease;
            }
            
            .logo-container img:hover {
                transform: scale(1.05);
            }
            
            .titulo-principal {
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: clamp(1.8rem, 4vw, 2.5rem);
                text-align: center;
                color: var(--azul-brillante);
                margin-bottom: 0.5rem;
                animation: fadeInUp 0.8s ease-out;
                text-shadow: 0 2px 4px var(--shadow-color);
            }
            
            .subtitulo-calculadora {
                font-family: 'Montserrat', sans-serif;
                font-weight: 600;
                font-size: clamp(1.3rem, 3vw, 1.8rem);
                text-align: center;
                color: #4BA9C3;
                margin: 2rem 0 1rem 0;
                padding: 1rem;
                background: rgba(75, 169, 195, 0.15);
                border-radius: 12px;
                border: 2px solid var(--azul-brillante);
            }
            
            .label-campo {
                font-family: 'Open Sans', sans-serif;
                font-weight: 600;
                font-size: clamp(1rem, 2vw, 1.15rem);
                color: var(--text-primary);
                margin: 1.5rem 0 0.5rem 0;
            }
            
            .texto-info {
                text-align: center;
                color: var(--text-secondary);
                font-size: clamp(0.9rem, 1.8vw, 1rem);
                margin: 0.5rem 0;
            }
            
            .stNumberInput > div > div > input {
                border: 2px solid var(--azul-brillante);
                border-radius: 10px;
                padding: 0.75rem;
                font-size: clamp(1rem, 2vw, 1.1rem);
                transition: all 0.3s ease;
                font-family: 'Open Sans', sans-serif;
                background: var(--bg-card);
                color: var(--text-primary);
            }
            
            .stNumberInput > div > div > input:focus {
                border-color: var(--naranja-energia);
                box-shadow: 0 0 0 3px rgba(243, 107, 45, 0.2);
                outline: none;
            }
            
            .resultado-container {
                background: linear-gradient(135deg, #4BA9C3 0%, #2881AB 100%);
                color: white;
                padding: 1.5rem;
                border-radius: 12px;
                margin: 1rem 0;
                box-shadow: 0 8px 20px rgba(40, 129, 171, 0.4);
                animation: slideInUp 0.5s ease-out;
            }
            
            .resultado-principal {
                font-family: 'Montserrat', sans-serif;
                font-weight: 700;
                font-size: clamp(1.3rem, 3vw, 1.6rem);
                margin-bottom: 0.5rem;
                color: #ffffff;
            }
            
            .resultado-secundario {
                font-family: 'Open Sans', sans-serif;
                font-size: clamp(0.95rem, 2vw, 1.1rem);
                opacity: 0.95;
                color: #ffffff;
            }
            
            .montos-rapidos-label {
                color: var(--text-primary);
                font-weight: 600;
                font-size: clamp(0.9rem, 1.8vw, 1rem);
                margin-bottom: 0.75rem;
                display: block;
            }
            
            .info-box {
                background: rgba(255, 197, 66, 0.2);
                border-left: 4px solid var(--amarillo-calido);
                padding: 1rem;
                border-radius: 8px;
                margin: 1rem 0;
                font-family: 'Open Sans', sans-serif;
                font-size: clamp(0.9rem, 1.8vw, 1rem);
                color: var(--text-primary);
            }
            
            .tasa-box {
                text-align: center;
                background: rgba(75, 169, 195, 0.2);
                padding: 1.2rem;
                border-radius: 12px;
                margin: 1rem 0;
                border: 2px solid var(--azul-brillante);
            }
            
            .tasa-principal {
                font-size: clamp(1.1rem, 2.5vw, 1.4rem);
                font-weight: 600;
                color: var(--azul-brillante);
                margin-bottom: 0.3rem;
            }
            
            .tasa-secundaria {
                font-size: clamp(0.8rem, 1.5vw, 0.9rem);
                color: var(--text-muted);
            }
            
            .whatsapp-btn {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 0.5rem;
                background: linear-gradient(135deg, #25D366 0%, #20BA5A 100%);
                color: white;
                padding: clamp(0.9rem, 2vw, 1.1rem) clamp(1.5rem, 3vw, 2rem);
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
            
            .footer {
                text-align: center;
                color: var(--text-muted);
                font-size: clamp(0.9rem, 1.8vw, 1rem);
                padding: 3rem 0 2rem 0;
                margin-top: 3rem;
                border-top: 1px solid rgba(255,255,255,0.1);
            }
            
            .footer strong {
                color: var(--azul-brillante);
            }
            
            @keyframes fadeInDown {
                from { opacity: 0; transform: translateY(-30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            @keyframes fadeInUp {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            @keyframes slideInUp {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            .stButton > button {
                width: 100%;
                border-radius: 8px;
                border: 2px solid var(--azul-brillante);
                background: rgba(75, 169, 195, 0.15);
                color: var(--text-primary);
                font-weight: 600;
                padding: 0.6rem 1rem;
                transition: all 0.3s ease;
                font-family: 'Montserrat', sans-serif;
            }
            
            .stButton > button:hover {
                background: var(--azul-brillante);
                color: white;
                border-color: var(--azul-brillante);
                transform: translateY(-2px);
            }
                
            /* Mapa de accesos rápidos */
        .mapa-container {
            background: rgba(75, 169, 195, 0.1);
            border: 2px solid var(--azul-brillante);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 2rem 0;
        }
        
        .mapa-titulo {
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: clamp(1.1rem, 2.5vw, 1.4rem);
            color: var(--azul-brillante);
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .mapa-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 0.8rem;
        }
        
        @media (min-width: 768px) {
            .mapa-grid {
                grid-template-columns: repeat(4, 1fr);
            }
        }
        
        .mapa-link {
            background: rgba(75, 169, 195, 0.15);
            border: 2px solid var(--azul-brillante);
            border-radius: 8px;
            padding: 0.7rem;
            text-align: center;
            text-decoration: none;
            color: var(--text-primary);
            font-family: 'Open Sans', sans-serif;
            font-weight: 600;
            font-size: clamp(0.85rem, 1.8vw, 0.95rem);
            transition: all 0.3s ease;
            display: block;
        }
        
        .mapa-link:hover {
            background: var(--azul-brillante);
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(75, 169, 195, 0.4);
        }
        
        /* Botón volver arriba */
        .volver-arriba {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: linear-gradient(135deg, #4BA9C3 0%, #2881AB 100%);
            color: white;
            padding: 0.8rem 1.2rem;
            border-radius: 25px;
            text-decoration: none;
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: 0.9rem;
            box-shadow: 0 4px 15px rgba(40, 129, 171, 0.5);
            transition: all 0.3s ease;
            z-index: 999;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        
        .volver-arriba:hover {
            background: linear-gradient(135deg, #3D9FC2 0%, #2881AB 100%);
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(40, 129, 171, 0.6);
        }
        
        /* Smooth scroll */
        html {
            scroll-behavior: smooth;
        }
        </style>
    """, unsafe_allow_html=True)