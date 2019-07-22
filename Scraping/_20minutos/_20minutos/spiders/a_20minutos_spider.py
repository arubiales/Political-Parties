# -*- coding: utf-8 -*-
from scrapy import Spider, Request
import os
from datetime import datetime
import re


class A20minutosSpiderSpider(Spider):
    name = '_20minutos_spider'
    allowed_domains = ['20minutos.es']
    start_urls = ['https://www.20minutos.es']

    def parse(self, response):
        dir_name = re.sub('\s', '_', str(datetime.today())[0:19]) #el directorio que se va a crear, ponemos nombre
        data_dir = '/'.join(str(os.getcwd()).split('/')[:-2]) #el directorio en el que queremos crear el nuevo directorio
        complete_data_dir = data_dir + dir_name #sumamos
        if not os.path.exists(complete_data_dir): #Creamos el directorio
            os.makedirs(complete_data_dir)
        filename = response.url + '.html' #creamos el archivo html
        with open(complete_data_dir + filename, 'wb') as f: #Guardamos la página principal
            f.write(response.body)
        url_list =  response.xpath('//a[@class="title"]/@href').extract() #extraemos todas las urls de la página principal
        stop_word_list = ['videos', 'blogs_opinion'] #añadimos cosas que no queremos que aparezcan en la url
        clean_urls_toscrape = [url for url in url_list if not any(word in url for word in stop_word_list)]
        [(yield Request(url, callback=self.save_function)) for url in clean_urls_toscrape] #vamos guardadon todas las url
        #en teoría no debería de scrapear los dominios que no sean 20minutos.es


    def save_function(self, web):
        filename = web.url + '.html'
        with open(self.complete_data_dir + filename, 'wb') as f:
            f.write(web.body)

#todo la fase de scrappeo está acabada, hay que testearla para ver los errores y después copiarlo para el resto de páginas. Te falta hacer el script de linux que arranque el ordenador y le ordene hacer todas estas tareas una vez tengas esto hecho. ya al menos tienes la información en carpetas
#todo Para programar el encendido, ejecución de un programa y apagado, usamos cron. TIENES EN EL ÚLTIMO TEMA DEL CURSO UDEMY y hay árticulos web