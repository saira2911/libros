from src.extraccion_selenium import extraer
from src.transformacion import transformacion_guardado
from src.carga import insert_data
import json

ruta_bruto = 'files/libros_original.json'
ruta_transformados = 'files/libros.json'

lista_libros = extraer()

with open(ruta_bruto, 'w', encoding='utf-8') as f:
    json.dump(lista_libros, f, ensure_ascii=False, indent=4)

transformacion_guardado(lista_libros, ruta_transformados)
insert_data(ruta_transformados, 'proyecto_libros', 'libros')




