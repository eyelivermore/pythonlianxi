from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import pymongo
import time

URL=  "http://fundf10.eastmoney.com/jjjz_000198.html"
def pege_auto(el,dr,code):
    """翻页"""
    #输入框
    try:
        input_box = el.until(EC.presence_of_element_located((By.CLASS_NAME,'pnum')))
        input_box.send_keys(code)#填入数字
        #找到确认按扭
        button = dr.find_element_by_class_name('pgo')
        button.click()
        el.until(EC.presence_of_element_located((By.CLASS_NAME,"cur")))
        dr.implicitly_wait(1)

        html = dr.page_source
        return html
    except :
        print(f'第{code}页出错了')
        pege_auto(el,dr,code)
        time.sleep(3)
    

def exeract_data(el,dr,code):
    """提取数据"""
    html = pege_auto(el,dr,code)


    ti = []
    values = []
    stop = BeautifulSoup(html,"lxml")
    date = re.compile('\d{4}-\d{2}-\d{2}')
    times = stop.findAll(re.compile('tr'))
    for i in times:
        d = i.find('td')
        if date.findall(str(d)) != []:
            ti.append(date.findall(str(d))[0])#时间
    
    data = stop.findAll('td',class_="tor bold")
    for i in data:
        if re.findall('>(.*?)%</td>',str(i)) != []:
            values.append(re.findall(r'>(.*?)%</td>',str(i))[0])


    print(ti,values)

    if ti!=[] and values!=[]:
        return ti,values
    else:
        print(f"出错了重新加载{code}")
        exeract_data(el,dr,code)


   

def data_save(db,times,date):
    """保存数据"""
    data_valus = db['data']
    bb=[]
    for i in range(len(times)):
        ds = {"日期":str(times[i]),'收益率':str(date[i])}
        bb.append(ds)

    data_valus.insert_many(bb)

    

    

def main(URL):
    #浏览器对象
    driver = webdriver.Firefox()
    #等待时间对象
    element = WebDriverWait(driver, 5)
    client = pymongo.MongoClient("localhost",27017)
    db = client["yuerbao_data"]
    driver.get(URL)
    for code in range(1,113):
        #填入页码输出页面信息
        #提取页面数据
        times,date = exeract_data(element,driver,code)
        data_save(db,times,date)
        print(f"第{code}页")
        
    

if __name__ =="__main__":
    main(URL)
