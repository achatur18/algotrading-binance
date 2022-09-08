import pandas as pd
from supertrend import Supertrend
from binance import Client


cols=["Kline open time",
"Open price",
"High",
"Low",
"Close",
"Volume",
"Kline close time",
"Quote asset volume",
"Number of trades",
"Taker buy base asset volume",
"Taker buy quote asset volume",
"Unused field"]

def Strategy_1_5_15(client, symbol='BTCUSDT', flag=False):
    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1MINUTE)
    df_1=pd.DataFrame(candles, columns=cols)
    flag_1=Supertrend(df_1, ewm=False)
    flag_1=flag_1['Supertrend'][len(flag_1)-1]


    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_5MINUTE)
    df_5=pd.DataFrame(candles, columns=cols)
    flag_5=Supertrend(df_5, ewm=False)
    flag_5=flag_5['Supertrend'][len(flag_5)-1]

    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_15MINUTE)
    df_15=pd.DataFrame(candles, columns=cols)
    flag_15=Supertrend(df_15, ewm=False)
    flag_15=flag_15['Supertrend'][len(flag_15)-1]

    if flag:
        return flag_1, flag_5,  flag_15

    return flag_1 and flag_5 and flag_15


def Strategy_5_15(client, symbol='BTCUSDT', flag=False):
    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_5MINUTE)
    df_5=pd.DataFrame(candles, columns=cols)
    flag_5=Supertrend(df_5, ewm=False)
    flag_5=flag_5['Supertrend'][len(flag_5)-1]

    candles = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_15MINUTE)
    df_15=pd.DataFrame(candles, columns=cols)
    flag_15=Supertrend(df_15, ewm=False)
    flag_15=flag_15['Supertrend'][len(flag_15)-1]

    if flag:
        return flag_5,  flag_15

    return flag_5 and flag_15