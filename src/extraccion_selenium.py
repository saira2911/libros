from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select

from time import sleep
from datetime import datetime

def extraer ():

    # Inicializar Chrome 
    driver = webdriver.Chrome()

    url = "https://www.goodreads.com/"
    driver.get(url)

    # Maximizar
    driver.maximize_window()

    sleep(5)

    lista_libros = []
    # Iterar por genero
    for genero in range(2, 17): # 2 a 17# hay 14 generos
        # entrar en la lista de cada genero
        driver.find_element("css selector", f"#choiceAwardCategories > div.gr-listOfLinks.u-defaultType > li:nth-child({genero}) > a").click()
                                             
        sleep(2)

        # Iterar por libro de la lista
        for i in range(3, 10): #3 a 23# en casi todas las listas hay 20 libros

            diccionario = {}
            # Cerrar ventana inicio sesion
            try: 
                driver.find_element("css selector", "#gca2023 > div:nth-child(4) > div > div > div.modal__close > button > img").click()

            except:
                pass
          
            sleep(2)
            # Toma el genero del titulo de la lista
            diccionario['genero'] = driver.find_element("css selector", "#choiceBody > div.gcaRightContainer > div:nth-child(2) > div.gcaMastheader.u-marginLeftMedium").text.replace("Best", "")
    
            # Hacer clic en el libro
            try:
                driver.find_element("css selector", f"#poll_2788{60+genero+1} > div.pollContents > div:nth-child({i}) > div.answerWrapper").click()
            except:
                continue
         
            sleep(2)
            
            # Extraer información del libro y agregarla al diccionario
            try:
                diccionario['titulo'] = driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageTitleSection > div.BookPageTitleSection__title > h1").text
            except:
                diccionario['titulo'] = 'No disponible'
            try:
                diccionario['autor'] = driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__contributor > h3 > div > span:nth-child(1) > a > span.ContributorLink__name").text
            except:
                diccionario['autor'] = 'No disponible'
            try:                
                diccionario['precio'] = driver.find_element("css selector", '#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__leftColumn > div > div.BookActions > div:nth-child(2) > div > div.Button__container.Button__container--block > button > span:nth-child(1)').text
            except:
                diccionario['precio'] = 'No disponible'
            try:                   
                diccionario['puntuacion'] = driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookPageMetadataSection__ratingStats > a > div:nth-child(1) > div").text
            except:
                diccionario['puntuacion'] = 'No disponible'

            # Fecha: hay que limpiar el texto y formatear
            try:
                publicacion = driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookDetails > div > span:nth-child(1) > span > div > p:nth-child(2)").text.split()
                del publicacion[0:2]
                fecha = " ".join(publicacion)
                fecha_datetime = datetime.strptime(fecha, '%B %d, %Y')
                fecha_formateada = fecha_datetime.strftime('%d/%m/%Y')
                diccionario['fecha_publicacion'] = fecha_formateada
            except:
                diccionario['fecha_publicacion'] = 'No disponible'

            # Numero de paginas y tipo de tapa salen del mismo texto
            try:
                texto = driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookDetails > div > span:nth-child(1) > span > div > p:nth-child(1)").text
                lista_texto = texto.split(",")
                
                diccionario['n_paginas'] = lista_texto[0].split()[0]
                diccionario['tapa'] = lista_texto[1].strip()
            except:
                diccionario['n_paginas'] = 'No disponible'
                diccionario['tapa'] = 'No disponible'

            # Premios es un array y esta dentro de un apartado donde hay que clicar
            try:    
                try:
                    driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookDetails > div > div > button > span:nth-child(1)").click()
                except: 
                    driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookDetails > div > div > button").click()

                diccionario['premios'] = driver.find_element("css selector", "#__next > div.PageFrame.PageFrame--siteHeaderBanner > main > div.BookPage__gridContainer > div.BookPage__rightColumn > div.BookPage__mainContent > div.BookPageMetadataSection > div.BookDetails > div > span:nth-child(2) > span > div > div:nth-child(1) > dd > div").text.split(",")
            except:
                diccionario['premios'] = 'No disponible'
                                                                    
            driver.back()
            # Añadimos el diccionario a la lista total
            lista_libros.append(diccionario)

        driver.back()

    

    return lista_libros

