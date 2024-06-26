from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv
from dateutil import parser


expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)

load_dotenv()
atlas = os.getenv("ATLAS_URI")
conexion = MongoClient(atlas)

def insert_data (ruta, database, collection):
    with open(ruta) as j:
        json_import_data = json.load(j)

    conexion[database][collection].insert_many(json_import_data)

    print(list(conexion[database][collection].find()))
    return