import pandas as pd

# Función para expandir la columna 'cliente'
def expand_cliente(cliente):
    try:
        # Validar si el valor ya es un diccionario
        if isinstance(cliente, dict):
            cliente_dict = cliente  # Ya es un diccionario, no se necesita convertir
        elif isinstance(cliente, str) and cliente.strip():
            cliente_dict = eval(cliente)  # Convertir cadena a diccionario
        else:
            return pd.Series({'error': 'Valor nulo o inválido'})  # Registrar el error
        
        # Normalizar datos anidados
        expanded = pd.json_normalize(cliente_dict)
        return expanded.iloc[0]  # Devolver la primera fila como Serie
    except Exception as e:
        print(f"Error al procesar el cliente: {cliente} - {e}")
        return pd.Series({'error': 'Error de procesamiento'})  # Registrar el error

# Aplicar la función para expandir la columna 'cliente'
df_expanded = df['cliente'].apply(expand_cliente)

# Concatenar las nuevas columnas con el DataFrame original
df_final = pd.concat([df.drop('cliente', axis=1), df_expanded], axis=1)

# Guardar el resultado en un nuevo archivo CSV
output_path = "/dbfs/mnt/processed/separados_web_clienteExpanded.csv"
df_final.to_csv(output_path, index=False)
print(f"Datos expandidos guardados en: {output_path}")

# Mostrar los resultados
display(df_final)
