import pandas as pd

#leer el archivo csv
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_loteExpanded.csv")

#funcion para expandir la columna 'estatus'
def expand_estatus(estatus):
    try:
        #validar si el valor es un diccionario
        if isinstance(estatus, dict):
            estatus_dict = estatus
        elif isinstance(estatus, str) and estatus.strip():
            estatus_dict = eval(estatus) #eval convierte una cadena con formato de diccionario ( como JSON en python), en un verdadero dicc de py
        else:
            return pd.Series({'error':'Valor nulo o invalido'})
        
        # Normalizar datos anidados y agregar prefijo del nombre de la columna
        expanded = pd.json_normalize(estatus_dict, sep='_')
        expanded.columns = [f"estatus_{col}" for col in expanded.columns]  # Agregar prefijo 'lote_' a todas las columnas anidadas
        return expanded.iloc[0]#se guarda el dato
    except Exception as e:
        print(f"Error al procesar el estatus: {estatus} - {e}")
        return pd.Series({'error': 'Error de procesamiento'})
    

#Aplicar la funcion para expandir la columna 'estatus'
df_expanded = df['estatus'].apply(expand_estatus)

#concatenar con el dataframe original y agregar las columnas expandidas al final
df_final = pd.concat([df.drop('estatus', axis=1), df_expanded], axis=1)

#guardar el archivo resultante
output_path = "/dbfs/mnt/PagWeb/Extract/vendidos_web_estatusExpanded.csv"
df_final.to_csv(output_path, index=False)
print(f"Datos expandidos guardados en: {output_path}")

#Mostrar los resultados
display(df_final)