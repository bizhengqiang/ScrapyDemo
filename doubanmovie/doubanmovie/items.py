# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()     # 电影名
    image_urls = scrapy.Field()     # 海报路径
    images = scrapy.Field()         # 图片
    image_paths = scrapy.Field()    # 图片保存路径
