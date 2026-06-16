import streamlit as st

st.title("Calculadora de IRA")

# Lista de matérias comuns (você pode alterar ou adicionar mais nomes aqui)
LISTA_MATERIAS = [
    "Selecionar...", "Matemática", "Cálculo I", "Cálculo II", "Física I", 
    "Física II", "Química", "Programação", "Álgebra Linear", 
    "Geometria Analítica", "Algoritmos", "Estrutura de Dados", "Outra"
]

soma_pontos = 0.0
soma_creditos = 0

# Cabeçalho das colunas
c1, c2, c3 = st.columns([2, 1, 1]) # O primeiro número (2) deixa a coluna do nome mais larga
c1.write("**Matéria**")
c2.write("**Nota**")
c3.write("**Créditos**")

# Loop para gerar as 5 linhas de matérias
for i in range(5):
    col_nome, col_nota, col_cred = st.columns([2, 1, 1])
    
    with col_nome:
        # Caixa de seleção para o aluno escolher a matéria
        materia_selecionada = st.selectbox("", LISTA_MATERIAS, key=f"m_{i}", label_visibility="collapsed")
    with col_nota:
        nota = st.number_input("", min_value=0.0, max_value=10.0, value=0.0, key=f"n_{i}", label_visibility="collapsed")
    with col_cred:
        cred = st.number_input("", min_value=0, value=0, key=f"c_{i}", label_visibility="collapsed")
        
    soma_pontos += nota * cred
    soma_creditos += cred

# Exibe o resultado final
if soma_creditos > 0:
    ira = soma_pontos / soma_creditos
    st.write(f"### Seu IRA: {ira:.2f}")
else:
    st.write("Selecione as matérias e digite as notas e créditos acima.")

st.divider()

if st.button("❌ Voltar ao Menu", use_container_width=True):
    st.session_state.pagina = "inicio"
    st.rerun()