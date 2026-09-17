
import requests
from bs4 import BeautifulSoup
import re

url = ' http://www.qu.la/book/4140/8123652.html'
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        print("好像出错了")
txt_name='好了'
html = get_html(url)
soup = BeautifulSoup(html,'lxml')
try:
    txt = soup.find('div',id='content').text
    strr = '\'chaptererror();\'*/w'
    for i in strr:
        txt =txt.replace(i,"")
    txt = re.sub(r'\s','',txt)
    title = soup.find('title').text
    print(txt)
    with open('d:/python练习/{}.txt'.format(txt_name),'a',encoding='utf-8') as f:
        f.write(title+"\n\n")
        f.write(txt)
       
except:
    print('好像出了点问题')                                               