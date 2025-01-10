import pandas as pd

#leer el archivo csv
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_asesorExpanded.csv")

df= df.drop('error', axis=1)

#guardar el archivo modificado con un nuevo nombre
df.to_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_asesorExpanded_SinError.csv", index=False)

display(df)