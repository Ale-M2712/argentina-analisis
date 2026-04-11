from sqlalchemy import create_engine, text
import pandas as pd

# Reemplazá con tus datos reales
usuario = "postgres"
clave = "Laput4madre"
host = "localhost"
puerto = "5432"
base = "Arg_Fiscal"

# Armá el string de conexión
url = f"postgresql+psycopg2://{usuario}:{clave}@{host}:{puerto}/{base}"
engine = create_engine(url)

def comprobar_conexion(): #verificar conexion a la db
  try:
    with engine.connect() as connection:
      # SQLAlchemy 2.0 requires an executable object (use text())
      result = connection.execute(text("SELECT 1"))
      # opcional: validar el valor retornado
      _ = result.scalar()
      print("Conexión exitosa a la base de datos.")
  except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
        
def comprobar_tabla(tabla): #verificar si la tabla existe en la db
  """Verifica si existe una tabla en la base de datos.

  Por compatibilidad con los CREATE en este fichero, también prueba con el
  prefijo 'tabla_' (p.ej. 'credito' -> 'tabla_credito').
  """
  try:
    with engine.connect() as connection:
      # Primero probamos el nombre tal cual
      result = connection.execute(text("SELECT to_regclass(:tabla)"), {"tabla": tabla})
      if result.scalar() is not None:
        print(f"La tabla '{tabla}' existe en la base de datos.")
        return True

      # Si no existe, probar con el prefijo 'tabla_' (ej. 'credito' -> 'tabla_credito')
      prefixed = f"tabla_{tabla}"
      result2 = connection.execute(text("SELECT to_regclass(:tabla)"), {"tabla": prefixed})
      if result2.scalar() is not None:
        print(f"La tabla '{prefixed}' existe en la base de datos (resuelta desde '{tabla}').")
        return True

      # Fallback: no encontrada
      print(f"La tabla '{tabla}' NO existe en la base de datos (ni '{prefixed}').")
      return False
  except Exception as e:
    print(f"Error al verificar la tabla '{tabla}': {e}")
    return False

def guardar_datos(df, tabla): #guardar datos en la db
    try:
        df.to_sql(tabla, engine, if_exists='append', index=False)
        print(f"Datos guardados en la tabla '{tabla}' exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos en la tabla '{tabla}': {e}")

def borrar_tabla(tabla): #borrar tabla de la db
  try:
    with engine.connect() as connection:
      # table name can't be parameterized easily; ensure caller passes a safe table name
      connection.execute(text(f"DROP TABLE IF EXISTS {tabla}"))
      print(f"Tabla '{tabla}' borrada exitosamente.")
  except Exception as e:
    print(f"Error al borrar la tabla '{tabla}': {e}")
def selector_tabla(tabla):
    if tabla == "credito":
        return crear_tabla_credito
    elif tabla == "recurso":
        return crear_tabla_recurso
    elif tabla == "pef":
        return crear_tabla_pef
    elif tabla == "transversal_financiero":
        return crear_tabla_transversal
    else:
        raise ValueError(f"Tabla desconocida: {tabla}")
crear_tabla_credito = """CREATE TABLE tabla_credito (
  impacto_presupuestario_anio INTEGER,
  impacto_presupuestario_mes INTEGER,
  ejercicio_presupuestario INTEGER,
  sector_id INTEGER,
  sector_desc TEXT,
  subsector_id INTEGER,
  subsector_desc TEXT,
  caracter_id INTEGER,
  caracter_desc TEXT,
  jurisdiccion_id INTEGER,
  jurisdiccion_desc TEXT,
  subjurisdiccion_id INTEGER,
  subjurisdiccion_desc TEXT,
  entidad_id INTEGER,
  entidad_desc TEXT,
  servicio_id INTEGER,
  servicio_desc TEXT,
  programa_id INTEGER,
  programa_desc TEXT,
  subprograma_id INTEGER,
  subprograma_desc TEXT,
  proyecto_id INTEGER,
  proyecto_desc TEXT,
  actividad_id INTEGER,
  actividad_desc TEXT,
  obra_id INTEGER,
  obra_desc TEXT,
  finalidad_id INTEGER,
  finalidad_desc TEXT,
  funcion_id INTEGER,
  funcion_desc TEXT,
  inciso_id INTEGER,
  inciso_desc TEXT,
  principal_id INTEGER,
  principal_desc TEXT,
  parcial_id INTEGER,
  parcial_desc TEXT,
  subparcial_id INTEGER,
  subparcial_desc TEXT,
  clasificador_economico_8_digitos_id INTEGER,
  clasificador_economico_8_digitos_desc TEXT,
  fuente_financiamiento_id TEXT,
  fuente_financiamiento_id_desc TEXT,
  ubicacion_geografica_id INTEGER,
  ubicacion_geografica_desc TEXT,
  unidad_ejecutora_id INTEGER,
  unidad_ejecutora_desc TEXT,
  prestamo_externo_id INTEGER,
  prestamo_externo_desc TEXT,
  codigo_bapin_id INTEGER,
  codigo_bapin_desc TEXT,
  credito_presupuestado NUMERIC(18,2),
  credito_vigente NUMERIC(18,2),
  credito_comprometido NUMERIC(18,2),
  credito_devengado NUMERIC(18,2),
  credito_pagado NUMERIC(18,2),
  ultima_actualizacion_fecha TEXT
);
ALTER TABLE tabla_credito
 ADD CONSTRAINT pk_credito PRIMARY KEY (
 impacto_presupuestario_anio, 
 impacto_presupuestario_mes, 
 ejercicio_presupuestario, 
 sector_id);"""
crear_tabla_recurso = """CREATE TABLE tabla_recurso (
  impacto_presupuestario_anio INTEGER,
  impacto_presupuestario_mes INTEGER,
  ejercicio_presupuestario INTEGER,
  sector_id INTEGER,
  sector_desc TEXT,
  subsector_id INTEGER,
  subsector_desc TEXT,
  caracter_id INTEGER,
  caracter_desc TEXT,
  jurisdiccion_id INTEGER,
  jurisdiccion_desc TEXT,
  subjurisdiccion_id INTEGER,
  subjurisdiccion_desc TEXT,
  entidad_id INTEGER,
  entidad_desc TEXT,
  servicio_id INTEGER,
  servicio_desc TEXT,
  tipo_id INTEGER,
  tipo_desc TEXT,
  clase_id INTEGER,
  clase_desc TEXT,
  concepto_id INTEGER,
  concepto_desc TEXT,
  subconcepto_id INTEGER,
  subconcepto_desc TEXT,
  fuente_financiamiento_id TEXT,
  fuente_financiamiento_id_desc TEXT,
  clasificador_economico_8_digitos_id INTEGER,
  clasificador_economico_8_digitos_desc TEXT,
  prestamo_externo_id INTEGER,
  prestamo_externo_desc TEXT,
  recurso_inicial NUMERIC(18,2),
  recurso_vigente NUMERIC(18,2),
  recurso_ingresado_percibido NUMERIC(18,2),
  ultima_actualizacion_fecha TEXT
);
ALTER TABLE tabla_recurso
 ADD CONSTRAINT pk_recurso PRIMARY KEY (
   ejercicio_presupuestario,
   impacto_presupuestario_anio,
   impacto_presupuestario_mes,
   jurisdiccion_id,
   tipo_id,
   concepto_id
);"""
crear_tabla_pef = """CREATE TABLE tabla_pef (
  trimestre INTEGER,
  finalidad_id INTEGER,
  finalidad_desc TEXT,
  funcion_id INTEGER,
  funcion_desc TEXT,
  sector_id INTEGER,
  sector_desc TEXT,
  subsector_id INTEGER,
  subsector_desc TEXT,
  caracter_id INTEGER,
  caracter_desc TEXT,
  jurisdiccion_id INTEGER,
  jurisdiccion_desc TEXT,
  subjurisdiccion_id INTEGER,
  subjurisdiccion_desc TEXT,
  entidad_id INTEGER,
  entidad_desc TEXT,
  servicio_id INTEGER,
  servicio_desc TEXT,
  programa_id INTEGER,
  programa_desc TEXT,
  subprograma_id INTEGER,
  subprograma_desc TEXT,
  proyecto_id INTEGER,
  proyecto_desc TEXT,
  actividad_id INTEGER,
  actividad_desc TEXT,
  obra_id INTEGER,
  obra_desc TEXT,
  medicion_fisica_id INTEGER,
  medicion_fisica_desc TEXT,
  tipo_medicion_fisica TEXT,
  unidad_medida_id TEXT,
  unidad_medida_desc TEXT,
  ubicacion_geografica_id INTEGER,
  ubicacion_geografica_desc TEXT,
  totalizador_avance_fisico TEXT,
  programacion_inicial_DA INTEGER,
  programación_inicial_ajustada INTEGER,
  programacion_anual_vig_cierre INTEGER,
  programacion_anual_vig_trim INTEGER,
  programacion_trim NUMERIC(18,2),
  programacion_acumulada_trim INTEGER,
  ejecutado_vigente_trim INTEGER,
  ejecutado_acumulado_trim INTEGER,
  ejecutado_cierre_acum_trim INTEGER,
  ejecucion_anual_de_cierre NUMERIC(18,2),
  tipo_causa_desvio TEXT,
  causa_desvio TEXT,
  causa_desvio_detalle TEXT,
  causa_desvio_comentario TEXT,
  porc_desvio_acum_trim NUMERIC(5,2),
  ultima_actualizacion_fecha TEXT
);
ALTER TABLE tabla_pef
ADD CONSTRAINT pk_pef PRIMARY KEY (
  trimestre,
  jurisdiccion_id,
  programa_id,
  medicion_fisica_id
 );"""
crear_tabla_transversal = """CREATE TABLE tabla_transversal_financiero (
  ejercicio_presupuestario INTEGER,
  sector_id INTEGER,
  sector_desc TEXT,
  subsector_id INTEGER,
  subsector_desc TEXT,
  caracter_id INTEGER,
  caracter_desc TEXT,
  jurisdiccion_id INTEGER,
  jurisdiccion_desc TEXT,
  subjurisdiccion_id INTEGER,
  subjurisdiccion_desc TEXT,
  entidad_id INTEGER,
  entidad_desc TEXT,
  servicio_id INTEGER,
  servicio_desc TEXT,
  programa_id INTEGER,
  programa_desc TEXT,
  subprograma_id INTEGER,
  subprograma_desc TEXT,
  proyecto_id INTEGER,
  proyecto_desc TEXT,
  actividad_id INTEGER,
  actividad_desc TEXT,
  obra_id INTEGER,
  obra_desc TEXT,
  finalidad_id INTEGER,
  finalidad_desc TEXT,
  funcion_id INTEGER,
  funcion_desc TEXT,
  fuente_financiamiento_id TEXT,
  fuente_financiamiento_desc TEXT,
  ubicacion_geografica_id INTEGER,
  ubicacion_geografica_desc TEXT,
  inciso_id INTEGER,
  inciso_desc TEXT,
  principal_id INTEGER,
  principal_desc TEXT,
  parcial_id INTEGER,
  parcial_desc TEXT,
  subparcial_id INTEGER,
  subparcial_desc TEXT,
  etiqueta_id TEXT,
  etiqueta_desc TEXT,
  ponderacion_credito NUMERIC(18,6),
  codigo_bapin_id INTEGER,
  codigo_bapin_desc TEXT,
  credito_inicial NUMERIC(18,2),
  credito_inicial_ponderado NUMERIC(18,2),
  credito_vigente NUMERIC(18,2),
  credito_vigente_ponderado NUMERIC(18,2),
  credito_ejecutado NUMERIC(18,2),
  credito_ejecutado_ponderado NUMERIC(18,2)
);
ALTER TABLE tabla_transversal_financiero
ADD CONSTRAINT pk_transversal_financiero PRIMARY KEY (
  jurisdiccion_id,
  programa_id,
  etiqueta_id
);"""
def crear_tabla(nombre_tabla):
    try:
        with engine.begin() as connection:
            connection.execute(text(selector_tabla(nombre_tabla)))
            print(f"Tabla '{nombre_tabla}' creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla '{nombre_tabla}': {e}")


# Ejemplo de uso
#crear_tabla("credito")