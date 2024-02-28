import csv
import os
import re
from openpyxl import Workbook

def extract_urls(path):
    urls = set()
    with open(path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for value in row:
                if 'url' in value and 'tag' not in value and '@' in value:
                    match = re.search(r'url:"(.*?)"', value)

                    if match:
                        url = match.group(1)

                        if url[-1].isdigit():
                            # diagnostic print statement
                            #print("url: ", value)
                            urls.add(match.group(1))
    return urls

def main():
    path = 'D:/499_data'
    index = 1
    wb = Workbook()
    ws = wb.active
    directory = os.fsencode(path)
    urls = set()

    ids = set()
    for file in os.listdir(directory):
        csv_path = os.path.join(directory, file)
        if os.path.isfile(csv_path):
            print(index, "   ", csv_path)
            index += 1
            urls = extract_urls(csv_path)

    # prints urls to console for me to open
    print(urls)

if __name__ == "__main__":
    main()
