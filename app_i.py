import streamlit as st

st.set_page_config(
    page_title = "Sistema IFAP",
    layout = "centered",
    initial_sidebar_state = "expanded" # Mudado para expanded para preencher as laterais
)

# Injeção de CSS para botões verdes, animação hover e barras customizadas
st.markdown(
    """
    <style>
        /* Estilização principal dos botões (Verde Claro) */
        .stButton > button {
            width: 100% !important;
            height: 60px !important;
            font-size: 18px !important;
            font-weight: bold !important;
            background-color: #2ecc71 !important; /* Verde claro */
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            transition: transform 0.2s ease-in-out, background-color 0.2s !important;
        }
        
        /* Efeito de zoom ao passar o mouse */
        .stButton > button:hover {
            transform: scale(1.03) !important;
            background-color: #27ae60 !important; /* Verde um pouco mais escuro no hover */
        }

        /* Estilização para as barras de progresso e métricas adicionadas */
        .metric-card {
            background-color: #f8f9fa;
            padding: 15px;
            border-left: 5px solid #2ecc71;
            border-radius: 4px;
            margin-bottom: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if st.session_state.pagina == "inicio":
    st.title("🟢 Sistema Acadêmico IFAP")
    st.caption("Painel do Estudante — Instituto Federal do Amapá")
    
    # --- CONTEÚDO EXTRA 1: Barra Lateral de Utilidades ---
    with st.sidebar:
        st.header("📋 Menu & Atalhos")
        st.write("Acesse os portais institucionais rapidamente:")
        st.link_button("🌐 Portal do Aluno SUAP", "https://ifap.edu.br", use_container_width=True)
        st.link_button("📅 Calendário Acadêmico", "https://ifap.edu.br", use_container_width=True)
        
        st.divider()
        st.subheader("⚙️ Status do Sistema")
        st.success("Conexão Segura")
        st.info("Período Letivo: 2026.1")

    # --- CONTEÚDO EXTRA 2: Indicadores Visuais e Barras de Progresso ---
    st.subheader("📊 Visão Geral do Semestre")
    
    # Linha com cartões informativos (Preenchimento de tela)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><strong>Média para Aprovação:</strong><br>🎯 6.0 pontos</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><strong>Frequência Mínima:</strong><br>📅 75% exigido</div>', unsafe_allow_html=True)

    # Barra de progresso do ano letivo corrente
    st.write("Progresso do Bimestre Atual:")
    st.progress(0.65, text="65% do conteúdo ministrado")
    
    st.divider()
    st.subheader("⚡ Ferramentas Disponíveis")
    st.write("Selecione uma das opções abaixo para iniciar os cálculos:")

    # --- BOTÕES ORIGINAIS (Agora estilizados em verde) ---
    if st.button("Calculadora da Nota 📊", type = "primary"):
        st.session_state.pagina = "nota"
        st.rerun()

    elif st.button("Calculadora de IRA", type = "primary"):
        st.session_state.pagina = "ira"
        st.rerun()
        
    st.divider()
    
    # --- CONTEÚDO EXTRA 3: Área de Avisos no Rodapé ---
    st.subheader("📢 Avisos Importantes")
    st.warning("Atenção: O cálculo de IRA considera todas as disciplinas cursadas, inclusive dependências e reprovações.")

elif st.session_state.pagina == "nota":
    with open("app_nota.py", encoding = "utf-8") as f:
        exec(f.read())

elif st.session_state.pagina == "ira":
    with open("app_IRA.py", encoding = "utf-8") as f:
        exec(f.read())


    elif st.button("Calculadora de IRA", type = "primary"):
        st.session_state.pagina = "ira"
        st.rerun()

elif st.session_state.pagina == "nota":
    with open("app_nota.py", encoding = "utf-8") as f:
        exec(f.read())

elif st.session_state.pagina == "ira":
    with open("app_IRA.py", encoding = "utf-8") as f:
        exec(f.read())
