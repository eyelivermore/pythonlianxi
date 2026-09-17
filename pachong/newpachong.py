from selenium import webdriver
from datetime import datetime
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re


def page_auto(url):#自动翻页

    url1 = "https://www.futunn.com/account/nnq?uid="
    rul = url1 + url
    browser.get(rul)
    idtextss = WebDriverWait(browser,5)#等待10秒
    try:
        element = idtextss.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#feedList > div:nth-child(1) > div.detailDiv01 ")
        ))#判断第一条是不是送种子的
    except:
        print(url,'没有定位到请',rul,"检查删除")
        return 1
        
    htmls = browser.page_source
    htmltxt = BeautifulSoup(htmls,"lxml")
    return htmltxt

def fenxi(htmll,i):
    try:
        time = htmll.select('span[class="time"]')[0].get_text()#时间,,是一个str类类
        if len(time)>11:#  6代表几分钟前 11代表今天 昨天
            return print(i,"则家伙太懒了,好多天没有更新")
 
 
       # txt = htmll.select('div[class="module"]')[0].get_text()#第一条里的文字
       #      if "package" in txt:
       #          return print(i,time,txt)


        #return
        


    except AttributeError:
        return print("有问题")
    # else:
    #     pass
    # finally:
    #     pass






    
def main():
    for i in idtext:
        i = re.sub("\D", "", i) 
        html=page_auto(i)
        fenxi(html,i)


if __name__=='__main__':
    htmls = open('D:/pachong/ftxt.txt',"r").read()
    idtext= htmls.split(",")
    browser = webdriver.Firefox()
    nowtime=datetime.now()
    endtime=datetime.now()
    print("开始")
    print(nowtime.strftime("%Y-%m-%d %H:%M:%S"))
    print("-"*30)
    main()
    print("-----END------")
    print(nowtime.strftime("%Y-%m-%d  %H:%M:%S"))