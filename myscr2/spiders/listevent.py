
import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from myscr2.items import ListItem


class ListSpider(Spider):
    name = "list"
    allowed_domains = ["pedaily.cn"]
    start_urls = [
        "http://zdb.pedaily.cn/ipo",
    ]
    url =   'http://zdb.pedaily.cn'

    def parse(self, response):
        content_link = Selector(response).xpath('//*[@id="ipo-list"]/li/dl/dt[5]/a/@href').extract()
        if content_link:
            yield scrapy.Request(self.url+content_link[0], callback=self.parse_item)


        next_page = response.xpath('/html/body/div[4]/div/div[1]/div[5]/div/div[1]/div/a[4]/@href')
        if next_page:
            next = response.urljoin(next_page.extract())[0]
            yield scrapy.Request(next, callback=self.parse)

    def parse_item(self, response):
            info = Selector(response)
            item = ListItem()
            item['name'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[1]/text()').extract()[0]
            item['field'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[2]/a[2]/text()').extract()[0]
            item['investor'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[3]/text()').extract()[0]
            item['list_time'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[4]/text()').extract()[0]
            item['issue_price'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[5]/text()').extract()[0]
            item['list_address'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[6]/text()').extract()[0]
            item['issue_num'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[7]/text()').extract()[0]
            item['stock_code'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[8]/text()').extact()[0]
            item['supp'] = info.xpath('/html/body/div[6]/div[1]/div/div[2]/div/ul/li[9]/text()').extract()[0]
            yield item















