from pymongo import MongoClient
import json
import os
from dateutil import parser
expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
from dotenv import load_dotenv

load_dotenv()
atlas = os.getenv("ATLAS_URI")
conexion = MongoClient(atlas)

def insert_data (path_json, database, collection):
    with open(path_json) as j:
        json_import_data = json.load(j)

    conexion[database][collection].insert_many(json_import_data)

def find_data (database, collection, filter = {}, limit= 0):

    return list(conexion[database][collection].find(filter).limit(limit))


# data = find_data('proyecto_libros', 'libros', {'genero': 'Fiction'}, 5)
# lista = [e['titulo'] for e in data]
# print(lista)