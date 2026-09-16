# CMPINAM — Introdução ao Aprendizado de Máquina

Materiais, atividades e recursos da disciplina de Introdução ao Aprendizado de Máquina do IFSP — Câmpus Campinas.

## Estrutura do repositório

- [`aulas/`](aulas/): apresentações, notebooks, exemplos e recursos das aulas.
- [`projeto/`](projeto/): orientações do projeto da disciplina e datasets disponibilizados.
- [`planejamento/`](planejamento/): ementa e planos de aula.
- [`assets/`](assets/): identidade visual e guia de padronização.
- [`referencias/`](referencias/): links e referências complementares.

Entregas de estudantes, notas, avaliações e referências de uso exclusivamente local não são versionadas.

## Conteúdo das aulas

1. Apresentação da disciplina
2. Ambiente de desenvolvimento em Python
3. Introdução ao aprendizado de máquina
4. Análise exploratória de dados
5. Regressão linear
6. Regressão polinomial e regularização
7. Classificação, regressão logística e métricas
8. Árvores de decisão
9. Validação cruzada e otimização de hiperparâmetros
10. K-vizinhos mais próximos (KNN)
11. Random Forest
12. Redes neurais

Consulte o [índice detalhado das aulas](aulas/README.md).

## Preparação do ambiente

Com Python instalado, crie um ambiente virtual na raiz do repositório:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

Algumas aulas possuem um `requirements.txt` próprio quando exigem dependências ou versões específicas.

## Projeto da disciplina

As orientações, o material de apoio e os datasets do projeto estão disponíveis em [`projeto/`](projeto/).
