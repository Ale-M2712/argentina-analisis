import requests

url_1 = "https://www.presupuestoabierto.gob.ar/api/v1/credito?format=csv"
url_2 = "https://www.presupuestoabierto.gob.ar/api/v1/recurso?format=csv"
url_3 = "https://www.presupuestoabierto.gob.ar/api/v1/pef?format=csv"
url_4 = "https://www.presupuestoabierto.gob.ar/api/v1/transversal_financiero?format=csv"

header = {
    "Authorization": "40d2c302-66ad-4671-a15f-73acc27ef763",
    "Content-Type": "application/json",
    "Accept": "text/csv"
}

pload = {
    "title": "Credito",
    "ejercicios": [1995],
    "columns": [
"impacto_presupuestario_anio",
"impacto_presupuestario_mes",
"ejercicio_presupuestario",
"sector_id",
"sector_desc",
"subsector_id",
"subsector_desc",
"caracter_id",
"caracter_desc",
"jurisdiccion_id",
"jurisdiccion_desc",
"subjurisdiccion_id",
"subjurisdiccion_desc",
"entidad_id",
"entidad_desc",
"servicio_id",
"servicio_desc",
"programa_id",
"programa_desc",
"subprograma_id",
"subprograma_desc",
"proyecto_id",
"proyecto_desc",
"actividad_id",
"actividad_desc",
"obra_id",
"obra_desc",
"finalidad_id",
"finalidad_desc",
"funcion_id",
"funcion_desc",
"inciso_id",
"inciso_desc",
"principal_id",
"principal_desc",
"parcial_id",
"parcial_desc",
"subparcial_id",
"subparcial_desc",
"clasificador_economico_8_digitos_id",
"clasificador_economico_8_digitos_desc",
"fuente_financiamiento_id",
"fuente_financiamiento_desc",
"ubicacion_geografica_id",
"ubicacion_geografica_desc",
"unidad_ejecutora_id",
"unidad_ejecutora_desc",
"prestamo_externo_id",
"prestamo_externo_desc",
"codigo_bapin_id",
"codigo_bapin_desc",
"credito_presupuestado",
"credito_vigente",
"credito_comprometido",
"credito_devengado",
"credito_pagado",
"ultima_actualizacion_fecha"
],
"filters":[
    {
      "column": "impacto_presupuestario_mes",
      "operator": "equal",
      "value": "10"}
]
}

# Función para hacer la solicitud y guardar el CSV (terminado)
def pedir_datos(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers) #tengo que armar lo de los json varios

    print(response.status_code) # Verifica el código de estado de la respuesta

    if response.status_code == 200: # Si la solicitud fue exitosa
        with open(f"{payload['title']}.csv", "wb") as f: # Guardar el contenido en un archivo CSV
            f.write(response.content)
        print("CSV guardado como credito.csv") # Mensaje de confirmación
    else:
        print("Error:", response.text) # Mensaje de error si la solicitud falla

pedir_datos(url_1, pload, header) #prueba