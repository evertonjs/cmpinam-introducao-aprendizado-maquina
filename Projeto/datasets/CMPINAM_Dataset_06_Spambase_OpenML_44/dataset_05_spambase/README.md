# Dataset 05 — Spambase

## Resumo do problema

O objetivo é classificar uma mensagem de e-mail como spam ou não spam a partir de 57 características numéricas extraídas do texto.

O alvo `is_spam` possui duas classes:

- `yes`: mensagem classificada como spam;
- `no`: mensagem legítima.

O dataset não contém os textos originais dos e-mails. Os atributos representam frequências de palavras e caracteres e características de sequências de letras maiúsculas.

## Finalidade didática

O dataset é adequado para trabalhar:

- classificação binária;
- regressão logística e árvores de decisão;
- modelos de alta dimensionalidade;
- seleção e importância de atributos;
- dados esparsos e assimétricos;
- custo diferenciado de falsos positivos e falsos negativos;
- ajuste do limiar de classificação;
- precisão, revocação, F1, ROC-AUC e matriz de confusão;
- generalização e atalhos específicos da fonte dos dados.

## Arquivos disponibilizados

- `spambase_train.csv`: conjunto de treinamento, com 3.680 e-mails;
- `spambase_test.csv`: conjunto de teste, com 921 e-mails;
- `metadata.json`: origem, transformações e estatísticas da divisão;
- `prepare_spambase.py`: script reprodutível de preparação.

Os CSVs usam codificação UTF-8, vírgula como separador e não incluem índice.

Para reproduzir a preparação, instale `pandas`, `scipy` e `scikit-learn` e execute:

```bash
python prepare_spambase.py
```

## Estrutura dos atributos

O dataset possui três grupos de atributos:

| Grupo | Quantidade | Significado |
| --- | ---: | --- |
| `word_freq_*` | 48 | Percentual das palavras do e-mail que corresponde ao termo indicado. |
| `char_freq_*` | 6 | Percentual dos caracteres correspondente ao símbolo indicado. |
| `capital_run_length_*` | 3 | Estatísticas de sequências consecutivas de letras maiúsculas. |

Os atributos de caracteres foram renomeados para evitar códigos percentuais pouco legíveis, como `char_freq_%21`. Por exemplo, o nome passou a ser `char_freq_exclamation`.

## Decisões de curadoria

O arquivo original foi convertido de ARFF para CSV sem excluir atributos ou registros.

Foram realizadas estas transformações:

1. alvo `class` renomeado para `is_spam`;
2. classes `0` e `1` convertidas para `no` e `yes`;
3. nomes dos seis caracteres especiais tornados legíveis;
4. divisão estratificada e consciente de grupos em aproximadamente 80% para treino e 20% para teste;
5. perfis com os mesmos 57 atributos foram mantidos no mesmo lado da divisão.

## Distribuição das classes

| Conjunto | E-mails | Não spam | Spam | Proporção de spam |
| --- | ---: | ---: | ---: | ---: |
| Treino | 3.680 | 2.230 | 1.450 | 39,40% |
| Teste | 921 | 558 | 363 | 39,41% |

As classes são suficientemente representadas. Um classificador que sempre prevê `no` alcança aproximadamente 60,60% de acurácia.

## Problemas encontrados na fonte

### Ordenação por classe

O ARFF contém primeiro os 1.813 spams e depois os 2.788 e-mails legítimos, com uma única transição de classe. Uma divisão baseada diretamente na ordem das linhas produziria conjuntos inválidos.

### Registros coincidentes

Foram encontradas:

- 391 linhas exatamente repetidas;
- 394 vetores de atributos repetidos;
- três perfis com os mesmos atributos, mas rótulos diferentes.

Os registros foram mantidos para preservar a distribuição original. Entretanto, o agrupamento utilizado na divisão impede que perfis idênticos apareçam simultaneamente em treino e teste.

### Divergência sobre valores ausentes

A página atual da UCI marca o dataset como possuindo valores ausentes. Porém, a documentação original afirma que não há ausências, e o arquivo ARFF do OpenML contém zero valores nulos. Os arquivos disponibilizados foram verificados e não possuem valores ausentes.

## Principal limitação: filtro personalizado

Os e-mails legítimos vieram principalmente de mensagens pessoais e profissionais relacionadas à Hewlett-Packard. Por isso, termos como `george`, `650`, `hp` e `hpl` podem funcionar como atalhos para identificar mensagens legítimas.

Esses atributos podem melhorar o desempenho no conjunto disponível sem produzir um filtro geral de spam. A própria documentação original alerta que `george` e o código de área `650` são indicadores específicos da coleção.

Uma atividade recomendada é comparar o modelo completo com outro que remova `word_freq_george` e `word_freq_650`.

## Checagem didática

Na divisão disponibilizada, uma regressão logística padronizada apresentou:

- acurácia: aproximadamente 93,16%;
- precisão para spam: 94,12%;
- revocação para spam: 88,15%;
- taxa de falsos positivos: 3,58%;
- ROC-AUC: 0,976.

Após retirar `word_freq_george` e `word_freq_650`, a taxa de falsos positivos caiu para aproximadamente 3,05%, enquanto a revocação de spam também caiu. Isso permite discutir o compromisso entre bloquear spam e não bloquear mensagens legítimas.

Esses resultados são somente verificações de sanidade e não constituem referência obrigatória para a atividade.

## Cuidados para as atividades

- Falsos positivos são particularmente importantes: classificar uma mensagem legítima como spam pode ser mais prejudicial que deixar passar uma mensagem indesejada.
- O limiar padrão de 0,5 não deve ser tratado como escolha obrigatória.
- As frequências de palavras e caracteres apresentam muitos zeros e valores extremos.
- A regressão logística deve receber padronização ajustada somente no treino.
- Árvores não exigem padronização, mas podem superajustar em um dataset com 57 atributos.
- Seleção de atributos, balanceamento e ajuste do limiar devem utilizar somente o conjunto de treino.
- O dataset não permite aplicar diretamente tokenização, TF-IDF, embeddings ou outros procedimentos de NLP sobre o texto original.

## Limitações

- Os dados foram coletados em 1999 e não representam o spam atual.
- A amostra é fortemente associada ao ambiente pessoal e profissional dos autores.
- Não existem identificadores de remetente, destinatário ou conversa para uma divisão independente por origem.
- Mensagens do mesmo autor ou contexto podem aparecer nos dois conjuntos sem que isso possa ser verificado.
- O dataset avalia atributos previamente extraídos, não um pipeline completo de classificação de e-mails.
- O bom desempenho não deve ser interpretado como evidência de funcionamento em e-mails atuais ou em português.

## Fonte, licença e citação

Fontes:

- OpenML — Spambase, dataset 44: https://www.openml.org/d/44
- UCI Machine Learning Repository — Spambase: https://archive.ics.uci.edu/dataset/94/spambase

A página atual da UCI disponibiliza o dataset sob licença Creative Commons Attribution 4.0 International (CC BY 4.0).

Referência sugerida:

> Hopkins, M., Reeber, E., Forman, G., & Suermondt, J. (1999). *Spambase* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C53G6X
