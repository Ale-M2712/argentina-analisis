import os
import json
from datetime import datetime

def fecha_actualizacion():
    ruta = "actualizacion.json"
    # Si el archivo no existe, lo crea con una fecha inicial
    if not os.path.exists(ruta):
        fecha_inicial = 1995
        mes_inicial = 1
        data = {"ultima_actualizacion_fecha": fecha_inicial}
        with open(ruta, "w") as f:
            json.dump(data, f, indent=4)
        print(f"🆕 Archivo creado con fecha: {fecha_inicial}")
        return fecha_inicial

    # Si existe, lo lee normalmente
    with open(ruta, "r") as f:
        data = json.load(f)
        return data["ultima_actualizacion_fecha"]

# Ejemplo de uso
print("📅 Fecha de última actualización:", fecha_actualizacion())

#funciona pero algo no me convence , deveria usar el mes tmb
