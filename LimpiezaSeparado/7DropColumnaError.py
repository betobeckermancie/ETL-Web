import pandas as pd

#leer el archivo csv original
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/separados_web_asesorExpanded.csv")

df = df.drop('error', axis=1)

#guardar el archivo modificado con nuevo nombre
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_SinError.csv", index=False)

display(df)