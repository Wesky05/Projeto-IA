import psycopg2
import pandas as pd

# Função para conectar ao banco PostgreSQL
def conectar_banco():
    conn = psycopg2.connect(
        host="easypanel.kwautomation.shop",  # Host externo do banco
        port="30420",  # Porta externa
        database="projeto_ia",  # Nome do banco de dados
        user="KEVIN",  # Nome de usuário
        password="kevin123",  # Senha
        sslmode="disable"  # Desabilitar SSL (se necessário)
    )
    return conn

# Função para exportar dados para um arquivo Excel
def exportar_para_excel():
    try:
        # Conectar ao banco de dados
        conn = conectar_banco()
        
        # Criar o cursor
        cursor = conn.cursor()
        
        # Consultar os dados da tabela requisicoes
        query = "SELECT nome, cpf, genero, suicidio_historico, familia_historico, substancias_uso, predicao FROM requisicoes"
        cursor.execute(query)
        
        # Obter todos os resultados da consulta
        dados = cursor.fetchall()
        
        # Criar um DataFrame do pandas com os dados
        df = pd.DataFrame(dados, columns=["Nome", "CPF", "Gênero", "Histórico de Suicídio", "Histórico Familiar", "Uso de Substâncias", "Predição"])
        
        # Exportar para um arquivo Excel
        df.to_excel("dados_requisicoes.xlsx", index=False)
        
        print("Exportação para Excel concluída com sucesso!")
        
    except Exception as e:
        print(f"Erro ao exportar para Excel: {e}")
        
    finally:
        # Fechar o cursor e a conexão com o banco
        cursor.close()
        conn.close()

# Chamar a função para exportar os dados
exportar_para_excel()
