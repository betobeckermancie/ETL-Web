import pandas as pd 
import roman

#leer el archivo csv
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_date.csv")

#funcion para convertir numeros romanos a enteros
def convert_roman_to_int(roman_value):
    try:
        return roman.fromRoman(roman_value)
    except roman.InvalidRomanNumeralError:
        return None #Manear errores en caso de valores no validos
    
#Aplicar la conversion a la columna
df['lote_manzana_etapa_nombre'] = df['lote_manzana_etapa_nombre'].apply(convert_roman_to_int)

#guardar el archivo actualizado
df.to_csv("/dbfs/mnt/PagWeb/Extract/vendidos_web_roman.csv", index=False)
print("Conversion a num romanos realizados y guardado")
display(df)
