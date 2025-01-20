# Leer el archivo CSV
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/Separados/separados_web_guionesBajos.csv")

# Lista de columnas a modificar
columnas_a_modificar = ['asesor_nombre', 'cliente_nombreCompleto'] #se agregan las columnas necesarias

# Reemplazar espacios por guiones bajos en las columnas seleccionadas
for columna in columnas_a_modificar:
    df[columna] = df[columna].apply(lambda x: x.replace('__', '_') if isinstance(x, str) else x)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv("/dbfs/mnt/PagWeb/Extract/Separados/separados_web_sinGuionesDobles.csv", index=False)

# Mostrar el DataFrame modificado
display(df)