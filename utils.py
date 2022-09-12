import pandas as pd

def get_balance(client, symbol):
    return float(round(float(client.get_asset_balance(asset=symbol).get('free')), 8))

def get_price(client, symbol):
    return float(round(float(client.get_symbol_ticker(symbol=symbol)['price']), 8))


def filter_df(df, true_range_threshold=200):
    high = df['High'].apply(float)
    low = df['Low'].apply(float)
    close = df['Close'].apply(float)

    # calculate ATR
    price_diffs = [high - low, 
                    high - close.shift(), 
                    close.shift() - low]

    true_range = pd.concat(price_diffs, axis=1)
    true_range = true_range.abs().max(axis=1)
    
    df=df[true_range<true_range_threshold]
    df.index=range(0, len(df))
    return df

def available_quantity(client, symbol):
    bal = str(get_balance(client, symbol))
    bals=bal.split(".")
    bal=float(bals[0]+"."+bals[1][:2])
    return bal

import datetime as dt
import yfinance as yf
def get_yf_data(symbol, interval, start = dt.datetime.now()-dt.timedelta(1), end = dt.datetime.now()):
    ohlc_data = yf.download(tickers=symbol,start=start,interval=interval)
    ohlc_data.columns=["open", "High", "Low", "Close", "adj close", "volume"]
    return ohlc_data
    