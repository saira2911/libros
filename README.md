# ETL de Datos con Interfaz en Telegram

## INDICE
1. [Introducción](#1-introducción)
2. [Requisitos](#2-requisitos)
3. [Librerias](#3-librerias)
4. [Instalacion](#4-instalacion)
5. [Uso](#5-uso)
6. [Estructura](#6-estructura)
7. [Aportaciones](#7-aportaciones)

# 1. 👋 Introduccion 

¡Bienvenidos al proyecto! Este proyecto se centra en la extracción, transformación y carga de datos utilizando técnicas de web scraping y MongoDB. Además, hemos desarrollado una interfaz de consulta a través de un bot de Telegram para facilitar el acceso a los datos.

# 2. ✅ Requisitos

Python 3.x
MongoDB
Cuenta en Telegram y un bot creado (obtener token desde @BotFather)

# 3. 📚 Librerías de Python

Estan agrupadas en el archivo requirements.txt
Puedes instalar todas las dependencias usando el siguiente comando:

```
pip install -r requirements.txt
```

# 4. 🔧 Instalación

## Clona el repositorio:
```
git clone https://github.com/saira2911/libros.git
cd libros
```

## Configura MongoDB:
- Asegúrate de tener MongoDB instalado y corriendo en tu máquina, o puedes usar Atlas.
- Crea un archivo .env dentro de src y configura las credenciales de conexión: ATLAS_URI='tu_uri'
- Crea la base de datos y la coleccion donde quieras guardar los datos

## Configura el bot de Telegram:
- Crea un bot en Telegram a través de @BotFather y obtén el token.
- Añade el token del bot en el archivo .env creado antes: TELEGRAM_TOKEN = 'tu_token'

## Ejecuta los scripts de extracción, transformación y carga:
```
python etl.py
```

## Inicia el bot de Telegram:
```
python bot.py
```


# 5. 👀 Uso

- Una vez que el bot esté en funcionamiento, puedes interactuar con él a través de Telegram.
- Los comandos disponibles te permitirán realizar consultas sobre los datos almacenados en MongoDB.

# 6. 🧩 Estructura del Proyecto

```

├── README.md
├── requirements.txt
├── etl.py
├── bot.py
├── files
│   └── librosv1.json
└── src
    ├── extraccion_selenium.py
    ├── transformacion.py
    └── carga.py
```


etl.py: Script principal para la extracción, transformación y carga de datos.
bot.py: Script para iniciar el bot de Telegram.
src/: Contiene los módulos para scraping, transformación y carga de datos.
files/: Directorio para almacenar datos en bruto y procesados.

# 7. ⭐ Aportaciones 

Por favor, siéntete libre de utilizar e inspirarte en este repositorio o de sugerir mejoras. ¡Muchas gracias! 😄
