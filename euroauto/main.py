import pandas as pd
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

url = 'https://spb.euroauto.ru/autoservice/'
info = []
start = int(input('start: '))
end = int(input('end: '))
filename = str(input('filename: '))


def parse(p_range, c_range, m_range, g_range):
    global p, c, m, g
    try:
        header = Headers(headers=True).generate()
        res = requests.get(url, headers=header).text
        soup = BeautifulSoup(res, 'lxml')
        parts = [item.text for item in soup.find('select', {'id': 'spare_part'}).findAll('option')]
        parts_value = [item.get('value') for item in soup.find('select', {'id': 'spare_part'}).findAll('option')]

        for p in range(p_range, end):
            try:
                url_ = f'https://spb.euroauto.ru/autoservice/{parts_value[p]}'
                res = requests.get(url_, headers=header, timeout=120).text
                soup = BeautifulSoup(res, 'lxml')
                cars = [item.text for item in soup.find('select', {'data-next': 'select_model'}).findAll('option')]
            except AttributeError:
                continue
            for c in range(c_range, len(cars)):
                try:
                    url_ = f'https://spb.euroauto.ru/autoservice/{parts_value[p]}/{cars[c]}'
                    res = requests.get(url_, headers=header, timeout=120).text
                    soup = BeautifulSoup(res, 'lxml')
                    items = soup.find('select', {'data-next': 'select_modification'})
                    marks = [item.text for item in items.findAll('option') if items is not None]
                    marks_value = [item.get('value') for item in items.findAll('option') if items is not None]
                except AttributeError:
                    continue

                for m in range(m_range, len(marks)):
                    try:
                        url_ = f'https://spb.euroauto.ru/autoservice/{parts_value[p]}/{cars[c]}/{marks_value[m]}'
                        res = requests.get(url_, headers=header, timeout=120).text
                        soup = BeautifulSoup(res, 'lxml')
                        gen = [item.text for item in soup.find('select', {'name': 'modification_urn'}).findAll('option')]
                        gen_value = [item.get('value') for item in soup.find('select',
                                                                             {'name': 'modification_urn'}).findAll(
                            'option')]
                    except AttributeError:
                        continue

                    for g in range(g_range, len(gen)):
                        try:
                            url_ = f'https://spb.euroauto.ru/autoservice/{parts_value[p]}/{cars[c]}/{marks_value[m]}/{gen_value[g]}'
                            res = requests.get(url_, headers=header, timeout=120).text
                            soup = BeautifulSoup(res, 'lxml')
                            try:
                                price = ' '.join([item.text for item in soup.findAll('h3')][1].split())
                                time = ' '.join([item.text for item in soup.findAll('h3')][2].split())
                            except:
                                price = '-'
                                time = '-'

                            if price == 'Запишитесь на диагностику!':
                                price = '-'
                            if time == 'Откройте франшизу Euroauto!':
                                time = '-'

                            info.append([parts[p], cars[c], marks[m], gen[g], price, time])
                        except AttributeError:
                            continue

                        df = pd.DataFrame(info)

                        with open(f'{filename}.csv', 'w', encoding='UTF-8', newline='') as csv_file:
                            df.to_csv(path_or_buf=csv_file)
            print(parts[p], p)
    except:
        parse(p_range=p, c_range=c, m_range=m, g_range=g)


def main():
    parse(p_range=start, c_range=1, m_range=1, g_range=1)
    print('DONE!!')


if __name__ == '__main__':
    main()
