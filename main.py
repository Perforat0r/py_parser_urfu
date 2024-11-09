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
        parse_page(page, file)