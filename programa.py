from sqlalchemy import create_engine
import pandas as pd
import json
import os
import datetime
import interaccion_json
import interaccion_db
import interaccion_APIs


#los datos estan expresados en millones de pesos

# Reemplazá con tus datos reales
usuario = "postgres"
clave = "Ale271202"
host = "localhost"
puerto = "5432"
base = "Arg_Fiscal"

# Parámetros para la solicitud de datos (terminado)
url_1 = "https://www.presupuestoabierto.gob.ar/api/v1/credito?format=csv"
url_2 = "https://www.presupuestoabierto.gob.ar/api/v1/recurso?format=csv"
url_3 = "https://www.presupuestoabierto.gob.ar/api/v1/pef?format=csv"
url_4 = "https://www.presupuestoabierto.gob.ar/api/v1/transversal_financiero?format=csv"

header = {
    "Authorization": "40d2c302-66ad-4671-a15f-73acc27ef763",
    "Content-Type": "application/json",
    "Accept": "text/csv"
}

# Armá el string de conexión
url = f"postgresql+psycopg2://{usuario}:{clave}@{host}:{puerto}/{base}"
engine = create_engine(url)
df = pd.read_csv("Clasificador presupuestario Apertura Programática.csv")
        

#bajar todos los datos y guardar en la db
def descargar_y_guardar(año, mes, tabla, url, header):
    anio= interaccion_json.ver_anio()
    mes= interaccion_json.ver_mes()
    interaccion_APIs.solicitar_datos(url, header, interaccion_APIs.pload(anio, mes, tabla))
    print(f"leyendo {tabla}.csv")
    df = pd.read_csv(f"{tabla}.csv")
    print("csv leido ,guardando en la db")
    interaccion_db.guardar_datos(df, tabla)
    os.remove(f"{tabla}.csv")
    print(f"{tabla} guardado y csv eliminado")



#ejecucion del programa
interaccion_db.comprobar_conexion()
interaccion_db.comprobar_tabla("credito")
interaccion_db.comprobar_tabla("recurso")
interaccion_db.comprobar_tabla("pef")
interaccion_db.comprobar_tabla("transversal_financiero")