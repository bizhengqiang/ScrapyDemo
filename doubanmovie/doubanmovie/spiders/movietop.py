# -*- coding: utf-8 -*-
# @Time    :2019/3/5 11:13
# @Author  :miracle
# @Filename:movietop.py
# @Software:PyCharm
import scrapy
from doubanmovie import items
class MovieSpider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://movie.douban.com/top250']
    def parse(self,response):
        item = items.DoubanmovieItem()
        # 用xpath选择器来获取
        for movieInfoList in response.xpath("//ol[@class = 'grid_view']/li"):
            # print(movieInfoList)
            movieNames =''
            for movieName in movieInfoList.xpath(".//span[@class ='title']/text()").extract():
                movieNames = movieNames+movieName
            item['movie_name'] = movieNames
            movie_poster = movieInfoList.xpath(".//img/@src").extract_first()
            item['image_urls'] = [movie_poster]
            yield item
        next_pageid = response.xpath("//span[@class='next']/a/@href").extract_first()
        print(next_pageid)
        if next_pageid is not None:
            nextPageUrl = 'https://movie.douban.com/top250{}'.format(next_pageid)
            print(nextPageUrl)
            yield scrapy.Request(nextPageUrl, callback=self.parse)










