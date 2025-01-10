import pandas as pd

#leer el csv desde la ruta 
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_clienteExpanded.csv")

#remplazar las columnas que empiezas con 'datos.' por 'cliente_'
df.columns = [col.replace("datos.", "cliente_") if col.startswith("datos.") else col for col in df.columns]

#guardar el dataframe renombrado en un nuevo archivo csv
df.to_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_clienteDatosForCliente.csv", index=False)

print("Archivo renombrado y guardado con exito")
display(df)