#cambiamos las columnas que tengan nombre al inicio como 'datos.' por 'cliente_' 
#para diferenciar entre los demas datos y no repetir
import pandas as pd

df= pd.read_csv("/dbfs/mnt/processed/separados_web_clienteExpanded.csv")

#remplanzar las columnas que empiezas con 'datos.' por 'cliente_'
df.columns = [col.replace("datos.", "cliente_") if col.startswith("datos.") else col for col in df.columns]

#guardar el dataframe renombrado en un nuevo archivo csv
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_renombradoColumnsCliente.csv", index=False)

print("Archivo renombrado y guardado exitosamente")
display(df)
