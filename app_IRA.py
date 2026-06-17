import streamlit as st

# Configuração da página para um visual mais limpo e focado
st.set_page_config(page_title="Calculadora de IRA - IFAP", page_icon="📊", layout="centered")

# Título moderno com subtítulo discreto e ícone
st.title("📊 Calculadora de IRA")
st.caption("Insira suas notas e matérias do IFAP para calcular o Índice de Rendimento Acadêmico.")
st.markdown("---")

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

# Função callback para atualizar a carga horária assim que a matéria muda
def atualizar_carga_horaria(indice):
    materia = st.session_state[f"m_{indice}"]
    if materia != "Outra":
        st.session_state[f"c_{indice}"] = DICIONARIO_MATERIAS.get(materia, 0)

soma_pontos = 0.0
soma_horas = 0

# 1. ETAPA: Descobrir o que já foi selecionado para poder filtrar
materias_selecionadas_anteriormente = []
for j in range(6):
    if f"m_{j}" in st.session_state:
        escolha = st.session_state[f"m_{j}"]
        if escolha not in ["Selecionar...", "Outra"]:
            materias_selecionadas_anteriormente.append(escolha)

# Cabeçalho das colunas com proporção otimizada (Nome maior que os inputs numéricos)
c1, c2, c3 = st.columns([2, 1, 1])
c1.markdown("<p style='font-weight:600; margin-bottom:-5px; color:#555;'>Matérias</p>", unsafe_html=True)
c2.markdown("<p style='font-weight:600; margin-bottom:-5px; color:#555;'>Nota (0-10)</p>", unsafe_html=True)
c3.markdown("<p style='font-weight:600; margin-bottom:-5px; color:#555;'>Carga Horária</p>", unsafe_html=True)

# 2. ETAPA: Renderizar as linhas dentro de um container minimalista uniforme
with st.container(border=True):
    for i in range(6):
        col_nome, col_nota, col_cred = st.columns([2, 1, 1])
        
        materia_atual_desta_linha = st.session_state.get(f"m_{i}", "Selecionar...")
        
        opcoes_disponiveis = [
            m 
            for m in LISTA_MATERIAS 
            if m == materia_atual_desta_linha or m not in materias_selecionadas_anteriormente or m in ["Selecionar...", "Outra"]
        ]
        
        if materia_atual_desta_linha not in opcoes_disponiveis:
            index_padrao = 0
        else:
            index_padrao = opcoes_disponiveis.index(materia_atual_desta_linha)

        # 1. Caixa de seleção da matéria
        with col_nome:
            materia_selecionada = st.selectbox(
                "", 
                opcoes_disponiveis, 
                index=index_padrao,
                key=f"m_{i}", 
                label_visibility="collapsed",
                on_change=atualizar_carga_horaria,
                args=(i,)
            )
        
        # 2. Campo de nota
        with col_nota:
            nota = st.number_input(
                "", 
                min_value=0.0, 
                max_value=10.0, 
                value=0.0, 
                step=0.5, # Ajustado para 0.5 para facilitar digitação acadêmica
                key=f"n_{i}", 
                label_visibility="collapsed"
            )
        
        # 3. Campo de carga horária
        with col_cred:
            if materia_selecionada == "Outra":
                hor = st.number_input(
                    "", 
                    min_value=0, 
                    max_value=200, 
                    value=st.session_state.get(f"c_{i}", 0) if st.session_state.get(f"m_{i}") == "Outra" else 0, 
                    step=20, 
                    key=f"c_{i}", 
                    label_visibility="collapsed"
                )
            else:
                hor_fixo = DICIONARIO_MATERIAS.get(materia_selecionada, 0)
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

st.markdown("<br>", unsafe_html=True)

# Exibe o resultado final de forma elegante
if soma_horas > 0:
    ira = soma_pontos / soma_horas
    
    # Exibe o resultado em um box moderno de destaque
    st.metric(label="Seu Índice de Rendimento Acadêmico", value=f"{ira:.2f}")
    
    # Feedback visual discreto baseado na nota
    if ira >= 7.0:
        st.success("Ótimo desempenho! Continue assim.", icon="✨")
    elif ira >= 5.0:
        st.info("Bom progresso. Você está na média.", icon="📈")
    else:
        st.warning("Atenção ao rendimento. Precisa de apoio?", icon="⚠️")
else:
    st.info("Selecione as matérias e informe as notas acima para calcular automaticamente.", icon="💡")

st.markdown("<br>", unsafe_html=True)

# Botão secundário elegante para o menu
if st.button("← Voltar ao Menu Inicial", use_container_width=True, type="secondary"):
    st.session_state.pagina = "inicio"
    st.rerun()
