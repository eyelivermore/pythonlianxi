# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import re
class StockPipeline(object):

    def open_spider(self,spider):
        self.f = open('baidustockinfo.csv','a+')
 
    def close_spider(self,spider):
        self.f.close()
 
    def process_item(self, item, spider):
        try:
            line = str(list(dict(item).values()))+'\n'
            lines = re.sub(r"'",'',line)
            lines = lines.strip('[]')
            self.f.write(lines)
        except:
            pass
        return item
