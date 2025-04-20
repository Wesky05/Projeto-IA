# Imagem base do Python
FROM python:3.10

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia tudo do projeto para dentro do container
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para rodar o FastAPI com uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
