import pandas as pd

#leer el archivo csv
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/Cancelados/cancelados_web_expanded.csv")

#remplazar los valores nulos en la columna 'asesor_nombre' por 'otro'
df['asesor_nombre'] = df['asesor_nombre'].fillna('otro')

#guardar el archivo actualizado
df.to_csv("/dbfs/mnt/PagWeb/Extract/Cancelados/cancelados_web_expanded.csv", index=False)

#mostrar cambios
display(df)
print("Valores nulos en 'asesor_nombre' reemplazados por 'otro'")
