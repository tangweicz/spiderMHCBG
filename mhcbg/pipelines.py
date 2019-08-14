# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import scrapy, logging

from scrapy.pipelines.images import ImagesPipeline

class mhcbgImgDownloadPipeline(ImagesPipeline):

    logger = logging.getLogger()

    def get_media_requests(self, item, info):

        img_url = item["image_urls"]

        for url in img_url:

            yield scrapy.Request(url)

    def item_completed(self, results, item, info):

        self.logger.info(results)




