from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random

# Initialize WebDriver
service = Service(executable_path="../chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open TikTok search page
driver.get("https://www.tiktok.com/search?lang=en&q=BloodStrike%20Thailand")

# Wait for the page to load fully
time.sleep(10)

# Scroll and capture HTML
scroll_times = 15  # Number of scroll actions

for i in range(scroll_times):
    # Scroll full page down
    driver.execute_script("window.scrollBy(0, window.innerHeight);")

    # Wait for new content to load
    delay = random.randint(2, 6)
    time.sleep(delay)

    # Extract and save HTML after each scroll
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    with open(f"tiktok_scroll_{i+1}.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    print(f"Scroll {i+1}: scrolled full page down with {delay}s delay.")

# Done
driver.quit()
print("Finished scrolling and saving.")




