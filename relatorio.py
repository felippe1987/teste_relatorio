import tabula as tb
import pandas as pd

lista_tabela = tb.read_pdf("relatorio.pdf", pages="all")

df_final = pd.concat(lista_tabela)
df_final.to_csv("dados_extraidos.csv", index=False)

