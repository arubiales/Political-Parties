# -*- coding: utf-8 -*-
import scrapy


class AbcSpiderSpider(scrapy.Spider):
    name = 'abc_spider'
    allowed_domains = ['https://www.abc.es/']
    start_urls = ['http://https://www.abc.es//']

    def parse(self, response):
        pass
