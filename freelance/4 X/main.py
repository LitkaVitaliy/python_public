import requests

from requests import Session
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from pprint import pprint
from proxy import proxies
from math import floor


def create_urls_from_xlsx():
    main_filename = 'main.xlsx'
    main_wb = load_workbook(main_filename)
    main_sheet = main_wb["Sheet1"]

    urls = []
    for i in range(2, 220794):
        car = main_sheet[f'A{i}'].value
        model = main_sheet[f'B{i}'].value
        search = main_sheet[f'C{i}'].value.replace(' ', '+')

        param = [search, car, model]
        site = f'https://www.farpost.ru/zapchasti/+/{param[0]}/model/{param[1]}+{param[2]}/'
        urls.append(site)

    return urls


def get_info_from_site():
    n = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Authorization': 'Bearer d1010d86244a2895e25e47e10d696b46290e2a92',
    }

    cookies = {
        '_gid': 'GA1.2.876007125.1658409330',
        '_ga': 'GA1.2.1762043390.1658409330',
        'last_search_auto_compatibility': 'model%3D%25D2%25E0%25E3%25C0%25C7%2B%25D2%25E0%25E3%25E5%25F0',
        'ring': 'c8332aa8f9a154e11416904e94221be4'
    }

    # for url in urls:
    session = Session()
    response = session.get(url='https://www.farpost.ru/zapchasti/+/электроусилитель руля/model/ТагАЗ+Тагер', headers=headers, cookies=cookies)
    return response.text


def main():
    # urls = create_urls_from_xlsx()
    print(get_info_from_site())


if __name__ == '__main__':
    main()
