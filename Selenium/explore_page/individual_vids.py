import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


service = Service(executable_path="../chromedriver.exe")
driver = webdriver.Chrome(service=service)

def videoinfo(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        video_urls = [line.strip() for line in file.readlines() if line.strip()]
    
    keywords = ["like-count", "comment-count", "undefined-count", "share-count"]
    
    for url in video_urls:
        print(f"\n {url}")
        driver.get(url)
        time.sleep(10)  
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        html_lines = soup.prettify().split("\n")

        for i, line in enumerate(html_lines):
            for keyword in keywords:
                if keyword in line:
                    next_line = html_lines[i + 1] if i < len(html_lines) - 1 else "N/A"
                    print(f"{keyword}: {next_line}")


videoinfo("tiktok_cliplist.html")

driver.quit()
