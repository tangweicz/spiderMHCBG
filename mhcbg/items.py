# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.pipelines.images import ImagesPipeline


class MhcbgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class mhCbgImageItem(scrapy.Item):
#
#     image_urls = scrapy.Field()
#
#     images = scrapy.Field()

class mhCbgAccountItem(scrapy.Item):

    basicPrice = scrapy.Field()#账号基础价格

    serverId = scrapy.Field()#服务器ID号

    accountId = scrapy.Field()#账号ID号

    shenqiPrice = scrapy.Field()#神器价格

    salePrice = scrapy.Field()#账号号主售价

    xiangruiPrice = scrapy.Field()#祥瑞价格

    beforeSummonNum = scrapy.Field()#请求处理召唤兽之前的数量

    qiangzhuangshensuPrice = scrapy.Field()#强壮神速价格

    summonPriceAndDetail = scrapy.Field()#召唤兽价格和详细信息

    summonPrice = scrapy.Field()#召唤兽价格

    summonNum = scrapy.Field()#召唤兽数量

    jinyiPrice = scrapy.Field()

    linkAddr = scrapy.Field()#最终的账号连接地址