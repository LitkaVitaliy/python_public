import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from openpyxl import load_workbook
from pprint import pprint


def get_data_from_main_page():
    header = Headers(headers=True).generate()
    main_url = f'https://superakb.ru/catalogue/category/akkumuliatory-starternye_315/?page={1}'
    res = requests.get(url=main_url, headers=header).text
    soup = BeautifulSoup(res, 'html5lib')
    items = soup.findAll('div', class_='row goods__catalogue') # .findAll('a')
    pprint(items)


if __name__ == "__main__":
    get_data_from_main_page()
