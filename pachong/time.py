from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    htmls = browser.page_source
    nn = BeautifulSoup(htmls,"lxml")
    try:
        times1 = nn.select('span[class="time"]')[0].get_text()
        if len(times1)>11:
            return
        soup1 = nn.select_one('a[class="orgLink"]').attrs['href']
        print(i, times1,soup1)
    except AttributeError:
        soup1 = nn.select_one('a[class="quote clearBox"]').attrs['href']
        print(i,'\n',times1,soup1)
    finally:
        return



htmls = open('D:/pachong/ftxt.txt',"r").read()
idtext= htmls.split(",")
url1 = "https://www.futunn.com/account/nnq?uid="
browser = webdriver.Chrome()
for i in idtext:
    i = re.sub("\D", "", i) 
    rul = url1 + i
    #print(rul)
    page_auto(rul)
print("------END------")
