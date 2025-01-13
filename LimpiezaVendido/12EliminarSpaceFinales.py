import pandas as pd

# Eliminar los guiones bajos al final de las palabras en la columna 'asesor_nombre'
df['asesor_nombre'] = df['asesor_nombre'].str.rstrip('_')
df['cliente_nombreCompleto'] = df['cliente_nombreCompleto'].str.rstrip('_')
df['lote_manzana_etapa_fraccionamiento_nombre'] = df['lote_manzana_etapa_fraccionamiento_nombre'].str.rstrip('_')

# Guardar el DataFrame actualizado en un nuevo archivo CSV
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_AllClean.csv", index=False)

# Mostrar el DataFrame actualizado
display(df)