
# coding: utf-8

# In[7]:




def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.text
    except:
        return "ERROR"


# In[8]:


def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    match_list = soup.find_all('div',attrs = {'class':'matchmain bisai_qukuai'})
    for match in match_list:
        time = match.find('div',attrs = {"class":"whenm"}).text.strip()
        teamname = match.find_all('span',attrs = {'class':'team_name'})
        if teamname[0].string[0:3] == 'php':
            team1_name = "没有名字"
        else:
            team1_name = teamname[0].string
        team1_sopport_level = match.find('span',class_="team_number_green").string
        team2_name = teamname[1].string
        team2_sopport_level = match.find('span',class_="team_number_red").string
        
        print('比赛时间:{}\n  战队一:{}  胜率:{}\n   战队二:{}  胜率:{} '.format(time,team1_name,team1_sopport_level,
                                                                  team2_name,team2_sopport_level))
                                                              


# In[10]:


import requests
from bs4 import BeautifulSoup
def main():
    url = 'http://dota2bocai.com/match'
    get_content(url)
  
if __name__ == '__main__':
    main()

