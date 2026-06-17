import streamlit as st

LISTA_MATERIAS = [
    "Selecionar...",
    "Inglês Instrumental",
    "Lógica Matemática",
    "Inovação Tecnológica", 
    "Introdução a Inteligência Artificial", 
    "Logica de Programação em IA", 
    "Comunicação Científica e Metodologia", 
    "Outra"
]

materiais = list (LISTA_MATERIAIS)

st.title("Seja Bem-Vindo ao Cálculo de Nota do Semestre")
st.header("Coloque sua média nas respectivas caixas de texto")

# Espaçamento vertical oficial do Streamlit para separar o header dos inputs
st.space("medium") 

n1 = st.number_input("Coloque a sua nota N1: ", step=10.0, min_value=0.0, max_value=100.0) 
n2 = st.number_input("Coloque a sua nota N2: ", step=10.0, min_value=0.0, max_value=100.0)

media = ((n1+n2)/2)/10

if media >= 7:
    st.subheader("Status: Aprovado")

elif media <= 5.99:
    st.subheader("Status: Reprovado")

else:
    st.subheader("Status: Recuperação")

st.write(f"Média: {media:.2f}")

st.divider()

if st.button("❌ Voltar ao Menu", use_container_width=True):
    st.session_state.pagina = "inicio"
    st.rerun()
