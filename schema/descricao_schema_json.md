# Descrição do Schema JSON
O JSON representa dados estruturados relacionados às operações do restaurante, incluindo informações sobre pedidos, itens do menu, impostos e transações.

## Campos
- **curUTC**: (string) Data e hora em UTC no formato ISO 8601.
- **locRef**: (string) Referência de localização do restaurante.
- **guestChecks**: (array) Lista de pedidos. Cada elemento contém detalhes como itens consumidos, impostos e status.

## guestChecks
```
{
    "guestCheckId": "integer",
    "chkNum": "integer",
    "opnBusDt": "string (date)",
    "opnUTC": "string (datetime)",
    "opnLcl": "string (datetime)",
    "clsdBusDt": "string (date)",
    "clsdUTC": "string (datetime)",
    "clsdLcl": "string (datetime)",
    "lastTransUTC": "string (datetime)",
    "lastTransLcl": "string (datetime)",
    "lastUpdatedUTC": "string (datetime)",
    "lastUpdatedLcl": "string (datetime)",
    "clsdFlag": "boolean",
    "gstCnt": "integer",
    "subTtl": "float",
    "nonTxblSlsTtl": "float | null",
    "chkTtl": "float",
    "dscTtl": "float",
    "payTtl": "float",
    "balDueTtl": "float | null",
    "rvcNum": "integer",
    "otNum": "integer",
    "ocNum": "integer | null",
    "tblNum": "integer",
    "tblName": "string",
    "empNum": "integer",
    "numSrvcRd": "integer",
    "numChkPrntd": "integer",
    "taxes": "array",
    "detailLines": "array"
}
```
## Campos
- **guestCheckId**: (**integer**) Identificador único do pedido.  
- **chkNum**: (**integer**) Número do pedido.  
- **opnBusDt**, **clsdBusDt**: (**date**) Datas de abertura e fechamento.  
- **opnUTC**, **opnLcl**, **clsdUTC**, **clsdLcl**: (**datetime**) Horários de abertura e fechamento em UTC e local.  
- **lastTransUTC**, **lastTransLcl**: (**datetime**) Horário da última transação.  
- **lastUpdatedUTC**, **lastUpdatedLcl**: (**datetime**) Última atualização do pedido.  
- **clsdFlag**: (**boolean**) Indica se o pedido foi fechado.  
- **gstCnt**: (**integer**) Número de convidados.  
- **subTtl**, **chkTtl**, **payTtl**: (**float**) Subtotal, total e pagamento.  
- **nonTxblSlsTtl**, **balDueTtl**: (**float | null**) Totais não tributáveis e saldo devido.  
- **rvcNum**, **otNum**, **ocNum**, **tblNum**, **empNum**: (**integer**) Números relacionados ao serviço e mesa.  
- **tblName**: (**string**) Nome ou número da mesa.  
- **numSrvcRd**, **numChkPrntd**: (**integer**) Rodadas de serviço e número de cheques impressos.  
- **taxes**: (**array**) Lista de impostos aplicados.  
- **detailLines**: (**array**) Lista de itens consumidos.  

## Taxes
```
{
    "taxNum": "integer",
    "txblSlsTtl": "float",
    "taxCollTtl": "float",
    "taxRate": "float",
    "type": "integer"
}
```
### Campos
- **taxNum**: (**integer**) Número do imposto.  
- **txblSlsTtl**: (**float**) Total de vendas tributáveis.  
- **taxCollTtl**: (**float**) Total de impostos recolhidos.  
- **taxRate**: (**float**) Taxa de imposto aplicada.  
- **type**: (**integer**) Tipo de imposto.  

## detailLines

```
{
    "guestCheckLineItemId": "integer",
    "rvcNum": "integer",
    "dtlOtNum": "integer",
    "dtlOcNum": "integer | null",
    "lineNum": "integer",
    "dtlId": "integer",
    "detailUTC": "string (datetime)",
    "detailLcl": "string (datetime)",
    "lastUpdateUTC": "string (datetime)",
    "lastUpdateLcl": "string (datetime)",
    "busDt": "string (date)",
    "wsNum": "integer",
    "dspTtl": "float",
    "dspQty": "float",
    "aggTtl": "float",
    "aggQty": "float",
    "chkEmpId": "integer",
    "chkEmpNum": "integer",
    "svcRndNum": "integer",
    "seatNum": "integer",
    "menuItem": "object"
}
```
### Campos


- **guestCheckLineItemId**: (**integer**) Identificador único da linha.  
- **rvcNum**, **dtlOtNum**, **dtlOcNum**, **lineNum**, **dtlId**: (**integer**) Dados de referência ao item.  
- **detailUTC**, **detailLcl**: (**datetime**) Datas e horários de detalhe em UTC e local.  
- **lastUpdateUTC**, **lastUpdateLcl**: (**datetime**) Última atualização do detalhe.  
- **busDt**: (**date**) Data do detalhe.  
- **wsNum**: (**integer**) Número da estação de trabalho.  
- **dspTtl**, **dspQty**: (**float**) Total e quantidade exibidos.  
- **aggTtl**, **aggQty**: (**float**) Total e quantidade agregados.  
- **chkEmpId**, **chkEmpNum**: (**integer**) Identificadores do empregado associado.  
- **svcRndNum**, **seatNum**: (**integer**) Rodada de serviço e número do assento.  

## MenuItem
```
{
    "miNum": "integer",
    "modFlag": "boolean",
    "inclTax": "float",
    "activeTaxes": "string",
    "prcLvl": "integer"
}
```
### Campos
- **miNum**: (**integer**) Identificador único do item do menu.  
- **modFlag**: (**boolean**) Indica se o item foi modificado.  
- **inclTax**: (**float**) Valor do imposto incluído.  
- **activeTaxes**: (**string**) Impostos ativos associados.  
- **prcLvl**: (**integer**) Nível de preço.  