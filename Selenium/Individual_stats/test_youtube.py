from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://seostudio.tools/youtube-video-statistics")
input_box = driver.find_element("id", "input")
input_box.send_keys("https://www.youtube.com/watch?v=PKLy0f6OPHE")
input_box.send_keys(Keys.ENTER)

time.sleep(6)

soup = BeautifulSoup(driver.page_source, 'html.parser')

td_tags = soup.find_all("td")
values = []
for i in range(len(td_tags) - 1):
    if "bg-gradient-success" in td_tags[i].get("class", []):
        values.append(td_tags[i + 1].text.strip())

print(values)

driver.quit()

