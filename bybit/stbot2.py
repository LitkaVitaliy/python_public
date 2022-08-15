from pybit import spot
from datetime import datetime
from time import sleep

API_KEY = '******************'
SECRET_API_KEY = '********************'
session = spot.HTTP(endpoint="https://api.bybit.com", api_key=API_KEY, api_secret=SECRET_API_KEY)

symbols = ['EOSUSDT', 'XRPUSDT', 'UNIUSDT', 'DOTUSDT', 'XLMUSDT', 'LTCUSDT',
           'DOGEUSDT', 'BITUSDT', 'ADAUSDT', 'XTZUSDT', 'AXSUSDT', 'DYDXUSDT',
           'GRTUSDT', 'SOLUSDT', 'OMGUSDT']


def is_order_open():
    return bool(session.query_active_order()['result'])  # есть ли открытые ордера


def trade():
    open_order = False
    symbol = 'XRPUSDT'
    period = '5m'  # период торговли
    buy_price = 0

    while True:

        klines = session.query_kline(symbol=symbol, interval=period, limit=100)['result']  # свечи
        prices = [float(price[4]) for price in klines]  # цены закрытия ордеров
        last_price = float(klines[-1][4])  # последняя цена закрытия ордера
        mean = round(sum(prices)/len(prices), 5)  # среднее значение цены закрытия

        # нет открытого ордера и последняя цена меньше ср. знач., можем покупать
        if not open_order and last_price <= mean:
            buy_price = last_price
            time = datetime.now().strftime('%m-%d %H:%M:%S')
            print(time, '[BUY]', symbol, buy_price)
            open_order = True

        if open_order:
            while True:
                klines = session.query_kline(symbol=symbol, interval=period, limit=100)['result']  # свечи
                last_price = float(klines[-1][4])  # последняя цена закрытия ордера

                if last_price > buy_price * (1 + 0.001 + 0.001):  # если ласт цена > цена покупки+коммисия + мин. навар
                    sell_price = last_price
                    time = datetime.now().strftime('%m-%d %H:%M:%S')
                    print(time, '[SELL]', symbol, sell_price, '\n')
                    open_order = False
                    break


def main():
    print('[START]')
    trade()


if __name__ == "__main__":
    main()
