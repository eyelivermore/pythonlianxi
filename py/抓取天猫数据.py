import requests
import re
import time
import pymongo

def requests_url(url):
    #请求数据
    html = requests.get(url)
    if html.status_code != 200:
        print("返回不成功")
        return None
    return html.text  

def text_data(str_text):
    #处理文本   
    ls = []
    text = re.findall(r'auctionSku":"(.*?)","anony',str_text)
    for i in range(len(text)):
       ls.append(text[i][-3:])
    return ls

def total(ls):
    #词频统计
    d= {}
    for i in ls:
        d[i] = d.get(i,0)+1
    return d

def main():
    client = pymongo.MongoClient("localhost",27017) 
    db = client['tianmo']
    collection = db['zhaobei']
    d = {}
    for i in range(50):
        try:
            url = "https://rate.tmall.com/list_detail_rate.htm?itemId=41336666995&spuId=297847616&sellerId=391817269&order=3&currentPage="+str(i)+"&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvu9vbvnQvUvCkvvvvvjiPPsLOljtnRLMZQjthPmPw1jDCPFMvAjYbRFdyAj3R3QhvCvmvphm5vpvhvvCCBvhCvvOvChCvvvmtvpvIvvCvpvvvvvvvvhpnvvvvf9vvBGwvvvUwvvCj1Qvvv99vvhNjvvvmm8yCvv9vvhh5MvpYZIyCvvOCvhE20RpEvpCW97c6YClre4Tx%2B3%2Bdafm653AXaZRQ0fJ6W3CQog0HKfUpejIUDaVTRLwpEcqhg8TJhX3kLixreCAK5kx%2F1RmKDBV7OyTxfBeOdigDN9GCvvpvvPMMRphvCvvvphmCvpvZ7DruMgMw7Di4uqb5MvC44ldXz69tvpvhvvCvpv%3D%3D&needFold=0&_ksTS=1538655375232_932&callback=jsonp933"

            html = requests_url(url)
            if html is None:
                print("请求失败")
            ls = text_data(html)
            for ib in ls:
                d[ib] = d.get(ib,0)+1
            time.sleep(3)
            
        except:
            continue
        print(f"第{i}完毕")   
    data = list(d.items())

    data.sort(key = lambda x:x[1] , reverse = True)
    print(data)
    collection.insert_one(d)
    print("存入完毕")


main()










