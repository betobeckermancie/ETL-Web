import pandas as pd
import roman 

#Leer archivo
df= pd.read_csv("/dbfs/mnt/PagWeb/Extract/separados_web_limpio.csv")

#Funcion para convertir numero romanos a enteros
def convert_roman_to_int(roman_value):
    try:
        # Intentar convertir el número romano a entero usando la función `fromRoman` de la librería `roman`
        return roman.fromRoman(roman_value)
    except roman.InvalidRomanNumeralError:
        return None #maneja errores en caso de valores no validos

#Aplicar la conversion a la columna
df['lote_manzana_etapa_nombre']= df['lote_manzana_etapa_nombre'].apply(convert_roman_to_int)

#guardar el archivo actualizado
df.to_csv("/dbfs/mnt/PagWeb/Extract/separados_web_AllCleaned.csv", index=False)

print("Conversión completada y archivo guardado.")
display(df)