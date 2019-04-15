# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import requests,json,random,threading,time,logging

from mhcbg.models.proxyIpModel import proxyIpModel

from twisted.internet.error import TCPTimedOutError, TimeoutError

# from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware


class MhcbgSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MhcbgDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):


        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest


        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)




class cbgDownloaderMiddleware(object):

    canUsedProxyIps = []

    logger = logging.getLogger()

    def process_request(self, request, spider):
        self.logger.info("---------------------------------"+request.url)

        if len(self.canUsedProxyIps) < 50:#可用代理目前不足50个

            proxyIps = proxyIpModel.getTwoHundredIp()#从数据库中取代理地址

            self.logger.info("-----------------------------------数据库中取到的代理地址列表：{}".format(proxyIps))

            if proxyIps:#数据库中有可以用的地址，那么验证每一个是否可用

                threadList = []

                self.logger.info("**********************数据库内不为空，开始去挨个验证每一个是否可用")

                for item in proxyIps:  # 循环验证

                    threadList.append(threading.Thread(target=self.runMysqlProxy, args=(item,)))

                for everyThread in threadList:
                    everyThread.start()

                for everyThread in threadList:
                    everyThread.join()

                del threadList

            else:#如果没有可用的地址

                threadList = []

                self.logger.info("**********************数据库内为空，开始去拉取代理数据")

                ipList = self.fromDailiServerGetProxyIps()

                self.logger.info("从代理上拿到的IP地址,{}".format(ipList))

                for item in ipList:  # 循环插入数据库

                    threadList.append(threading.Thread(target=self.runDailiServerProxy, args=(item,)))

                for everyThread in threadList:
                    everyThread.start()

                for everyThread in threadList:
                    everyThread.join()

                del threadList


        while len(self.canUsedProxyIps) < 50:

            threadList = []

            ipList = self.fromDailiServerGetProxyIps()

            self.logger.info("从代理上拿到的IP地址：".format(ipList))

            for item in ipList:#循环插入数据库

                threadList.append(threading.Thread(target=self.runDailiServerProxy, args=(item,)))

            for everyThread in threadList:
                everyThread.start()

            for everyThread in threadList:
                everyThread.join()

            del threadList

        randomNum = random.randint(0, len(self.canUsedProxyIps)-1)

        request.meta["proxy"] = self.canUsedProxyIps[randomNum]

        self.logger.info("####################################{}".format(self.canUsedProxyIps))

        self.logger.info("####################################{}".format(self.canUsedProxyIps[randomNum]))

        self.logger.info("+++++++++++++++++++++++++++++++++++++++++正在用"+self.canUsedProxyIps[randomNum]+"的代理去请求，"+request.url)

        return None

    def fromDailiServerGetProxyIps(self):

        # result = requests.get("http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=&city=0&yys=0&port=1&pack=34238&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=")
        #
        # result = json.loads(result.text)
        #
        # print(result)
        #
        # ipList = list()
        #
        # if type(result) == dict:
        #
        #     ipDict = result.get("data", None)
        #
        #     if ipDict != None:
        #
        #         for item in ipDict:
        #
        #             httpStr = "http://"+item["ip"]+":"+str(item["port"])
        #
        #             print(httpStr)
        #
        #             ipList.append(httpStr)
        #
        #         else:
        #
        #             print(result)
        #
        # return ipList



        result = requests.get("http://tpv.daxiangdaili.com/ip/?tid=555093498677388&num=100&delay=5&category=2&protocol=https&filter=on") #"http://tpv.daxiangdaili.com/ip/?tid=555954874838865&num=100&filter=on"

        ipList = list(map(self.addHttp, result.text.split("\r\n")))

        return ipList

    def addHttp(self, ipAddr):

        return "http://"+ipAddr

    def runTestProxy(self, proxyUrl):

        headStr = {

            'Accept': '*/*',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',

            'Accept-Encoding': 'gzip, deflate, sdch',

            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

        try:

            res = requests.get("http://www.hualongxiang.com", proxies={"http": proxyUrl}, headers=headStr, timeout=3, allow_redirects=False)

            if res.status_code != 200:

                self.canUsedProxyIps.remove(proxyUrl)

        except:

            self.canUsedProxyIps.remove(proxyUrl)

    def runMysqlProxy(self, proxyItem):

        headStr = {

            'Accept': '*/*',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',

            'Accept-Encoding': 'gzip, deflate, sdch',

            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

        try:

            res = requests.get("http://www.hualongxiang.com", proxies={"http": proxyItem.ipAddr}, headers=headStr, timeout=3, allow_redirects=False)

            if res.status_code == 200:

                if not proxyItem.ipAddr in self.canUsedProxyIps: self.canUsedProxyIps.append(proxyItem.ipAddr)

        except:

            proxyItem.deleteOne()


    def runDailiServerProxy(self, proxyUrl):

        headStr = {

            'Accept': '*/*',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',

            'Accept-Encoding': 'gzip, deflate, sdch',

            'Accept-Language': 'zh-CN,zh;q=0.8'
        }

        try:

            res = requests.get("http://www.hualongxiang.com", proxies={"http": proxyUrl}, headers=headStr, timeout=3, allow_redirects=False)

            if res.status_code == 200:

                proxyModel = proxyIpModel()

                proxyModel.ipAddr = proxyUrl

                proxyModel.insertOne()

                if not proxyUrl in self.canUsedProxyIps: self.canUsedProxyIps.append(proxyUrl)

        except:

            pass

class allProcessExceptionMiddleware(object):

    allException = [TimeoutError, TCPTimedOutError]

    logger = logging.getLogger()

    def process_response(self, request, response, spider):

        if response.status != 200:

            self.logger.warning(request.url+"该链接使用代理"+str(request.meta["proxy"])+"运行结果为："+str(response.status)+",可能在上面已经被重试了，可运行 curl -x "+str(request.meta["proxy"])+" -L "+request.url+" 进行测试")

        return response




