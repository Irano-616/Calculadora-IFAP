import streamlit as st

st.title("Calculadora de IRA")

# Lista de matérias comuns (você pode alterar ou adicionar mais nomes aqui)
LISTA_MATERIAS = [
    "Selecionar...", "Inglês Instrumental", "Lógica Matemática", "Inovação Tecnológica", 
    "Introdução a Inteligência Artificial", "Logica de Programação em IA", "Comunicação Científica e Metodologia", "Outra"
]

soma_pontos = 0.0
soma_horas = 0  # Corrigido: Padronizado para rastrear a carga horária total

# Cabeçalho das colunas
c1, c2, c3 = st.columns([2, 1, 1]) # O primeiro número (2) deixa a coluna do nome mais larga
c1.write("**Matérias**")
c2.write("**Nota (0 a 10)**")
c3.write("**Carga Horária (Horas)**")

# Loop para gerar as 6 linhas de matérias
for i in range(6):
    col_nome, col_nota, col_cred = st.columns([2, 1, 1])
    
    with col_nome:
        # Caixa de seleção para o aluno escolher a matéria
        materia_selecionada = st.selectbox("", LISTA_MATERIAS, key=f"m_{i}", label_visibility="collapsed")
    with col_nota:
        # Mantido de 0 a 100 conforme o padrão do IFAP
        nota = st.number_input("", min_value=0.0, max_value=10.0, value=0.0, step=1.0, key=f"n_{i}", label_visibility="collapsed")
    with col_cred:
        # Alterado max_value e step para se adequar a cargas horárias reais (ex: 40h, 60h, 80h)
        hor = st.number_input("", min_value=0, max_value=200, value=0, step=20, key=f"c_{i}", label_visibility="collapsed")
        
    soma_pontos += nota * hor
    soma_horas += hor  # Corrigido: Usando a mesma variável definida no escopo global

# Exibe o resultado final
if soma_horas > 0:  # Corrigido: Verifica se a soma das horas é maior que zero para evitar divisão por zero
    ira = soma_pontos / soma_horas
    st.write(f"### Seu IRA: {ira:.2f}")
else:
    st.write("Digite as notas e as cargas horárias acima para calcular.")

st.divider()

if st.button("❌ Voltar ao Menu", use_container_width=True):
    st.session_state.pagina = "inicio"
    st.rerun()
