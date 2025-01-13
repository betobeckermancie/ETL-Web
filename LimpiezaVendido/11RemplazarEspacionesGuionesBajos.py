import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/separados_web_CreatedClean.csv")

# Lista de columnas a modificar
columnas_a_modificar = ['asesor_nombre', 'cliente_nombreCompleto', 'lote_manzana_etapa_fraccionamiento_nombre'] #se agregan las columnas necesarias

# Reemplazar espacios por guiones bajos en las columnas seleccionadas
for columna in columnas_a_modificar:
    df[columna] = df[columna].apply(lambda x: x.replace(' ', '_') if isinstance(x, str) else x)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_modified.csv", index=False)

# Mostrar el DataFrame modificado
display(df)