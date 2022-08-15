import time
import pandas as pd
import ta
from time import localtime, time, strftime, sleep
from collections import Counter
from indicators import *
from ta import trend
from ta import momentum
from pybit import spot

session = spot.HTTP(endpoint="https://api.bybit.com")

symbols = ['EOSUSDT', 'XRPUSDT', 'UNIUSDT', 'DOTUSDT', 'BTTUSDT', 'XLMUSDT', 'LTCUSDT',
           'DOGEUSDT', 'BITUSDT', 'ADAUSDT', 'XTZUSDT', 'AXSUSDT', 'DYDXUSDT', 'PERPUSDT',
           'GRTUSDT', 'SOLUSDT', 'OMGUSDT', 'LUNCUSDT', 'XRP3LUSDT',
           'XRP3SUSDT', 'BTC3SUSDT', 'BTC3LUSDT', 'ETH3SUSDT', 'ETH3LUSDT',
           'USDTDAI', 'USTCUSDT', 'MVUSDT', 'PORTUGALUSDT', 'GRPCUSDT', 'USDTETH', 'DFGUSDT', 'SOLOUSDT',
           'WERUSDT', 'SHIBUSDT',
           'SOL3SUSDT', 'SOL3LUSDT', 'FFFFUSDT', 'ZENUSDT', 'ICXUSDT', 'STXUSDT',
           'VINUUSDT', 'TRIBLUSDT', 'AVAXUSDT', 'SANDUSDT', 'BUSDUSDT', 'HNTUSDT']


def klines(symbol):
    df = pd.DataFrame(session.query_kline(symbol=symbol, interval="1m", timeout=120)['result'])
    df = df.iloc[:, :5]
    df.columns = ['Time', 'Open', 'High', 'Low', 'Close']
    df = df.set_index('Time')
    df.index = pd.to_datetime(df.index, unit='ms')
    df = df.astype(float)

    df['RSI'] = ta.momentum.rsi(df.Close, window=14)
    df['STOCH'] = ta.momentum.stoch(low=df.Low, high=df.High, close=df.Close, window=9, smooth_window=6)
    df['STOCHRSI'] = ta.momentum.stochrsi(close=df.Close, window=14)
    df['MACD'] = ta.trend.macd(close=df.Close, window_fast=12, window_slow=26)
    df['Signal'] = df.MACD.ewm(span=9).mean()
    df['WILLIAMSPR'] = ta.momentum.williams_r(high=df.High, low=df.Low, close=df.Close)
    df['CCI'] = ta.trend.cci(high=df.High, low=df.Low, close=df.Close, window=14)
    df['UltimOscil'] = ta.momentum.ultimate_oscillator(high=df.High, low=df.Low, close=df.Close)
    df['ROC'] = ta.momentum.roc(close=df.Close)

    df.dropna(inplace=True)
    return df


def main():
    buy_price = 0
    balance_usdt = 11
    qty = 10
    number_of_coins = 0
    open_order = False

    while True:

        # secs = strftime('%S', localtime(time()))

        # if secs == "01":
        try:
            for symbol in symbols:
                df = klines(symbol)

                ind_list = forecast(df)
                count = Counter(ind_list)

                for_sell = count[-1]
                for_buy = count[1]
                for_wait = count[0]

                res = max(for_sell, for_buy, for_wait)

                if res == for_buy and not open_order:
                    buy_price = df.Close.iloc[-1]
                    number_of_coins = qty * 0.9998 / buy_price

                    balance_usdt -= qty
                    open_order = True

                    print(number_of_coins)
                    print(f"{df.index[-1]}  [BUY {symbol}]\nPrice: {buy_price}\nSell by >: {buy_price * 1.005}")

                if open_order:
                    while True:
                        df = klines(symbol)

                        sell_price = df.Close.iloc[-1]
                        if sell_price >= buy_price * 1.005:
                            sold_for = number_of_coins * 0.9998 * sell_price

                            balance_usdt += sold_for
                            number_of_coins = 0
                            open_order = False
                            print(f"{df.index[-1]}  [SELL {symbol}]  Price: {sell_price}\n"
                                  f"Balance_usdt: {balance_usdt}\n"
                                  f"Earn: {balance_usdt - qty}\n\n")
                            break

        except Exception as err:
            print(err)
        # sleep(1)


if __name__ == "__main__":
    # start_time = time.time()
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
