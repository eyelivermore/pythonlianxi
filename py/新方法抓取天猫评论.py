import requests
import re
import json
import time

def requests_urel(url):
    r = requests.get(url)
    if r.status_code !=200:
        print("连接错误")
    time.sleep(2)
    return r.text

def dow_data(url,d):
    #抓取数据
    html = requests_urel(url)

    #先处理返回结果
    html = html.lstrip('\r\njsonp744(').rstrip(')')
    #把json对象转换成python对象
    jd = json.loads(html)
    #把字典里面的值取出来
    ls = jd['rateDetail']['rateList']
    for i in ls:
        d.append(i['auctionSku'])
    

def data_process(d):
    lsre = []
    for x in range(len(d)):
        lsr = re.findall(r'尺码:(.*?)（',d[x])[0].strip()
        lsre.append(lsr)
    ds= {}
    for di in lsre:
        ds[di]=ds.get(di,0)+1
    items = list(ds.items())
    items.sort(key = lambda x:x[1] , reverse = True)  
    print(items)  

def main():
    d= []
    for i in range(1,55):
        url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=570360894700&spuId=977554329&sellerId=772687801&order=3&currentPage='+str(i)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hv19vEvbQvUvCkvvvvvjiPPscvQjtERLLZtjljPmPwgjrWPssZQjEjRszZ6jtV3QhvChCCvvm5vpvhphvhHvGCvvpvvPMMvphvCyCUvvvvvvyCvh1hgL%2BvIsE9Zj%2BO3w0AhjxPWDNBlLyzOvZf8cc6hBH%2BmB%2BKaNpBnAYbOyTxfXuKNB9fb57%2BhfURbVQHYE7re36kayNpzC0OwyEzpf2XkphvCyEmmvpf58yCvv3vpvoXucEG%2FfyCvm3vpvvvvvCvphCvVhwvvhjUphvwv9vvBj1vpCQmvvChxhCvjvUvvhBZRphvChCvvvv%3D&needFold=0&_ksTS=1539005763515_743&callback=jsonp744'
        dow_data(url,d)
        print(f"这是第{i}页")
    data_process(d)

if __name__=="__main__":
    main()
    
