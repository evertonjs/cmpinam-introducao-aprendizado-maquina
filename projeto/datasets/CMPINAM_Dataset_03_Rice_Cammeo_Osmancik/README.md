# Dataset 03 — Rice: Cammeo e Osmancik

## Resumo do problema

O objetivo é identificar automaticamente a variedade de um grão de arroz — `cammeo` ou `osmancik` — utilizando sete características morfológicas extraídas de sua imagem.

Cada linha representa um único grão. As imagens passaram por processamento computacional e foram transformadas em medidas relacionadas a tamanho, contorno e formato. A tarefa é de classificação binária, com `variety` como variável-alvo.

Em uma aplicação, um modelo desse tipo poderia auxiliar a classificação ou a inspeção automática de grãos. O dataset fornecido, entretanto, não contém as imagens originais, apenas os atributos já extraídos.

## Finalidade didática

Este é um dataset especialmente adequado para introduzir:

- classificação binária;
- separação entre atributos e alvo;
- divisão entre treino e teste;
- regressão logística;
- KNN e a importância da padronização;
- árvores de decisão;
- matriz de confusão e métricas de classificação;
- fronteiras de decisão;
- correlação e multicolinearidade;
- seleção de atributos e PCA.

Como todos os atributos são numéricos, os estudantes podem concentrar-se no funcionamento dos modelos antes de estudar codificação de variáveis categóricas.

## Arquivos disponibilizados

- `rice_train.csv`: conjunto de treinamento, com 3.048 grãos;
- `rice_test.csv`: conjunto de teste, com 762 grãos;
- `metadata.json`: origem, transformações e estatísticas da divisão;
- `prepare_rice.py`: script reprodutível de preparação.

Os CSVs usam codificação UTF-8, vírgula como separador e não incluem índice.

Para reproduzir a preparação, instale `pandas`, `scipy` e `scikit-learn` e execute:

```bash
python prepare_rice.py
```

## Decisões de curadoria

O arquivo original em formato ARFF foi convertido para CSV sem remover atributos ou registros.

Foram realizadas apenas estas transformações:

1. nomes das colunas convertidos para `snake_case`;
2. alvo `Class` renomeado para `variety`;
3. nomes das variedades convertidos para letras minúsculas;
4. `area` e `convex_area` preservadas como valores inteiros;
5. atributos contínuos arredondados para seis casas decimais, eliminando precisão numérica excessiva sem alterar sua utilidade didática;
6. divisão aleatória estratificada em 80% para treino e 20% para teste, com `random_state=42`.

Não há valores ausentes, linhas duplicadas nem vetores de atributos duplicados na fonte.

## Distribuição das classes

As classes apresentam um desequilíbrio moderado, mas nenhuma delas é rara.

| Conjunto | Grãos | `cammeo` | `osmancik` | Proporção de `cammeo` |
| --- | ---: | ---: | ---: | ---: |
| Treino | 3.048 | 1.304 | 1.744 | 42,78% |
| Teste | 762 | 326 | 436 | 42,78% |

O conjunto de teste deve permanecer separado durante padronização, treinamento, seleção de atributos e ajuste de hiperparâmetros.

## Dicionário de dados

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `area` | inteira | Número de pixels dentro dos limites do grão. |
| `perimeter` | contínua | Comprimento do contorno do grão, calculado a partir dos pixels de sua borda. |
| `major_axis_length` | contínua | Comprimento do maior eixo associado ao formato do grão. |
| `minor_axis_length` | contínua | Comprimento do menor eixo associado ao formato do grão. |
| `eccentricity` | contínua | Medida do alongamento da elipse equivalente ao grão. Valores mais altos indicam forma mais alongada. |
| `convex_area` | inteira | Número de pixels da menor região convexa que envolve o grão. |
| `extent` | contínua | Razão entre a área do grão e a área de sua caixa delimitadora. |
| `variety` | alvo categórico | Variedade do grão: `cammeo` ou `osmancik`. |

## Cuidados para as atividades

- Os atributos possuem escalas bastante diferentes. `area`, por exemplo, está na ordem de dezenas de milhares, enquanto `eccentricity` e `extent` variam aproximadamente entre 0 e 1.
- KNN, regressão logística regularizada e outros modelos sensíveis à escala devem usar padronização ajustada somente nos dados de treino.
- Árvores de decisão não exigem padronização para realizar as divisões.
- `area` e `convex_area` são quase redundantes, com correlação aproximada de 0,999.
- `perimeter` também apresenta correlação elevada com `area`, `convex_area` e `major_axis_length`.
- A multicolinearidade pode afetar a interpretação dos coeficientes da regressão logística, mesmo quando o desempenho preditivo permanece bom.
- Como as duas classes são razoavelmente representadas, acurácia, precisão, revocação, F1 e matriz de confusão podem ser interpretadas sem a severidade de desbalanceamento observada nos datasets anteriores.

## Limitações

- O dataset contém atributos derivados, mas não fornece as imagens que originaram as medidas.
- O estudante não poderá reproduzir a etapa de segmentação e extração das características visuais.
- Foram avaliadas somente duas variedades cultivadas na Turquia; o modelo não deve ser generalizado para outras variedades sem novos dados.
- O desempenho pode depender das condições de captura das imagens e do processo utilizado para extrair os atributos.
- A UCI não informa uma divisão por lote, origem ou sessão de captura. A separação disponibilizada é, portanto, aleatória e estratificada.

## Fonte, licença e citação

Fonte: UCI Machine Learning Repository — Rice (Cammeo and Osmancik)  
https://archive.ics.uci.edu/dataset/545/rice+cammeo+and+osmancik

Licença: Creative Commons Attribution 4.0 International (CC BY 4.0).

Referência sugerida:

> *Rice (Cammeo and Osmancik)* [Dataset]. (2019). UCI Machine Learning Repository. https://doi.org/10.24432/C5MW4Z

Artigo associado:

> Cinar, I., & Koklu, M. (2019). Classification of Rice Varieties Using Artificial Intelligence Methods. *International Journal of Intelligent Systems and Applications in Engineering, 7*(3), 188–194. https://doi.org/10.18201/ijisae.2019355381
