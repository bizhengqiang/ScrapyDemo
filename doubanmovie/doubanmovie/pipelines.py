# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from doubanmovie.items import DoubanmovieItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy
import os
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        return item

class DoubanMoviePoster(ImagesPipeline):
    '''

    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    '''
    def get_media_requests(self, item, info):
        for imgUrl in item['image_urls']:
            # print(imgUrl)
            yield scrapy.Request(imgUrl, meta={'name': item['movie_name']})

    def file_path(self, request, response=None, info=None):
        imgName = u"./"+request.meta['name'].split('/')[0]+'.jpg'
        return imgName
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

