
# coding: utf-8

# In[264]:


import requests
from bs4 import BeautifulSoup
import re
def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding="gbk"
        return r.text
    except:
        print = "someting wrong"


# In[265]:


def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    movies_list = soup.find('ul',class_="picList clearfix")
    movies = movies_list.find_all('li')
    for top in movies:
        img_url = "http:" + top.find('img')['src']
        name = top.find('span',class_="sTit").text
        actors = top.find('p',class_="pActor")
        actor = ' '
        for act in actors.contents:
            actor = actor + act.string + ' '

        try:
            time = top.find('span',class_="sIntro").text
        except:
            time = "还没有上映时间"
        intor = top.find('p',class_="pTxt pIntroShow").text
        intor = re.sub(r"展开全部(.*)"," ",intor)

       
        
        with open('D:/python练习/pepo/电影.txt','a+',encoding='utf-8') as f:
             f.write('片名:{}\t{}\n{}\n{}\n\n'.format(name ,time,actor ,intor))
#         with open('D:/python练习/pepo/'+name+'.jpg','wb+') as f:
#             f.write(requests.get(img_url).content)

        
        print('片名:{}\t{}\n{}\n{}\n\n'.format(name ,time,actor ,intor))


# In[266]:


url = 'http://dianying.2345.com/top/'
def main():
    get_content(url)
    
if __name__=='__main__':
    main()

