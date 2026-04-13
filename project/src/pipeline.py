import requests
import json
import os 

carpeta_actual = os.path.dirname(os.path.abspath(__file__))


def query_dataset(dataset_id):#esto obtiene el nombre del archivo de query a partir de su id
    with open(f"{carpeta_actual}/ids.json" ,"r") as ids:
        archivo = json.load(ids)
        dataset_file = archivo[f"{dataset_id}"]
        print(f"Dataset ID {dataset_id} corresponde a {dataset_file}")
    with open(f"{os.path.dirname(os.path.dirname(__file__))}\\datasets_query\\{dataset_file}", "r") as query_file:
        query = query_file.read()
        print(f"Query para dataset ID {dataset_id}:\n{query}")
if __name__ == "__main__":
    query_dataset(1)
    query_dataset(2)