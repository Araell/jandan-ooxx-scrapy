# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
import scrapy
import os

class PageSpider(scrapy.Spider):
    name = "pagespider"
    allowed_domains = ["jandan.net/ooxx"]
    if not os.path.exists('./htmls'):
        os.mkdir('./htmls')

    start_urls = []
    for page in range(1342, 1352):
        start_urls.append('http://jandan.net/ooxx/page-%d' % page)
    # http://jandan.net/ooxx/page-1362
    print '------------urls------------'
    print start_urls
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        filename = hxs.select("//span[@class='current-comment-page']/text()").extract()[0] + ".html"
        open('./htmls/' + filename, 'wb').write(response.body)
        pass
