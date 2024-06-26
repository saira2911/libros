import json

def transformacion_guardado (lista, ruta):
    for i, e in enumerate(lista):
        e['genero'] = e['genero'].strip()
        try:
            e['precio'] = float(e['precio'].replace('Kindle $', ''))
        except:
            pass
        e['puntuacion'] = float(e['puntuacion'])
        e['n_paginas'] = int(e['n_paginas'])
     
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
    return

