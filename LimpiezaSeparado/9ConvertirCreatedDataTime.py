import pandas as pd

df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/separados_web_limpio.csv")
# Convertir la columna createdAt a datetime
df['createdAt'] = pd.to_datetime(df['createdAt'])
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_datetime.csv", index=False)
display(df)