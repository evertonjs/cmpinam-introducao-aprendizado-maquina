# Dataset 07 — HTRU2: candidatos a pulsares

## Visão geral

Estatísticas extraídas de sinais captados por radiotelescópio. O objetivo é identificar se cada candidato corresponde a um pulsar real ou a interferência e ruído.

- **Tarefa:** classificação binária
- **Alvo:** `is_pulsar`
- **Classes:** `1` para pulsar e `0` para não pulsar
- **Atributos preditores:** 8, todos numéricos

## Arquivos

- `train.csv`: 14.318 candidatos para treinamento.
- `test.csv`: 3.580 candidatos para avaliação final.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A divisão estratificada fornecida deve ser preservada durante os experimentos.

## Distribuição das classes

| Conjunto | Registros | Classe `0` | Classe `1` |
| --- | ---: | ---: | ---: |
| Treino | 14.318 | 13.007 | 1.311 |
| Teste | 3.580 | 3.252 | 328 |

A classe positiva representa aproximadamente 9,16% dos registros.

## Variáveis

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `mean_integrated_profile` | numérica | Média do perfil integrado do pulso. |
| `std_integrated_profile` | numérica | Desvio-padrão do perfil integrado do pulso. |
| `excess_kurtosis_integrated_profile` | numérica | Excesso de curtose do perfil integrado. |
| `skewness_integrated_profile` | numérica | Assimetria do perfil integrado. |
| `mean_dm_snr_curve` | numérica | Média da curva DM–SNR. |
| `std_dm_snr_curve` | numérica | Desvio-padrão da curva DM–SNR. |
| `excess_kurtosis_dm_snr_curve` | numérica | Excesso de curtose da curva DM–SNR. |
| `skewness_dm_snr_curve` | numérica | Assimetria da curva DM–SNR. |
| `is_pulsar` | alvo | `1` para pulsar real e `0` para interferência ou ruído. |

## Orientações de uso

- Não use somente acurácia: prever sempre a classe `0` já produziria aproximadamente 90,84% de acerto.
- Considere PR-AUC, precisão, revocação e F1, além de ROC-AUC.
- Um falso negativo deixa de encaminhar um candidato real para inspeção; um falso positivo aumenta o trabalho de revisão.
- As variáveis são estatísticas resumidas, não imagens nem séries temporais brutas.
- O conjunto não contém posição no céu e não permite inferir propriedades físicas ou localização dos pulsares.

## Fonte e licença

UCI Machine Learning Repository — [HTRU2](https://archive.ics.uci.edu/dataset/372/htru2).

Licença: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Referência: Lyon, R. (2015). *HTRU2* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C5DK6R](https://doi.org/10.24432/C5DK6R).
