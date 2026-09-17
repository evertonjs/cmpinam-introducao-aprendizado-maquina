# Dataset 03 — Rice: Cammeo e Osmancik

## Visão geral

Dados morfológicos extraídos de imagens de grãos de arroz. O objetivo é identificar automaticamente uma das duas variedades avaliadas.

- **Tarefa:** classificação binária
- **Alvo:** `variety`
- **Classes:** `cammeo` e `osmancik`
- **Atributos preditores:** 7, todos numéricos

## Arquivos

- `rice_train.csv`: 3.048 grãos para treinamento.
- `rice_test.csv`: 762 grãos para avaliação final.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A divisão fornecida deve ser preservada durante os experimentos.

## Distribuição das classes

| Conjunto | Registros | `cammeo` | `osmancik` |
| --- | ---: | ---: | ---: |
| Treino | 3.048 | 1.304 | 1.744 |
| Teste | 762 | 326 | 436 |

## Variáveis

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `area` | inteira | Número de pixels dentro dos limites do grão. |
| `perimeter` | numérica | Comprimento do contorno do grão. |
| `major_axis_length` | numérica | Comprimento do maior eixo do grão. |
| `minor_axis_length` | numérica | Comprimento do menor eixo do grão. |
| `eccentricity` | numérica | Medida do alongamento da elipse equivalente. |
| `convex_area` | inteira | Número de pixels da menor região convexa que envolve o grão. |
| `extent` | numérica | Razão entre a área do grão e a área de sua caixa delimitadora. |
| `variety` | alvo | Variedade `cammeo` ou `osmancik`. |

## Orientações de uso

- Os atributos possuem escalas diferentes; KNN e modelos lineares regularizados devem usar padronização ajustada somente no treino.
- `area` e `convex_area` são quase redundantes, e outros atributos de tamanho também apresentam forte correlação.
- O dataset contém apenas os atributos extraídos, não as imagens originais.
- As observações representam somente duas variedades cultivadas na Turquia.

## Fonte e licença

UCI Machine Learning Repository — [Rice (Cammeo and Osmancik)](https://archive.ics.uci.edu/dataset/545/rice+cammeo+and+osmancik).

Licença: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Referência: *Rice (Cammeo and Osmancik)* (2019) [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5MW4Z](https://doi.org/10.24432/C5MW4Z).
