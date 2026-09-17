import requests
import json
import random


url = "https://rate.tmall.com/list_detail_rate.htm?itemId=41336666995&spuId=297847616\
&sellerId=391817269&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=&groupI\
d=&ua=098%23E1hvk9vpvBvvUvCkvvvvvjiPPsL\
v6ji2n2sy6jthPmPhgjEVR2SZ1jDWRsFv1j189phv2nQwhlSWzYswzRbv7u6Cvvyv980rW9vv2vKrvpvEvvHxxL\
OvvUk7CQhvmBsw7DdNpjeEmuwCvvpvvhHhRphvCvvvphvCvpvVvv\
BvpvvvKphv8vvvphvvvvvvvvCh2pvvvBZvvhNjvvvmjvvvBGwvvvUUvvCj1Qvvv9kivpvUvvCCE0FEHUk\
EvpvVvpCmpYFymphvLUCkVByaY2Kzr2E9ZbmxdXeK5kx%2F1nmKHd8rwos6kCh7%2BulQbNLvHdoJV5aHgbv\
qrqpAOH2%2BFfmt%2B3C1pKFE%2BFuTRogRD764diTAVAQPvpvhvv2MMgwCvvpv9hCvRphvCvvvphmrvpvEvvjH1hIv\
vCfxRphvCvvv\
phv%3D&needFold=0&_ksTS=1538041994026_1146&callback=jsonp1147"

user_agent_list = [\
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]#这个列表是随机表头信息反爬用的 

ua = random.choice(user_agent_list)#随机抽取列表晨面的一条当User-Agent
headers = {
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Referer':'https://gupiao.baidu.com/',
    'User-Agent':ua
    }#构造请求头

r = requests.get(url=url,headers=headers)

print(r.status_code)
print(r.encoding)

