# -*- coding: utf-8 -*-
import scrapy


class ElperiodicoSpiderSpider(scrapy.Spider):
    name = 'elperiodico_spider'
    allowed_domains = ['https://www.elperiodico.com/es/global/']
    start_urls = ['http://https://www.elperiodico.com/es/global//']

    def parse(self, response):
        pass
