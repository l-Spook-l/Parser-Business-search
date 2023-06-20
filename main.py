import re
import openpyxl
import requests
from bs4 import BeautifulSoup


list_company = []
list_company_address = []
local_count_company = 0
page = 0
count_company = 0

city_1 = "kharkov"
city_2 = "dnepropetrovsk"
city_3 = "zaporizhzhe"

book = openpyxl.Workbook()
sheet = book.active

while True:
    response = requests.get(url=f"http://{city_3}.ukr-prom.com/?page={page}")
    page += 1

    src = response.text
    soup = BeautifulSoup(src, "lxml")

    company = soup.find_all("h3")

    for item in company:
        local_count_company += 1
        count_company += 1

        item_name = item.next_element.text  # Названия компании
        item_link = item.next.get("href")  # Cсылка
        company_page = requests.get(url=item_link)  # Получаем страницу компании
        src_2 = company_page.text
        soup_2 = BeautifulSoup(src_2, "lxml")
        company_address = soup_2.find(text=re.compile("Адрес")).find_next().text

        list_company_address.append(company_address.split())

        print(f"{item_name}: {' '.join(company_address.split())}")

        sheet[f"A{count_company}"] = item_name
        sheet[f"B{count_company}"] = ' '.join(company_address.split())
        book.save("Enterprises.xlsx")

    if local_count_company < 10:
        break
    local_count_company = 0

book.close()
print(len(list_company_address))
print(count_company)
