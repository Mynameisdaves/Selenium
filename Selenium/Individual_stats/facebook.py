import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import pyperclip

def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.25))

def login(driver, email, password):
    driver.get("https://www.facebook.com/login")
    time.sleep(random.uniform(1.5, 3))
    
    input_box = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "pass")
    time.sleep(6)

    human_typing(input_box, email)
    time.sleep(random.uniform(1.5, 2.5))

    human_typing(password_input, password)
    time.sleep(random.uniform(1.0, 3.5))

    password_input.send_keys(Keys.ENTER)
    time.sleep(7)

def scroll_and_share(driver):
    current_scroll_position = 0  
    for i in range(15): 
        extra_pixels = random.randint(0, 300)
        scroll_amount = driver.execute_script("return window.innerHeight;") + extra_pixels

        current_scroll_position += scroll_amount
        driver.execute_script(f"window.scrollTo(0, {current_scroll_position});")
        print(f"🌀 Scrolled to {current_scroll_position}px (Scroll {i+1}/15)")
        time.sleep(random.uniform(2.0, 5.0))

        try:
            share_button = driver.find_element(By.CSS_SELECTOR, 'span[data-ad-rendering-role="share_button"]')
            driver.execute_script("arguments[0].click();", share_button)
            print("✅ Clicked the Share button")
            time.sleep(random.uniform(2, 4))

            copy_link = driver.find_element(By.XPATH, "//span[text()='Copy link']")
            copy_link.click()
            time.sleep(random.uniform(1.5, 3))
            print("✅ Clicked Copy link button")

            copied_link = pyperclip.paste()
            print(f"🔗 Fresh copied link: {copied_link}")

            search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search Facebook" and @type="search"]')
            search_input.click()
            search_input.send_keys(copied_link)
            time.sleep(random.uniform(0.5, 2.0))

            current_value = search_input.get_attribute("value")
            print(f"📋 Current input value after scroll {i+1}: {current_value}")

            search_input.clear()
            print(f"🧹 Cleared search input after scroll {i+1}")

            driver.execute_script(f"window.scrollTo(0, {current_scroll_position});")
            print(f"↩️ Re-scrolled to {current_scroll_position}px after action")

            time.sleep(random.uniform(2, 5))

        except Exception as e:
            print(f"❗ Error during share/copy after scroll {i+1}: {e}")

if __name__ == "__main__":
    options = uc.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('start-maximized')

    driver = uc.Chrome(options=options)

    try:
        login(driver, "yourusername", "yourpassword")
        print("✅ Logged in successfully!")

        driver.get("https://www.facebook.com/OfficialBloodStrikeNetEase/")
        time.sleep(random.uniform(3, 5))

        while True:
            scroll_and_share(driver)
            print("🔁 Completed one full 15x scroll/share cycle, repeating...")
            time.sleep(random.uniform(10, 20))

    finally:
        input("Press Enter to exit...\n")
        driver.quit()
