import pandas as pd

#leer el archivo csv
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_clienteDatosForCliente.csv")

#Funcion para expandir la columna 'lote'
def expand_lote(lote):
    try:
        #validar si el valor ya es un diccionario
        if isinstance(lote, dict):
            lote_dict = lote
        elif isinstance(lote, str) and lote.strip():
            lote_dict = eval(lote) #eval convierte una cadena con formato de diccionario (como JSON en python), en un verdadro dicc de py
        else:
            return pd.Series({'error': 'Valor nulo o inválido'})
        
        #Normalizar datos anidados y agregar prefijo del nombre de la columna
        expanded = pd.json_normalize(lote_dict, sep='_')
        expanded.columns = [f"lote_{col}" for col in expanded.columns] #agregar prefijo 'lote_' a todas las columnas anidadas
        return expanded.iloc[0]
    
    except Exception as e:
        print(f"Error al procesar el lote: {lote} - {e}")
        return pd.Series({'error': 'Error de procesamiento'})
    

#Aplicar la funcion para expandir la columna 'lote'
df_expanded = df['lote'].apply(expand_lote)

#Concatenar con el dataframe original y agregar las columnas expandidas al final
df_final = pd.concat([df.drop('lote', axis=1), df_expanded], axis=1)

#guardar el archivo resultante
output_path = "/dbfs/mnt/PagWeb/Extract/vendidos_web_loteExpanded.csv"
df_final.to_csv(output_path, index=False)
print(f"Datos expandidos guardados en: {output_path}")

#Mostrar los resultados
display(df_final)
