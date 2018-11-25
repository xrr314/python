# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Images360Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from scrapy import Item,Field
class ImageItem(Item):
    # 设置保存的数据库中的表名
    collection = table = 'images'
    id = Field()
    url =Field()
    title = Field()
    thumb = Field()