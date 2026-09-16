# Dataset 07 — Adult / Census Income

## Resumo do problema

O objetivo é prever se a renda anual de uma pessoa é **superior a US$ 50 mil** a
partir de características do Censo dos Estados Unidos de 1994. É um problema de
**classificação binária**: `income_over_50k = 1` para renda acima de US$ 50 mil e
`0` para renda menor ou igual a esse valor.

O conjunto é útil para estudar pipelines com variáveis numéricas e categóricas,
valores ausentes, desbalanceamento e avaliação de equidade. Ele não deve ser
tratado como retrato atual da economia: o limiar monetário não foi corrigido pela
inflação e os registros são históricos.

## Arquivos

- `train.csv`: 32.561 registros do arquivo oficial `adult.data`.
- `test.csv`: 16.281 registros do arquivo oficial `adult.test`.
- `metadata.csv`: dicionário das 13 colunas entregues.
- `split_info.json`: estratégia de divisão, contagens e ausências.
- `prepare_dataset.py`: reprodução da curadoria a partir dos arquivos UCI.
- `baseline_example.py`: regressão logística e auditoria descritiva por grupos.
- `baseline_results.json`: resultados produzidos pelo script de baseline.
- `LICENSE_SOURCE.md`: fonte, citação e licença.

## Curadoria aplicada

A divisão oficial da UCI foi preservada, evitando criar um corte aleatório novo.
Os nomes foram convertidos para `snake_case`, os pontos finais dos rótulos do
arquivo de teste foram removidos e a variável-alvo foi codificada como 0/1.

Duas colunas da fonte não estão nos CSVs:

- `fnlwgt`: peso amostral do Censo, não uma característica pessoal comum para
  inferência. Seu uso exigiria uma discussão específica sobre ponderação.
- `education_num`: codificação ordinal redundante com `education`.

Os símbolos `?` da fonte foram convertidos em campos vazios. Eles ocorrem em
`workclass`, `occupation` e `native_country`. A imputação deve ser ajustada apenas
no treino e depois aplicada ao teste.

Há perfis repetidos depois da remoção das duas colunas. Eles foram preservados:
sem identificadores pessoais, linhas iguais podem representar pessoas diferentes.

## Distribuição da classe

| Parte | Classe 0 | Classe 1 | Positivos |
|---|---:|---:|---:|
| Treino | 24.720 | 7.841 | 24,08% |
| Teste | 12.435 | 3.846 | 23,62% |

Por causa do desbalanceamento moderado, não use apenas acurácia. Relate também
precisão, revocação, F1, ROC-AUC e PR-AUC.

## Variáveis sensíveis e uso responsável

`race` e `sex` são mantidas para permitir auditoria de desempenho e disparidades,
mas o baseline as exclui dos preditores. `native_country`, `relationship` e
`marital_status` também podem funcionar como proxies. Remover atributos sensíveis
não garante equidade: outras variáveis podem preservar informações correlacionadas.

Este conjunto é indicado para ensino e experimentação. Não deve fundamentar
decisões reais sobre emprego, crédito, seguro, remuneração ou acesso a serviços.
Os grupos e rótulos refletem limitações do Censo de 1994, inclusive uma variável
de sexo estritamente binária na fonte.

## Baseline

Execute:

```bash
python baseline_example.py
```

O pipeline faz imputação, padronização numérica, one-hot encoding e regressão
logística. Ele não usa `race` nem `sex` como preditores e gera métricas globais e
uma auditoria descritiva por esses grupos. Os resultados são referência de
sanidade, não meta de desempenho nem comprovação de justiça.

Resultados obtidos na divisão oficial: acurácia 0,851; precisão 0,730; revocação
0,584; F1 0,649; ROC-AUC 0,904; PR-AUC 0,758. Pequenas diferenças podem ocorrer
com outras versões das bibliotecas.

## Fonte

Becker, B. & Kohavi, R. (1996). *Adult* [Dataset]. UCI Machine Learning
Repository. https://doi.org/10.24432/C5XW20

Licença da fonte: CC BY 4.0. Consulte `LICENSE_SOURCE.md`.
