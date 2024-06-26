from src.extraccion_selenium import extraer
from src.transformacion import transformacion_guardado
from src.carga import insert_data

ruta = 'files/libros.json'

lista_libros = extraer()
transformacion_guardado(lista_libros, ruta)
insert_data(ruta, 'proyecto_libros', 'libros')




