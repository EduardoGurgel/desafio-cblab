# Desafio Engenheiro de Dados CB LAB

Este projeto implementa a carga de dados de um JSON para um banco de dados relacional PostgreSQL. A solução é containerizada usando Docker e permite visualização dos dados via Adminer.

## Estrutura do Projeto

- **`data/ERP.json`**: Arquivo JSON com os dados.
- **`scripts/`**:
  - `init_db.sql`: Script SQL para criar as tabelas no PostgreSQL.
  - `load_json.py`: Script Python para processar e carregar os dados no banco.
- **`docker-compose.yml`**: Orquestração dos contêineres.
- **`Dockerfile`**: Configuração do contêiner Python.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/EduardoGurgel/desafio-cblab.git
   cd desafio-engenheiro-dados
2. Suba os serviços:
    ```bash
    docker-compose up --build
3. Acesse o Adminer em: 
    ```bash
    http://localhost:8080
3. Conecte ao PostgreSQL:
    ```bash
    Server: db
    User: user
    Password: password
    Database: restaurant