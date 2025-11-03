import os
import json


def fecha_actualizacion():
    """Devuelve (anio, mes) de la última actualización.

    Esta función asegura:
    - manejar archivos faltantes creando uno por defecto
    - tolerar JSON inválido recreándolo con valores por defecto
    - soportar claves con y sin 'ñ' por compatibilidad (migración)
    """
    ruta = "actualizacion.json"

    # Si el archivo no existe, lo crea con una fecha inicial
    if not os.path.exists(ruta):
        fecha_inicial = 1995
        mes_inicial = 1
        data = {"ultima_actualizacion_anio": fecha_inicial, "ultima_actualizacion_mes": mes_inicial}
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"🆕 Archivo creado con fecha: {fecha_inicial}-{mes_inicial}")
        return fecha_inicial, mes_inicial

    # Si existe, lo lee con manejo de errores
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # El archivo existe pero contiene JSON inválido -> reescribir con valores por defecto
        fecha_inicial = 1995
        mes_inicial = 1
        data = {"ultima_actualizacion_anio": fecha_inicial, "ultima_actualizacion_mes": mes_inicial}
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"⚠️ JSON inválido en {ruta}. Reescrito con fecha por defecto: {fecha_inicial}-{mes_inicial}")
        return fecha_inicial, mes_inicial

    # Compatibilidad con clave con 'ñ' o sin ella
    anio = data.get("ultima_actualizacion_anio")
    if anio is None:
        # intentar la clave con 'ñ' si existe (migración de versiones antiguas)
        anio = data.get("ultima_actualizacion_año")
    mes = data.get("ultima_actualizacion_mes", 1)

    # Valores por defecto si algo falta
    if anio is None:
        anio = 1995

    return anio, mes


def sumar_meses():
    """Incrementa en 1 el mes de `actualizacion.json` y lo persiste.

    Usa las mismas claves estandarizadas: `ultima_actualizacion_anio` y `ultima_actualizacion_mes`.
    """
    año, mes = fecha_actualizacion()
    if mes == 12:
        año += 1
        mes = 1
    else:
        mes += 1

    data = {"ultima_actualizacion_anio": año, "ultima_actualizacion_mes": mes}
    with open("actualizacion.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"🔄 Fecha actualizada a: {año}-{mes}")

def ver_anio():
    año, mes = fecha_actualizacion()
    return año

def ver_mes():
    año, mes = fecha_actualizacion()
    return mes

# if __name__ == "__main__":
#     # Ejemplos de uso (solo cuando se ejecuta el script directamente)
#     print("📅 Fecha de última actualización:", fecha_actualizacion())
#     for _ in range(12):
#         sumar_meses()
#         print("📅 Nueva fecha de actualización:", fecha_actualizacion())