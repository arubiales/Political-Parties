# -*- coding: utf-8 -*-
from scrapy import Spider, Request


class ElPaisSpiderSpider(Spider):
    name = 'el_pais_spider'
    allowed_domains = ['https://elpais.com/']
    start_urls = ['http://https://elpais.com//']

    def parse(self, response):
        pass

