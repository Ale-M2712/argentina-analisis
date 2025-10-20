from sqlalchemy import create_engine
import pandas as pd
import json
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
#solicitud de datos
interaccion_APIs.solicitar_datos(url_1, header, interaccion_APIs.pload)#cambia los parametros 
# Armá el string de conexión
url = f"postgresql+psycopg2://{usuario}:{clave}@{host}:{puerto}/{base}"
engine = create_engine(url)
df = pd.read_csv("Clasificador presupuestario Apertura Programática.csv")
interaccion_db.guardar_datos(df,'Clasificador presupuestario Apertura Programática')
#def actualizar_db():
