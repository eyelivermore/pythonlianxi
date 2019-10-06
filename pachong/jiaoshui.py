from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://seed.futunn.com/?user_id=1371425&auth_token=727891&clienttype=12&clientver=9.1.592&clientlang=0"

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(url)
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()