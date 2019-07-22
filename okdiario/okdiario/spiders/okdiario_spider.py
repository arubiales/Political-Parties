# -*- coding: utf-8 -*-
import scrapy


class OkdiarioSpiderSpider(scrapy.Spider):
    name = 'okdiario_spider'
    allowed_domains = ['https://okdiario.com/']
    start_urls = ['http://https://okdiario.com//']

    def parse(self, response):
        pass
