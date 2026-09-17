# Dataset 01 — Bank Marketing

## Visão geral

Dados de campanhas telefônicas de uma instituição bancária portuguesa. O objetivo é prever se um cliente contratará um depósito a prazo.

- **Tarefa:** classificação binária
- **Alvo:** `subscribed`
- **Classes:** `yes` e `no`
- **Atributos preditores:** 19

## Arquivos

- `bank_marketing_train.csv`: 32.940 registros para treinamento.
- `bank_marketing_test.csv`: 8.236 registros para avaliação final.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A divisão fornecida deve ser preservada durante os experimentos.

## Distribuição das classes

| Conjunto | Registros | `no` | `yes` |
| --- | ---: | ---: | ---: |
| Treino | 32.940 | 29.229 | 3.711 |
| Teste | 8.236 | 7.308 | 928 |

A classe positiva representa aproximadamente 11,27% dos registros.

## Variáveis

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `age` | numérica | Idade do cliente. |
| `job` | categórica | Tipo de ocupação. |
| `marital` | categórica | Estado civil. |
| `education` | categórica | Escolaridade. |
| `default` | categórica | Indica inadimplência de crédito. |
| `housing` | categórica | Indica empréstimo habitacional. |
| `loan` | categórica | Indica empréstimo pessoal. |
| `contact` | categórica | Meio de contato da campanha. |
| `month` | categórica | Mês do último contato. |
| `day_of_week` | categórica | Dia da semana do último contato. |
| `campaign` | numérica | Quantidade de contatos na campanha atual. |
| `pdays` | numérica | Dias desde o contato anterior; `999` indica que não houve contato anterior. |
| `previous` | numérica | Quantidade de contatos anteriores. |
| `poutcome` | categórica | Resultado da campanha anterior. |
| `emp_var_rate` | numérica | Taxa de variação do emprego. |
| `cons_price_idx` | numérica | Índice de preços ao consumidor. |
| `cons_conf_idx` | numérica | Índice de confiança do consumidor. |
| `euribor_3m` | numérica | Taxa Euribor de três meses. |
| `nr_employed` | numérica | Número de empregados. |
| `subscribed` | alvo | Indica a contratação do depósito a prazo. |

## Orientações de uso

- A variável original `duration` não está presente porque só é conhecida após o término da ligação e causaria vazamento de dados.
- Algumas colunas usam `unknown` como categoria; avalie se ela deve ser tratada como ausência de informação.
- A acurácia isolada é inadequada devido ao desbalanceamento. Considere precisão, revocação, F1, ROC-AUC e PR-AUC.
- Ajuste codificação, padronização e reamostragem somente com os dados de treino.
- Os dados são históricos, coletados em Portugal entre 2008 e 2010.

## Fonte e licença

UCI Machine Learning Repository — [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).

Licença: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Referência: Moro, S., Rita, P. e Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5K306](https://doi.org/10.24432/C5K306).
