import requests

url_1 = "https://www.presupuestoabierto.gob.ar/api/v1/credito?format=csv"
url_2 = "https://www.presupuestoabierto.gob.ar/api/v1/recurso?format=csv"
url_3 = "https://www.presupuestoabierto.gob.ar/api/v1/pef?format=csv"
url_4 = "https://www.presupuestoabierto.gob.ar/api/v1/transversal_financiero?format=csv"

headers = {
    "Authorization": "40d2c302-66ad-4671-a15f-73acc27ef763",
    "Content-Type": "application/json",
    "Accept": "text/csv"
}

payload = {
    "title": "Clasificador presupuestario Apertura Programática",
    "ejercicios": [2021,2022,2023,2024,2025],
    "columns": [
       "ejercicio_presupuestario",
       "servicio_id",
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
       "ultima_actualizacion_fecha"
    ]
}

response = requests.post(url_1, json=payload, headers=headers)

print(response.status_code)

if response.status_code == 200:
    with open("credito.csv", "wb") as f:
        f.write(response.content)
    print("CSV guardado como credito.csv")
else:
    print("Error:", response.text)