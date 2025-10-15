from sqlalchemy import create_engine
import pandas as pd
import interaccion_db
import interaccion_APIs


# Reemplazá con tus datos reales
usuario = "postgres"
clave = "Ale271202"
host = "localhost"
puerto = "5432"
base = "Arg_Fiscal"

# Armá el string de conexión
url = f"postgresql+psycopg2://{usuario}:{clave}@{host}:{puerto}/{base}"
engine = create_engine(url)
df = pd.read_csv("Clasificador presupuestario Apertura Programática.csv")
interaccion_db.guardar_datos(df,'Clasificador presupuestario Apertura Programática')
