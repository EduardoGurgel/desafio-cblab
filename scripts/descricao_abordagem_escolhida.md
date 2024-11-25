# Abordagem escolhida

## 1. Abordagem e Justificativa

### Abordagem Escolhida

1. **Transcrição do JSON para Tabelas SQL**:
   - Eu escolhi estrutura JSON, que foi convertida em um conjunto de tabelas normalizadas no banco de dados PostgreSQL.
   - Cada entidade relevante do JSON foi mapeada para uma tabela, mantendo os relacionamentos entre elas:
     - **guestChecks**: Representa o pedido principal.
     - **taxes**: Lista de impostos aplicados ao pedido.
     - **detailLines**: Detalhes dos itens consumidos, incluindo o menu e outras instâncias (como descontos, taxas e erros etc...).
     - **menuItem**: Detalhes dos itens do menu, como preço, impostos e status.

2. **Automação  que fiz com Python**:
   - O script **`load_json.py`** utiliza a biblioteca `psycopg2` para conectar-se ao banco PostgreSQL e carregar os dados do JSON diretamente nas tabelas.
   - O script automatiza o processo de inserção, garantindo que as estruturas do JSON sejam traduzidas para o banco de dados.

3. **Infraestrutura Containerizada**:
   - Utilizei Docker para facilitar a implantação e configuração do ambiente.
   - O arquivo **`docker-compose.yml`** que criei gerencia três serviços:
     - **PostgreSQL**: Para armazenamento dos dados.
     - **Adminer**: Interface gráfica para visualização e manipulação do banco.
     - **Aplicação Python**: Responsável pela leitura e carga dos dados do JSON.

---

### Justificativa

1. **Normalização**:
   - A estrutura normalizada melhora a consistência e reduz redundâncias.
   - Relacionamentos claros entre tabelas permitem consultas mais eficientes e manutenção mais simples.

2. **Escalabilidade**:
   - A separação dos dados em tabelas distintas facilita a expansão do modelo, como a adição de novos tipos de linhas no **`detailLines`** (por exemplo, **`discount`**, **`serviceCharge`**, etc.).

3. **Reprodutibilidade**:
   - A automação com Docker permite que o projeto seja facilmente replicado em diferentes ambientes.
   - A inclusão de um script de inicialização (**`init_db.sql`**) garante que o banco seja configurado corretamente desde o início.

4. **Flexibilidade**:
   - A escolha do PostgreSQL oferece suporte avançado a tipos de dados e relacionamentos, adequado para a complexidade do JSON.
   - O Python foi utilizado pela facilidade de manipular arquivos JSON e integrar-se ao banco.

---
