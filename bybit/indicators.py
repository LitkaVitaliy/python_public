

def rsi(df):
    if df.RSI[-1] > 70:
        return -1  # sell
    elif df.RSI[-1] < 30:
        return 1  # buy
    else:
        return 0  # wait


def stoch(df):
    if df.STOCH[-1] > 80:
        return -1  # sell
    elif df.STOCH[-1] < 20:
        return 1  # buy
    else:
        return 0  # wait


def stochrsi(df):
    if df.STOCHRSI[-1] > .8:
        return -1  # sell
    elif df.STOCHRSI[-1] < .2:
        return 1  # buy
    else:
        return 0  # wait


def macd(df):
    if df.MACD.iloc[-1] - df.Signal.iloc[-1] > 0 > df.MACD.iloc[-2] - df.Signal.iloc[-2]:
        return 1
    elif df.MACD.iloc[-1] - df.Signal.iloc[-1] < 0 < df.MACD.iloc[-2] - df.Signal.iloc[-2]:
        return -1
    else:
        return 0


def william_r(df):
    if df.WILLIAMSPR[-1] > -20:
        return -1  # sell
    elif df.WILLIAMSPR[-1] < -80:
        return 1  # buy
    else:
        return 0  # wait


def cci(df):
    if df.CCI[-1] > 100:
        return -1  # sell
    elif df.CCI[-1] < -100:
        return 1  # buy
    else:
        return 0  # wait


def ultim_oscil(df):
    if df.UltimOscil[-1] > 70:
        return -1  # sell
    elif df.CCI[-1] < 30:
        return 1  # buy
    else:
        return 0  # wait


def roc(df):
    if df.ROC[-1] < 0:
        return -1  # sell
    elif df.ROC[-1] > 0:
        return 1  # buy
    else:
        return 0  # wait


def forecast(df):
    rsi_val = rsi(df)
    stoch_val = stoch(df)
    stochrsi_val = stochrsi(df)
    macd_val = macd(df)
    william_r_val = william_r(df)
    cci_val = cci(df)
    ultim_oscil_val = ultim_oscil(df)
    roc_val = roc(df)

    ind_list = [rsi_val, stoch_val, stochrsi_val, macd_val, william_r_val, cci_val, ultim_oscil_val, roc_val]

    return ind_list
