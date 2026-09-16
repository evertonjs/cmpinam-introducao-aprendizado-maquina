# Dataset 04 — Electricity

## Resumo do problema

O dataset descreve o mercado de eletricidade de New South Wales, na Austrália, considerando também informações do estado vizinho de Victoria. Cada linha representa um período de 30 minutos e contém preços, demanda e transferência programada de energia entre os dois estados.

O alvo `nsw_price_class` possui duas classes:

- `up`: o preço de New South Wales está acima da referência baseada na média móvel das 24 horas anteriores;
- `down`: o preço está abaixo dessa referência.

Portanto, o problema consiste em classificar o estado do preço em relação à média móvel recente. O conjunto é amplamente usado para estudar classificação em fluxo de dados e mudança de conceito.

### O que o problema não representa

O alvo não informa diretamente se o preço do próximo período ficará maior ou menor que o preço atual. Assim, apresentar a atividade simplesmente como “prever se o preço vai subir ou cair no futuro” seria impreciso.

Além disso, `nsw_price_normalized` participa do próprio contexto usado para definir a classe. O exercício deve ser tratado como benchmark de classificação do estado atual ou de aprendizado em fluxo, e não como um sistema realista de negociação ou previsão futura de preços.

## Finalidade didática

O dataset é adequado para trabalhar:

- classificação binária;
- regressão logística e árvores de decisão;
- dados temporais e separação sequencial;
- mudança de distribuição e concept drift;
- efeito do limiar de classificação;
- comparação entre validação aleatória e temporal;
- avaliação de modelos em fluxo;
- importância de definir corretamente a variável-alvo.

## Arquivos disponibilizados

- `electricity_train.csv`: 36.240 registros, correspondentes a 755 blocos de 48 períodos;
- `electricity_test.csv`: 9.072 registros, correspondentes a 189 blocos de 48 períodos;
- `metadata.json`: origem, transformações e estatísticas da divisão;
- `prepare_electricity.py`: script reprodutível de preparação.

Os CSVs usam codificação UTF-8, vírgula como separador e não incluem índice. A ordem das linhas deve ser preservada.

Para reproduzir a preparação, instale `pandas` e `scipy` e execute:

```bash
python prepare_electricity.py
```

## Decisões de curadoria

O arquivo original em ARFF foi convertido para CSV sem remover registros ou atributos.

Foram realizadas as seguintes transformações:

1. nomes das colunas convertidos para `snake_case` e marcados como normalizados quando necessário;
2. alvo `class` renomeado para `nsw_price_class`;
3. classes convertidas para `up` e `down`;
4. códigos do dia da semana convertidos para categorias como `day_1` e `day_7`;
5. período normalizado convertido novamente para `period_index`, de 1 a 48;
6. divisão sequencial em aproximadamente 80% para treino e 20% para teste, alinhada a dias completos;
7. nenhuma aleatorização ou estratificação foi aplicada.

Não há valores ausentes, linhas duplicadas ou vetores de atributos duplicados.

## Distribuição das classes

| Conjunto | Registros | `down` | `up` | Proporção de `up` |
| --- | ---: | ---: | ---: | ---: |
| Treino | 36.240 | 21.097 | 15.143 | 41,79% |
| Teste | 9.072 | 4.978 | 4.094 | 45,13% |

A alteração da proporção de `up` entre treino e teste faz parte da mudança temporal dos dados e não deve ser corrigida artificialmente por estratificação.

## Dicionário de dados

| Variável | Tipo didático | Descrição |
| --- | --- | --- |
| `date_normalized` | numérica temporal | Representação normalizada da data fornecida pelo OpenML. |
| `day` | categórica | Código anonimizado do dia da semana, de `day_1` a `day_7`. |
| `period_index` | inteira temporal | Período de meia hora dentro do dia, de 1 a 48. |
| `nsw_price_normalized` | numérica | Preço normalizado da eletricidade em New South Wales. |
| `nsw_demand_normalized` | numérica | Demanda normalizada em New South Wales. |
| `vic_price_normalized` | numérica | Preço normalizado da eletricidade em Victoria. |
| `vic_demand_normalized` | numérica | Demanda normalizada em Victoria. |
| `transfer_normalized` | numérica | Transferência programada e normalizada de eletricidade entre os estados. |
| `nsw_price_class` | alvo categórico | Estado `up` ou `down` do preço de NSW em relação à média móvel recente. |

## Cuidados para as atividades

- O treino contém os primeiros registros e o teste contém os registros seguintes. Não use `train_test_split` aleatório para substituir essa divisão em uma avaliação temporal.
- Pré-processamento e escolha de hiperparâmetros devem usar apenas o conjunto de treino.
- Validação cruzada aleatória comum mistura passado e futuro. Para ajustes, use divisões sequenciais como `TimeSeriesSplit`.
- `day` é uma categoria; seus códigos não representam uma grandeza contínua.
- `period_index` tem comportamento cíclico: o período 48 está temporalmente próximo do período 1 do dia seguinte.
- As variáveis já foram normalizadas na versão publicada. O dataset não permite recuperar com segurança os preços e demandas originais.
- O custo de erros pode variar ao longo do tempo; além das métricas agregadas, é útil calcular desempenho por blocos temporais.

## Anomalia no atributo de data

O arquivo é utilizado como fluxo na ordem em que foi publicado, mas `date_normalized` apresenta cinco reduções ao longo dessa sequência. Também existem códigos normalizados de data repetidos para blocos diferentes.

Por esse motivo:

- a ordem original das linhas foi preservada;
- o arquivo não foi reordenado por `date_normalized`;
- não foram inventadas datas civis;
- a separação foi descrita como sequencial pela ordem do ARFF, e não como reconstrução perfeita do calendário.

Essa limitação é uma boa oportunidade para discutir qualidade de metadados e validação de atributos temporais.

## Checagem didática

Em uma avaliação simples, a divisão sequencial apresentou comportamento diferente da divisão aleatória. Uma regressão logística obteve aproximadamente 65,3% de acurácia na separação sequencial e 76,3% na separação aleatória. A diferença mostra que embaralhar dados temporais pode alterar substancialmente a avaliação.

Esses valores são apenas verificações de sanidade e não constituem resultados de referência para a atividade.

## Limitações

- Os dados cobrem apenas o mercado australiano de NSW e Victoria entre maio de 1996 e dezembro de 1998.
- Os valores foram normalizados por terceiros e não estão nas unidades econômicas originais.
- O alvo é definido em relação a uma média móvel, e não como preço futuro.
- O dataset não contém a média móvel utilizada na construção do alvo.
- A versão do OpenML é principalmente um benchmark histórico de concept drift, não um conjunto atual para decisões no mercado de energia.

## Fonte, licença e referências

Fonte: OpenML — Electricity, dataset 151  
https://www.openml.org/d/151

O campo de licença no OpenML está registrado como `Public`. Atribua a fonte e os autores ao redistribuir ou adaptar o material.

Referências indicadas pelo OpenML:

> Harries, M. (1999). *Splice-2 Comparative Evaluation: Electricity Pricing*. Technical Report, University of New South Wales.

> Gama, J., Medas, P., Castillo, G., & Rodrigues, P. (2004). Learning with Drift Detection. *SBIA Brazilian Symposium on Artificial Intelligence*, 286–295.
