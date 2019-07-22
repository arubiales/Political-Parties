# -*- coding: utf-8 -*-
import scrapy


class ElMundoSpiderSpider(scrapy.Spider):
    name = 'el_mundo_spider'
    allowed_domains = ['https://www.elmundo.es/']
    start_urls = ['http://https://www.elmundo.es//']

    def parse(self, response):
        pass
