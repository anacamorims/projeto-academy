import pandas as pd
import sqlite3


# 1 EXTRAÇÃO
df_base_interna = pd.read_csv('base_interna.csv')


# 3. TRANSFORMAÇÃO
colunas_tratamento = ["price","accommodates","bedrooms", "beds", "bathrooms_text", 
"room_type", "review_scores_rating","minimum_nights", "number_of_reviews", "property_type", 
"latitude", "longitude"]
df_base_interna = df_base_interna[colunas_tratamento]


# TRATAMENTO DA COLUNA 'price'
# RENOMEAR COLUNA 'price' PARA 'preco'
df_base_interna.rename(
    columns={'price': 'preco'},
    inplace=True
)
df_base_interna ['preco'] = df_base_interna ['preco'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)

# TRATAMENTO DA COLUNA 'preco' PARA float
df_base_interna ['preco'] = df_base_interna ['preco'].astype(float)

# DIAGNÓSTICO
print(df_base_interna['preco'].head())
print(df_base_interna['preco'].dtype)
print(df_base_interna['preco'].info())
print(df_base_interna['preco'].describe())
print("TOTAL DE VALORES NULOS:", df_base_interna['preco'].isnull().sum())


# TRATAMENTO DA COLUNA 'accommodates'
# RENOMEAR COLUNA 'accommodates' PARA 'hospedes'
df_base_interna.rename(
    columns={'accommodates': 'hospedes'},
    inplace=True
)

# VER MÍNIMO E MÁXIMO 
df_base_interna['hospedes'].min(), df_base_interna['hospedes'].max()

# DIAGNÓSTICO
print(df_base_interna['hospedes'].head())
print(df_base_interna['hospedes'].dtype)
print("QUANTIDADE DE VALORES NULOS:", df_base_interna['hospedes'].isnull().sum())
print(
    "QUANTIDADE MÍNIMA DE HÓSPEDES:",
    df_base_interna['hospedes'].min(),
    "QUANTIDADE MÁXIMA DE HÓSPEDES:",
    df_base_interna['hospedes'].max()
)


#TRATAMENTO DA COLUNA 'bathrooms_text'
# CRIAR COLUNA 'banheiros' A PARTIR DA COLUNA 'bathrooms_text'
df_base_interna['banheiros'] = (
    df_base_interna['bathrooms_text']
    .str.extract(r'(\d+\.?\d*)')
    .astype(float)
)

# VER MÍNIMO E MÁXIMO (DIAGNÓSTICO)
print(
"min de banheiros:",
    df_base_interna['banheiros'].min(),
    "max de banheiros:",
    df_base_interna['banheiros'].max()
)

# CORREÇÃO DOS VALORES INVÁLIDOS
df_base_interna.loc[
    (df_base_interna['banheiros'] <= 0) |
    (df_base_interna['banheiros'] > 6),
    'banheiros'
] = None

 #TRATAMENTO DE VALORES NULOS - SUBSTITUIR POR MEDIANA
df_base_interna['banheiros'] = (
    df_base_interna['banheiros']
    .fillna(df_base_interna['banheiros'].median())
)

 #CONFERIR O RESULTADO
print(
    df_base_interna[['bathrooms_text', 'banheiros']].head()
)
print(df_base_interna['banheiros'].dtype)
print(df_base_interna['banheiros'].info())
print(df_base_interna['banheiros'].describe())
print("VALORES NULOS:", df_base_interna['banheiros'].isnull().sum())
print(
    "DEPOIS DO TRATAMENTO -> Min banheiros:",
    df_base_interna['banheiros'].min(),
    "Max banheiros:",
    df_base_interna['banheiros'].max()
)


# TRATAMENTO DA CULUNA 'bedrooms'
# RENOMEAR COLUNA 'bedrooms' PARA 'quartos'
df_base_interna.rename(
    columns={'bedrooms': 'quartos'},
    inplace=True
)

# VER MÍNIMO E MÁXIMO (DIAGNÓSTICO)
print(
    "min de quartos:",
    df_base_interna['quartos'].min(),
    "max de quartos:",
    df_base_interna['quartos'].max()
)

# CORREÇÃO DOS VALORES INVÁLIDOS
df_base_interna.loc[
    (df_base_interna['quartos'] <= 0) |
    (df_base_interna['quartos'] > 6),
    'quartos'
] = None

# TRATAMENTO DE VALORES NULOS - SUBSTITUIR POR MEDIANA
df_base_interna['quartos'] = (
    df_base_interna['quartos']
    .fillna(df_base_interna['quartos'].median())
)

# CONFERIR O RESULTADO
print(df_base_interna[['quartos']].head())
print(df_base_interna['quartos'].dtype)
print(df_base_interna['quartos'].info())
print(df_base_interna['quartos'].describe())
print("QUANTIDADE DE VALORES NULOS:", df_base_interna['quartos'].isnull().sum())
print("min de quartos:",df_base_interna['quartos'].min(),"max de quartos:",df_base_interna['quartos'].max())

# TRATAMENTO DA COLUNA 'beds'
# RENOMEAR COLUNA 'beds' PARA 'camas'
df_base_interna.rename(
    columns={'beds': 'camas'},
    inplace=True
)

# VER MÍNIMO E MÁXIMO (DIAGNÓSTICO)
print(
    "min de camas:",
    df_base_interna['camas'].min(),
    "max de camas:",
    df_base_interna['camas'].max()
)

# CORREÇÃO DOS VALORES INVÁLIDOS
df_base_interna.loc[
    (df_base_interna['camas'] <= 0) |
    (df_base_interna['camas'] > 6),
    'camas'
] = None

# TRATAMENTO DE VALORES NULOS - SUBSTITUIR POR MEDIANA
df_base_interna['camas'] = (
    df_base_interna['camas']
    .fillna(df_base_interna['camas'].median())
)

# CONFERIR O RESULTADO
print(df_base_interna[['camas']].head())
print(df_base_interna['camas'].dtype)
print(df_base_interna['camas'].info())
print(df_base_interna['camas'].describe())
print("QUANTIDADE DE VALORES NULOS:", df_base_interna['camas'].isnull().sum())
print("min de camas:", df_base_interna['camas'].min(), "max de camas:", df_base_interna['camas'].max())


# TRATAMENTO DA COLUNA 'room_type'
# RENOMEAR COLUNA 'room_type' PARA 'tipo_de_quarto'
df_base_interna.rename(
    columns={'room_type': 'tipo_de_quarto'},
    inplace=True
)

# TRATAR VALORES NULOS - SUBSTITUIR POR 'moda'
df_base_interna['tipo_de_quarto'] = (
    df_base_interna['tipo_de_quarto']    .fillna(df_base_interna['tipo_de_quarto'].mode()[0])
)

df_base_interna = pd.get_dummies(
    df_base_interna,
    columns=['tipo_de_quarto'],
    prefix='tipo_quarto',
    drop_first=False
)

# CONFERIR O RESULTADO
print(df_base_interna.filter(like='tipo_quarto').head())
print( "QUANTIDADE DE VALORES NULOS:", df_base_interna.filter(like='tipo_quarto').isnull().sum())


# TRATAMENTO DA COLUNA 'review_scores_rating'
# RENOMEAR COLUNA 'review_scores_rating' PARA 'nota_avaliacao'
df_base_interna.rename(
    columns={'review_scores_rating': 'nota_avaliacao'},
    inplace=True
)

# TRATAMENTO DE VALORES NULOS - SUBSTITUIR POR MEDIANA
df_base_interna['nota_avaliacao'] = (
    df_base_interna['nota_avaliacao']
    .fillna(df_base_interna['nota_avaliacao'].median())
)

# VER MÍNIMO E MÁXIMO (DIAGNÓSTICO)
print(
    "min de nota_avaliacao:",
    df_base_interna['nota_avaliacao'].min(),
    "max de nota_avaliacao:",
    df_base_interna['nota_avaliacao'].max()
)

# RESULTADO DO TRATAMENTO
print(df_base_interna['nota_avaliacao'].dtype)
print(df_base_interna['nota_avaliacao'].head())
print("QUANTIDADE DE VALORES NULOS:", df_base_interna['nota_avaliacao'].isnull().sum())


# TRATAMENTO DA COLUNA 'minimum_nights'
# RENOMEAR COLUNA 'minimum_nights' PARA 'noites_minimas'
df_base_interna.rename(
    columns={'minimum_nights': 'noites_minimas'},
    inplace=True
)

# VER MÍNIMO E MÁXIMO (DIAGNÓSTICO)
print(
    "min de noites_minimas:",
    df_base_interna['noites_minimas'].min(),
    "max de noites_minimas:",
    df_base_interna['noites_minimas'].max()
)

# CORREÇÃO DOS VALORES INVÁLIDOS
df_base_interna.loc[
    (df_base_interna['noites_minimas'] <= 0) |
    (df_base_interna['noites_minimas'] > 30),
    'noites_minimas'
] = None

# TRATAR VALORES NULOS - SUBSTITUIR POR MEDIANA
df_base_interna['noites_minimas'] = (
    df_base_interna['noites_minimas']
    .fillna(df_base_interna['noites_minimas'].median())
)

# CONFERIR O RESULTADO
print(df_base_interna['noites_minimas'].head())
print(df_base_interna['noites_minimas'].dtype)
print(df_base_interna['noites_minimas'].info())
print(df_base_interna['noites_minimas'].describe())
print("QUANTIDADE DE VALORES NULOS:", df_base_interna['noites_minimas'].isnull().sum())
print(
    "min de noites_minimas:",
    df_base_interna['noites_minimas'].min(),
    "max de noites_minimas:",
    df_base_interna['noites_minimas'].max()
)


# TRATAMENTO DA COLUNA 'number_of_reviews'
# RENOMEAR PARA 'quantidade_avaliacoes'
df_base_interna.rename(
    columns={'number_of_reviews': 'quantidade_avaliacoes'},
    inplace=True
)

# GARANTIR CONVERSÃO PARA NÚMERO
df_base_interna['quantidade_avaliacoes'] = pd.to_numeric(
    df_base_interna['quantidade_avaliacoes'],
    errors='coerce'
)

# LOG TRANSFORM - CRIAR COLUNA 'reviews_log' COM O LOGARITMO DA QUANTIDADE DE AVALIAÇÕES
import numpy as np

df_base_interna["reviews_log"] = np.log1p(df_base_interna["quantidade_avaliacoes"])

# DIAGNÓSTICO
print(df_base_interna['quantidade_avaliacoes'].head())
print(df_base_interna['quantidade_avaliacoes'].dtype)
print(df_base_interna['quantidade_avaliacoes'].info())
print(df_base_interna['quantidade_avaliacoes'].describe())
print(min(df_base_interna['quantidade_avaliacoes']), max(df_base_interna['quantidade_avaliacoes']))
print("TOTAL DE VALORES NULOS:", df_base_interna['quantidade_avaliacoes'].isnull().sum())
print("original -> min de quantidade_avaliacoes:", df_base_interna['quantidade_avaliacoes'].min(), "max de quantidade_avaliacoes:", df_base_interna['quantidade_avaliacoes'].max())
print("log -> min de reviews_log:", df_base_interna['reviews_log'].min(), "max de reviews_log:", df_base_interna['reviews_log'].max())

