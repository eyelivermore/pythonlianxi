# -*- coding: UTF-8 -*-
import pandas as pd 
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def tianmao(url):
    '''打开网页点击评论'''
    try:
        dirver.get(url)
        element =webs.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#J_RateCounter"))
        ).click()#加载页面点击评论
    except:
        print("加载页面出错了")


def dakaitaobao(url):
    '''打开网页点击评论'''
    try:
        dirver.get(url)
        element =webs.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#J_RateCounter"))
        ).click()#加载页面点击评论
    except:
        print("加载页面出错了")


def fanye():
    '''翻页输出页面源码'''
    try:
        dd = webs.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#reviews")))
        #加载评论页面
        texts = webs.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR,"#reviews > div > div > div > div > div > div.tb-revbd > div > ul > li.pg-next")))
        #找到点击下一页
        html = dirver.page_source  #得到HTML源码
        texts.click()    #点击下一页    
        return html
    except:
        print("翻面出错了")


def get_products(html,ls):
    '''抓取数据'''
    try:
        soup = BeautifulSoup(html,"lxml")
        li =soup.find_all("li",class_="J_KgRate_ReviewItem kg-rate-ct-review-item") 
        for i in li:
            ping = i.find("div",class_="tb-r-info").text
            txt = ping[18:].strip(" ")
            txt = txt.replace(" ","")
            ls.append(txt)
    except:
        print(" ")

    


def tongji(lists,counts,nm):
    '''词条统计'''
    txt = "{},{}\n"
    for i in lists:
        i = i.replace("\n","")
        if i=="":
            continue
        counts[i] = counts.get(i,0)+1
    items = list(counts.items())
    items.sort(key = lambda x:x[1] , reverse = True)

    # for t in range(len(items)):
    #     w,wo = items[t]
    #     print(w,wo)

    try:
        with open(nm+".csv","a+",errors='ignore') as f:
            f.write(txt.format("品种","数量"))
            for t in range(0,len(items)):
                w, wo = items[t]
                print(txt.format(w,wo))
                f.write(txt.format(w,wo))
    except:
        print("编码问题")






dirver = webdriver.Firefox()#火狐浏览器
#dirver = webdriver.phantomJS()
#dirver = webdriver.Chrome()

webs = WebDriverWait(dirver, 10)

def main():
    nme = "淘宝评论SDK数据"#在这里给取名字放在""里面,.csv不要去掉
    url = "https://item.taobao.com/item.htm?spm=a230r.1.14.2371.88356d1dMwmL6K&id=41315223357&ns=1&abbucket=11#detail"
    #想折那个网页就把网址复制过来,放在" "里面替换掉就可以了
    ls = []
    d = {}
    i=0
    dakaitaobao(url)
    zzz = 40#数字代表抓取页评论你想抓多少页评论就把他改成多少
    while i<=zzz:
        html = fanye()
        get_products(html,ls)
        i +=1
        print("第{}页".format(i))
    tongji(ls,d,nme)

    print("抓取结束")
if __name__=="__main__":
    main()
