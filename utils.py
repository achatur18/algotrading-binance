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