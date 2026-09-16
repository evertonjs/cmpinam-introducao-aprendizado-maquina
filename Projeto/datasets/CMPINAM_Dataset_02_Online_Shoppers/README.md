# Dataset 02 — Online Shoppers Purchasing Intention

## Resumo do problema

Uma loja virtual gostaria de identificar, durante uma sessão de navegação, se o visitante provavelmente concluirá uma compra. Cada registro representa uma sessão e reúne informações sobre páginas visitadas, tempo de permanência, métricas de navegação, origem do tráfego, dispositivo, período e tipo de visitante.

O objetivo é construir um classificador binário para prever `purchase`:

- `yes`: a sessão terminou em compra;
- `no`: a sessão não terminou em compra.

Essa previsão poderia apoiar ações como personalização da experiência, recomendação de produtos ou intervenção para reduzir abandono. Em uma aplicação real, toda variável utilizada precisa estar disponível no instante em que o modelo produz a previsão.

## Finalidade didática

O dataset é adequado para atividades sobre:

- classificação binária;
- regressão logística e árvores de decisão;
- variáveis numéricas e categóricas;
- desbalanceamento de classes;
- matriz de confusão, precisão, revocação, F1, ROC-AUC e Average Precision;
- análise de importância de atributos;
- vazamento de dados e definição do instante da previsão;
- interpretação de comportamento de navegação.

## Arquivos disponibilizados

- `online_shoppers_train.csv`: conjunto de treinamento, com 9.864 sessões;
- `online_shoppers_test.csv`: conjunto de teste, com 2.466 sessões;
- `metadata.json`: origem, transformações e estatísticas da divisão;
- `prepare_online_shoppers.py`: script reprodutível de preparação.

Os CSVs usam codificação UTF-8, vírgula como separador e não incluem índice.

Para reproduzir a preparação, instale `pandas` e `scikit-learn` e execute:

```bash
python prepare_online_shoppers.py
```

## Decisões de curadoria

O único arquivo completo disponibilizado pela UCI foi preservado, com seus 12.330 registros e 17 atributos de entrada.

Foram aplicadas apenas transformações pedagógicas e de organização:

1. nomes de colunas convertidos para `snake_case` e tornados mais descritivos;
2. alvo `Revenue` renomeado para `purchase`;
3. valores booleanos convertidos para `yes` e `no`;
4. códigos de sistema operacional, navegador, região e tráfego convertidos em categorias textuais, como `os_2` e `traffic_4`;
5. abreviações dos meses padronizadas em letras minúsculas;
6. divisão estratificada e consciente de grupos em aproximadamente 80% para treino e 20% para teste, com `random_state=42`.

A fonte contém 125 linhas exatamente iguais. Elas foram mantidas porque a documentação informa que cada sessão pertence a um usuário diferente. Entretanto, perfis idênticos foram agrupados no mesmo lado da divisão para evitar que apareçam simultaneamente em treino e teste.

## Distribuição da classe

Somente 15,47% das sessões terminam em compra. Um classificador que sempre prevê `no` já alcança aproximadamente 84,53% de acurácia.

| Conjunto | Sessões | `no` | `yes` | Proporção de `yes` |
| --- | ---: | ---: | ---: | ---: |
| Treino | 9.864 | 8.338 | 1.526 | 15,47% |
| Teste | 2.466 | 2.084 | 382 | 15,49% |

O conjunto de teste deve permanecer separado durante pré-processamento, treinamento, escolha de atributos, ajuste de hiperparâmetros e definição do limiar de classificação.

## Dicionário de dados

| Variável | Tipo didático | Descrição |
| --- | --- | --- |
| `administrative_pages` | numérica | Quantidade de páginas administrativas visitadas. |
| `administrative_duration` | numérica | Tempo total em páginas administrativas. |
| `informational_pages` | numérica | Quantidade de páginas informativas visitadas. |
| `informational_duration` | numérica | Tempo total em páginas informativas. |
| `product_related_pages` | numérica | Quantidade de páginas relacionadas a produtos visitadas. |
| `product_related_duration` | numérica | Tempo total em páginas relacionadas a produtos. |
| `bounce_rate` | numérica | Taxa média de rejeição associada às páginas da sessão. |
| `exit_rate` | numérica | Taxa média de saída associada às páginas da sessão. |
| `page_value` | numérica | Valor médio atribuído às páginas visitadas antes de transações. |
| `special_day` | numérica | Proximidade da visita a uma data comercial especial, entre 0 e 1. |
| `month` | categórica | Mês da sessão. |
| `operating_system` | categórica | Código anonimizado do sistema operacional. |
| `browser` | categórica | Código anonimizado do navegador. |
| `region` | categórica | Código anonimizado da região. |
| `traffic_type` | categórica | Código anonimizado da origem ou tipo de tráfego. |
| `visitor_type` | categórica | Visitante novo, recorrente ou outro. |
| `weekend` | categórica binária | Indica se a sessão ocorreu no fim de semana. |
| `purchase` | alvo binário | Indica se a sessão terminou em compra. |

As durações não têm unidade explicitamente confirmada na página da UCI e não devem ser rotuladas como segundos sem outra documentação que sustente essa interpretação.

## Cuidados para as atividades

- `operating_system`, `browser`, `region` e `traffic_type` são códigos de categorias, não grandezas numéricas ordenadas. Por isso, não devem ser tratados como medidas contínuas.
- Não há valores ausentes formais no arquivo.
- Os valores numéricos têm escalas muito diferentes; modelos lineares podem se beneficiar de padronização.
- As distribuições de contagens e durações são assimétricas e contêm valores extremos legítimos.
- Como a classe positiva é minoritária, a acurácia deve ser acompanhada de métricas voltadas à classe `yes`.
- Qualquer transformação ou reamostragem deve ser ajustada somente no conjunto de treino, preferencialmente dentro de um `Pipeline`.
- O custo de um falso positivo e de um falso negativo precisa ser relacionado à intervenção escolhida pela loja.

### Atenção especial a `page_value`

`page_value` é um atributo extremamente associado à compra. Ele foi mantido porque integra o dataset original e o estudo de previsão em tempo real. Entretanto, a turma deve definir claramente o instante da previsão e verificar como esse valor seria calculado em produção.

Se `page_value` incorporar informações da própria transação que se deseja prever, haverá vazamento de dados. Uma atividade recomendada é comparar modelos com e sem esse atributo e discutir por que o desempenho muda tanto.

## Limitações

- Os dados vieram de um único site de comércio eletrônico e de um período de um ano; não representam automaticamente outros setores, sites ou períodos.
- Os códigos anônimos impedem interpretar substantivamente categorias específicas de navegador, região, sistema operacional e tráfego.
- Não há carimbo temporal completo para construir uma separação cronológica confiável.
- As variáveis descrevem comportamento acumulado na sessão. Uma aplicação em tempo real precisa determinar em qual ponto da navegação esses valores serão observados.

## Fonte, licença e citação

Fonte: UCI Machine Learning Repository — Online Shoppers Purchasing Intention Dataset  
https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

Licença: Creative Commons Attribution 4.0 International (CC BY 4.0).

Referência sugerida:

> Sakar, C., & Kastro, Y. (2018). *Online Shoppers Purchasing Intention Dataset* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5F88Q

Artigo associado:

> Sakar, C. O., Polat, S. O., Katircioglu, M., & Kastro, Y. (2019). Real-time prediction of online shoppers’ purchasing intention using multilayer perceptron and LSTM recurrent neural networks. *Neural Computing and Applications, 31*, 6893–6908. https://doi.org/10.1007/s00521-018-3523-0
