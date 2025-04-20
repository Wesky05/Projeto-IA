# import streamlit as st
# import mysql.connector
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Configurações da página
# st.set_page_config(page_title="Dashboard Pacientes", layout="centered")

# # Conexão com o banco
# def conectar_banco():
#     return mysql.connector.connect(
#         host="localhost",      
#         user="root",
#         password="Eme#8710",
#         database="paciente"
#     )

# # Carregar dados da tabela paciente
# def carregar_dados():
#     conexao = conectar_banco()
#     cursor = conexao.cursor()
#     cursor.execute("SELECT nome, cpf, campo1, campo2, campo3, campo4 FROM paciente")
#     resultados = cursor.fetchall()
#     colunas = ["Nome", "CPF", "Campo 1", "Campo 2", "Campo 3", "Campo 4"]
#     df = pd.DataFrame(resultados, columns=colunas)
#     conexao.close()
#     return df

# # Exibição dos dados
# st.title("📊 Dashboard de Pacientes")

# # Barra lateral para filtro por tipo sanguíneo
# dados = carregar_dados()
# tipos_sanguineos = dados["Campo 2"].unique()
# tipo_filtrado = st.sidebar.selectbox("Filtrar por Tipo Sanguíneo:", ["Todos"] + list(tipos_sanguineos))

# # Barra lateral para filtro por plano de saúde
# planos = dados["Campo 3"].unique()
# plano_filtrado = st.sidebar.selectbox("Filtrar por Plano de Saúde:", ["Todos"] + list(planos))

# # Campo de pesquisa por CPF na barra lateral
# cpf_pesquisar = st.sidebar.text_input("Pesquisar por CPF (formato: XXX.XXX.XXX-XX):")

# # Filtra os dados de acordo com o tipo sanguíneo e plano de saúde
# if tipo_filtrado != "Todos":
#     dados = dados[dados["Campo 2"] == tipo_filtrado]

# if plano_filtrado != "Todos":
#     dados = dados[dados["Campo 3"] == plano_filtrado]

# # Verifica se o CPF foi inserido
# if cpf_pesquisar:
#     # Filtra o paciente pelo CPF digitado
#     paciente_encontrado = dados[dados["CPF"] == cpf_pesquisar]
    
#     if not paciente_encontrado.empty:
#         # Exibe os dados do paciente encontrado
#         st.write("### Dados do Paciente Encontrado:")
#         st.dataframe(paciente_encontrado)
#     else:
#         # Mensagem caso o paciente não seja encontrado
#         st.write("### Nenhum paciente encontrado com esse CPF.")
# else:
#     # Se nenhum CPF foi pesquisado, exibe a lista filtrada de pacientes
#     st.write("### Lista de Pacientes Filtrados:")
#     st.dataframe(dados)

#     # Contagem de pacientes filtrados
#     st.markdown(f"**Total de pacientes exibidos:** {len(dados)}")

#     # Gráfico de barras da distribuição de pacientes por tipo sanguíneo
#     tipo_sanguineo_count = dados["Campo 2"].value_counts()

#     # Configuração do gráfico de barras
#     fig, ax = plt.subplots(figsize=(5, 5))
#     sns.barplot(x=tipo_sanguineo_count.index, y=tipo_sanguineo_count.values, ax=ax, palette="viridis")
#     ax.set_title("Distribuição de Pacientes por Tipo Sanguíneo", fontsize=12)
#     ax.set_xlabel("Tipo Sanguíneo", fontsize=10)
#     ax.set_ylabel("Quantidade de Pacientes", fontsize=10)

#     # Diminui o tamanho da legenda e rotaciona levemente para não sobrepor
#     ax.set_xticklabels(tipo_sanguineo_count.index, rotation=30, ha='right', fontsize=8)


#     # Gráfico de pizza da distribuição de pacientes por plano de saúde
#     plano_count = dados["Campo 3"].value_counts()

#     # Configuração do gráfico de pizza
#     fig_pizza, ax_pizza = plt.subplots(figsize=(5, 5))
#     ax_pizza.pie(plano_count, labels=plano_count.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(plano_count)))
#     ax_pizza.set_title("Distribuição de Pacientes por Plano de Saúde", fontsize=12)

#     # Colocando os gráficos lado a lado
#     col1, col2 = st.columns(2)
    
#     # Exibindo o gráfico de barras na primeira coluna
#     with col1:
#         st.pyplot(fig)
    
#     # Exibindo o gráfico de pizza na segunda coluna
#     with col2:
#         st.pyplot(fig_pizza)

import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# Configurações da página
st.set_page_config(page_title="Dashboard Pacientes", layout="wide")

# Conexão com o banco
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",      
        user="root",
        password="",
        database=""
    )

# Carregar dados da tabela paciente
def carregar_dados():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, cpf, campo1, campo2, campo3, campo4 FROM paciente")
    resultados = cursor.fetchall()
    colunas = ["Nome", "CPF", "Campo 1", "Campo 2", "Campo 3", "Campo 4"]
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
tipos_sanguineos = dados["Campo 2"].unique()
tipo_filtrado = st.sidebar.selectbox("Tipo Sanguíneo:", ["Todos"] + list(tipos_sanguineos))

planos = dados["Campo 3"].unique()
plano_filtrado = st.sidebar.selectbox("Plano de Saúde:", ["Todos"] + list(planos))

cpf_pesquisar = st.sidebar.text_input("Pesquisar CPF (XXX.XXX.XXX-XX):")

# Aplicar filtros
if tipo_filtrado != "Todos":
    dados = dados[dados["Campo 2"] == tipo_filtrado]
if plano_filtrado != "Todos":
    dados = dados[dados["Campo 3"] == plano_filtrado]

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
    total_planos = dados["Campo 3"].nunique()
    total_tipos = dados["Campo 2"].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Pacientes", total_pacientes, "Total filtrado")
    with col2:
        metric_card("Tipos Sanguíneos", total_tipos, "Distintos")
    with col3:
        metric_card("Planos de Saúde", total_planos, "Distintos")

    st.markdown("---")

    # Tabela 
    st.subheader("Lista de Pacientes")
    st.dataframe(dados, use_container_width=True, height=180)

    # Gráficos 
    tipo_sanguineo_count = dados["Campo 2"].value_counts()
    plano_count = dados["Campo 3"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(2.5, 2))
    sns.barplot(
        x=tipo_sanguineo_count.index,
        y=tipo_sanguineo_count.values,
        ax=ax1,
        palette="Purples"
    )
    ax1.set_title("Tipos Sanguíneos", fontsize=8, color="#6A1B9A")
    ax1.set_xlabel("")
    ax1.set_ylabel("Quantidade", fontsize=6)
    ax1.tick_params(axis='x', labelrotation=30, labelsize=4)
    ax1.tick_params(axis='y', labelsize=6)
    ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

    fig2, ax2 = plt.subplots(figsize=(2.5, 2))
    cores_roxas = sns.color_palette("Purples", n_colors=len(plano_count))

    ax2.pie(
        plano_count,
        labels=plano_count.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=cores_roxas,
        textprops={'fontsize': 6}
    )
    ax2.set_title("Planos de Saúde", fontsize=8, color="#6A1B9A")


    col4, col5 = st.columns(2)
    with col4:
        st.pyplot(fig1)
    with col5:
        st.pyplot(fig2)
