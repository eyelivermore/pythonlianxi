from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import datetime

def page_auto(url,i):#自动翻页
    browser.get(url=rul)
    idtextss = WebDriverWait(browser,10)#等待10秒
    try:
        element = idtextss.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#feedList > div:nth-child(1)")
        ))#判断第一条是不是送种子的
        htmls = browser.page_source
        print("得到ID:",i)
        return htmls
        
    except:
        pass
        

def fenxirul(htmls,i):  #分析页面拿到连接
    #设定比较基准日期
    dm = datetime.datetime.strptime('2018-07-21 00:20','%Y-%m-%d %H:%M')
    try:
        #用正则表达式找到发表的日期
        times = re.findall(r"<a target=\"_blank\" href=\"/nnq/detail.*?\">(.*?)</a>",htmls)
        #找到时间
        print(i,"发表在",times[0],'长度',len(times[0]))
        
        if len(times[0])==4: # 第一个是发达详情
            if len(times[1])>4 and len(times[1])>8:#第二 几个小时内的
                with open ('id.csv',"a+") as f:
                    f.write(i+',')
                    print("写入",i,"发表时间",times[1])
            elif len(times[1])==8:#找到今天昨天的
                with open ('id.csv',"a+") as f:
                    f.write(i+',')
                    print("写入",i,"发表时间",times[1])
            elif len(times[1])==16:#两天以前的
                time_1 = datetime.datetime.strptime(times[1],"%Y-%m-%d %H:%M")
                time_c =eval(str(dm -time_1).split(' ')[0])
                if time_c<60:
                    with open ('id.csv',"a+") as f:
                        f.write(i+",")
                        print("写入2个月以内的",i,"发表时间",times[0])   

        elif len(times[0])>4 and len(times[0])<8:#几个波动时内的
            with open ('id.csv',"a+") as f:
                f.write(i+',')
                print("写入几分种前",i,"发表时间",times[0])
        elif len(times[0])==8:#今天昨天的
            with open ('id.csv',"a+") as f:
                f.write(i+',')
                print("写入当日",i,"发表时间",times[0])
          
        elif len(times[0])==16:#两天以前的
            time_1 = datetime.datetime.strptime(times[0],"%Y-%m-%d %H:%M")
            time_c =eval(str(dm -time_1).split(' ')[0])
            print(time_c)
            if time_c<60:
                with open ('id.csv',"a+") as f:
                    f.write(i+",")
                    print("写入2个月以内的",i,"发表时间",times[0])                
                    

    except:
        pass



    
htmls = open('D:/pyexe/ftxt.txt',"r").read()
idtext= htmls.split(",")
url1 = "https://www.futunn.com/account/nnq?uid="
browser = webdriver.Firefox()
#browser = webdriver.Chrome()
for i in idtext:
    i = re.sub("\D", "", i) 
    rul = url1 + i
    html = page_auto(rul,i)
    fenxirul(html,i)

   

 
print("-----END------")