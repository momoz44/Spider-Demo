
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from myscr2.items import HouseItem

class HouseSpider(Spider):
    name = "house"
    allowed_domains = ["lianjia.com"]
    start_urls = ["http://cd.lianjia.com/ershoufang/"]
    baselink = "http://cd.lianjia.com/ershoufang/pg"
    k=1
    def parse(self, response):

        table = Selector(response).xpath('//*[@class="info clear"]/div[1]')
        i=0
        for each in table:
            content_link = each.xpath('//*[@class="info clear"]/div[1]/a/@href').extract()[i]
            i = i+1
            yield scrapy.Request(content_link, callback=self.parse_item)

        self.k = self.k + 1
        nextlink = self.baselink + str(self.k)
        if self.k <= 100:
            yield scrapy.Request(nextlink, callback=self.parse)



    def parse_item(self, response):

        item = HouseItem()
        item['hname'] = response.xpath('/html/body/div[3]/div/div/div[1]/h1/text()').extract()[0]
        item['hstructure'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()').extract()[
            0]
        item['hfloor'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()').extract()[0]
        item['harea'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()').extract()[0]
        item['htype'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()').extract()[0]
        item['hinarea'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').extract()[0]
        item['hbtype'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').extract()[0]
        item['hfaced'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').extract()[0]
        item['hbstructure'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[8]/text()').extract()[0]
        item['hdecoration'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract()[0]
        item['helevatorrange'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()').extract()[0]
        item['helevator'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').extract()[0]
        item['hrights'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[12]/text()').extract()[0]

        item['hlisttime'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/text()').extract()[0]
        item['hlisttype'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[2]/text()').extract()[0]
        item['hlasttime'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[3]/text()').extract()[0]
        item['huse'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[4]/text()').extract()[0]
        item['hholdtime'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[5]/text()').extract()[0]
        item['hrightshold'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[6]/text()').extract()[0]
        item['hplege'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[7]/span[2]/text()').extract()[0]
        item['hphoto'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[8]/text()').extract()[0]

        #item['hkeypoint'] = response.xpath('/html/body/div[7]/div[1]/div[2]/div/div[2]/div[2]/text()').extract()[0]
        #item['hkeypoint'] = response.xpath(u'(normalize-space(//*[@class="introContent showbasemore"]/div[2]/div[2]/\
        # text())').extract()[0]
        #item['hkeypoint'] = response.xpath('//*[@class="introContent showbasemore"]/div[2]/div[2]/text()').extract()[0]
        #item['htaxpay'] = response.xpath('//*[@class="introContent showbasemore"]/div[3]/div[2]/text()').extract()[0]
        #item['hdecorationinfo'] = response.xpath('//*[@class="introContent showbasemore"]/div[4]/div[2]/text()').extract()[0]
        #item['hyardinfo'] = response.xpath('//*[@class="introContent showbasemore"]/div[5]/div[2]/text()').extract()[0]
        #item['htypeinfo'] = response.xpath('//*[@class="introContent showbasemore"]/div[6]/div[2]/text()').extract()[0]

        yield item



