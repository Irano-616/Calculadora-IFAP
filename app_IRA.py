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
    "Outra": 0  # Permite que o aluno defina manualmente se for uma matéria extra
}

# Lista gerada a partir das chaves do dicionário para abastecer o selectbox
LISTA_MATERIAS = list(DICIONARIO_MATERIAS.keys())

soma_pontos = 0.0
soma_horas = 0

# Cabeçalho das colunas
c1, c2, c3 = st.columns([2, 1, 1])
c1.write("**Matérias**")
c2.write("**Nota (0 a 10)**")
c3.write("**Carga Horária (Horas)**")

# Loop para gerar as 6 linhas de matérias
for i in range(6):
    col_nome, col_nota, col_cred = st.columns([2, 1, 1])
    
    with col_nome:
        materia_selecionada = st.selectbox("", LISTA_MATERIAS, key=f"m_{i}", label_visibility="collapsed")
    
    with col_nota:
        nota = st.number_input("", min_value=0.0, max_value=10.0, value=0.0, step=1.0, key=f"n_{i}", label_visibility="collapsed")
    
    with col_cred:
        # Se o usuário escolher "Outra", ele pode digitar a carga horária na mão.
        # Caso contrário, o sistema busca o valor fixo no dicionário e desabilita o campo.
        if materia_selecionada == "Outra":
            hor = st.number_input("", min_value=0, max_value=200, value=0, step=20, key=f"c_{i}", label_visibility="collapsed")
        else:
            hor_fixo = DICIONARIO_MATERIAS[materia_selecionada]
            # Exibe o valor em um campo desabilitado (cinza) para o usuário visualizar
            st.number_input("", min_value=0, max_value=200, value=hor_fixo, key=f"c_{i}", label_visibility="collapsed", disabled=True)
            hor = hor_fixo
        
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

