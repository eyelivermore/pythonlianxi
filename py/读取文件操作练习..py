import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url)
        print(r.raise_for_status())
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockinfo(storck_list_url):
    try:
        infodict ={} 
        html = getHTMLText(storck_list_url)
        stop = BeautifulSoup(html,"lxml")
        stockinfo = stop.find("div",class_="stock-bets")
        
        stockname = stockinfo(class_="bets-name")[0]
        infodict.update({"股票名称":stockname.text.split()[0]})
        stockkey = stockinfo("dt")
        stockvalues = stockinfo("dd")
        for i in range(len(stockkey)):
            key = re.findall(r'<dt>(.*?)</dt>',stockkey[i])
            val = re.findall(r'<dd>(.*?)</dd>',stockvalues[i])
            print(key,val)
            infodict[key] = val

    except:

        print("出错了")

def main():
    storck_list_url = "https://gupiao.baidu.com/stock/sz300033.html"
    opencsv = "D:/python练习/baidu.csv"
    getStockinfo(storck_list_url)

main()
    