# -*- coding: utf-8 -*-
import scrapy


class ElmundoSpiderSpider(scrapy.Spider):
    name = 'elmundo_spider'
    allowed_domains = ['https://www.elmundo.es/']
    start_urls = ['http://https://www.elmundo.es//']

    def parse(self, response):
        pass
