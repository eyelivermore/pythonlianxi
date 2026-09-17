# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = "stocks"

    def start_requests(self):  
        start_urls = 'http://quote.eastmoney.com/stocklist.html'

        yield scrapy.Request(url = start_urls,  
            headers ={'User-Agent': "your agent string"},callback = self.parse)  
    

        
    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}",href)[0]
                url = "https://gupiao.baidu.com/stock/" + stock + ".html"
                yield scrapy.Request(url,callback = self.parse_stock,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'})
            except:
                continue 
    def parse_stock(self,response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keylist = stockInfo.css("dt").extract()
        valuelist = stockInfo.css("dd").extract()
        for i in range(len(keylist)):
            #key = re.findall(r'>.*</dt>',keylist[i])[0][1:-5]
            key = re.findall(r'<dt>(.*?)</dt>',keylist[i])[0]
            try:
                #val = re.findall(r'>(.*?)</dd>',valuelist(i))[0][0:-5]
                val = re.findall(r'<dd>(.*?)</dd>',valuelist[i])[0]
            except:
                val = "--"
            print(key,val)
            infoDict[key]=val
        infoDict.update(
            {"股票名称":re.findall(r'\s.*\(',name)[0].split()[0]+ \
            re.findall(r'\>.*\<',name)[0][1:-1]})
        yield infoDict







