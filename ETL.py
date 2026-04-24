import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1 EXTRAÇÃO
df_base_interna = pd.read_csv('bases/base_interna.csv')

#Inicialização do LabelEncoder por coluna
le_bairro= LabelEncoder();
# le_tipo_quarto= LabelEncoder(); - não vou usar
le_tipo_propriedade= LabelEncoder();

# MAPA DE MAPEAMENTO - TIPO DE QUARTO
mapa_tipo_quarto = {
    "entire home/apt": "casa_apto_inteiro",
    "hotel room": "quarto_hotel",
    "private room": "quarto_privativo",
    "shared room": "quarto_compartilhado"
}

# MAPA DE AGRUPAMENTO - TIPO DE PROPRIEDADE (REGRA DE NEGÓCIO)
mapa_tipo_propriedade = {

    # ESPAÇO INTEIRO – RESIDENCIAL
    "entire home": "espaco_inteiro_residencial",
    "entire condo": "espaco_inteiro_residencial",
    "entire rental unit": "espaco_inteiro_residencial",
    "entire guesthouse": "espaco_inteiro_residencial",
    "entire guest suite": "espaco_inteiro_residencial",
    "entire townhouse": "espaco_inteiro_residencial",
    "entire cottage": "espaco_inteiro_residencial",
    "entire bungalow": "espaco_inteiro_residencial",
    "entire villa": "espaco_inteiro_residencial",
    "entire vacation home": "espaco_inteiro_residencial",
    "entire serviced apartment": "espaco_inteiro_residencial",
    "entire loft": "espaco_inteiro_residencial",
    "entire chalet": "espaco_inteiro_residencial",
    "entire place": "espaco_inteiro_residencial",
    "tiny home": "espaco_inteiro_residencial",

    # QUARTO PRIVATIVO – RESIDENCIAL
    "private room": "quarto_privativo_residencial",
    "private room in home": "quarto_privativo_residencial",
    "private room in condo": "quarto_privativo_residencial",
    "private room in rental unit": "quarto_privativo_residencial",
    "private room in townhouse": "quarto_privativo_residencial",
    "private room in villa": "quarto_privativo_residencial",
    "private room in cabin": "quarto_privativo_residencial",
    "private room in guest suite": "quarto_privativo_residencial",
    "private room in farm stay": "quarto_privativo_residencial",
    "private room in casa particular": "quarto_privativo_residencial",

    # HOSPEDAGEM COMERCIAL
    "room in hotel": "hospedagem_comercial",
    "room in boutique hotel": "hospedagem_comercial",
    "private room in bed and breakfast": "hospedagem_comercial",
    "private room in hostel": "hospedagem_comercial",
    "shared room in hostel": "hospedagem_comercial",

}

# 2. TRANSFORMAÇÃO - SELEÇÃO DE COLUNAS para TRATAMENTO (Limpeza Bruta)
colunas_tratamento = ["price","accommodates","bedrooms", "beds", "bathrooms_text", 
"room_type", "review_scores_rating","minimum_nights", "number_of_reviews", "property_type",
"latitude", "longitude", "neighbourhood_cleansed"]
df_base_interna = df_base_interna[colunas_tratamento]

#inserir colunas de ano e mês para integrar ao ipca - pode mudar para base do AIRBNB ( adiconar coluna 'last_scraped' ou 'calendar_last_scraped' e extrair ano e mês a partir dela)
df_base_interna ["ano"] = 2025
df_base_interna ["mes"] = 9

# RENOMEAR TODAS AS COLUNAS NO INÍCIO
df_base_interna.rename(
    columns={
        'price': 'preco',
        'accommodates': 'hospedes',
        'bedrooms': 'quartos',
        'beds': 'camas',
        'room_type': 'tipo_de_quarto',
        'review_scores_rating': 'nota_avaliacao',
        'minimum_nights': 'noites_minimas',
        'number_of_reviews': 'quantidade_avaliacoes',
        'property_type': 'tipo_de_propriedade',
        'neighbourhood_cleansed': 'bairro'
    },
    inplace=True
)

#atribui variáveis as colunas de interesse para tratamento - evitar hardcoding
coluna_preco = "preco"
coluna_hospedes = "hospedes"
coluna_quartos = "quartos"
coluna_camas = "camas"
coluna_tipo_de_quarto = "tipo_de_quarto"
coluna_nota_avaliacao = "nota_avaliacao"
coluna_noites_minimas = "noites_minimas"
coluna_quantidade_avaliacoes = "quantidade_avaliacoes"
coluna_tipo_de_propriedade = "tipo_de_propriedade"
coluna_bairro = "bairro"
coluna_latitude = "latitude"
coluna_longitude = "longitude"

# TRATAMENTO DA COLUNA 'price'
df_base_interna [coluna_preco] = df_base_interna [coluna_preco].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
# TRATAMENTO DA COLUNA 'preco' PARA float
df_base_interna [coluna_preco] = df_base_interna [coluna_preco].astype(float)

#TRATAMENTO DA COLUNA 'bathrooms_text'
# CRIAR COLUNA 'banheiros' A PARTIR DA COLUNA 'bathrooms_text'
df_base_interna['banheiros'] = (
    df_base_interna['bathrooms_text']
    .str.extract(r'(\d+\.?\d*)')
    .astype(float)
)
# REMOVER COLUNA 'bathrooms_text' APÓS EXTRAÇÃO DE INFORMAÇÃO
df_base_interna.drop('bathrooms_text', axis=1, inplace=True)

#Normalizar tipo_de_quarto - todos valores minúsculos
df_base_interna[coluna_tipo_de_quarto] = (
    df_base_interna[coluna_tipo_de_quarto]
    .str.strip()
    .str.lower()
)

#Label encoder para 'tipo_de_quarto'
#df_base_interna ["tipo_de_quarto_encode"] = le_tipo_quarto.fit_transform(df_base_interna ["tipo_de_quarto"]) + 1

#Renomeor categorias de 'tipo de quarto' para português
df_base_interna[coluna_tipo_de_quarto] = df_base_interna[coluna_tipo_de_quarto].map(mapa_tipo_quarto)

df_base_interna_dummies = pd.get_dummies(
    df_base_interna[coluna_tipo_de_quarto],
    prefix='tipo_quarto',
    drop_first=False
)

#juntar as colunas dummies com a base original (horizontalmente)
df_base_interna = pd.concat([df_base_interna, df_base_interna_dummies], axis=1)

# TRATAMENTO DA COLUNA 'quantidade_avaliacoes'
# GARANTIR CONVERSÃO PARA NÚMERO
df_base_interna[coluna_quantidade_avaliacoes] = pd.to_numeric(
    df_base_interna[coluna_quantidade_avaliacoes],
    errors='coerce'
)

# DEFINIR A COLUNA DE PROPRIEDADE PARA TRATAMENTO
#atribui uma variável para evitar hardcoding

# NORMALIZAÇÃO
df_base_interna[coluna_tipo_de_propriedade] = (
    df_base_interna[coluna_tipo_de_propriedade]
    .fillna("outros")
    .astype(str)
    .str.strip()
    .str.lower()
)

# APLICAR AGRUPAMENTO
df_base_interna["tipo_de_propriedade_grupo"] = (
    df_base_interna[coluna_tipo_de_propriedade]
    .map(mapa_tipo_propriedade)
    .fillna("outros")
)

# CRIAR VARIÁVEIS DO LABEL ENCODER PARA 'tipo_de_propriedade_grupo'
df_base_interna ["tipo_de_propriedade_grupo"] = le_tipo_propriedade.fit_transform(df_base_interna ["tipo_de_propriedade_grupo"]) + 1

# TRATAMENTO DA COLUNA 'latitude'
# TRATAMENTO DA COLUNA 'latitude' PARA float
df_base_interna [coluna_latitude] = df_base_interna [coluna_latitude].astype(float)

# TRATAMENTO DA COLUNA 'longitude'
# TRATAMENTO DA COLUNA 'longitude' PARA float
df_base_interna [coluna_longitude] = df_base_interna [coluna_longitude].astype(float)

# CRIAR VARIÁVEIS DO LABEL ENCODER 'bairro_grupo'
df_base_interna ["bairro_encode"] = le_bairro.fit_transform(df_base_interna ["bairro"]) + 1