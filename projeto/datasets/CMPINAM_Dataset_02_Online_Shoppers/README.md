# Dataset 02 — Online Shoppers Purchasing Intention

## Visão geral

Cada registro representa uma sessão em uma loja virtual. O objetivo é prever se a sessão terminará em compra a partir de informações de navegação, origem do tráfego, dispositivo e período.

- **Tarefa:** classificação binária
- **Alvo:** `purchase`
- **Classes:** `yes` e `no`
- **Atributos preditores:** 17

## Arquivos

- `online_shoppers_train.csv`: 9.864 sessões para treinamento.
- `online_shoppers_test.csv`: 2.466 sessões para avaliação final.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A divisão fornecida deve ser preservada durante os experimentos.

## Distribuição das classes

| Conjunto | Registros | `no` | `yes` |
| --- | ---: | ---: | ---: |
| Treino | 9.864 | 8.338 | 1.526 |
| Teste | 2.466 | 2.084 | 382 |

A classe positiva representa aproximadamente 15,47% dos registros.

## Variáveis

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `administrative_pages` | numérica | Quantidade de páginas administrativas visitadas. |
| `administrative_duration` | numérica | Tempo total em páginas administrativas. |
| `informational_pages` | numérica | Quantidade de páginas informativas visitadas. |
| `informational_duration` | numérica | Tempo total em páginas informativas. |
| `product_related_pages` | numérica | Quantidade de páginas de produtos visitadas. |
| `product_related_duration` | numérica | Tempo total em páginas de produtos. |
| `bounce_rate` | numérica | Taxa média de rejeição associada às páginas da sessão. |
| `exit_rate` | numérica | Taxa média de saída associada às páginas da sessão. |
| `page_value` | numérica | Valor médio atribuído às páginas visitadas antes de transações. |
| `special_day` | numérica | Proximidade da visita a uma data comercial especial. |
| `month` | categórica | Mês da sessão. |
| `operating_system` | categórica | Código anonimizado do sistema operacional. |
| `browser` | categórica | Código anonimizado do navegador. |
| `region` | categórica | Código anonimizado da região. |
| `traffic_type` | categórica | Código anonimizado da origem do tráfego. |
| `visitor_type` | categórica | Tipo de visitante. |
| `weekend` | categórica binária | Indica sessão ocorrida no fim de semana. |
| `purchase` | alvo | Indica se a sessão terminou em compra. |

## Orientações de uso

- `operating_system`, `browser`, `region` e `traffic_type` são categorias, não grandezas numéricas ordenadas.
- As escalas numéricas são diferentes; modelos lineares podem se beneficiar de padronização.
- A classe positiva é minoritária, portanto não avalie o modelo apenas pela acurácia.
- `page_value` tem forte associação com o alvo. Defina o instante da previsão e verifique se essa informação estaria disponível para evitar vazamento de dados.
- Os dados representam um único comércio eletrônico durante aproximadamente um ano.

## Fonte e licença

UCI Machine Learning Repository — [Online Shoppers Purchasing Intention Dataset](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset).

Licença: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Referência: Sakar, C. e Kastro, Y. (2018). *Online Shoppers Purchasing Intention Dataset* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5F88Q](https://doi.org/10.24432/C5F88Q).
