import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

search = 'Мастер-маникюра'

driver = webdriver.Chrome(service=Service('chromedriver/chromedriver.exe'))
driver.maximize_window()

headers = {
    'Accept': '*/*',
    'Host': 'www.olx.ua',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode    ': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'X-Platform-Type': 'mobile-html5',
    'Authorization': 'Bearer d1010d86244a2895e25e47e10d696b46290e2a92',
}


def write_xlsx(result):
    pass


def get_name_phone(url_list):

    r = requests.get(url_list[0], headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    name = soup.find('h4', class_='css-1rbjef7-Text eu5v0x0').get_text()
    pprint(name)

    try:
        driver.get('https://www.olx.ua/d/uk/obyavlenie/naraschivanie-manikyur-pedikyur-depilyatsiya-harkovskoe-shosse-IDBm2nt.html')
        sleep(3)
        cookie_btn = driver.find_element(By.CLASS_NAME, 'css-wqpdas-BaseStyles')
        cookie_btn.click()
        phone_btn = driver.find_element(By.CLASS_NAME, 'css-65ydbw-BaseStyles')
        phone_btn.click()

        phone = soup.find()
        pprint(phone)
        sleep(30)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_data_from_main_page():
    page = 1
    site = 'https://www.olx.ua'
    main_url = f'https://www.olx.ua/d/uk/kiev/q-{search}/?page={page}'

    url_list = []  # хранит в себе список юрл с страницы
    city_list = []
    area_list = []

    r = requests.get(main_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    title = soup.findAll('h6', class_='css-v3vynn-Text eu5v0x0')
    urls = soup.findAll('a', class_='css-1bbgabe')  # все юрл
    geos = soup.findAll('p', class_='css-p6wsjo-Text eu5v0x0')  # все гео

    [url_list.append(site + url['href']) for url in urls]
    [city_list.append(geo.get_text().split(' ')[0][:-1]) for geo in geos]
    [area_list.append(geo.get_text().split(' ')[1]) for geo in geos]

    pprint(url_list[0])
    pprint(city_list[0])
    pprint(area_list[0])
    pprint(title[0].get_text())

    get_name_phone(url_list)


get_data_from_main_page()
