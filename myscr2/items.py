# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class ListItem(Item):       #上市公司信息
    name = Field()          #公司名称
    field = Field()         #所属行业
    investor = Field()      #投资方
    list_time = Field()     #上市时间
    issue_price = Field()   #发行价
    list_address = Field()  #上市地点
    issue_num = Field()     #发行数量
    stock_code = Field()    #股票代码
    supp = Field()          #vc/pe支持



class HouseItem(Item):
    hname = Field()
    hstructure = Field()
    hfloor = Field()
    harea = Field()
    htype = Field()
    hinarea = Field()
    hbtype = Field()
    hfaced = Field()
    hbstructure = Field()
    hdecoration = Field()
    helevatorrange = Field()
    helevator = Field()
    hrights = Field()

    hlisttime = Field()
    hlisttype = Field()
    hlasttime = Field()
    huse = Field()
    hholdtime = Field()
    hrightshold = Field()
    hplege = Field()
    hphoto = Field()

    hkeypoint = Field()
    htaxpay = Field()
    hdecorationinfo = Field()
    hyardinfo = Field()
    htypeinfo = Field()

    #houseinfo = Field()
    #houseaddress = Field()
    #linktest = Field()