# Dataset 06 — HTRU2: classificação de candidatos a pulsares

## Resumo do problema

O objetivo é estimar se um sinal detectado por um radiotelescópio corresponde a um **pulsar real** ou a interferência/ruído. Cada linha representa um candidato e contém oito estatísticas numéricas extraídas do perfil integrado do pulso e da curva DM–SNR. A variável-alvo é `is_pulsar`: `1` indica pulsar e `0` indica não pulsar.

Pulsares são raros. Por isso, este é um problema de classificação binária desbalanceada: apenas 1.639 dos 17.898 registros (9,16%) pertencem à classe positiva.

## Decisão de curadoria

O link analisado aponta para a competição **Kaggle Playground Series S3E10**, que usa 117.564 exemplos sintéticos gerados a partir do HTRU2. Como arquivos de competição ficam sujeitos às regras de acesso e redistribuição da Kaggle, este pacote não republica os dados sintéticos.

Para uso didático e distribuição à turma, adotamos o **HTRU2 original**, que tem as mesmas oito variáveis, observações reais verificadas por anotadores humanos e licença CC BY 4.0. Essa escolha também facilita discutir a diferença entre dados observacionais e dados sintéticos.

## Estrutura dos arquivos

- `train.csv`: 14.318 registros, com 13.007 não pulsares e 1.311 pulsares.
- `test.csv`: 3.580 registros, com 3.252 não pulsares e 328 pulsares.
- `metadata.csv`: descrição das variáveis e correspondência com os nomes da competição.
- `split_info.json`: parâmetros e contagens da divisão.
- `prepare_dataset.py`: script que baixa a fonte e recria a divisão.
- `baseline_example.py`: regressão logística com avaliação probabilística.
- `LICENSE_SOURCE.md`: licença e forma de citação da fonte.

Os dois CSVs possuem a variável-alvo. O conjunto de teste foi separado para avaliação pedagógica, não é o `test.csv` sem rótulos da competição Kaggle.

## Divisão treino/teste

- Proporção: 80% treino e 20% teste.
- Método: amostragem aleatória estratificada pela classe.
- Semente: `42`.
- Valores ausentes: nenhum.
- Registros duplicados: nenhum.
- Vetores de atributos duplicados: nenhum.

O identificador `id` da competição não foi incluído, pois é apenas um identificador de linha e não representa uma medida astronômica.

## Uso didático recomendado

Este dataset é apropriado para:

- regressão logística e interpretação de probabilidades;
- árvores de decisão e métodos de ensemble;
- padronização de variáveis;
- comparação entre acurácia, precisão, revocação, F1, ROC-AUC e PR-AUC;
- desbalanceamento de classes e escolha de limiar;
- calibração e `log loss`.

Não use somente acurácia: um classificador que sempre prevê “não pulsar” já alcança 90,84% no teste, mas encontra zero pulsares.

## Baselines na divisão fornecida

| Modelo | Log loss | ROC-AUC | PR-AUC | Acurácia | Precisão (pulsar) | Revocação (pulsar) | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Frequência da classe | 0,3063 | 0,5000 | 0,0916 | 0,9084 | 0,0000 | 0,0000 | 0,0000 |
| Regressão logística com padronização | 0,0695 | 0,9710 | 0,9328 | 0,9796 | 0,9443 | 0,8262 | 0,8813 |
| Árvore de decisão regularizada | 0,0817 | 0,9730 | 0,9141 | 0,9788 | 0,9286 | 0,8323 | 0,8778 |

Os valores são referências, não metas obrigatórias. O limiar usado para as métricas de classe foi 0,5.

## Cuidados de interpretação

- As variáveis são estatísticas resumidas do sinal, não imagens nem séries temporais brutas.
- A classe positiva é rara; PR-AUC, precisão e revocação merecem atenção especial.
- Um falso negativo pode deixar de encaminhar um candidato real para inspeção. Um falso positivo aumenta o trabalho de revisão. O limiar deve refletir esse custo.
- O conjunto não contém posição no céu nem outros detalhes astronômicos. Não serve para inferir propriedades físicas ou localização dos pulsares.
- O split é aleatório porque a fonte não fornece ordem temporal nem identificadores de observação que sustentem uma divisão temporal ou por grupo.

## Fontes

- UCI HTRU2: https://archive.ics.uci.edu/dataset/372/htru2
- DOI: https://doi.org/10.24432/C5DK6R
- Competição analisada: https://www.kaggle.com/competitions/playground-series-s3e10
