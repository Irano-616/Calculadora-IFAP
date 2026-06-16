import streamlit as st

st.set_page_config(
    page_title = "Sistema IFAP",
    layout = "centered",
    initial_sidebar_state = "collapsed"
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