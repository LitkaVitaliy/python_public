import requests

base = 'https://fapi.binance.com'
path = '/fapi/v1/ticker/price'
param = {'symbol': 'BTCUSDT'}
url = base + path


def getPrice():
    r = requests.get(url, params=param)
    if r.status_code == 200:
        data = r.json()
        return data
    else:
        print("Some error")


while True:
    with open('pr.txt', 'a') as file:
        file.write(f'{float(getPrice()["price"])}, {getPrice()["time"]}\n')
