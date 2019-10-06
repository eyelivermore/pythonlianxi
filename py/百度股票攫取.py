import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    html = getHTMLText(stockURL,"GB2312")
    soup = BeautifulSoup(html, 'lxml') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def getStockinfo(lst,stockURL,opencsv):
    counte = 0
    for stock in lst:
        url = stockURL + stock +".html"
        html = getHTMLText(url)
        try:
            if html =="":
                continue
            infodict ={} 
            stop = BeautifulSoup(html,"lxml")
            stockinfo = stop.find("div",class_="stock-bets")
            
            stockname = stockinfo(class_="bets-name")[0]
            infodict.update({"股票名称":stockname.text.split()[0]})
            stockkey = stockinfo("dt")
            stockvalues = stockinfo("dd")
            for i in range(len(stockkey)):
                key = stockkey[i].text
                val = stockvalues[i].text
                infodict[key] = val

            with open(opencsv,"a+") as f:
                f.write(str(infodict)+"\n")
                counte +=1
                print("\r当年进度:{:.2f}%".format(counte*100/len(lst),end=""))
        except:
            counte +=1
            print("\r当年进度:{:.2f}%".format(counte*100/len(lst),end=""))
            print("出错了")
            continue
            

def main():
    slist=[]
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'http://gupiao.baidu.com/stock/'
    opencsv = "D:/python练习/baidu.csv"
    getStockList(slist,stock_list_url)
    getStockinfo(slist,stock_info_url,opencsv)

main()