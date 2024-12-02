#GET - https://api.casaspecsa.com/api/venta/all-transacciones
#SI QUIERE TRAER SOLO LAS TRANSACCIONES YA SEA VENDIDAS, SEPARADAS(O INICIADAS) O CANCELADAS AGREGAR estatus COMO VARIABLE 

#valores aceptados: 
#<"Vendido" || "Cancelado" || "Separado" || "Iniciado">

#ejemplo:
#GET - https://api.casaspecsa.com/api/venta/all-transacciones?estatus=Vendido

#se extrae solo la data relacionada a pagos y separaciones para hacer un analisis mas minucioso
import requests
import pandas as pd
import os

#URL base de la api(traer toda la info existente)
BASE_URL ="https://api.casaspecsa.com/api/venta/all-transacciones?estatus=Iniciado"

#Parametros iniciales
limit = 10 #numero de registros que se taera por pagina
page=1 #inicio de pagina
all_data=[] #Lista para guardar toda la data

#ruta para guardar en databricks
output_dir  = "/dbfs/mnt/PagWeb/Extract"
output_file = os.path.join(output_dir, "Iniciados_web.csv")

#Crear la ruta si no existe
if not os.path.exists(output_file):
    os.makedirs(output_file)
    print(f"Ruta creada: {output_dir}")
else:
    print(f"Ruta ya existe:{output_dir}")

#Funcion para extraer datos con paginación
while True:
    #Crear la URL con parametros
    params = {"limit": limit, "page":page}

    try:
        #Solicitud a la API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() #verifica que tipo de error existe

        #Extraer datos en formato JSON
        data=response.json()

        #Verificar si hay datos en la pagina actual
        if not data or len(data)==0:
            print("No hay mas datos disponibles.")
            break #termina

        #Agregar los datos al listado general
        all_data.extend(data)
        print(f"Pagina {page} procesada con exito. Registros obtenidos:{len(data)}")

        #incrementar el numero de pagina
        page +=1
    #muestra el error de api en caso de presentarse
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar la API:{e}")
        break

#Convertir los datos a un DataFrame de Pandas
df=pd.DataFrame(all_data)#se guardan aqui

#guardar los datos en un archivo csv en databricks
df.to_csv(output_file, index=False)
print(f"Datos exportaos a {output_file}")

