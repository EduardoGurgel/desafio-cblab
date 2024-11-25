# Desafio 2 - Solução

Endpoints e informações:
- **`/bi/getFiscalInvoice`**: Informações fiscais das lojas.
- **`/res/getGuestChecks`**: Detalhes dos pedidos realizados.
- **`/org/getChargeBack`**: Dados de estornos.
- **`/trans/getTransactions`**: Transações realizadas.
- **`/inv/getCashManagementDetails`**: Detalhes de gerenciamento de caixa.

---

## 1. Por que armazenar as respostas das APIs?
Armazenar as respostas das APIs em um data lake traz diversos benefícios. Em primeiro lugar, garante um histórico de dados, permitindo que informações de dias anteriores sejam consultadas, mesmo que os endpoints sejam atualizados ou desativados. Além disso, promove consistência, evitando inconsistências decorrentes de alterações em tempo real nas APIs. Outro ponto importante é a possibilidade de realizar análises agregadas, combinando dados de diferentes endpoints ou períodos de forma eficiente. O data lake também oferece escalabilidade, viabilizando o processamento em massa com ferramentas como Spark, Hadoop ou SQL engines. Por fim, sua flexibilidade permite que os dados armazenados sejam transformados e carregados em diferentes plataformas, como data warehouses ou sistemas de BI.

---

## 2. Como armazenar os dados?

### Estrutura de Pastas

A estrutura de pastas que escolhi, foi projetada para garantir organização e fácil acesso. Cada resposta de API será armazenada separadamente, com subdiretórios baseados na loja (`storeId`) e na data (`busDt`).

```plaintext
data_lake/
├── bi/
│   └── getFiscalInvoice/
│       ├── store_<storeId>/
│       │   ├── 2024-01-01.json
│       │   ├── 2024-01-02.json
│       │   └── ...
├── res/
│   └── getGuestChecks/
│       ├── store_<storeId>/
│       │   ├── 2024-01-01.json
│       │   ├── 2024-01-02.json
│       │   └── ...
├── org/
│   └── getChargeBack/
│       ├── store_<storeId>/
│       │   ├── 2024-01-01.json
│       │   ├── 2024-01-02.json
│       │   └── ...
├── trans/
│   └── getTransactions/
│       ├── store_<storeId>/
│       │   ├── 2024-01-01.json
│       │   ├── 2024-01-02.json
│       │   └── ...
└── inv/
    └── getCashManagementDetails/
        ├── store_<storeId>/
        │   ├── 2024-01-01.json
        │   ├── 2024-01-02.json
        │   └── ...
```

## 3. Justificando a estrutura

**Hierarquia Clara**: Diretórios organizados por endpoint, loja e data facilitam buscas específicas.

**Compatibilidade**: Estrutura compatível com ferramentas como Spark, AWS S3 ou HDFS do Hadoop por exemplo.

**Modularidade**: Adição de novos endpoints ou modificações nas APIs não afetam a estrutura existente.

**Desempenho**: Facilita o particionamento de dados, melhorando o desempenho de análises.

## 4. Impacto da Mudança no Endpoint getGuestChecks
Se o campo guestChecks.taxes for renomeado para guestChecks.taxation, haverá impactos no processamento e armazenamento:

1. Impactos Scripts de Transformação:

    - Alteração necessária no código que consome os dados para mapear o novo campo corretamente.
    - Scripts que dependem de guestChecks.taxes falharão até serem atualizados.

2. Compatibilidade com Dados Anteriores:

    - Dados já armazenados no data lake continuarão com o campo taxes. Será necessário criar um processo de migração ou manter suporte para ambos os formatos (taxes e taxation).

3. Consistência de Dados:

    - Para manter a consistência, pode ser necessário um esquema padronizado que trate diferentes versões dos dados.

## 5. Abordagem proposta

1. Versionamento de Esquema:

    -  Manter um controle de versão para o schema dos dados em um arquivo, por exemplo:

```
{
    "version": "1.1",
    "changes": {
        "renamed_fields": {
            "guestChecks.taxes": "guestChecks.taxation"
        }
    }
}
```
2. Atualização Incremental:

    - Adaptar os scripts para reconhecer automaticamente o schema da versão e processar ambos os formatos.

3. Documentação
    - Documentar todas as alterações nos endpoints e seus impactos nos pipelines de dados.

