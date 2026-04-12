import requests
import json
import os 

carpeta_actual = os.path.dirname(os.path.abspath(__file__))


def query_dataset(dataset_id):
    with open(f"{carpeta_actual}/ids.json" ,"r") as ids:
        archivo = json.load(ids)
        dataset_file = archivo[f"{dataset_id}"]
        print(f"Dataset ID {dataset_id} corresponde a {dataset_file}")

if __name__ == "__main__":
    query_dataset(1)
    query_dataset(2)