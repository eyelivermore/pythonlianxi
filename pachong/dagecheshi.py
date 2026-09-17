from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import re


url = "https://www.futunn.com/account/nnq?uid=7186941"
browser = webdriver.PhantomJS()
browser.get(url)
htmls = browser.page_source
# htmls = open('D:/pachong/html.txt',"r",encoding='UTF-8').read()
nn = BeautifulSoup(htmls,"lxml")
times = nn.select_one('span[class="time"]')
soup1 = nn.select_one('a[class="orgLink"]').attrs['href']
times1 = nn.select('span[class="time"]')[0].get_text()
times2 = nn.select('span[class="title"]')[0].get_text()#'种子是str属性'
txt = nn.select('div[class="txtBox01"]')[0].get_text()

# print('种子的长度',len(times2))
# print(type(times2))AttributeError:
# print(times2)
# print(times1)#时间nderrxEor:I
print(type(txt))
# if "package"  not in txt:
# 	print(txt)


