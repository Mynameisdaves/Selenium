import re
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = uc.ChromeOptions()
options.add_argument("--disable-background-timer-throttling")
options.add_argument("--disable-backgrounding-occluded-windows")
options.add_argument("--disable-renderer-backgrounding")
options.add_argument("--start-maximized")

driver = uc.Chrome(options=options)


with open("tiktok_cliplist1.html", "r", encoding="utf-8") as file:
    lines = file.readlines()

video_urls = [re.search(r'https://www\.tiktok\.com/@[^"]+/video/\d+', line).group(0) for line in lines if '/video/' in line]
video_ids = [re.search(r'/video/(\d+)', url).group(1) for url in video_urls]

results = []
incomplete_entries = []

def get_stats(tiktok_url):
    driver.get("https://countik.com/live-video-views-counter")
    time.sleep(2)

    input_box = driver.find_element(By.ID, "search")
    input_box.clear()
    input_box.send_keys(tiktok_url)
    input_box.send_keys(Keys.ENTER)

    time.sleep(11)

    html = driver.page_source
    numbers = re.findall(r'<h5 class="count">([\d,\.]+)</h5>', html)
    cleaned = [n.replace(',', '') for n in numbers]
    return cleaned

for tiktok_url, vid in zip(video_urls, video_ids):
    try:
        stats = get_stats(tiktok_url)
        print(f"{vid} - {stats}")
        if len(stats) >= 4:
            results.append([vid] + stats[:4])
        else:
            incomplete_entries.append((tiktok_url, vid))
    except Exception as e:
        print(f"Failed to process {vid}: {e}")
        incomplete_entries.append((tiktok_url, vid))

print("\nRetrying incomplete entries...\n")
for tiktok_url, vid in incomplete_entries:
    try:
        stats = get_stats(tiktok_url)
        print(f"{vid} - {stats}")
        if len(stats) >= 4:
            results.append([vid] + stats[:4])
        else:
            print(f"Still incomplete for {vid}")
    except Exception as e:
        print(f"Failed to retry {vid}: {e}")

driver.quit()

print("\nFinal Results:")
for row in results:
    print(row)
