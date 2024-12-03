import pandas as pd

#funcion para expandir la columna 'cliente'
def expand_cliente(cliente):
    try:
        #validar si el valor ya es un diccionario
        if isinstance(cliente, dict):
            cliente_dict =cliente # ya es un diccionario , no se necesita convertir
        elif isinstance(cliente, str) and cliente.strip():
            cliente_dict = eval(cliente) #convertir cadena a diccionario
        else:
            return pd.Series({'error':'Valor nuelo o invalido'})
            #registra el error
        
        #Normalizar los datos anidados
        expanded = pd.json_normalize(cliente_dict)
        return expanded.iloc[0]#devolver la primer fila como serie
    except Exception as e:
        print(f"Error al procesar el cliente: {cliente} - {e}")
        return pd.Series({"error":"Error de procesamiento"})
        #registrar el error

# aplicar la funcion para expandir la columna 'cliente'
df_expanded = df['cliente'].apply(expand_cliente)

#concatenar las nuevas columnas con el dataframe original
df_final = pd.concat([df.drop('cliente', axis=1), df_expanded], axis=1)

#guardar el resultado en un nuevo archivo csv
out_path= "/dbfs/mnt/processed/separados_web_clienteExpanded.csv"
df_final.to_csv(out_path, index=False)
print(f"Datos expandidos guardados en: {output_path}")

#Mostrar resultados
display(df_final)