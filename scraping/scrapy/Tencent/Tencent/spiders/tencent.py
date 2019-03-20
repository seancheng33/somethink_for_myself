# -*- coding: utf-8 -*-
import scrapy

from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURL = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        # items = []
        for node in node_list:
            item = TencentItem()

            positionName = node.xpath("./td[1]/a/text()").extract()
            positionLink = node.xpath("./td[1]/a/@href").extract()
            positionType = node.xpath("./td[2]/text()").extract()
            peopleNumber = node.xpath("./td[3]/text()").extract()
            workLocation = node.xpath("./td[4]/text()").extract()
            publishTime = node.xpath("./td[5]/text()").extract()

            item['positionName'] = positionName[0]
            item['positionLink'] = positionLink[0]
            if len(positionType):
                item['positionType'] = positionType[0]
            else:
                item['positionType'] = ''
            item['peopleNumber'] = peopleNumber[0]
            item['workLocation'] = workLocation[0]
            item['publishTime'] = publishTime[0]

            yield item

        # if self.offset < 3070:
        #     self.offset += 10
        #     url = self.baseURL + str(self.offset)
        #     yield scrapy.Request(url, callback=self.parse)

        if len(response.xpath("//a[@class='noactive' and @id='next']")) == 0:
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("https://hr.tencent.com/"+url,callback=self.parse)