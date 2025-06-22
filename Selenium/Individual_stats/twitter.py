from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
import random

driver = webdriver.Chrome()
driver.get("https://x.com/i/flow/login")
time.sleep(8)

seen_links = set()

try:
    input_box = driver.find_element(By.NAME, "text")
    input_box.send_keys("Dorsy61341")
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Davids67")
    password_input.send_keys(Keys.ENTER)
    time.sleep(11)

    driver.get("https://x.com/search?q=%23barcelona&src=typed_query&f=media")
    time.sleep(8)

    for i in range(15):
        html = driver.page_source
        new_links = re.findall(r'<a href="(/\w+/status/\d+/(photo|video)/\d+)"', html)
        links_only = [match[0] for match in new_links]
        seen_links.update(links_only)

        print(f"[{i+1}/15] Scrolled & found {len(seen_links)} unique tweet links so far...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(3, 7))

except Exception as e:
    print("❌ Error while collecting links:", str(e))

finally:
    driver.quit()

print("\n💾 Visiting 3 tweets and saving HTML files...\n")

link_list = list(seen_links)

for count, link in enumerate(link_list[:3]):
    try:
        full_url = f"https://x.com{link}"
        driver = webdriver.Chrome()
        driver.get(full_url)
        time.sleep(6)

        page_source = driver.page_source

        with open(f"tweet_{count+1}.html", "w", encoding="utf-8") as f:
            f.write(page_source)

        print(f"✅ Saved: tweet_{count+1}.html from {full_url}")
        driver.quit()

    except Exception as e:
        print(f"❌ Error processing {link}:", str(e))
        driver.quit()

input("\nDone. Press Enter to exit...\n")



