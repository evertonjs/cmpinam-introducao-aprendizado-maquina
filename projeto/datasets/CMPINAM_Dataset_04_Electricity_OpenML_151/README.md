# Dataset 04 — Electricity

## Visão geral

Dados do mercado de eletricidade de New South Wales e Victoria, na Austrália. Cada registro representa um período de 30 minutos. O objetivo é classificar o preço de New South Wales em relação à média móvel recente.

- **Tarefa:** classificação binária com ordem temporal
- **Alvo:** `nsw_price_class`
- **Classes:** `up` e `down`
- **Atributos preditores:** 8

O alvo não indica diretamente se o preço futuro subirá ou cairá. Este conjunto deve ser tratado como benchmark histórico de classificação em fluxo e mudança de conceito.

## Arquivos

- `electricity_train.csv`: 36.240 registros iniciais da sequência.
- `electricity_test.csv`: 9.072 registros posteriores da sequência.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A ordem das linhas e a divisão temporal fornecida devem ser preservadas.

## Distribuição das classes

| Conjunto | Registros | `down` | `up` |
| --- | ---: | ---: | ---: |
| Treino | 36.240 | 21.097 | 15.143 |
| Teste | 9.072 | 4.978 | 4.094 |

## Variáveis

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `date_normalized` | numérica temporal | Representação normalizada da data. |
| `day` | categórica | Código do dia da semana, de `day_1` a `day_7`. |
| `period_index` | inteira temporal | Período de meia hora dentro do dia, de 1 a 48. |
| `nsw_price_normalized` | numérica | Preço normalizado em New South Wales. |
| `nsw_demand_normalized` | numérica | Demanda normalizada em New South Wales. |
| `vic_price_normalized` | numérica | Preço normalizado em Victoria. |
| `vic_demand_normalized` | numérica | Demanda normalizada em Victoria. |
| `transfer_normalized` | numérica | Transferência programada e normalizada entre os estados. |
| `nsw_price_class` | alvo | Estado `up` ou `down` do preço de NSW em relação à média móvel recente. |

## Orientações de uso

- Não substitua a divisão fornecida por uma separação aleatória: isso misturaria passado e futuro.
- Para ajuste de hiperparâmetros, use validação sequencial, como `TimeSeriesSplit`.
- `day` é uma categoria e `period_index` possui comportamento cíclico.
- As variáveis já foram normalizadas e não podem ser convertidas com segurança para as unidades econômicas originais.
- `date_normalized` possui repetições e algumas reduções ao longo da sequência; preserve a ordem original das linhas.
- Os dados cobrem o período de maio de 1996 a dezembro de 1998.

## Fonte e licença

OpenML — [Electricity, dataset 151](https://www.openml.org/d/151).

O campo de licença no OpenML está registrado como `Public`. Ao redistribuir ou adaptar os dados, mantenha a atribuição à fonte e aos autores.

Referência: Harries, M. (1999). *Splice-2 Comparative Evaluation: Electricity Pricing*. Technical Report, University of New South Wales.
