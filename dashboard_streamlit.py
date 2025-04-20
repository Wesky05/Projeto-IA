import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# Configurações da página
st.set_page_config(page_title="Dashboard Pacientes", layout="wide")

# Conexão com o banco
def conectar_banco():
    conn = psycopg2.connect(
        host="easypanel.kwautomation.shop",  # Host externo do banco
        port="30420", 
        database="projeto_ia",  
        user="KEVIN",  
        password="kevin123",  
        sslmode="disable"  
    )
    return conn

# 
def carregar_dados():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, cpf, genero, suicidio_historico, familia_historico, substancias_uso, predicao FROM requisicoes")
    resultados = cursor.fetchall()
    colunas = ["Nome", "CPF", "Gênero", "Histórico de Suicídio", "Histórico Familiar", "Substâncias de Uso", "Predição"]
    df = pd.DataFrame(resultados, columns=colunas)
    conexao.close()
    return df

# Ocultar a barra do Streamlit (navbar e rodapé)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Ajustar margens/padding para ocupar melhor o espaço da tela
st.markdown("""
    <style>
        .block-container {
            padding-top: 0.1rem;
            padding-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Ajuste Barra lateral
st.markdown("""
    <style>
        /* Cor de fundo da barra lateral */
        section[data-testid="stSidebar"] {
            background-color: #56447A;
        }

        /* Cor do texto na barra lateral */
        section[data-testid="stSidebar"] .css-1cpxqw2 {
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Estilo dos cards 
def metric_card(title, value, subtitle):
    st.markdown(f"""
        <div style="background-color: #ffffff; padding: 6px; border-radius: 8px; 
                    text-align: center; box-shadow: 1px 1px 4px rgba(0,0,0,0.1); 
                    font-size: 10px;">
            <h5 style="color: #6A1B9A; margin: 0;">{title}</h5>
            <h3 style="color: #8E24AA; margin: 5px 0;">{value}</h3>
            <p style="color: #A66BBE; margin: 0;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)

dados = carregar_dados()

# Filtros laterais
generos = dados["Gênero"].unique()
genero_filtrado = st.sidebar.selectbox("Gênero:", ["Todos"] + list(generos))

suicidio_historico = dados["Histórico de Suicídio"].unique()
suicidio_filtrado = st.sidebar.selectbox("Histórico de Suicídio:", ["Todos"] + list(suicidio_historico))

familia_historico = dados["Histórico Familiar"].unique()
familia_filtrado = st.sidebar.selectbox("Histórico Familiar:", ["Todos"] + list(familia_historico))

cpf_pesquisar = st.sidebar.text_input("Pesquisar CPF (XXX.XXX.XXX-XX):")

# Aplicar filtros
if genero_filtrado != "Todos":
    dados = dados[dados["Gênero"] == genero_filtrado]
if suicidio_filtrado != "Todos":
    dados = dados[dados["Histórico de Suicídio"] == suicidio_filtrado]
if familia_filtrado != "Todos":
    dados = dados[dados["Histórico Familiar"] == familia_filtrado]

# Se CPF for pesquisado
if cpf_pesquisar:
    paciente_encontrado = dados[dados["CPF"] == cpf_pesquisar]
    if not paciente_encontrado.empty:
        st.subheader("🔎 Paciente Encontrado")
        st.dataframe(paciente_encontrado, height=150)
    else:
        st.warning("Nenhum paciente encontrado com esse CPF.")
else:
    # Métricas
    total_pacientes = len(dados)
    total_generos = dados["Gênero"].nunique()
    total_suicidio = dados["Histórico de Suicídio"].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Pacientes", total_pacientes, "Total filtrado")
    with col2:
        metric_card("Gêneros", total_generos, "Distintos")
    with col3:
        metric_card("Histórico de Suicídio", total_suicidio, "Distintos")

    st.markdown("---")

    # Tabela 
    st.subheader("Lista de Pacientes")
    st.dataframe(dados, use_container_width=True, height=180)

    # Gráficos 
    genero_count = dados["Gênero"].value_counts()
    suicidio_count = dados["Histórico de Suicídio"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(2.5, 2))
    sns.barplot(
        x=genero_count.index,
        y=genero_count.values,
        ax=ax1,
        palette="Purples"
    )
    ax1.set_title("Gêneros", fontsize=8, color="#6A1B9A")
    ax1.set_xlabel("")
    ax1.set_ylabel("Quantidade", fontsize=6)
    ax1.tick_params(axis='x', labelrotation=30, labelsize=4)
    ax1.tick_params(axis='y', labelsize=6)
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

    fig2, ax2 = plt.subplots(figsize=(2.5, 2))
    cores_roxas = sns.color_palette("Purples", n_colors=len(suicidio_count))

    ax2.pie(
        suicidio_count,
        labels=suicidio_count.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=cores_roxas,
        textprops={'fontsize': 6}
    )
    ax2.set_title("Histórico de Suicídio", fontsize=8, color="#6A1B9A")


    col4, col5 = st.columns(2)
    with col4:
        st.pyplot(fig1)
    with col5:
        st.pyplot(fig2)
