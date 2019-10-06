# -*- coding: utf-8 -*-
import scrapy
import re
import random
'''
这个是一个scrapy架构的爬虫
'''
#重新提交一下
class BaidustockSpider(scrapy.Spider):
    #系统自动生成的一个类
    name = 'baidustock'
    #爬虫的名字 运行爬虫输入 scrapy crawl <name>爬虫的名字
    
    def satrt_requests(self):
        start_urls = ['http://quote.eastmoney.com/stocklist.html']
        #第一个请求连接,也是爬虫的开始第一步
        request = scrapy.Request(url=start_urls,callback=self.parse)
        yield request

 

#从DOWNLOADER返回一个response由parse接受这相当于第6步
    def parse(self, response):
        #这是一个回调函数,接受spider发来的的request请求返回的response
        for href in response.css('a::attr(href)').extract():
            #用CSS方法提取用start_urls反回response的网页信息
            user_agent_list = [\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
                "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
                "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
                "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
                "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
                ]#这个列表是随机表头信息反爬用的 

            ua = random.choice(user_agent_list)#随机抽取列表晨面的一条当User-Agent
            headers = {
                'Accept-Encoding':'gzip, deflate, sdch, br',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Connection':'keep-alive',
                'Referer':'https://gupiao.baidu.com/',
                'User-Agent':ua
                }#构造请求头




            try:
                stocks = re.findall(r"[s][hz][603]\d{5}",href)[0]
                #提取每个大循环变量href里面的股票代码
                url = "https://gupiao.baidu.com/stock/"+stocks+".html"
                #构造一个百度股票url
                request = scrapy.Request(url,callback= self.parrse_stock,headers=headers)
                #用scrapy的一个请求方法Request生成一个请求callback参数传入一个是回调函数parrse_stock
                yield request
                #这个相当于是第7步再发一个Request给中间件ENGINE
            except:
                continue

    def parrse_stock(self,response):
        #这相当于第8步向item pipelines发送item
        '''自己编写的一个函数用来
           处理从baidu股票上反回的response信息
        '''
        infoDict = {}#定义一个字典
        stockinfo = response.css('.stock-bets')
        #找到这个求签提取股票信息
        name = response.css('.bets-name').extract()[0]
        #找到股票名字的html标签
        keylist = stockinfo.css("dt").extract()
        #在股票信息里面提取个个信息名称 反回一个列表
        valuslist = stockinfo.css('dd').extract()
        #提示信息名称后面的数值反回一个列表
        for i in range(len(keylist)):
            #把返回的列表进行信息配对
            key = re.findall(r">(.*?)</dt>",keylist[i])[0]
            #名字
            try:
                valus = re.findall(r'>(.*?)</dd>', valuslist[i])[0]
                #值
            except:
                valus = "non"
                #没有值的用--表示
            infoDict[key] = valus
            #建值对形式添加到字典
            infoDict.update(
                {'股票名称':re.findall(r'\s(.*?)\(',name)[0].split()[0],
                 "代码":re.findall('\>(.*?)\<',name)[0]})
                #反股票名称追加到字典
        yield infoDict
        #返回这个字典

