FROM python:3.11

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta
EXPOSE 8000

# Comando para rodar o app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
