from unittest import case
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

def pload(año, mes, tabla):
    # Validar parámetros
    if not isinstance(año, int):
        raise ValueError("El parámetro 'año' debe ser un número entero")
    if not isinstance(mes, int) or mes < 1 or mes > 12:
        raise ValueError("El parámetro 'mes' debe ser un número entre 1 y 12")
    if tabla not in ["credito", "recurso", "pef", "transversal_financiero"]:
        raise ValueError("'tabla' debe ser una de: credito, recurso, pef, transversal_financiero")
        
    if tabla == "credito":
        pload = {
    "title": "Credito",
    "ejercicios": [año],
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
      "value": f"{mes}"
}
]
}
    elif tabla == "recurso":
        pload = {
    "title": "recurso",
    "ejercicios": [año],
    "columns": [
"impacto_presupuestario_fecha",
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
"tipo_id",
"tipo_desc",
"clase_id",
"clase_desc",
"concepto_id",
"concepto_desc",
"subconcepto_id",
"subconcepto_desc",
"fuente_financiamiento_id",
"fuente_financiamiento_desc",
"clasificador_economico_8_digitos_id",
"clasificador_economico_8_digitos_desc",
"prestamo_externo_id",
"prestamo_externo_desc",
"recurso_inicial",
"recurso_vigente",
"recurso_ingresado_percibido",
"ultima_actualizacion_fecha"
],
"filters":[
    {
      "column": "impacto_presupuestario_mes",
      "operator": "equal",
      "value": f"{mes}"}
]
}
    elif tabla == "pef":
        pload = {
    "title": "pef",
    "ejercicios": [año],
    "columns": [
"ejercicio_presupuestario",
"trimestre",
"finalidad_id",
"finalidad_desc",
"funcion_id",
"funcion_desc",
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
"medicion_fisica_id",
"medicion_fisica_desc",
"tipo_medicion_fisica",
"unidad_medida_id",
"unidad_medida_desc",
"ubicacion_geografica_id",
"ubicacion_geografica_desc",
"totalizador_avance_fisico",
"programacion_inicial_DA",
"programacion_inicial_ajustada",
"programacion_anual_vig_cierre",
"programacion_anual_vig_trim",
"programacion_trim",
"programacion_acumulada_trim",
"ejecutado_vigente_trim",
"ejecutado_acumulado_trim",
"ejecutado_cierre_acum_trim",
"ejecucion_anual_de_cierre",
"tipo_causa_desvio",
"causa_desvio",
"causa_desvio_detalle",
"causa_desvio_comentario",
"porc_desvio_acum_trim",
"ultima_actualizacion_fecha"
],
"filters":[
    {
      "column": "impacto_presupuestario_mes",
      "operator": "equal",
      "value": f"{mes}"}
]
}
    elif tabla == "transversal_financiero":
        pload = {
    "title": "transversal_financiero",
    "ejercicios": [año],
    "columns": [
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
"fuente_financiamiento_id",
"fuente_financiamiento_desc",
"ubicacion_geografica_id",
"ubicacion_geografica_desc",
"inciso_id",
"inciso_desc",
"principal_id",
"principal_desc",
"parcial_id",
"parcial_desc",
"subparcial_id",
"subparcial_desc",
"etiqueta_id",
"etiqueta_desc",
"ponderacion_credito",
"codigo_bapin_id",
"codigo_bapin_desc",
"credito_inicial",
"credito_inicial_ponderado",
"credito_vigente",
"credito_vigente_ponderado",
"credito_ejecutado",
"credito_ejecutado_ponderado"
],
"filters":[
    {
      "column": "impacto_presupuestario_mes",
      "operator": "equal",
      "value": f"{mes}"}
]
}
    return pload

# Función para hacer la solicitud y guardar el CSV (terminado)
def pedir_datos(url, payload, headers):
    print(f"Solicitando datos para {payload['title']} del año {payload['ejercicios'][0]} y mes {payload['filters'][0]['value']}...")
    response = requests.post(url, json=payload, headers=headers) #tengo que armar lo de los json varios
    
    if response.status_code == 200: # Si la solicitud fue exitosa
        with open(f"{payload['title']}.csv", "wb") as f: # Guardar el contenido en un archivo CSV
            f.write(response.content)
        print("CSV guardado como credito.csv") # Mensaje de confirmación
    else:
        print(response.status_code)
        print("Error:", response.text) # Mensaje de error si la solicitud falla

pedir_datos(url_1, pload(1995, 5, "credito"), header) #prueba