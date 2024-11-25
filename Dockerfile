FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir psycopg2-binary pandas

COPY scripts /app/scripts
COPY data /app/data
