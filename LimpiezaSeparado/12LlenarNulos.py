import pandas as pd

#leer archivo csv
df= pd.read_csv("/dbfs/mnt/PagWeb/Extract/Separados/separados_web_sinGuionesDobles.csv")

#remplazar valores nulos
df['asesor_nombre'] =df['asesor_nombre'].fillna("Otro")

#guardar
df.to_csv("/dbfs/mnt/PagWeb/Extract/Separados/separados_web_FillNulos.csv", index=False)