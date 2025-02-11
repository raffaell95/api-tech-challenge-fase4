# Usando uma imagem oficial do Python como base
FROM python:3.12-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para a imagem
COPY ./api/requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da API e o modelo .h5 para a imagem
COPY . ./app

# Expor a porta em que a API estará rodando
EXPOSE 8000

RUN pip install uvicorn

# Set the command to run FastAPI app
CMD ["uvicorn", "api.src.server:app", "--host", "0.0.0.0", "--port", "8000"]