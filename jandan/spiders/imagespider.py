# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import os

class ImageSpider(scrapy.Spider):
    name = "imagespider"
    allowed_domains = ["jandan.net/ooxx"]
    counter = 0
    #page range 900 - 1364
    start_page = 1300
    end_page = 1311
    if not os.path.exists('./images/%d-%d' % (start_page, end_page)):
        os.mkdir('./images/%d-%d' % (start_page, end_page))

    start_urls = []
    for page in range(start_page, end_page):
        start_urls.append('http://jandan.net/ooxx/page-%d' % page)

    def parse(self, response):
        sel = Selector(response)
        img_urls = sel.xpath("//div[@class='text']/p/img/@src").extract()
        req_list = []
        for url in img_urls:
            if 'thumbnail' in url:
                url = url.replace('thumbnail', 'large')
            req = Request(url, callback=self.download, dont_filter=True)
            req_list.append(req)
        return req_list

    def download(self, response):
        str = response.url
        self.counter = self.counter + 1
        str = str.split('/')
        print '----------------Image Get----------------', self.counter, str[-1]
        imgfile = open('./images/%d-%d' % (self.start_page, self.end_page) + '/' + str[-1], 'wb')
        imgfile.write(response.body)
        imgfile.close()