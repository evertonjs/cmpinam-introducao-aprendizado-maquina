# Dataset 06 — Spambase

## Visão geral

Características numéricas extraídas de mensagens de e-mail. O objetivo é classificar cada mensagem como spam ou legítima. Os textos originais não fazem parte do conjunto.

- **Tarefa:** classificação binária
- **Alvo:** `is_spam`
- **Classes:** `yes` e `no`
- **Atributos preditores:** 57, todos numéricos

## Arquivos

- `spambase_train.csv`: 3.680 mensagens para treinamento.
- `spambase_test.csv`: 921 mensagens para avaliação final.

Os arquivos usam UTF-8, vírgula como separador e não possuem coluna de índice. A divisão fornecida deve ser preservada durante os experimentos.

## Distribuição das classes

| Conjunto | Registros | `no` | `yes` |
| --- | ---: | ---: | ---: |
| Treino | 3.680 | 2.230 | 1.450 |
| Teste | 921 | 558 | 363 |

## Variáveis

| Grupo | Quantidade | Descrição |
| --- | ---: | --- |
| `word_freq_*` | 48 | Frequência percentual da palavra indicada no nome da variável. |
| `char_freq_*` | 6 | Frequência percentual do caractere indicado no nome da variável. |
| `capital_run_length_average` | 1 | Comprimento médio das sequências de letras maiúsculas. |
| `capital_run_length_longest` | 1 | Maior sequência de letras maiúsculas. |
| `capital_run_length_total` | 1 | Total de letras maiúsculas. |
| `is_spam` | alvo | `yes` para spam e `no` para mensagem legítima. |

## Orientações de uso

- Falsos positivos podem ser especialmente prejudiciais, pois correspondem a mensagens legítimas enviadas para a caixa de spam.
- As variáveis possuem muitos zeros e valores extremos; modelos sensíveis à escala podem exigir padronização.
- Termos como `george`, `650`, `hp` e `hpl` refletem a coleção pessoal e profissional usada na construção do dataset e podem funcionar como atalhos específicos da fonte.
- O conjunto foi coletado em 1999 e não representa necessariamente mensagens atuais ou escritas em português.
- Como os textos não estão disponíveis, este dataset não permite aplicar diretamente tokenização, TF-IDF ou embeddings.

## Fonte e licença

- UCI Machine Learning Repository — [Spambase](https://archive.ics.uci.edu/dataset/94/spambase)
- OpenML — [Spambase, dataset 44](https://www.openml.org/d/44)

Licença: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Referência: Hopkins, M., Reeber, E., Forman, G. e Suermondt, J. (1999). *Spambase* [Dataset]. UCI Machine Learning Repository. [https://doi.org/10.24432/C53G6X](https://doi.org/10.24432/C53G6X).
