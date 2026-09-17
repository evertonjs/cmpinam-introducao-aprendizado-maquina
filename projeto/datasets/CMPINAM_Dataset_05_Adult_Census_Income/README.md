# Dataset 05 — Adult / Census Income

## Visão geral

Dados históricos do Censo dos Estados Unidos de 1994. O objetivo é prever se a renda anual registrada é superior a US$ 50 mil.

- **Tarefa:** classificação binária
- **Alvo:** `income_over_50k`
- **Classes:** `1` para renda superior a US$ 50 mil e `0` para renda menor ou igual
- **Atributos preditores:** 12

## Arquivos

- `train.csv`: 32.561 registros para treinamento.
- `test.csv`: 16.281 registros para avaliação final.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A divisão oficial da fonte foi preservada e deve ser mantida durante os experimentos.

## Distribuição das classes

| Conjunto | Registros | Classe `0` | Classe `1` |
| --- | ---: | ---: | ---: |
| Treino | 32.561 | 24.720 | 7.841 |
| Teste | 16.281 | 12.435 | 3.846 |

## Variáveis

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `age` | inteira | Idade em anos. |
| `workclass` | categórica | Tipo de vínculo ou setor de trabalho. |
| `education` | categórica | Escolaridade declarada. |
| `marital_status` | categórica | Estado civil. |
| `occupation` | categórica | Grupo ocupacional. |
| `relationship` | categórica | Papel familiar informado. |
| `race` | categórica sensível | Categoria racial conforme a fonte histórica. |
| `sex` | categórica sensível | Sexo binário conforme a fonte histórica. |
| `capital_gain` | inteira | Ganho de capital anual. |
| `capital_loss` | inteira | Perda de capital anual. |
| `hours_per_week` | inteira | Horas trabalhadas por semana. |
| `native_country` | categórica | País de origem informado. |
| `income_over_50k` | alvo | Indica se a renda anual supera US$ 50 mil. |

## Orientações de uso

- Há campos ausentes em `workclass`, `occupation` e `native_country`; ajuste a imputação somente com o conjunto de treino.
- O alvo é moderadamente desbalanceado. Use métricas como precisão, revocação, F1, ROC-AUC e PR-AUC além da acurácia.
- `race` e `sex` devem ser considerados em auditorias de desempenho e equidade. Removê-los dos preditores não garante equidade, pois outras variáveis podem atuar como proxies.
- Os dados e as categorias são históricos; o limiar de renda não está corrigido pela inflação.
- O conjunto é adequado para ensino e experimentação, não para decisões reais sobre pessoas.

## Fonte e licença

UCI Machine Learning Repository — [Adult](https://archive.ics.uci.edu/dataset/2/adult).

Licença: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Referência: Becker, B. e Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5XW20](https://doi.org/10.24432/C5XW20).
