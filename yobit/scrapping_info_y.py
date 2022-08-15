import requests


def get_info():
    url = 'https://yobit.net/api/3/info'

    req = requests.get(url=url)
    data = req.text

    with open('info.txt', 'w') as file:
        file.writelines(data)

    return data


def get_ticker(coin1='btc', coin2='usd'):
    # url = 'https://yobit.net/api/3/ticker/btc_usd-eth_usd-xrp_usd?ignor_invalid=1'
    url = f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignor_invalid=1'

    req = requests.get(url=url)
    data = req.text

    with open('ticker.txt', 'w') as file:
        file.writelines(data)

    return data


def get_depth(coin1='btc', coin2='usd', limit=150):
    url = f'https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignor_invalid=1'

    req = requests.get(url=url)
    data = req.text

    with open('depth.txt', 'w') as file:
        file.writelines(data)

    bids = req.json()[f'{coin1}_{coin2}']['bids']
    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

    return f'Total bids: {total_bids_amount}$'


def get_trades(coin1='btc', coin2='usd', limit=150):
    url = f'https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignor_invalid=1'

    req = requests.get(url=url)
    data = req.text
    trades = req.json()

    with open('trades.txt', 'w') as file:
        file.writelines(data)

    total_trade_ask = 0
    total_trade_bid = 0

    for item in trades[f'{coin1}_{coin2}']:
        if item['type'] == 'ask':
            total_trade_ask += item['price'] * item['amount']
        elif item['type'] == 'bid':
            total_trade_bid += item['price'] * item['amount']
        else:
            print('Error???')

    info = f'[-] Total {coin1} SELL: {round(total_trade_ask, 2)}$\n[+] Total {coin1} BUY: {round(total_trade_bid, 2)}$'

    return info


def main():
    # print(get_info())
    print(get_ticker())
    # print(get_depth())
    # print(get_trades())


if __name__ == '__main__':
    main()
