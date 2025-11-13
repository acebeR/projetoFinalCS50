# Use imagem oficial do Python
FROM python:3.13-slim

# Defina diretório de trabalho
WORKDIR /app

# Copie arquivos de requirements
COPY requirements.txt .

# Instale dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código
COPY ./app ./app

# Exponha porta do FastAPI
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
