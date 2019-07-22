# -*- coding: utf-8 -*-
import scrapy


class EldiarioSpiderSpider(scrapy.Spider):
    name = 'eldiario_spider'
    allowed_domains = ['https://www.eldiario.es/']
    start_urls = ['http://https://www.eldiario.es//']

    def parse(self, response):
        pass
