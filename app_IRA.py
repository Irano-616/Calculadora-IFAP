import streamlit as st

st.title("Calculadora de IRA")

# Dicionário mapeando cada matéria à sua carga horária fixa do IFAP
DICIONARIO_MATERIAS = {
    "Selecionar...": 0,
    "Inglês Instrumental": 40,
    "Lógica Matemática": 80,
    "Inovação Tecnológica": 80,
    "Introdução a Inteligência Artificial": 80,
    "Logica de Programação em IA": 80,
    "Comunicação Científica e Metodologia": 40,
    "Outra": 0
}

LISTA_MATERIAS = list(DICIONARIO_MATERIAS.keys())

soma_pontos = 0.0
soma_horas = 0

# Cabeçalho das colunas
c1, c2, c3 = st.columns()
c1.write("**Matérias**")
c2.write("**Nota (0 a 10)**")
c3.write("**Carga Horária (Horas)**")

# 1. ETAPA: Descobrir o que já foi selecionado para poder filtrar
materias_selecionadas_anteriormente = []
for j in range(6):
    # Verifica se a chave já existe no estado do Streamlit
    if f"m_{j}" in st.session_state:
        escolha = st.session_state[f"m_{j}"]
        # Ignora "Selecionar..." e "Outra" da regra de repetição
        if escolha not in ["Selecionar...", "Outra"]:
            materias_selecionadas_anteriormente.append(escolha)

# 2. ETAPA: Renderizar as linhas com as opções filtradas
for i in range(6):
    col_nome, col_nota, col_cred = st.columns()
    
    # Criamos uma lista de opções específica para ESTA linha
    # Mantém o que o usuário já escolheu nesta linha OU o que ainda está livre
    materia_atual_desta_linha = st.session_state.get(f"m_{i}", "Selecionar...")
    
    opcoes_disponiveis = [
        m 
        for m in LISTA_MATERIAS 
        if m == materia_atual_desta_linha or m not in materias_selecionadas_anteriormente or m in ["Selecionar...", "Outra"]
    ]
    
    # Garante que o valor atual está dentro das opções para não quebrar o Streamlit
    if materia_atual_desta_linha not in opcoes_disponiveis:
        index_padrao = 0
    else:
        index_padrao = opcoes_disponiveis.index(materia_atual_desta_linha)

    # 1. Caixa de seleção da matéria (com a lista filtrada)
    with col_nome:
        materia_selecionada = st.selectbox(
            "", 
            opcoes_disponiveis, 
            index=index_padrao,
            key=f"m_{i}", 
            label_visibility="collapsed"
        )
    
    # 2. Busca a carga horária padrão
    hor_fixo = DICIONARIO_MATERIAS.get(materia_selecionada, 0)
    
    # 3. Campo de nota
    with col_nota:
        nota = st.number_input(
            "", 
            min_value=0.0, 
            max_value=10.0, 
            value=0.0, 
            step=1.0, 
            key=f"n_{i}", 
            label_visibility="collapsed"
        )
    
    # 4. Campo de carga horária
    with col_cred:
        if materia_selecionada == "Outra":
            hor = st.number_input(
                "", 
                min_value=0, 
                max_value=200, 
                value=0, 
                step=20, 
                key=f"c_{i}", 
                label_visibility="collapsed"
            )
        else:
            hor = st.number_input(
                "", 
                min_value=0, 
                max_value=200, 
                value=hor_fixo, 
                key=f"c_{i}", 
                label_visibility="collapsed", 
                disabled=True
            )
            
    soma_pontos += nota * hor
    soma_horas += hor

# Exibe o resultado final
if soma_horas > 0:
    ira = soma_pontos / soma_horas
    st.write(f"### Seu IRA: {ira:.2f}")
else:
    st.write("Digite as notas e selecione as matérias acima para calcular.")

st.divider()

if st.button("❌ Voltar ao Menu", use_container_width=True):
    st.session_state.pagina = "inicio"
    st.rerun()
