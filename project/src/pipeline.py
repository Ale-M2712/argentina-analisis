import requests
import json
import os 

carpeta_actual = os.path.dirname(os.path.abspath(__file__))

header = {
    "Authorization": "40d2c302-66ad-4671-a15f-73acc27ef763",
    "Content-Type": "application/json",
    "Accept": "text/csv"
}


def query_dataset(dataset_id):#esto obtiene el nombre del archivo de query a partir de su id
    with open(f"{carpeta_actual}/ids.json" ,"r") as ids:
        archivo = json.load(ids)
        dataset_file = archivo[f"{dataset_id}"]
        #print(f"Dataset ID {dataset_id} corresponde a {dataset_file}") #prueba
    with open(f"{os.path.dirname(os.path.dirname(__file__))}\\datasets_query\\{dataset_file}", "r") as query_file:
        query = query_file.read()

    return query
        #print(f"Query para dataset ID {dataset_id}:\n{query}") #prueba

def make_query(id ,year ,month):#levanta el payload de para la consulta en la fecha dada
    querytext = query_dataset(id)
    url = json.loads(querytext)["url"]
    title = json.loads(querytext)["title"]
    columns = json.loads(querytext)["columns"]
    filtro = json.loads(querytext)["filtros"][0]
    filtro_usado = json.loads(querytext)["filtros"][1]
    def filtrador (filtro_usado):
        if filtro_usado == "month":
            return month
        else:
            return year
    
    payload = {"title": title,
        "ejercicios":[year],
        "columns": columns,
        "filters":[
            {
            "column": f"{filtro}",
            "operator": "equal",
            "value": f"{filtrador(filtro_usado)}"
            }
]
    }
    return url ,payload

def execute_query(url ,payload ,headers):
    response =requests.post(url, json=payload, headers=headers)
    with open(f"{os.path.dirname(os.path.dirname(__file__))}\\data\\{payload.get('title')}.csv", "wb") as f: # Guardar el contenido en un archivo CSV
        f.write(response.content)
    return response



if __name__ == "__main__":
    print(query_dataset(3))
    execute_query(*make_query(3,2023,5), header)
