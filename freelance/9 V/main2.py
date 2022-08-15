import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint


def get_data_from_main_page():
    header = Headers(headers=True).generate()

    main_url = f'https://mediakit.iportal.ru/our-team'
    res = requests.get(url=main_url, headers=header).text
    soup = BeautifulSoup(res, 'lxml')
    # items = soup.find('div', {'id': 'allrecords'}).find('div', {'data-artboard-height': 380})
    i2 = soup.find('div', {'data-artboard-height': 380}).findAll('div', class_='tn-atom')

    for item in i2:
        pprint(item.text.split('  '))
    # print(items.text.replace('\n', ''))
    # l_items = []
    # for item in items:
    #     l_items.append(item.text.replace('\n', ''))
        # print(item.text.replace('\n', ''))

    # print(l_items)
    # for item in l_items:
    #     print(item)


if __name__ == "__main__":
    get_data_from_main_page()
