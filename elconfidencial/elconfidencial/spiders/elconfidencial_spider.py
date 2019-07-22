# -*- coding: utf-8 -*-
import scrapy


class ElconfidencialSpiderSpider(scrapy.Spider):
    name = 'elconfidencial_spider'
    allowed_domains = ['https://www.elconfidencial.com/']
    start_urls = ['http://https://www.elconfidencial.com//']

    def parse(self, response):
        pass
