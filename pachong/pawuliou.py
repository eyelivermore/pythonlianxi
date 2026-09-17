import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url,timeout = 15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "ccl"

def fenxihtml(url):
    r = get_html(url)
    soup = BeautifulSoup(r,"lxml")
    name = soup.find_all(class_="tuanitem-meta-title")
    tel = soup.find_all(class_="nprice")
    address = soup.find_all(class_="hot_add")

    for i in  range(len(name)):
        with open("data.csv","a+") as f:
            f.write(name[i].text+","+tel[i].text+","+address[i].text+"\n")



def main():
    
    for i in range(1,183):
        url= f"http://www.wb9156.com/?page={i}"
        fenxihtml(url)
        print(f"{i}")
main()




