from fake_headers import Headers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

ser = Service('chromedriver/chromedriver.exe')
op = webdriver.ChromeOptions()
op.headless = True
driver = webdriver.Chrome(service=ser, options=op)

base_url = 'https://www.staff-clothes.com'
headers = Headers(headers=True).generate()


def main():
    try:
        url = input('URL: ')  # for ex. https://www.staff-clothes.com/ua/m/staff-tactical/c1114/
        driver.get(url=url)

        for i in range(800):
            driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.END)

        code = driver.page_source
        soup = BeautifulSoup(code, 'lxml')

        names = [item.text for item in soup.findAll('span', class_='product-card__info--title')]

        prices = [item.text for item in soup.findAll('span', class_='product-card__info--price')]

        sizes = [item.text for item in soup.findAll('span', class_='product-card__info--sizes')]

        urls = [base_url+item.find('a').get('href') for item in soup.findAll('div', class_='catalog__product-catalog')]

        df = pd.DataFrame()
        df['name'] = names
        df['size'] = sizes
        df['price'] = prices
        df['url'] = urls

        with open('csv_data.csv', 'w', encoding='UTF-8', newline='') as csv_file:
            df.to_csv(path_or_buf=csv_file)

        print('DONE!')

    except Exception as err:
        print(err)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
