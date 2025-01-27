import pandas as pd
from unidecode import unidecode

#cargar el dataframe
df = pd.read_csv("/dbfs/mnt/PagWeb/Extract/Separados/separados_web_AllClean_lowercase.csv")

#lista de columnas en las que deseas eliminar acentos
columns_to_modify = ['cliente_primerNombre', 'cliente_segundoNombre', 'cliente_primerApellido', 'cliente_segundoApellido', 'cliente_nombreCompleto', 'lote_sku', 'lote_manzana_etapa_fraccionamiento_nombre', 'lote_fachada_modelo_nombre', 'estatus_nombre', 'asesor_nombre']

#quitar acentos a registros de las columnas seleccionadas
output_path = "/dbfs/mnt/PagWeb/Extract/Separados/separados_web_AllClean.csv"
df.to_csv(output_path, index=False)

#verificar
print(f"Archivo guardado en: {output_path}")
display(df.head())
