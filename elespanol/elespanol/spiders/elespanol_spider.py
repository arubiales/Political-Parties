# -*- coding: utf-8 -*-
import scrapy


class ElespanolSpiderSpider(scrapy.Spider):
    name = 'elespanol_spider'
    allowed_domains = ['https://www.elespanol.com/']
    start_urls = ['http://https://www.elespanol.com//']

    def parse(self, response):
        pass
