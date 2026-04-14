# INTEGRAÇÃO
import sqlite3
from ETL import df_base_interna
from tratamento_base_externa import ipca_final

base_integrada = df_base_interna.merge(
ipca_final,
on = ["ano", "mes"],
how = "left"
)

print (base_integrada.dtypes)