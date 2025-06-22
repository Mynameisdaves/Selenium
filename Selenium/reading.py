from PIL import Image
import pytesseract
import re

#citation: https://cloudinary.com/guides/web-performance/extract-text-from-images-in-python-with-pillow-and-pytesseract 
def extract_stats(image_path, numbers):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    for line in text.splitlines():
        line = line.strip()
        if re.search(r'[a-zA-Zก-๙]', line):
            continue
        line_numbers = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:\.\d+)?', line)
        for n in line_numbers:
            cleaned = int(n.replace(',', '').replace('.', '')) if '.' in n else int(n.replace(',', '').replace('.', ''))
            numbers.append(cleaned)

    labels = ["views", "likes", "comments", "shares"]
    for i in range(min(4, len(numbers))):
        print(f"numbers[{i}] {labels[i]}: {numbers[i]}")


numbers = []
print(extract_stats('Individual_stats/screenshot_7489161696720784658.png', numbers))



