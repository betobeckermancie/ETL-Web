#codigo para cambiar el nombre de las columnas ya que se repiten varios
import pandas as pd

#leer el csv desde la ruta especificada
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web.csv")

#diccionario con los cambios de nombres en columnas/agregar nombres de columnas a cambiar por nuevos nombres
new_column_names ={
    'id': 'id_gral',
    'folio': 'folio_gral'
    # Agrega todos los nombres de columnas que deseas cambiar
}

#renombar las columnas
df.rename(columns = new_column_names, inplace=True)

#guardar el dataframe renombrado en un nuevo archivo csv
df.to_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_renamedColumns.csv", index=False)

print("Archivo renombrado y guardado con exito")
display(df)