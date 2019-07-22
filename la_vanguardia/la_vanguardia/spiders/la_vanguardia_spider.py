# -*- coding: utf-8 -*-
import scrapy


class LaVanguardiaSpiderSpider(scrapy.Spider):
    name = 'la_vanguardia_spider'
    allowed_domains = ['https://www.lavanguardia.com/']
    start_urls = ['http://https://www.lavanguardia.com//']

    def parse(self, response):
        pass
