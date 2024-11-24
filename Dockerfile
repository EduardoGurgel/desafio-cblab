FROM python:3.10-slim

# Atualizar pacotes do sistema e instalar dependências
RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Instalar bibliotecas Python necessárias
RUN pip install --no-cache-dir psycopg2-binary pandas

# Copiar scripts e dados para o contêiner
COPY scripts /app/scripts
COPY data /app/data
