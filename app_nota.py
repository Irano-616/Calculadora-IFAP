import streamlit as st

st.title("Seja Bem-Vindo ao Cálculo de Nota do Semestre")
st.header("Coloque sua média nas respectivas caixas de texto")

st.space() # O espaço entre o st.header e as variaveis n1 e n2

n1 = st.number_input("Coloque a sua nota N1: ", step=None) 
n2 = st.number_input("Coloque a sua nota N2: ", step=None)

media = ((n1+n2)/2)/10

if media >= 7:
    st.subheader("Status: Aprovado")

elif media <= 5.99:
    st.subheader("Status: Reprovado")

else:
    st.subheader("Status: Recuperação")

st. write(f"Média: {media:.2f}")

st.divider()

if st.button("❌ Voltar ao Menu", use_container_width=True):
    st.session_state.pagina = "inicio"
    st.rerun()
