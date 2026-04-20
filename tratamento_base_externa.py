import pandas as pd

# 1. EXTRAÇÃO
df_base_ipca = pd.read_csv ('bases/base_ipca.csv')

# print (df_base_ipca.head())
# print (df_base_ipca.info ())
       
# 2. TRANSFORMAÇÃO
df_base_ipca = df_base_ipca.rename(columns={"Unnamed: 0": "ano"})

# GARANTIR QUE O NOME DAS COLUNAS ESTEJA LIMPOS
df_base_ipca.columns = (
    df_base_ipca.columns
        .str.strip()
        .str.replace(".", "", regex=False)
)

# 3. FILTRAR POR ANO "2025"
ipca_2025 = df_base_ipca[df_base_ipca["ano"] == 2025].copy()

# 4. TRATAR O IPCA MENSAL (Setembro)
ipca_2025["Set"] = (
    ipca_2025["Set"]
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float) / 100
)

# 5. TRATAR O IPCA ACUMULADO NO ANO
ipca_2025["Ano"] = (
    ipca_2025["Ano"]
        .str.replace("%", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float) / 100
)

# 6.CRIAR O MODELO DataFrame FINAL (modelo para o banco)
ipca_final = pd.DataFrame({
    "ano": ipca_2025["ano"].values,
    "mes": 9,
    "ano_mes": "2025-09",
    "ipca_mensal": ipca_2025["Set"].values,
    "ipca_acumulado_ano": ipca_2025["Ano"].values
})

ipca_final["ano_mes"] = pd.to_datetime(ipca_final["ano_mes"], format="%Y-%m")