import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup




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
        #jiazhai = webs.until(EC.presence_of_element_located((BY.CSS_SELECTOR,"#reviews > div")))
        html = dirver.page_source  #得到HTML源码

        texts.click()    #点击下一页    
        return html
        
    except:
        print("翻面出错了")


def get_products(pinglist,html,dicts):
    '''抓取数据'''
    try:
        soup = BeautifulSoup(html,"lxml")
        #whtml = soup.find("div",class_="tb-revbd")
        li =soup.find_all("li",class_="J_KgRate_ReviewItem kg-rate-ct-review-item") 
        for i in li:
            #time = i.find("span",class_="tb-r-date").string
            ping = i.find("div",class_="tb-r-info").text#得到SDK数据
            #txt = ping
            #txt = ping[18:23] + ','+ping[23:27]+","+ping[27:]
            #txt = ('{}'.format(ping))
            key = ping[23:].strip(" ")
            key = key.replace(' ',"")
            pinglist.append(key)
            

            # with open("淘宝数据2.csv","a+",errors='ignore') as f:#淘宝数据3这个是给文件取的名字,这个可以改

            #     f.write(ping)

    except:
        print(" ")
dirver = webdriver.Firefox()#打开浏览器
webs = WebDriverWait(dirver, 10)#等待页面加载

def main():
    
    url = 'https://item.taobao.com/item.htm?spm=a230r.7195193.1997079397.9.iE93Q5&id=528571917196&abbucket=5'
    #url = "https://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-17388734043.2.2f59216fVzOYdp&id=520456515215"
    #要打开的网址
   
    d = {}
    i=0
    dakaitaobao(url)
    pinglist = []
    while i<2:#2代表抓取页评论你想抓多少页评论就把他改成多少
        
        html = fanye()
        get_products(pinglist,html,d)
        i +=1
        print("第{}页".format(i))
    print("结束")
    for key in pinglist:
        d[key] = d.get(key,0)+1
    dlist = list(d.items())
    dlist.sort(key = lambda x:x[1] , reverse = True)
    for i in range(len(dlist)):
        print(dlist[i])
    
    #
if __name__=="__main__":
    main()
