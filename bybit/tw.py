from tradingview_ta import TA_Handler, Interval
from datetime import datetime
from time import sleep

symbols = ['EOSUSDT', 'XRPUSDT', 'UNIUSDT', 'DOTUSDT', 'XLMUSDT', 'LTCUSDT',
           'DOGEUSDT', 'BITUSDT', 'ADAUSDT', 'XTZUSDT', 'AXSUSDT', 'DYDXUSDT',
           'GRTUSDT', 'SOLUSDT', 'OMGUSDT']


def get_time():
    return datetime.now().strftime('%m-%d %H:%M:%S')


def trade():
    open_order = False

    while True:
        try:

            for symbol in symbols:
                anal = TA_Handler(
                    symbol=symbol,
                    screener="crypto",
                    exchange="ByBit",
                    interval=Interval.INTERVAL_5_MINUTES
                )
                res = anal.get_analysis().summary['RECOMMENDATION']

                if not open_order and res == 'BUY':
                    time = get_time()
                    buy_price = anal.get_analysis().indicators['close']
                    print(time, symbol, res, buy_price)
                    open_order = True

                if open_order:
                    while True:
                        res = anal.get_analysis().summary['RECOMMENDATION']
                        sell_price = anal.get_analysis().indicators['close']
                        if res == 'SELL' and sell_price >= buy_price:
                            time = get_time()
                            print(time, symbol, res, sell_price, '\n')
                            open_order = False
                            break

                        sleep(300)

        except Exception as err:
            print(err)


trade()
