# Imagem base
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos do projeto
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expor porta padrão do Streamlit
EXPOSE 8501

# Comando de inicialização
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
