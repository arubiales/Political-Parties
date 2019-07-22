# -*- coding: utf-8 -*-
import scrapy


class PublicoSpiderSpider(scrapy.Spider):
    name = 'publico_spider'
    allowed_domains = ['https://www.publico.es/']
    start_urls = ['http://https://www.publico.es//']

    def parse(self, response):
        pass
