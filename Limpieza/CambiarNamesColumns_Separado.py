#codigo para cambiar el nombre de las columnnas ya que se repiten varios
import pandas as pd

#leer el achivo fuente
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/separados_web.csv")

#diccionario para los cambios de nombres en columnas
#agregar columnas a cambiar por nuevos nombres

new_column_names={
    "id": "id_gral",
    "folio": "folio_gral"
    #Agregar todos los nombres de columnas a cambiar
}

#renombar las columnas
df.rename(columns=new_column_names, inplace=True)

#guardar el dataframe renombrado en un nuevo archivo csv
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_renombradoColumns.csv", index=False)

print("Archivo renombrado y guardado exitosamente")
display(df)