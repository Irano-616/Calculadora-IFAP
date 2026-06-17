import streamlit as st

st.set_page_config(
    page_title = "Sistema IFAP",
    layout = "centered",
    initial_sidebar_state = "collapsed"
)

# Injeção de CSS genérico para injetar o efeito em qualquer botão da tela
st.markdown(
    """
    <style>
        /* Aplica as alterações de tamanho em todos os botões do app */
        .stButton > button {
            width: 100% !important;
            height: 55px !important;
            font-size: 18px !important;
            transition: transform 0.2s ease-in-out !important;
        }
        
        /* Aplica o efeito de crescimento (zoom sutil) ao passar o mouse */
        .stButton > button:hover {
            transform: scale(1.04) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if st.session_state.pagina == "inicio":
    st.title("🟢 Sistema Acadêmico IFAP")

    if st.button("Calculadora da Nota 📊", type = "primary"):
        st.session_state.pagina = "nota"
        st.rerun()

    elif st.button("Calculadora de IRA", type = "primary"):
        st.session_state.pagina = "ira"
        st.rerun()

elif st.session_state.pagina == "nota":
    with open("app_nota.py", encoding = "utf-8") as f:
        exec(f.read())

elif st.session_state.pagina == "ira":
    with open("app_IRA.py", encoding = "utf-8") as f:
        exec(f.read())

