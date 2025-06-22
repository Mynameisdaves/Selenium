from selenium import webdriver
import time
import re

# Helper function to convert 3.7K, 4.5M, etc. into numbers
def convert_to_number(value):
    value = value.replace(",", "").strip()
    multiplier = 1
    if value.lower().endswith('k'):
        multiplier = 1_000
        value = value[:-1]
    elif value.lower().endswith('m'):
        multiplier = 1_000_000
        value = value[:-1]
    elif value.lower().endswith('b'):
        multiplier = 1_000_000_000
        value = value[:-1]

    try:
        return int(float(value) * multiplier)
    except ValueError:
        return None

# Analyze HTML source
def process_page_source(page_source, url=None):
    print(f"\n📄 Analyzing page: {url if url else 'Local File'}\n")

    # Find the position of the first div with role="group"
    div_match = re.search(r'<div[^>]+role\s*=\s*["\']group["\']', page_source, re.IGNORECASE)
    if not div_match:
        print("⚠️ No <div> with role='group' found. Skipping.\n")
        return

    # Split the HTML into before and after the <div role="group">
    before_group_html = page_source[:div_match.start()]
    after_group_html = page_source[div_match.start():]

    # 1. Find the FIRST numeric span BEFORE role=group
    pre_match = re.search(
        r'<span class="[^"]*">\s*(\d{1,3}(?:,\d{3})*(?:\.\d+)?[KMBkmb]?)\s*</span>',
        before_group_html
    )

    if pre_match:
        value = pre_match.group(1)
        converted = convert_to_number(value)
        print("✅ First numeric <span> BEFORE role='group':")
        print(f"💬 Value: {value}")
        print(f"🔢 Converted: {converted}")
        print("-" * 40)
    else:
        print("❌ No numeric span found before role='group'.")

    # 2. Collect all matching spans AFTER role="group"
    matches = re.findall(
        r'(<span class="[^"]*">\s*(?:\d{1,3}(?:,\d{3})*(?:\.\d+)?[KMBkmb]?|\s*)\s*</span>)',
        after_group_html
    )

    if matches:
        print("✅ Matching <span> tags AFTER role='group':")
        for full_tag in matches:
            content_match = re.search(r'>(.*?)<', full_tag)
            if content_match:
                value = content_match.group(1).strip()
                if value:
                    numeric_value = convert_to_number(value)
                    print(f"💬 Tag: {full_tag}")
                    print(f"🔢 Value: {value} → {numeric_value}")
                else:
                    print(f"💬 Tag (empty or space): {full_tag}")
                print("-" * 40)
    else:
        print("❌ No matching <span> tags found after role='group'.")

# --- PART 1: Load a live page from X
driver = webdriver.Chrome()
url = "https://x.com/_alz3abi11/status/1912119572137906545/video/1"

try:
    driver.get(url)
    time.sleep(6)
    page_source = driver.page_source
    process_page_source(page_source, url)
except Exception as e:
    print(f"❌ Error loading live page: {str(e)}")
finally:
    driver.quit()

# --- PART 2: Loop through local tweet_*.html files
for i in range(1, 4):
    filename = f"tweet_{i}.html"
    print(f"\n📄 Processing {filename}...\n")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            page_source = file.read()
        process_page_source(page_source)
    except FileNotFoundError:
        print(f"❌ File {filename} not found.")
    except Exception as e:
        print(f"❌ Error reading {filename}: {str(e)}")

input("\nDone. Press Enter to exit...\n")
