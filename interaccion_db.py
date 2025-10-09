from sqlalchemy import create_engine
import pandas as pd

# Reemplazá con tus datos reales
usuario = "postgres"
clave = "Ale271202"
host = "localhost"
puerto = "5432"
base = "Arg_Fiscal"

# Armá el string de conexión
url = f"postgresql+psycopg2://{usuario}:{clave}@{host}:{puerto}/{base}"
engine = create_engine(url)

def guardar_datos(df, tabla):
    try:
        df.to_sql(tabla, engine, if_exists='replace', index=False)
        print(f"Datos guardados en la tabla '{tabla}' exitosamente.")
    except Exception as e:
        print(f"Error al guardar los datos en la tabla '{tabla}': {e}")