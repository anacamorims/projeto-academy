# INTEGRAÇÃO
import pandas as pd
import sqlite3
from ETL import df_base_interna
from tratamento_base_externa import ipca_final

base_integrada = df_base_interna.merge(
ipca_final,
on = ["ano", "mes"],
how = "left"
)

# 3. CARGA - EXPORTAR PARA BANCO DE DADOS SQLITE
# CONECTAR AO BANCO DE DADOS (OU CRIAR SE NÃO EXISTIR)
conexao = sqlite3.connect('base_tratada.db')

# EXPORTAR O DATAFRAME PARA O BANCO DE DADOS
base_integrada.to_sql('base_tratada', conexao, if_exists='replace', index=False)

# Ler a tabela do SQLite
df_sqlite = pd.read_sql('SELECT * FROM base_tratada', conexao)

# Printar as primeiras linhas
print(df_sqlite)

# FECHAR A CONEXÃO
conexao.close()
