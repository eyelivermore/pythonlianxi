
# coding: utf-8

# In[10]:


import requests
from bs4 import BeautifulSoup
def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.text
    except:
        return "ERROR"


# In[68]:


def get_content(url):
    comments =[]
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    liTags = soup.find_all('li',attrs = {"class":' j_thread_list clearfix'})
    for li in liTags:
        try:
            comment = {}
            #这是标题
            comment['title'] = li.find('a',attrs = {'class':'j_th_tit '}).text.strip()
            #这是连接
            comment['link']= "http://tieba.baidu.com"+li.find('a',attrs = {'class':'j_th_tit '})['href']
            #这是名字
            comment['name'] = li.find('span',attrs = {'class':'tb_icon_author '}).text.strip()
            #时间
            comment['time'] = li.find('span',attrs = { 'class':"pull-right is_show_create_time"}).text.strip()
            #
            comment['replyNum'] = li.find('span',attrs = {'class':'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题')
    return comments


# In[66]:


def Out2File(dict):
    with open('TTBT.txt',"a+",encoding="utf-8",) as f:
        for comment in dict:
            f.write('标题:{}\t 连接 :{} \t 发贴人:{} \t 发贴时间:{}\t 回复数量{} \n'.format(
            comment['title'],comment['link'],comment['name'],comment['time'],comment['replyNum']))
        f.close
        print('当前页面爬取完成')
        
        


# In[70]:


def main(base_url,deep):
    url_list = []
    for i in range(0,deep):
        url_list.append(base_url + "&pn"+str(50*i))
        
    print('连接下载完成')                     
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print("所有信息保存完成")

base_url = "http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8"
deep = 3
if __name__ == '__main__':
    main(base_url, deep)

