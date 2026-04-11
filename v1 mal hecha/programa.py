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
        

#bajar todos los datos y guardar en la db
def descargar_y_guardar(tabla, url, header):
    anio= interaccion_json.ver_anio()
    mes= interaccion_json.ver_mes()
    interaccion_APIs.pedir_datos(url, interaccion_APIs.pload(anio, mes, tabla), header)
    print(f"leyendo {tabla}.csv")
    df = pd.read_csv(f"{tabla}.csv")  # no encuentra el csv
    print("csv leido ,guardando en la db")
    interaccion_db.guardar_datos(df, tabla)
    os.remove(f"{tabla}.csv")
    print(f"{tabla} guardado y csv eliminado")

def descargar_y_guardar_todo(header):
    fecha = interaccion_json.ver_anio(), interaccion_json.ver_mes()
    fecha_actual = datetime.datetime.now().year, datetime.datetime.now().month
    print(f"Fecha de actualizacion: {fecha[0]}-{fecha[1]}")
    while (fecha < fecha_actual):
        print(f"Descargando y guardando datos para {fecha[0]}-{fecha[1]}")
        descargar_y_guardar("credito", url_1, header) #funciona  -- efecto adicional , me guarda las cosas en una tabla llamada credito | modificar generacion de tablas
        descargar_y_guardar("recurso", url_2, header) #funciona  -- efecto adicional , me guarda las cosas en una tabla llamada recurso | modificar generacion de tablas
        if (fecha[0]>=2007):
            descargar_y_guardar("pef", url_3, header)
        descargar_y_guardar("transversal_financiero", url_4, header) # no funciona, no carga nada , es una por año asi que voy a tener que modificar la logica
        interaccion_json.sumar_meses()
        fecha = interaccion_json.ver_anio(), interaccion_json.ver_mes()
    print("Descarga y guardado completados.")
#ejecucion del programa
print("verificando conexion a la db...")
interaccion_db.comprobar_conexion()
print("comprobando tablas...")
print("tabla credito:")
if(not(interaccion_db.comprobar_tabla("credito"))):
    if input("¿Desea crearla? (s/n): ").lower() == 's':
        interaccion_db.crear_tabla("credito")
print("tabla recurso:")
if(not(interaccion_db.comprobar_tabla("recurso"))):
    if input("¿Desea crearla? (s/n): ").lower() == 's':
        interaccion_db.crear_tabla("recurso")
print("tabla pef:")
if(not(interaccion_db.comprobar_tabla("pef"))):
    if input("¿Desea crearla? (s/n): ").lower() == 's':
        interaccion_db.crear_tabla("pef")
print("tabla transversal_financiero:")
if(not(interaccion_db.comprobar_tabla("transversal_financiero"))):
    if input("¿Desea crearla? (s/n): ").lower() == 's':
        interaccion_db.crear_tabla("transversal_financiero")

print("descargando y guardando datos...")
descargar_y_guardar_todo(header)