# CMPINAM — Padrão das Aulas (Slides)

Este arquivo define o padrão visual, estrutural e técnico das aulas da disciplina **CMPINAM · Introdução ao Aprendizado de Máquina**.

## Referência canônica atual

A referência canônica passa a ser a **Aula 02 — Fundamentos do Aprendizado de Máquina**.

- Primeiro, padronizar completamente a Aula 02.
- Depois, aplicar o padrão consolidado da Aula 02 às demais aulas.
- Não usar a Aula 10 como referência nesta etapa.
- Preservar a identidade visual já consolidada na Aula 02: fundo claro, tipografia limpa, acento verde, cards minimalistas, muito espaço em branco e hierarquia forte.

Idioma: **português (BR)**.
Disciplina: **CMPINAM · Introdução ao Aprendizado de Máquina** — Curso de Tecnologia em Análise e Desenvolvimento de Sistemas (IFSP).

---

## 1. Formato técnico

- Slides em **1920×1080 (16:9)** usando `deck-stage.js`:
  ```html
  <deck-stage width="1920" height="1080">
  ```
- Cada slide deve ser um `<section>` filho direto do `<deck-stage>`.
- Cada `<section>` deve ter:
  ```html
  data-label="Título interno"
  data-screen-label="NN Título curto"
  ```
- A numeração deve ser sempre com **dois dígitos** no `data-screen-label` e no `.rh-right`:
  - `01`, `02`, `03`...
- O logo do IFSP deve permanecer em:
  ```text
  assets/ifsp-logo.jpg
  ```

---

## 2. Paleta de cores

Usar apenas os tokens da própria Aula 02. Não inventar novas cores.

Tokens principais:

```css
--paper:#FCFCFE;
--tint;
--tint-2;
--ink:#16161D;
--ink-soft:#565664;
--muted:#9A9AAA;
--line:#E5E5EE;
--line-2:#D6D6E2;
--accent:oklch(0.585 0.16 142);
--accent-d;
--accent-soft;
--accent-line;
```

Regras:

- Verde é o **único acento visual**.
- Usar verde com parcimônia: números, barras curtas, palavras-chave, bordas de destaque.
- Não usar cores extras para diferenciar categorias, a menos que já existam na Aula 02 e sejam indispensáveis.
- Evitar gradientes, sombras fortes, excesso de ícones ou aparência de dashboard.

---

## 3. Tipografia

Usar a escala da Aula 02:

```css
--font-display: Space Grotesk;
--font-body: IBM Plex Sans;
--font-mono: JetBrains Mono;

--type-display:108px;
--type-title:66px;
--type-subtitle:42px;
--type-lead:32px;
--type-body:27px;
--type-small:24px;
--type-micro:19px;
```

Regras:

- Títulos principais: `h1.title`.
- Rótulos superiores: `.kicker`.
- Texto introdutório: `.lead`.
- Texto mínimo em slide: **24px**.
- Evitar reduzir fonte para caber conteúdo. Preferir cortar, dividir ou reorganizar.

---

## 4. Estrutura base dos slides

Slides internos devem seguir a estrutura:

```html
<section data-label="..." data-screen-label="NN ...">
  <div class="runhead">
    <div class="rh-left">
      <span class="rh-code">CMPINAM</span>
      <span class="rh-sep">/</span>
      <span>Seção</span>
    </div>
    <div class="rh-right">NN</div>
  </div>

  <div class="frame">
    <div class="kicker">...</div>
    <h1 class="title">...</h1>
    <!-- conteúdo -->
  </div>
</section>
```

Regras:

- A capa não usa `.runhead`.
- Todos os outros slides usam `.runhead`.
- `.rh-right` é obrigatório em todos os slides internos.
- O `.frame` organiza o conteúdo em coluna.
- Evitar `margin-top` inline em blocos que devem ancorar no rodapé.

---

## 5. Famílias de layout da Aula 02

A Aula 02 deve ser padronizada por famílias. Não criar um layout novo para cada slide.

### Família A — Quatro cards conceituais

Usar quando o slide apresenta **quatro ideias equivalentes**: forças, aplicações, problemas, recomendações ou dimensões.

Slides da Aula 02 nesta família:

- 07 — Por que usar AM
- 11 — Aprendizado não supervisionado
- 19 — Desafios: os dados
- 23 — No Free Lunch

#### Variante A1 — Quatro cards sem imagem

Usar quando não há imagem de apoio.

Estrutura:

```html
<div class="card-grid-4 grow">
  <div class="concept-card">
    <div class="card-num">01</div>
    <div class="card-title">Título</div>
    <p>Descrição curta.</p>
    <div class="card-meta">método · exemplo · palavra-chave</div>
  </div>
  ...
</div>
```

Regras:

- Grade 2×2.
- Cards com mesma altura.
- Espaçamento amplo entre cards.
- Cada card deve ter:
  - número `01–04`;
  - barra ou marcador verde curto;
  - título forte;
  - descrição curta;
  - linha final com exemplo, método ou palavra-chave.
- Não usar linhas horizontais longas atravessando o slide.
- Não usar aparência de tabela.

#### Variante A2 — Quatro cards com imagem lateral

Usar quando há uma imagem de apoio no mesmo slide.

Exemplo da Aula 02:

- 07 — Por que usar AM

Estrutura:

```html
<div class="media-card-layout grow">
  <image-slot ...></image-slot>
  <div class="card-grid-4 compact">
    ...
  </div>
</div>
```

Regras:

- Imagem à esquerda.
- Cards à direita em grade 2×2 compacta.
- A linguagem visual dos cards deve ser a mesma da Variante A1.
- A numeração continua obrigatória nos quatro cards.
- A imagem é apoio visual; não deve competir com o título.

#### Quando usar numeração nos cards

Usar numeração quando os cards formam:

- uma enumeração fechada;
- quatro dimensões equivalentes;
- recomendações ou forças principais;
- problemas de uma mesma família;
- consequências práticas de uma definição.

Não usar numeração quando forem:

- apenas dois lados de uma comparação;
- referências/vídeos;
- exemplos independentes sem sequência de leitura;
- cards que já têm identidade própria.

---

### Família B — Definição, contrato ou frase de referência (`.note`)

A caixa `.note` deve ser usada somente quando o slide precisa interromper a leitura para fixar uma definição, tarefa, contrato ou frase de referência.

Uso correto:

```html
<div class="note">
  <div class="note-k">Em uma frase</div>
  <p>Texto curto da definição ou referência.</p>
</div>
```

Regras:

- `.note` verde = referência, definição, tarefa, enunciado ou contrato.
- Sempre deve ter `.note-k`.
- Rótulos recomendados:
  - `Em uma frase`
  - `Definição`
  - `Exemplo`
  - `Tarefa`
  - `Ponto de partida`
- Não usar `.note` verde apenas para observação leve ou comentário final.
- No máximo **uma `.note` verde por slide**.
- Se a `.note` estiver no meio do fluxo, pode ter espaçamento antes/depois.
- Se for o último elemento do `.frame`, não usar `margin-top` inline; deixar ancorar no rodapé.

Caso específico:

- No slide 23, a caixa verde `Em uma frase` faz sentido porque fixa o Teorema do No Free Lunch antes dos desdobramentos.
- Ela deve continuar como `.note`, mas o restante do slide deve usar a mesma família de cards conceituais dos slides 07, 11 e 19.

---

### Família C — Observação ou síntese de fechamento (`.note.mute`)

Usar `.note.mute` para observações, sínteses finais ou fechamento no rodapé.

Uso correto:

```html
<div class="note mute">
  <p><span class="strong">Ideia principal:</span> texto de fechamento.</p>
</div>
```

Regras:

- `.note.mute` é cinza, não verde.
- Nunca usar `.note-k` dentro de `.note.mute`.
- Deve fechar a leitura do slide, preferencialmente no rodapé.
- Não usar estilo inline para simular essa caixa.
- No máximo uma `.note.mute` por slide.

Diferença fundamental:

- `.note` verde = interrompe e fixa uma referência.
- `.note.mute` cinza = fecha e sintetiza.

---

### Família D — Ideia-chave ou alerta (`.idea`)

Usar `.idea` para uma frase curta com ícone, dentro do fluxo ou no rodapé.

Regras:

- Usar para intuição, armadilha ou regra que não pode ser esquecida.
- Não usar `.note-k`.
- Abrir a frase com `<b>`:
  - `Ideia-chave:`
  - `Atenção:`
  - `Nunca:`
- Ícones permitidos:
  - lâmpada: intuição ou ideia-chave;
  - triângulo de alerta: erro a evitar.
- No máximo uma `.idea` por slide.

---

### Família E — Processo ou sequência (`.steps`)

Usar `.steps` quando houver sequência, processo, roteiro, divisão de conjuntos, comparação guiada ou lista de ações.

Slides da Aula 02 que usam essa família:

- 13 — Aprendizado por reforço
- 14 — Batch × Online
- 17 — Estudo de caso
- 18 — Modelo linear
- 21 — Bias × Variância
- 22 — Treino / Validação / Teste
- 25 — Síntese
- 26 — Referências
- 27 — Exercícios propostos

Regras:

- Usar quando a ordem importa ou quando o aluno deve percorrer os itens.
- A numeração fica no componente `.steps .n`, não em cards.
- Evitar misturar `.steps` e cards conceituais no mesmo nível visual.
- Se houver duas colunas de steps, elas devem ter a mesma lógica e densidade.

---

### Família F — Comparação lado a lado

Usar quando o slide compara dois conceitos, abordagens ou problemas.

Exemplos possíveis na Aula 02:

- Tradicional × Aprendizado de Máquina
- Batch × Online
- Instance-based × Model-based
- Overfitting × Underfitting

Regras:

- Usar duas colunas equilibradas.
- Cada lado deve ter título, descrição curta e exemplo.
- Não numerar os lados da comparação.
- Usar divisores, contraste tipográfico ou títulos para separar os lados.
- Não transformar comparação binária em cards numerados.

---

### Família G — Slides com imagem

Usar imagem quando ela ajuda a concretizar o conceito.

Regras:

- Imagem deve ter função didática clara.
- Se houver imagem + cards, usar a Variante A2.
- Se houver imagem + explicação, manter duas áreas bem definidas:
  - imagem como apoio visual;
  - texto como explicação.
- Evitar imagem decorativa sem relação direta com a fala.
- Usar `image-slot` com raio e proporção consistentes.

---

### Família H — Vídeos, referências e debate

Usar para slides de recursos externos, vídeos ou perguntas para discussão.

Exemplo da Aula 02:

- 24 — Para assistir e debater

Regras:

- Não usar o padrão de quatro cards conceituais.
- Cards de vídeo podem usar `.vcard`.
- Perguntas de debate não devem usar a mesma aparência de cards conceituais numerados.
- Separar claramente recurso externo de pergunta ao aluno.

---

## 6. Regras de densidade

- Cada slide deve ter uma função didática clara.
- Preferir uma ideia central por slide.
- Evitar parágrafos longos.
- Evitar mais de quatro blocos principais no mesmo slide.
- Quando houver quatro blocos, usar a Família A.
- Quando houver processo, usar a Família E.
- Quando houver comparação binária, usar a Família F.
- Quando houver fechamento, usar `.note.mute`.

---

## 7. Regras de padronização textual

Cards conceituais devem seguir este formato:

```text
Título
Descrição curta.
Exemplo · técnica · palavra-chave
```

Evitar:

```text
Título
frase longa com definição, método, exemplo e comentário tudo junto no mesmo parágrafo.
```

Preferir:

```text
Clustering
Agrupa dados semelhantes.
k-Means · HCA · segmentação de clientes
```

---

## 8. Checklist antes de finalizar uma aula

- [ ] A Aula 02 foi usada como referência principal.
- [ ] Todos os slides internos têm `.runhead`.
- [ ] Todos os slides internos têm numeração em `.rh-right`.
- [ ] A capa não usa `.runhead`.
- [ ] Não há cores novas fora dos tokens.
- [ ] Cards conceituais equivalentes usam o mesmo padrão.
- [ ] Slides com 4 conceitos usam a Família A.
- [ ] Slides com imagem + 4 conceitos usam a Variante A2.
- [ ] `.note` verde é usada só para definição, tarefa, exemplo ou referência.
- [ ] `.note.mute` cinza é usada só para fechamento ou síntese.
- [ ] `.idea` é usada só para intuição ou alerta.
- [ ] `.steps` é usado só para sequência/processo.
- [ ] Comparações binárias não usam numeração.
- [ ] Não há `margin-top` inline em bloco final ancorado no rodapé.
- [ ] O slide não parece tabela quando deveria ser card.
- [ ] O texto está legível e sem excesso.

---

## 9. Objetivo da padronização

A Aula 02 deve se tornar o modelo-base da disciplina. Ao concluir sua padronização, usar o padrão aqui registrado para revisar e ajustar as demais aulas do projeto CMPINAM.

---

## 10. Histórico de consolidação da Aula 02

### Rodada 1 — `.note`, `.note.mute` e `.idea` — APROVADA

A padronização dos três componentes foi aprovada e passa a ser obrigatória:

- `.note`: caixa verde de definição, referência, exemplo, tarefa, contrato ou enunciado; sempre com `.note-k`.
- `.note.mute`: caixa cinza de síntese ou observação de fechamento; nunca com `.note-k`.
- `.idea`: caixa verde com ícone exclusivamente para intuição ou alerta; nunca com `.note-k`.
- No máximo uma instância de cada tipo por slide.
- Não simular nenhuma dessas caixas com estilos inline.
- Quando o componente for o último filho do `.frame`, preservar a ancoragem automática no rodapé e não usar `margin-top` inline.

Esta decisão foi validada na Aula 02 e deve ser preservada nas rodadas seguintes.
---

## Rodada 2 — Famílias de cards

A Aula 02 passa a distinguir cards pela **função didática**, não apenas pela aparência. Ao criar ou revisar slides, escolher primeiro a função do bloco e só depois aplicar o componente visual correspondente.

### 2.1 Card conceitual numerado

Usar quando o slide apresenta um conjunto fechado de ideias equivalentes que devem ser lidas como coleção organizada.

Uso típico:
- quatro forças;
- quatro aplicações;
- quatro desafios;
- quatro recomendações;
- dimensões equivalentes de um mesmo conceito.

Estrutura recomendada:

```html
<div class="concept-grid">
  <div class="concept-card">
    <div class="concept-n">01</div>
    <div class="concept-h">Título curto</div>
    <p class="concept-desc">Descrição objetiva.</p>
    <div class="concept-meta"><b>Palavra-chave</b> · exemplo</div>
  </div>
</div>
```

Regras:
- usar numeração `01`, `02`, `03`, `04` apenas quando houver uma enumeração fechada;
- todos os cards devem ter a mesma estrutura interna;
- a descrição deve explicar o que é ou o que faz;
- a linha final deve trazer exemplo, técnica, consequência ou palavra-chave;
- evitar frases longas no corpo do card;
- não usar `.feat sm` para esse padrão.

### 2.2 Variante com imagem lateral

Quando o slide precisa de uma imagem de apoio, manter a mesma linguagem dos cards e apenas adaptar a composição.

Estrutura:

```html
<div class="layout-image-cards">
  <image-slot ...></image-slot>
  <div class="concept-grid compact">...</div>
</div>
```

Regras:
- a imagem não muda a função dos cards;
- os cards continuam numerados se forem uma coleção fechada;
- usar versão compacta apenas por restrição de espaço;
- não reduzir o texto abaixo do mínimo definido para a aula.

### 2.3 Card de categoria sem numeração

Usar quando os blocos são categorias independentes e não precisam de ordem de leitura.

Exemplos:
- tipos equivalentes;
- recursos;
- categorias paralelas;
- exemplos independentes.

Regras:
- não usar `01`, `02`, etc.;
- o título da categoria é suficiente para orientar a leitura;
- se a ordem não importa, a numeração vira decoração e deve ser removida.

### 2.4 Card de comparação

Usar quando o slide compara duas abordagens ou conceitos.

Exemplos:
- Batch × Online;
- Instance-based × Model-based.

Regras:
- não usar números sequenciais;
- os dois lados devem ter estrutura paralela;
- cada card deve responder aos mesmos critérios: definição, funcionamento, vantagem/limitação e exemplo;
- evitar que um lado tenha muito mais texto que o outro.

### 2.5 Card de estado

Usar quando o slide mostra estados de um fenômeno, não uma lista de conceitos.

Exemplos:
- underfitting;
- bom ajuste;
- overfitting.

Regras:
- usar rótulos sem numeração;
- destacar o estado alvo com classe semântica, como `.is-target`;
- destacar um caso importante com `.is-accent`;
- nunca usar `style="border-color:..."` para marcar o estado.

### 2.6 Destaques semânticos

Destaques visuais devem usar classes semânticas, não estilos inline.

Preferir:

```html
<div class="concept-card is-accent">...</div>
<div class="concept-card is-target">...</div>
```

Evitar:

```html
<div style="border-color:var(--accent)">...</div>
```

Objetivo: permitir que o padrão seja replicado automaticamente e que mudanças visuais possam ser feitas no CSS sem revisar cada slide manualmente.


---

## Rodada 3 — Uso da numeração interna

A numeração interna dos componentes (`01`, `02`, `03`, `04` etc.) deve ter função semântica. Ela não pode ser usada apenas como recurso decorativo.

### 3.1 Quando usar numeração

Usar números quando o conteúdo representar pelo menos uma destas situações:

- sequência ou ordem de execução;
- etapas de um processo;
- percurso de leitura obrigatório;
- conjunto fechado de princípios, forças, fatores ou desafios;
- itens de uma atividade ou exercício;
- enumeração que precisa ser referenciada durante a explicação.

Exemplos válidos na Aula 02:

- quatro forças do aprendizado de máquina;
- quatro aplicações do aprendizado não supervisionado;
- quatro desafios relacionados aos dados;
- recomendações práticas derivadas do No Free Lunch;
- etapas de treinamento, validação ou experimentação;
- questões numeradas de uma atividade.

### 3.2 Quando não usar numeração

Não usar números quando os elementos forem apenas:

- conceitos em comparação;
- categorias equivalentes sem ordem;
- alternativas paralelas;
- exemplos independentes;
- estados de um fenômeno;
- vídeos, referências ou recursos;
- dois lados de uma oposição conceitual.

Exemplos:

- Batch × Online;
- Instance-based × Model-based;
- Underfitting × bom ajuste × Overfitting;
- referências bibliográficas;
- recursos para assistir;
- categorias que podem ser lidas em qualquer ordem.

### 3.3 Relação com as famílias de cards

A decisão de numerar deve vir depois da escolha da família do card.

- **Card conceitual numerado:** usar quando há coleção fechada ou percurso de leitura.
- **Card de categoria:** não numerar quando a ordem não importa.
- **Card de comparação:** não numerar.
- **Card de estado:** não numerar.
- **Card de exercício:** numerar quando os itens precisam ser identificados.
- **Card de referência ou vídeo:** não numerar.

### 3.4 Formato visual

Quando a numeração for necessária:

- usar sempre dois dígitos: `01`, `02`, `03`...;
- manter posição, escala, cor e espaçamento consistentes;
- não misturar `1`, `02`, `III` ou letras no mesmo conjunto;
- não repetir o número no título e em outro elemento do mesmo card;
- o número deve orientar a leitura, não competir com o título.

Exemplo correto:

```html
<div class="concept-card">
  <div class="concept-n">01</div>
  <div class="concept-h">Simplifica</div>
  <p class="concept-desc">Substitui muitas regras manuais por um modelo que aprende padrões.</p>
</div>
```

Exemplo incorreto:

```html
<div class="concept-card">
  <div class="concept-n">01</div>
  <div class="concept-h">01 · Simplifica</div>
</div>
```

### 3.5 Numeração do slide

A numeração interna não substitui a numeração da apresentação.

- todo slide interno continua com número na `.rh-right`;
- a numeração da `.rh-right` identifica a posição do slide;
- a numeração dentro dos cards identifica itens do conteúdo;
- as duas funções não devem ser confundidas.

Esta regra foi validada na Aula 02 e deve ser aplicada às demais aulas depois que o padrão completo da Aula 02 estiver consolidado.


---

## Rodada 4 — Padronização do componente `.steps`

A Aula 02 usa listas estruturadas em vários contextos. A regra consolidada é que `.steps` é um **componente-base**, mas sua aparência deve variar conforme a função didática. Não usar `.steps` como lista genérica para qualquer conteúdo.

### 4.1 Variantes oficiais de `.steps`

Usar uma variante semântica sempre que a lista tiver papel definido:

- `.list-anatomy` — partes equivalentes de um conceito, fórmula ou mecanismo. Pode usar letras ou símbolos, não números sequenciais.
- `.list-compare` — argumentos paralelos em uma comparação. Usa marcadores simples, sem numeração e sem setas que sugiram processo.
- `.list-process` — etapas realmente ordenadas. Usa numeração e conectores visuais.
- `.list-formula` — elementos de fórmula ou parâmetros. Usa símbolos como chave conceitual.
- `.list-diagnostic` — sinais de diagnóstico ou interpretação. Usa marcadores sem sugerir sequência.
- `.list-summary` — síntese final da aula. Usa números maiores apenas quando as ideias formam uma coleção fechada.
- `.list-refs` — referências bibliográficas. Não deve parecer uma sequência de passos.
- `.list-exercises` — questões ou tarefas. Usa numeração para identificação, não para indicar fluxo técnico.

### 4.2 Quando usar `.steps`

Usar `.steps` quando o conteúdo precisa de uma leitura em blocos bem definidos, com separação clara entre itens.

Exemplos válidos:

- etapas de um processo de ML;
- decomposição de um conceito;
- parâmetros de uma equação;
- diagnóstico de viés e variância;
- síntese da aula;
- exercícios numerados.

### 4.3 Quando evitar `.steps`

Evitar `.steps` quando o conteúdo for:

- card conceitual curto;
- comparação que precisa de dois painéis simétricos;
- referência visual ou vídeo;
- frase de fechamento;
- definição única.

Nesses casos, preferir `concept-card`, `dcard`, `.note`, `.note.mute`, `.idea`, `vcard` ou outro componente específico.

### 4.4 Relação com numeração

A variante determina se há numeração.

- Processo e exercícios: geralmente numerados.
- Comparação, anatomia, referência e diagnóstico: geralmente não numerados.
- Síntese: numerada apenas quando for uma coleção fechada de ideias essenciais.

### 4.5 Regra técnica

Não ajustar `.steps` com `gap`, `margin-top`, `font-size` ou `border` inline em cada slide. Esses valores devem ficar nas classes de variante.

Correto:

```html
<ul class="steps list-process">
  <li><span class="n">01</span><span class="t">Separar treino e teste.</span></li>
</ul>
```

Incorreto:

```html
<ul class="steps" style="gap:18px; margin-top:30px">
  <li>...</li>
</ul>
```

A Rodada 4 foi validada na Aula 02 e deve orientar o uso de listas estruturadas nas demais aulas depois da consolidação completa do padrão.


---

## Rodada 5 — Padronização de slides de comparação

A Aula 02 possui comparações com funções didáticas diferentes. A regra consolidada é separar **comparações binárias** de **comparações de estados** e manter uma gramática visual consistente dentro de cada família.

### 5.1 Comparação binária

Usar para dois conceitos ou abordagens colocados lado a lado, como:

- Batch × Online;
- Instance-based × Model-based.

Os dois lados devem ter **estrutura paralela**.

Regras obrigatórias:

- dois painéis com mesma largura e mesma altura visual;
- mesmo `padding`, mesmo `gap` e mesma hierarquia tipográfica;
- mesma quantidade de níveis de informação em ambos os lados;
- sem numeração interna, pois não há sequência;
- não usar bullets em apenas um dos lados;
- não usar fundo verde em apenas um dos lados;
- não criar um painel visualmente “mais importante” sem justificativa didática;
- o verde deve aparecer apenas como acento: rótulo, barra, palavra-chave ou marcador discreto;
- títulos, resumo e informações devem ocupar posições equivalentes nos dois lados.

Estrutura recomendada:

```html
<div class="compare-grid compare-binary">
  <article class="compare-card">
    <div class="compare-k">Batch</div>
    <h3>Treina com todos os dados disponíveis</h3>
    <p class="compare-desc">Resumo curto do conceito.</p>
    <div class="compare-info">
      <div><span class="label">Como funciona</span><p>...</p></div>
      <div><span class="label">Quando usar</span><p>...</p></div>
      <div><span class="label">Exemplo</span><p>...</p></div>
    </div>
  </article>

  <article class="compare-card">
    <div class="compare-k">Online</div>
    <h3>Atualiza o modelo continuamente</h3>
    <p class="compare-desc">Resumo curto do conceito.</p>
    <div class="compare-info">
      <div><span class="label">Como funciona</span><p>...</p></div>
      <div><span class="label">Quando usar</span><p>...</p></div>
      <div><span class="label">Exemplo</span><p>...</p></div>
    </div>
  </article>
</div>
```

A quantidade exata de campos internos pode variar conforme o conteúdo, mas os dois lados devem usar **os mesmos campos e a mesma ordem**.

### 5.2 Bullets em comparações

Não misturar formatos dentro da mesma comparação.

Se a comparação usar bullets:

- ambos os lados usam bullets;
- mesmos recuos, marcadores e espaçamento;
- quantidade semelhante de itens.

Preferência do padrão da Aula 02: em comparações conceituais, usar **mini-blocos com rótulos curtos** em vez de bullets tradicionais quando isso melhorar a leitura.

### 5.3 Fundo e destaque

Em comparação binária, os dois lados devem partir do mesmo fundo neutro.

Evitar:

```html
<div class="compare-card" style="background:var(--accent-soft)">...</div>
<div class="compare-card">...</div>
```

Preferir:

```html
<div class="compare-card">...</div>
<div class="compare-card">...</div>
```

Quando houver necessidade real de destacar uma diferença, usar uma classe semântica discreta, sem alterar toda a gramática do card.

### 5.4 Comparação de estados

Usar quando os elementos representam estados de um mesmo fenômeno, como:

- Underfitting;
- Bom ajuste;
- Overfitting.

Nesse caso, usar três painéis equivalentes e tratar o estado desejado como alvo.

Regras:

- três cards com mesma estrutura, largura proporcional e altura visual;
- sem numeração interna;
- o estado central/alvo pode receber destaque sutil com classe semântica como `.is-target`;
- o destaque não deve mudar a estrutura interna nem aumentar muito o peso visual;
- verde pode marcar o estado desejado, mantendo os demais em fundo neutro;
- títulos e descrições devem permanecer paralelos.

Exemplo:

```html
<div class="compare-grid compare-states">
  <article class="state-card">...</article>
  <article class="state-card is-target">...</article>
  <article class="state-card">...</article>
</div>
```

### 5.5 Espaçamento

Comparações devem usar tokens/classes de layout, não ajustes manuais por slide.

Padronizar:

- distância entre título e comparação;
- gap entre painéis;
- padding interno;
- distância entre rótulo, título, descrição e informações;
- alinhamento do conteúdo no topo.

Evitar diferenças como `gap:32px` em um slide e `gap:48px` em outro da mesma família sem motivo funcional.

### 5.6 Regra semântica

A escolha do componente depende da pergunta didática:

- **“Qual a diferença entre A e B?”** → comparação binária;
- **“Como reconhecer três estados de um mesmo fenômeno?”** → comparação de estados;
- **“Quais são quatro ideias independentes?”** → cards conceituais, não comparação;
- **“Qual é a sequência?”** → `.steps list-process`, não comparação.

### 5.7 Slides validados na Aula 02

A regra foi validada nos seguintes casos:

- Slide 14 — Batch × Online: comparação binária;
- Slide 15 — Instance-based × Model-based: comparação binária;
- Slide 20 — Underfitting × Bom ajuste × Overfitting: comparação de estados.

Os slides 14 e 15 devem manter **a mesma gramática visual**, incluindo estrutura interna, ausência/presença de bullets, espaçamento e tratamento de fundo.

A Rodada 5 foi validada na Aula 02 e deve orientar slides de comparação nas demais aulas depois da consolidação completa do padrão.


---

## Rodada 6 — Slides com imagem

A Aula 02 define duas funções visuais para imagens:

### 1. Imagem de apoio
Usar quando a imagem reforça a explicação, mas não substitui o conteúdo textual.

Regras:
- imagem integrada à área principal do slide;
- proporção e altura padronizadas por classe;
- raio e acabamento iguais aos demais elementos visuais da aula;
- não usar `width`, `height`, `border-radius` ou `margin` inline no `image-slot`;
- a imagem não deve competir com o título.

### 2. Imagem lateral com cards
Usar quando a imagem oferece contexto visual e os cards carregam a explicação.

Regras:
- imagem à esquerda;
- cards à direita em grade compacta;
- a linguagem dos cards deve permanecer a mesma dos cards conceituais numerados;
- a presença da imagem não autoriza mudar numeração, hierarquia ou espaçamento dos cards;
- a imagem deve ter altura e raio definidos por classe.

### Convenção
Slides com imagem devem usar variantes de layout explícitas, como `layout-image-support` ou `layout-image-cards`, evitando ajustes individuais em cada slide.


## Rodada 7 — Estilos inline e centralização do CSS

A Aula 02 deve evitar estilos inline no markup dos slides. O objetivo é impedir que
cada slide crie seus próprios valores de margem, gap, largura, tamanho ou cor e,
assim, preservar a consistência quando o padrão for replicado em outras aulas.

### Regra geral

- Não usar `style="..."` em elementos de conteúdo dos slides para resolver layout,
  espaçamento, tipografia, cor ou dimensão recorrente.
- Transformar padrões repetidos em classes CSS reutilizáveis e semânticas.
- Valores de espaçamento recorrentes devem vir de tokens em `:root` ou de classes de
  layout já definidas.
- Exceções só são aceitáveis quando o valor é intrínseco a um elemento técnico
  gerado dinamicamente (por exemplo, internals de um Web Component), nunca como
  solução artesanal para um slide específico.

### Famílias de classes consolidadas

Priorizar classes como:

- `.layout-image-cards` para imagem + cards;
- `.layout-comparison` para comparação binária;
- `.layout-state-trio` para comparação de estados;
- `.layout-two-col-balanced` para duas colunas equilibradas;
- `.concept-grid` e suas variantes para cards conceituais;
- classes de largura e ritmo já existentes (`.w-*`, `.flow-title`,
  `.lead-under-title`, etc.) em vez de `max-width` ou `margin-top` inline.

### Regra para manutenção

Ao perceber dois ou mais slides repetindo a mesma combinação de propriedades CSS,
criar ou reutilizar uma classe. Não copiar valores inline de um slide para outro.
A Aula 02 deve ser tratada como sistema de componentes, não como coleção de slides
ajustados individualmente.


---

## Rodada 8 — Ritmo vertical e espaçamento entre blocos

A Aula 02 deve usar ritmo vertical padronizado apenas em slides cuja composição segue uma estrutura simples.
A regra não deve ser aplicada globalmente a slides com diagrama, imagem, código, comparação complexa ou composição própria.

### Sequência padrão

Quando o slide segue estrutura simples, usar a sequência:

```text
kicker → título → lead opcional → conteúdo principal → fechamento opcional
```

Regras:

- o espaçamento entre título e lead deve ser consistente;
- o espaçamento entre lead e conteúdo deve ser consistente;
- cards conceituais em grade devem começar na mesma altura visual entre slides da mesma família;
- fechamentos no rodapé devem respeitar o respiro inferior já definido;
- não resolver ritmo vertical com `margin-top` inline.

### Onde aplicar

Aplicar o ritmo padrão em slides simples, especialmente:

- slides de cards conceituais;
- slides de síntese;
- slides cujo conteúdo principal é uma única família visual.

Na Aula 02, a regra foi validada principalmente nos slides 07, 11, 19, 23 e 25.

### Onde não aplicar automaticamente

Não aplicar a regra global em slides com composição específica, como:

- diagramas;
- imagens estruturais;
- código;
- comparações com layout próprio;
- slides finais com blocos de função diferente;
- qualquer slide em que a composição dependa de posicionamento interno entre elementos.

O slide 12 foi o caso de validação desta regra: ele possui lead, diagrama e bloco de intuição.
Ele deve preservar sua composição própria por classes específicas, sem voltar a `style="..."` inline.

### Regra de manutenção

Antes de aplicar uma classe de ritmo, identificar a família didática do slide.
Ritmo vertical é uma convenção de família, não uma regra global cega.
Se a classe quebrar uma composição especial, criar uma variante semântica para aquela família.


---

## Rodada 9 — Títulos e leads

A Aula 02 define um padrão único para a relação entre `kicker`, `h1.title`, `.lead` e conteúdo principal.

### Regras

- Todo slide de conteúdo começa com `.kicker` e `h1.title`.
- Usar `.lead` somente quando o título precisa de uma frase de contexto para orientar a leitura do conteúdo principal.
- Não usar `.lead` quando houver uma `.note` imediatamente abaixo do título com função de definição, regra ou enunciado.
- O `.lead` padrão deve usar `max-width:68ch`, `font-size:var(--type-lead)` e ritmo visual consistente.
- Não criar larguras individuais de lead em cada slide, exceto em composições especiais já previstas por classe de layout.
- A largura de `68ch` evita leads estreitos demais, reduz quebras excessivas e mantém a frase de apoio visualmente alinhada ao peso do título.
- A sequência visual preferencial é: `.kicker` → `h1.title` → `.lead` opcional → conteúdo principal.

### Quando usar lead

Use `.lead` quando:

- o título é conceitual ou metafórico;
- a leitura dos cards depende de uma frase de enquadramento;
- o slide abre uma família de exemplos, problemas ou aplicações;
- o aluno precisa entender por que aqueles elementos aparecem juntos.

Evite `.lead` quando:

- o título já é autoexplicativo;
- o slide contém uma `.note` de definição logo abaixo;
- o conteúdo principal é um diagrama que já explica a relação;
- o slide é divisor, capa, referência ou exercício.


---

## Rodada 10 — Fechamentos de slide

A Aula 02 consolidou três formas oficiais de encerrar um slide:

1. **Sem fechamento**: usar quando o conteúdo principal já conclui a ideia e não há síntese adicional necessária.
2. **`.note.mute` no rodapé**: usar para síntese ou fechamento discreto. Deve aparecer no fim da `.frame`, sem `.note-k`, com texto em tom secundário e destaque pontual em `<span class="strong">`.
3. **`.idea` no rodapé ou dentro de composição**: usar apenas para intuição-chave ou alerta. A lâmpada indica intuição; o triângulo indica erro a evitar. Não usar `.idea` como definição, tarefa ou nota genérica.

Regras:
- Não criar fechamentos soltos com estilos locais.
- Não usar `.note` verde para síntese final comum; verde interrompe o fluxo, cinza fecha.
- O fechamento deve ter função didática clara: sintetizar, alertar ou reforçar uma intuição.
- Quando o bloco de fechamento for o último elemento da `.frame`, usar a ancoragem padrão no rodapé, sem `margin-top` inline.


---

## Rodada 11 — Slides finais

Os slides finais da Aula 02 foram padronizados como uma sequência didática de encerramento, com funções distintas e ordem fixa.

### Ordem final

A sequência aprovada para o encerramento da aula é:

- **24 — Para assistir e debater**
- **25 — Síntese**
- **26 — Exercícios propostos**
- **27 — Referências**

A ordem **exercícios antes de referências** foi adotada por funcionar melhor pedagogicamente: primeiro o aluno sintetiza, depois pratica, e por fim consulta as fontes.

### Regras por slide

#### Slide 24 — Para assistir e debater
- Manter os **cards de vídeo** como componente próprio.
- Não descaracterizar a composição dos vídeos ao padronizar os slides finais.
- As perguntas de discussão aparecem como bloco complementar, sem competir visualmente com os vídeos.

#### Slide 25 — Síntese
- Encerrar o conteúdo com poucas ideias essenciais.
- O slide deve funcionar como fechamento didático, e não introduzir conteúdo novo.

#### Slide 26 — Exercícios propostos
- Usar componente de atividade/exercício.
- Os exercícios devem vir antes das referências.
- A numeração aqui é funcional, pois identifica itens de prática.

#### Slide 27 — Referências
- Aparência bibliográfica, sem parecer processo ou lista de tarefas.
- Deve funcionar como fechamento técnico/institucional do material.

### Regra geral

Nos slides finais, a padronização deve respeitar a **função didática específica** de cada slide.
Não forçar um único componente em todos eles. Padronizar o sistema, não apagar a identidade de cada função.


---

## Rodada 12 — Dividers de seção

Os dividers da Aula 02 foram consolidados como uma única família visual para marcar transições entre grandes blocos da aula.

### Slides de referência

- **08 — Os paradigmas de aprendizado**
- **16 — O fluxo de trabalho**

### Regras

- Usar a mesma estrutura de `.divider` nos divisores de seção.
- A numeração do slide permanece no canto superior direito, com dois dígitos, sem runhead textual à esquerda.
- O rótulo da parte (`.d-num`) aparece acima do título e identifica o macrobloco da aula.
- O título do divider usa a mesma escala, largura máxima e alinhamento em todos os divisores.
- O subtítulo (`.d-sub`) usa a mesma largura máxima e o mesmo espaçamento em relação ao título.
- A barra de acento no rodapé do divider deve manter a mesma espessura e posição.
- Não criar variantes visuais diferentes para cada transição de seção sem necessidade didática real.
- O divider deve funcionar como pausa visual clara entre partes da aula, mantendo a identidade da Aula 02.

### Regra de consistência

Ao criar novos dividers, copiar a estrutura semântica e as classes já consolidadas na Aula 02, alterando apenas:

- número do slide;
- identificação da parte;
- título;
- subtítulo.

Não alterar espaçamentos, escala tipográfica, posição da numeração ou barra de acento para “encaixar” conteúdo específico.

---

## Status do padrão

A **Aula 02 — Fundamentos do Aprendizado de Máquina** é a referência-base para a padronização visual, estrutural e técnica das demais aulas de CMPINAM.

As regras deste documento devem ser tratadas como fonte principal de decisão de design. Ao adaptar outras aulas, preservar a função didática do conteúdo e escolher componentes e famílias de layout conforme as regras consolidadas aqui, em vez de reproduzir soluções visuais ad hoc.
