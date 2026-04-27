# Projeto Academy - Previsão de Preços Airbnb Rio de Janeiro

## 📋 Descrição

Projeto acadêmico desenvolvido pela **Equipe 1** com objetivo de construir e treinar modelos de **Machine Learning para previsão de preços** de acomodações no Airbnb da cidade do Rio de Janeiro. O projeto integra dados de preços com indicadores econômicos (IPCA) para criar uma base consolidada e realizar análises preditivas.

**Objetivo Principal:** Prever o preço de aluguel de imóveis no Airbnb baseado em características do imóvel e índices econômicos.

---

## 📊 Dados e Contexto

- **Fonte de Dados:** Base interna do Airbnb Rio de Janeiro + IPCA (Índice Nacional de Preços ao Consumidor Amplo)
- **Período:** Setembro de 2025
- **Localização:** Rio de Janeiro, RJ
- **Tipo de Análise:** Regressão (Previsão de valores contínuos)

### Características dos Dados

O dataset contém informações sobre:
- **Preço** de aluguel
- **Capacidade** (número de hóspedes)
- **Estrutura** (quartos, camas, banheiros)
- **Tipo de quarto** (entire home/apt, hotel room, private room, shared room)
- **Tipo de propriedade** (residencial, comercial, etc.)
- **Localização** (bairro, latitude, longitude)
- **Avaliações** (nota de avaliação, número de reviews)
- **Restrições** (noites mínimas)
- **Índices Econômicos** (IPCA mensal e acumulado)

---

## 🏗️ Estrutura do Projeto

```
projeto-academy/
│
├── README.md                          # Este arquivo
├── main.py                            # Script principal que executa todo o pipeline
├── base_tratada.db                    # Banco de dados SQLite com dados processados
│
├── bases/                             # Dados brutos
│   ├── base_interna.csv               # Dados do Airbnb
│   └── base_ipca.csv                  # Dados do IPCA
│
├── scripts/                           # Scripts de processamento
│   ├── ETL.py                         # Extração, transformação de dados internos
│   ├── tratamento_base_externa.py     # Processamento dados IPCA
│   └── integracao.py                  # Integração de bases e carga em DB
│
├── modelos/                           # Notebooks com modelos de ML
│   ├── regressao-linear-modelo.ipynb           # Regressão Linear
│   ├── randon-forest.ipynb                     # Random Forest
│   └── extra-trees.ipynb                       # Extra Trees
│
└── análises/                          # Notebooks exploratórios
    ├── eda.ipynb                      # Análise Exploratória de Dados
    └── metricasModelos.ipynb          # Comparação de métricas dos modelos
```

---

## 🔧 Dependências

O projeto utiliza as seguintes bibliotecas Python:

```

pandas              # Manipulação e análise de dados
numpy               # Metricas dos algoritmos de Machine Learning
scikit-learn        # Algoritmos de Machine Learning
matplotlib          # Visualização de dados
seaborn             # Visualizações estatísticas avançadas
sqlite3             # Banco de dados (nativo do Python)
```

---

## 📦 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone ou acesse o repositório:**
```bash
cd projeto-academy
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

## 🚀 Como Executar

### Executar todo o pipeline (ETL + Integração)

```bash
python main.py
```

Este comando executará em sequência:
1. `ETL.py` - Extração e transformação dos dados do Airbnb
2. `tratamento_base_externa.py` - Processamento dos dados do IPCA
3. `integracao.py` - Integração das bases e carga no SQLite

### Executar scripts individuais

```bash
python scripts/ETL.py
python scripts/tratamento_base_externa.py
python scripts/integracao.py
```

### Explorar os dados e modelos

- Abra os notebooks em Jupyter Notebook ou VS Code:
```bash
jupyter notebook
```

Acesse:
- `eda.ipynb` - Para exploração dos dados
- `modelos/regressao-linear-modelo.ipynb` - Modelo linear
- `modelos/randon-forest.ipynb` - Modelo Random Forest
- `modelos/extra-trees.ipynb` - Modelo Extra Trees
- `metricasModelos.ipynb` - Comparação de desempenho

---

## 📈 Pipeline de Processamento (ETL)

### 1️⃣ Extração (E)
- **Fonte:** Arquivos CSV (base_interna.csv, base_ipca.csv)
- Leitura e carregamento em DataFrames

### 2️⃣ Transformação (T)

#### Dados Airbnb:
- Seleção de colunas relevantes
- Renomeação para português
- **Label Encoding** de variáveis categóricas:
  - Bairros (1-81+)
  - Tipos de propriedade (1-4)
  - Tipos de quarto (1-4)
- Tratamento de valores nulos
- Criação de features (ano, mês)

#### Dados IPCA:
- Extração de dados referentes a 2025
- Conversão de porcentagens para valores numéricos
- Limpeza de dados

### 3️⃣ Carga (L)
- Integração das bases por (ano, mês)
- Exportação para SQLite: `base_tratada.db`
- Tabela: `base_tratada`

---

## 🤖 Modelos de Machine Learning

O projeto implementa e compara **3 modelos de regressão**:

### 1. **Regressão Linear**
- Arquivo: `modelos/regressao-linear-modelo.ipynb`
- Características:
  - Modelo baseline simples e interpretável
  - Assume relação linear entre features e target
  - Inclui normalização de features
  - Tratamento de valores nulos

### 2. **Random Forest**
- Arquivo: `modelos/randon-forest.ipynb`
- Características:
  - Ensemble de árvores de decisão
  - Captura relações não-lineares
  - Reduz overfitting através de agregação
  - Modelo com transformação logarítmica do target

### 3. **Extra Trees (Extremely Randomized Trees)**
- Arquivo: `modelos/extra-trees.ipynb`
- Características:
  - Variação mais rápida do Random Forest
  - Thresholds aleatórios nas features
  - Menos tendência ao overfitting
  - Análise de importância de features

### Métricas de Avaliação
Todos os modelos são avaliados com:
- **R² (Coeficiente de Determinação)** - Proporção da variância explicada
- **RMSE (Root Mean Squared Error)** - Erro quadrático médio
- **MAE (Mean Absolute Error)** - Erro absoluto médio

---

## 🎯 Análise Exploratória de Dados (EDA)

### Arquivo: `eda.ipynb`

Inclui:
- Estatísticas descritivas
- Distribuições de preços
- Correlações entre variáveis
- Análise por bairro
- Análise por tipo de propriedade
- Visualizações de padrões geográficos

---

## 📊 Codificação das Variáveis Categóricas

### Tipos de Propriedade (Label Encoded)
```
1 → Espaço Inteiro Residencial
2 → Hospedagem Comercial
3 → Outros
4 → Quarto Privativo Residencial
```

### Tipos de Quarto (Label Encoded)
```
1 → Entire home/apt
2 → Hotel room
3 → Private room
4 → Shared room
```

### Bairros (Label Encoded)
```
1 → Abolição
2 → Alto da Boa Vista
3 → Anchieta
... (total de 81+ bairros do Rio de Janeiro)
27 → Cidade Nova
```

---

## 📁 Banco de Dados

### SQLite - `base_tratada.db`

**Tabela:** `base_tratada`

Colunas principais:
- `preco` - Preço da acomodação (target)
- `hospedes` - Capacidade de hóspedes
- `quartos`, `camas`, `banheiros` - Estrutura
- `tipo_de_quarto` - Codificado (1-4)
- `tipo_propriedade` - Codificado (1-4)
- `nota_avaliacao` - Rating do Airbnb
- `bairro` - Codificado numericamente
- `latitude`, `longitude` - Coordenadas
- `noites_minimas` - Mínimo de noites
- `numero_reviews` - Quantidade de avaliações
- `ano`, `mes` - Período (2025-09)
- `ipca_mensal` - IPCA do mês
- `ipca_acumulado_ano` - IPCA acumulado no ano

---

## 💡 Fluxo de Uso

1. **Preparação:**
   - Colocar `base_interna.csv` em `bases/`
   - Colocar `base_ipca.csv` em `bases/`

2. **Processamento:**
   - Executar `python main.py`
   - Gera `base_tratada.db`

3. **Exploração:**
   - Abrir `eda.ipynb` para análise inicial

4. **Modelagem:**
   - Executar os notebooks dos modelos em `modelos/`
   - Comparar resultados em `metricasModelos.ipynb`

5. **Resultados:**
   - Consultar banco de dados: `base_tratada.db`
   - Analisar métricas e previsões

---

## 📝 Observações Importantes

- Os dados são referentes a **setembro de 2025**
- O IPCA utilizado é específico do período 2025-09
- Label Encoding foi escolhido para variáveis categóricas
- Transformação logarítmica é aplicada em alguns modelos para melhor captura de padrões
- Recomenda-se utilizar um ambiente virtual para isolamento de dependências

---

## 👥 Grupo Responsável

**Equipe 1** - Projeto Academy

---

## 📄 Licença

Projeto acadêmico para fins educacionais.

---

## 📧 Contato

Para dúvidas sobre o projeto, consulte os membros da Equipe.
Adriana Melo - AdrianaQMelo
Ana Amorim - anacamorims (Repository Owner)
Bianka Sales - biankadesouza
Daniela Carvalho - Daniella1806
Isabella Braga - Isabella-Braga