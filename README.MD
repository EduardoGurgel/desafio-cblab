# Desafio Engenheiro de Dados CB LAB
# DESAFIO 01

Este projeto implementa a carga de dados de um JSON para um banco de dados relacional PostgreSQL. A solução é containerizada usando Docker e permite visualização dos dados via Adminer.

## 1 - Descrição do Schema JSON
Aqui pode ser encontrado a descrição em detalhes:
[Descrição do Schema JSON](/schema/descricao_schema_json.md).

## 2 - Descrição da abordagem escolhida
Aqui pode ser encontrado a descrição em detalhes, justificando a abordagem escolhida em detalhes:
[Descrição abordagem escolhida](/scripts/descricao_abordagem_escolhida.md).

# DESAFIO 02
Aqui pode ser encontrado o motivo pelo qual deve-se armazenar as respostas das API's, como eu armazenaria os dados e verificando a resposta do Endpoint getGuestChecks, caso tenha sido alterada: 
[Desafio 02](/data_lake/desafio_02.md).

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
   cd desafio-cblab
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