# -*- coding: utf-8 -*-
import scrapy
from gsglSpider.items import GsglspiderItem

class TransportSpider(scrapy.Spider):
    name = 'transport'
    allowed_domains = ['gsgl.00cha.com']
    start_urls = ['https://gsgl.00cha.com/s_shanxi.html']

    def parse(self, response):
        node_list = response.xpath("//div[@class='sj']")

        items = []
        for node in node_list:

            item = GsglspiderItem()

            text = node.xpath("./text()").extract()

            item['text']=text[0]
            items.append(item)

        return items
