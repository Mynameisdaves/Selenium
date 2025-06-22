from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import random
import re

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query=football")
time.sleep(6)

scroll_times = 15
matches = set() 

for i in range(scroll_times):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    delay = random.randint(2, 6)
    time.sleep(delay)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    html = soup.prettify()
    found = re.findall(
        r"https://i\.ytimg\.com/vi/([\w-]{11})/[^\"'\s]+\.(?:jpg|webp)\?[^\"'\s]+", html
    )
    matches.update(found)

    print(f"Scroll {i+1}: found {len(found)} new video IDs, total so far: {len(matches)}")


driver.close()

video_ids = sorted(matches)
video_urls = [f"https://www.youtube.com/watch?v={vid}" for vid in video_ids]

print(f"\n✅ Found {len(video_urls)} unique video URLs:")
for url in video_urls:
    print(url)

