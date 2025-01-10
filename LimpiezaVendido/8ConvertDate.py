import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_CreatedClean.csv")

# Convertir la columna 'createdAt' a datetime y extraer solo la fecha
df['createdAt'] = pd.to_datetime(df['createdAt']).dt.date

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df.to_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_date.csv", index=False)

# Mostrar el DataFrame resultante
display(df)