import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import random
import re

driver = uc.Chrome()
driver.get("https://www.tiktok.com/search?lang=en&q=BloodStrike%20Thailand")
time.sleep(10)

scroll_times = 15
matches = set()

for i in range(scroll_times):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    delay = random.randint(2, 6)
    time.sleep(delay)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    html = soup.prettify()
    found = re.findall(r"https://www\.tiktok\.com/@[^\s\"']+/video/\d+", html)
    before_count = len(matches)
    matches.update(found)
    print(f"Scroll {i+1}: found {len(matches) - before_count} new links, total: {len(matches)}")

driver.quit()

video_urls = sorted(matches)
print(f"\n Found {len(video_urls)} unique TikTok video URLs:")
for url in video_urls:
    print(url)


