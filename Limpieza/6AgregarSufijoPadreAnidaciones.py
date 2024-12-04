import pandas as pd

# Leer archivo CSV
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/separados_web_estatusExpanded.csv")

# Función para expandir la columna 'asesor'
def expand_asesor(asesor):
    try:
        # Validar si el valor ya es un diccionario
        if isinstance(asesor, dict):
            asesor_dict = asesor
        elif isinstance(asesor, str) and asesor.strip():
            asesor_dict = eval(asesor)#eval convierte una cadena con formato de diccionario(como JSON en python), en un verdadero dicc de py
        else:
            return pd.Series({'error': 'Valor nulo o inválido'})
        
        # Normalizar datos anidados y agregar prefijo del nombre de la columna
        expanded = pd.json_normalize(asesor_dict, sep='_')
        expanded.columns = [f"asesor_{col}" for col in expanded.columns]  # Agregar prefijo 'lote_' a todas las columnas anidadas
        return expanded.iloc[0]
    except Exception as e:
        print(f"Error al procesar el asesor: {asesor} - {e}")
        return pd.Series({'error': 'Error de procesamiento'})



# Aplicar la función para expandir la columna 'asesor'
df_expanded = df['asesor'].apply(expand_asesor)

# Concatenar con el DataFrame original y agregar las columnas expandidas al final
df_final = pd.concat([df.drop('asesor', axis=1), df_expanded], axis=1)

# Guardar el archivo resultante
output_path = "/dbfs/mnt/PagWeb/Extract/separados_web_asesorExpanded.csv"
df_final.to_csv(output_path, index=False)
print(f"Datos expandidos guardados en: {output_path}")


# Mostrar los resultados
display(df_final)