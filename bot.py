import telebot
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import mongo_functions

load_dotenv()
token = os.getenv("TELEGRAM_TOKEN")
atlas = os.getenv("ATLAS_URI")
bot = telebot.TeleBot(token)

stringList = {1: "Libros", 2: "Autores", 3: "Genero"}
chat = {}

@bot.message_handler(commands=['start', 'help']) #cada vez que al bot le llegue el comando start o help activara esta funcion
def mensaje_bienvenida(message):
    markup = telebot.types.InlineKeyboardMarkup()
    for key, value in stringList.items():
        markup.add(telebot.types.InlineKeyboardButton(text=value,
                                          callback_data= value))

    bot.send_message(message.chat.id, "Hola, ¿en que puedo ayudarte?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def respuesta_uno(callback):
    opcion = callback.data
    chat['opcion']=opcion
    if opcion == 'Libros':
        bot.send_message(callback.message.chat.id, 'Escribe el nombre del libro que quieres buscar')
    elif opcion == 'Autores':
        bot.send_message(callback.message.chat.id, 'Escribe el nombre del autor que quieres buscar')
    else:
        bot.send_message(callback.message.chat.id, 'Escribe el genero que quieres buscar')

@bot.message_handler(content_types='text')
def respuesta_dos(message):

    conexion = MongoClient(atlas)
    
    if chat['opcion'] == 'Libros':
        mensaje_total = ''
        data= mongo_functions.find_data('proyecto_libros', 'libros', {'titulo': message.text})
        for k,v in data[0].items():
            if k !=  '_id':
                mensaje = f"{k.title()}: {v}\n"
                mensaje_total = mensaje_total + mensaje
        bot.send_message(message.chat.id, f"Los datos que tengo de {message.text} son:\n{mensaje_total}")

    elif chat['opcion'] == 'Autores':
        data= mongo_functions.find_data('proyecto_libros', 'libros', {'autor': message.text})
        lista = [e['titulo'] for e in data]

        if len(lista) == 1:
            bot.send_message(message.chat.id, f"El único libro que tengo de {message.text} es:\n{lista[0]}")

        else:
            bot.send_message(message.chat.id, f"Los libros que tengo de {message.text} son:\n{lista}")

    else:
        data= mongo_functions.find_data('proyecto_libros', 'libros', {'genero': message.text.title()})
        lista = [e['titulo'] for e in data]

        if len(lista) == 1:
            bot.send_message(message.chat.id, f"El único libro que tengo de {message.text.title()} es:\n{lista[0]}")

        else:
            bot.send_message(message.chat.id, f"Los libros que tengo de {message.text.title()} son:\n{lista}")

bot.polling()

