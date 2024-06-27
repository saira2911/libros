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

    """
    Esta funcion inserta datos en una coleccion dada de mongoDB.

    Args:
    ruta: ruta donde se encuentra el archivo (json) que vamos a insertar.
    database: la BBDD donde se encuentra la coleccion
    collection: la coleccion donde queremos insertar los datos

    Returns:
    Imprime el contenido de la coleccion
    """

    with open(ruta) as j:
        json_import_data = json.load(j)

    conexion[database][collection].insert_many(json_import_data)

    return print(list(conexion[database][collection].find()))