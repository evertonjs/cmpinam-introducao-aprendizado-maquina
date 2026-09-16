# Dataset 01 — Bank Marketing

## Finalidade didática

Dataset de classificação binária para prever se um cliente assinará um depósito a prazo (`subscribed`: `yes` ou `no`) a partir de dados de campanhas telefônicas de uma instituição bancária portuguesa.

É especialmente adequado para atividades sobre:

- classificação binária;
- regressão logística e árvores de decisão;
- pré-processamento de variáveis categóricas;
- avaliação além da acurácia;
- desbalanceamento de classes;
- vazamento de dados;
- interpretação responsável de dados pessoais e históricos.

## Arquivos disponibilizados

- `bank_marketing_train.csv`: conjunto de treinamento, com 32.940 registros;
- `bank_marketing_test.csv`: conjunto de teste, com 8.236 registros;
- `metadata.json`: origem, transformações e estatísticas da divisão;
- `prepare_bank_marketing.py`: script que reproduz a preparação a partir do arquivo original.

Os CSVs usam codificação UTF-8, vírgula como separador e não incluem índice.

Para reproduzir a preparação, instale `pandas` e `scikit-learn` e execute:

```bash
python prepare_bank_marketing.py
```

O script baixa o pacote oficial da UCI e recria os dois CSVs e o arquivo de metadados.

## Decisões de curadoria

Foi utilizada a versão `bank-additional-full.csv`, com 41.188 registros e 20 atributos de entrada. Ela é a versão completa enriquecida com indicadores sociais e econômicos e é a variante mais próxima da usada por Moro, Cortez e Rita (2014).

Foram aplicadas as seguintes transformações:

1. remoção das 12 linhas exatamente duplicadas na fonte;
2. exclusão de `duration`;
3. normalização dos nomes com pontos para `snake_case`;
4. renomeação do alvo `y` para `subscribed`;
5. divisão estratificada e consciente de grupos em aproximadamente 80% para treino e 20% para teste, com `random_state=42`.

### Por que `duration` foi excluída?

`duration` representa a duração da última ligação. Esse valor só existe depois que a chamada termina, quando o resultado da oferta já é conhecido. Usá-lo para decidir quem deve ser contatado produziria um modelo artificialmente otimista. A própria documentação da UCI recomenda descartá-lo em um cenário preditivo realista.

### Por que a divisão foi estratificada e consciente de grupos?

A classe positiva é minoritária: cerca de 11,27% dos registros têm `subscribed=yes`. A estratificação mantém praticamente a mesma proporção nos dois conjuntos. O agrupamento impede que registros com o mesmo perfil de atributos, depois da retirada de `duration`, apareçam simultaneamente no treino e no teste.

| Conjunto | Registros | `no` | `yes` | Proporção de `yes` |
| --- | ---: | ---: | ---: | ---: |
| Treino | 32.940 | 29.229 | 3.711 | 11,27% |
| Teste | 8.236 | 7.308 | 928 | 11,27% |

O conjunto de teste deve permanecer separado durante treinamento, seleção de atributos, ajuste de hiperparâmetros e escolha de limiares.

## Dicionário de dados

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
| `campaign` | numérica | Número de contatos na campanha atual, incluindo o último. |
| `pdays` | numérica | Dias desde o contato anterior; `999` indica ausência de contato anterior. |
| `previous` | numérica | Número de contatos anteriores à campanha atual. |
| `poutcome` | categórica | Resultado da campanha de marketing anterior. |
| `emp_var_rate` | numérica | Taxa trimestral de variação do emprego. |
| `cons_price_idx` | numérica | Índice mensal de preços ao consumidor. |
| `cons_conf_idx` | numérica | Índice mensal de confiança do consumidor. |
| `euribor_3m` | numérica | Taxa Euribor de três meses. |
| `nr_employed` | numérica | Número trimestral de empregados. |
| `subscribed` | alvo categórico | Assinatura do depósito a prazo: `yes` ou `no`. |

## Cuidados para as atividades

- A UCI informa ausência de valores nulos formais, mas várias colunas usam `unknown`; portanto, `unknown` deve ser tratado como categoria explícita ou como ausência semântica, conforme o objetivo da aula.
- `pdays=999` é um código sentinela para “não contatado anteriormente”, e não uma quantidade comum de dias.
- A acurácia isolada é inadequada: um classificador que sempre prevê `no` já alcança aproximadamente 88,73%.
- Recomenda-se avaliar matriz de confusão, precisão, revocação, F1, ROC-AUC e, devido ao desbalanceamento, curva Precision–Recall ou Average Precision.
- Transformações como `OneHotEncoder`, padronização, seleção de atributos e reamostragem devem ser ajustadas somente nos dados de treino, preferencialmente dentro de um `Pipeline`.
- Idade, ocupação, estado civil e escolaridade pedem discussão sobre viés, finalidade de uso, privacidade e impacto sobre diferentes grupos.
- Os dados cobrem maio de 2008 a novembro de 2010 em Portugal. O desempenho obtido não deve ser generalizado automaticamente para outros países ou períodos.

## Limitação da divisão adotada

O arquivo original está ordenado aproximadamente no tempo. Para uma aula introdutória e para comparação controlada de classificadores, foi usada uma divisão aleatória estratificada. Essa escolha mistura períodos econômicos entre treino e teste e pode produzir uma estimativa otimista para uma implantação futura. Uma atividade avançada pode comparar esse resultado com uma validação temporal baseada na ordem original.

## Fonte, licença e citação

Fonte: UCI Machine Learning Repository — Bank Marketing  
https://archive.ics.uci.edu/dataset/222/bank+marketing

Licença: Creative Commons Attribution 4.0 International (CC BY 4.0).

Referência sugerida:

> Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5K306

Artigo associado:

> Moro, S., Cortez, P., & Rita, P. (2014). A data-driven approach to predict the success of bank telemarketing. *Decision Support Systems, 62*, 22–31. https://doi.org/10.1016/j.dss.2014.03.001
