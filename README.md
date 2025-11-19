# Documentação dos Notebooks — Projeto: House Prices (Kaggle)

Este documento descreve apenas os notebooks presentes na pasta `notebooks/` deste repositório, explicando objetivo, passos principais, entradas/saídas, dependências e como executá-los localmente. O conteúdo serve como guia rápido para entender o que cada notebook faz e como reproduzir os resultados.

**Escopo:** explicação exclusiva dos notebooks (não cobre scripts, dados brutos ou arquivos auxiliares).

## Sumário
- `1.0_compreendendo_os_objetivos.ipynb`
- `1.1_compreendendo_os_dados.ipynb`
- `1.2_preparação_dos_dados.ipynb`
- `1.3_modelagem_lightGBM.ipynb`
- `agr_vai_ LightGBM.ipynb`
- `agr_vai_FR0.89.ipynb`
- `agr_vai_FRLog.ipynb`

---

**Como usar esta documentação**: abra o notebook correspondente em `notebooks/` e execute as células em ordem; siga as instruções de ambiente na seção "Dependências" abaixo.

---

## `1.0_compreendendo_os_objetivos.ipynb`
- **Objetivo:** apresentar o desafio (Kaggle House Prices — Advanced Regression Techniques), objetivos do projeto e métricas de avaliação (RMSE / RMSLE, dependendo do pré-processamento). Fornece visão geral do que se espera como entregável.
- **Resumo dos passos:**
  - Introdução ao problema e métrica do concurso.
  - Descrição do conjunto de dados fornecido pelo Kaggle.
  - Metas de modelagem e critérios para submissão.
- **Entradas:** nenhum arquivo de dados processado — conteúdo explicativo do desafio; referências a `data/train.csv` e `data/test.csv`.
- **Saídas:** decisões de escopo e notas de abordagem.
- **Como executar:** abrir e ler; é um notebook conceitual.

## `1.1_compreendendo_os_dados.ipynb`
- **Objetivo:** exploração inicial dos dados (EDA) para identificar características, distribuições, valores ausentes e relações com a variável alvo (`SalePrice`).
- **Resumo dos passos:**
  - Leitura de `data/train.csv` e `data/test.csv`.
  - Visualizações: histogramas, boxplots, scatterplots e heatmaps de correlação.
  - Análise de valores ausentes por coluna e por amostra.
  - Identificação de features categóricas e numéricas.
- **Entradas:** `data/train.csv`, `data/test.csv`.
- **Saídas:** insights para pré-processamento (lista de colunas problemáticas, colunas para transformação, primeiras ideias de engenharia de features).
- **Células-chave:** seção de análise de valores ausentes e correlação com `SalePrice` — útil para priorizar transformações.
- **Como executar:** executar todas as células de EDA; recomenda-se usar um kernel com plotagem (colab ou Jupyter local).

## `1.2_preparação_dos_dados.ipynb`
- **Objetivo:** limpeza e engenharia de features para transformar os dados brutos em conjuntos prontos para modelagem.
- **Resumo dos passos:**
  - Tratamento de valores ausentes (imputação por média/mediana/modo ou regras específicas por coluna).
  - Conversão de variáveis categóricas (one-hot encoding, label encoding ou ordinal encoding conforme necessário).
  - Transformações numéricas (log da variável alvo se necessário, escalonamento quando aplicável).
  - Criação de features derivadas (somas, relações entre colunas, agrupamentos).
  - Separação em conjuntos de treino/validação e geração de arquivos limpos (`df_clear.csv`, `df_clear_test.csv`) quando presente.
- **Entradas:** `data/train.csv`, `data/test.csv`.
- **Saídas:** datasets processados — verifica se os arquivos `notebooks/df_clear.csv` e `notebooks/df_clear_test.csv` são criados/atualizados.
- **Como executar:** executar células na ordem; se for necessário recriar os CSVs, confirme o caminho de saída antes de rodar.

## `1.3_modelagem_lightGBM.ipynb`
- **Objetivo:** treinar um modelo LightGBM (ou pipeline com LightGBM) usando os dados processados, validar performance e gerar submissão no formato requerido pelo Kaggle.
- **Resumo dos passos:**
  - Leitura dos dados processados (`df_clear.csv` / `df_clear_test.csv` ou preprocessamento inline).
  - Definição de features e target (`SalePrice` ou sua transformação log).
  - Split treino/validação ou cross-validation (K-Fold/Stratified se aplicável).
  - Treinamento do modelo LightGBM, ajuste de hiperparâmetros e avaliação (RMSE / RMSLE).
  - Geração de predições no conjunto de teste e escrita do arquivo de submissão `sample_submission.csv` atualizado.
- **Entradas:** arquivos processados gerados no passo anterior.
- **Saídas:** modelo (se serializado), métricas de validação e arquivo de submissão pronto.
- **Como executar:** certifique-se de ter `lightgbm` instalado; execute células de treinamento e exporte o CSV de submissão.

## `agr_vai_ LightGBM.ipynb`, `agr_vai_FR0.89.ipynb`, `agr_vai_FRLog.ipynb`
- **Objetivo (conjunto):** notebooks experimentais/iterativos com variações em modelagem e tentativa de melhorar score. Geralmente representam tentativas com:
  - diferentes pipelines de transformação;
  - transformação da variável alvo (por exemplo, log) — indicado pelo sufixo `FRLog`;
  - ajustes de features ou tratamento específico para alcançar uma fractional score (ex.: `FR0.89` sugere experimento visando 0.89 em alguma métrica).
- **Resumo dos passos:**
  - Reaproveitam preparação e variam hiperparâmetros ou transformações.
  - Comparam resultados e salvam versões de submissão.
- **Entradas/Saídas:** mesmas do notebook de modelagem; múltiplos arquivos de submissão podem ser gerados.
- **Como executar:** são notebooks de experimento: rodar somente após entender `1.2` e `1.3`; revise comentários e célular de resumo de resultados.

## Notas sobre os arquivos `df_clear.csv` e `df_clear_test.csv`
- Esses arquivos (quando presentes em `notebooks/`) são versões intermediárias/dumped dos datasets após a etapa de limpeza/engenharia e são usados pelos notebooks de modelagem para acelerar iterações.

## Dependências recomendadas
- **Python 3.8+**: ambiente com as bibliotecas abaixo.
- **Dependências comuns:**
  - `pandas`, `numpy` — manipulação de dados
  - `matplotlib`, `seaborn` — visualização
  - `scikit-learn` — pré-processamento, métricas, validação
  - `lightgbm` — modelo principal em `1.3`
  - opcional: `xgboost`, `catboost` se houver experimentos

Instalar dependências (exemplo):
```
pip install pandas numpy matplotlib seaborn scikit-learn lightgbm
```

## Como executar os notebooks localmente
- Abra o diretório raiz do projeto com Jupyter / VS Code Notebook.
- Ative seu ambiente Python (virtualenv/conda) e instale dependências.
- Carregue cada notebook pela ordem sugerida:
  1. `1.0_compreendendo_os_objetivos.ipynb`
  2. `1.1_compreendendo_os_dados.ipynb`
  3. `1.2_preparação_dos_dados.ipynb`
  4. `1.3_modelagem_lightGBM.ipynb`
  5. Notebooks experimentais (`agr_vai_ ...`)

## Boas práticas e recomendações
- Execute os notebooks em ordem para manter dependências (EDA → preparação → modelagem).
- Verifique caminhos de leitura/gravação de CSV antes de executar (algumas células podem sobrescrever arquivos em `notebooks/`).
- Se for reproduzir submissões, confirme se o `sample_submission.csv` do `data/` está sendo usado como template.
- Documente alterações experimentais nos notebooks experimentais para rastreabilidade.

## Próximos passos sugeridos (opcional)
- Adicionar um `requirements.txt` ou `environment.yml` com versões exatas.
- Converter células críticas em scripts reprodutíveis (`src/`) para CI/execução programática.
- Incluir instruções de como gerar os `df_clear*.csv` passo a passo no README principal.

---

Se quiser, eu posso:
- criar um `requirements.txt` com as dependências detectadas;
- adicionar um README mais completo que inclua também o fluxo de dados;
- ou gerar uma versão em inglês do documento.

Arquivo criado: `NOTEBOOKS_DOCUMENTATION.md` (na raiz do repositório).
