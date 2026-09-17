from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import re

def page_auto(url):#自动翻页
    browser.get(url=rul)
    idtextss = WebDriverWait(browser,5)#等待10秒
    try:
        element = idtextss.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#feedList > div:nth-child(1) > div.detailDiv01 ")
        ))#判断第一条是不是送种子的
        return fenxirul(rul) 
    except:
        return fenxirul(rul)
        

def fenxirul(url):  #分析页面拿到连接
    
    try:
        times1 = browser.find_element_by_class_name('time')
        #times2 = nn.select('div[class="txtBox01"]')[0].get_text()#第一条里的文字
        #times1 = nn.select('span[class="time"]')[0].get_text()#时间
        #if len(times1)>11#昨天
        if len(times1)>11:#  6代表几分钟前 11代表今天 昨天
            return
        soup1 = nn.select_one('a[class="orgLink"]').attrs['href']
        print(i,times1)
    except AttributeError:
        soup1 = nn.select_one('a[class="quote clearBox"]').attrs['href']
        print(i,times1)
    finally:
        return



htmls = open('D:/pachong/ftxt.txt',"r").read()
idtext= htmls.split(",")
url1 = "https://www.futunn.com/account/nnq?uid="
browser = webdriver.Firefox()
for i in idtext:
    i = re.sub("\D", "", i) 
    rul = url1 + i
    #print(rul)
    page_auto(rul)

print("-----END------")
