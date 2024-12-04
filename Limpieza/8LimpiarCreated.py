import pandas as pd

# leer el archivo CSV
input_path = "/dbfs/mnt/PagWeb/Extract/separados_web_SinError.csv"
df= pd.read_csv(input_path)

#modificar el contenido de la columna 'createdAt' para eliminar todo
#despues de la 'T'
df['createdAt']= df['createdAt'].str.split('T').str[0]

# guardar el archivo actualizado
output_path = "/dbfs/mnt/PagWeb/Extract/separados_web_limpio.csv"
df.to_csv(output_path, index=False)

print(f"Archivo modificado guardado en: {output_path}")
display(df)
