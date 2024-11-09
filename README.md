# Simple Web Python Parser

This project is a simple web scraper using Beautiful Soup library in Python. It allows you to extract the necessary information from HTML and present it in a convenient form. This project is an UrFU homework.

## Description 

Web Parser downloads the HTML content of a web page. It uses Beautiful Soup, lxml and requests to find and extract elements according to specified rules. This can be useful for extracting text, links, and other data from web pages. This parser also places all extracted data in the ```.txt``` file.

## Setup

Before you begin, make sure you have Python 3.6 or higher installed. Then run the following commands:

```
pip install beautifulsoup4
pip install requests
pip install lxml
```

## Usage

This code below shows how it's working. This project also has simple error handlers.

```python
import requests
from bs4 import BeautifulSoup

base_url = "http://www.encspb.ru/object/2816946435/D_1803401815/{}?lc=ru"

def parse_page(page_number, file):

  url = base_url.format(page_number, file)
  print(f"Loading page {page_number}: {url}")

  response = requests.get(url)

  if response.status_code == 200:
    src = response.text

    soup = BeautifulSoup(src, "lxml")

    name_decemberist_tables = soup.find_all("table", class_="table")

    cleaned_texts = []

    for table in name_decemberist_tables:
      text = table.get_text(separator=' ', strip=True)
      file.write(f"Page {page_number}:\n{text}\n\n")

      cleaned_texts.append(text)

    for text in cleaned_texts:
      print(text)
  else:
    print(f"Error loading page {page_number}: {response.status_code}")

with open("results.txt", "w", encoding="utf-8") as file:
    for page in range(1, 13):
```

## Settings

Customize the correct URL and filters to extract the data you want from different pages. If you need to extract any other elements, use Beatiful Soup methods such as ```soup.find()``` and ```soup.find_all()``` with the necessary arguments.

## License 

This project released under the MIT License.