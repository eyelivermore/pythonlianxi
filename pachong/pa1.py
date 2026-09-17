from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
wwww = webdriver.Chrome()
wait = WebDriverWait(wwww, 10)#等待时间

def shoushuo():#打开浏览器攻取页码娄
    try:

        wwww.get("https://www.taobao.com/")
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))#l输入框等待
         )
        annui = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#J_TSearchForm > div.search-button > button")))#按纽
        input.send_keys('计算机')#输入"美食"
        annui.click()

        total = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.total")))#获取多少页
        return total.text
    except TimeoutException:
        return shoushuo()

def next_page(page_number):#翻页函数
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input"))
        )#页码框
        annui = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")))#确定控场
        input.clear()
        input.send_keys(page_number)
        annui.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active > span"),str(page_number)))
    except TimeoutException:
        next_page(page_number)

def main():
    total = shoushuo()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total+1):
        next_page(i)

if __name__=='__main__':
    main()