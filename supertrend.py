import pandas as pd
import numpy as np

def Supertrend(df, atr_period=10, multiplier=5.0, ewm=False, param=1):
    
    high = df['High'].apply(float)
    low = df['Low'].apply(float)
    close = df['Close'].apply(float)
    
    # calculate ATR
    price_diffs = [high - low, 
                    high - close.shift(), 
                    close.shift() - low]
    true_range = pd.concat(price_diffs, axis=1)
    true_range = true_range.abs().max(axis=1)
    # default ATR calculation in supertrend indicator
    if ewm:
        atr = true_range.ewm(alpha=1/atr_period,min_periods=atr_period).mean() 
    # elif :
    #     atr = true_range.ewm(span=param,min_periods=atr_period).mean() 
    else:
        atr = true_range.ewm(com=param,min_periods=atr_period).mean() 
    
    # HL2 is simply the average of high and low prices
    hl2 = (high + low) / 2
    # upperband and lowerband calculation
    # notice that final bands are set to be equal to the respective bands
    final_upperband = upperband = hl2 + (multiplier * atr)
    final_lowerband = lowerband = hl2 - (multiplier * atr)
    
    # initialize Supertrend column to True
    supertrend = [True] * len(df)
    
    for i in range(1, len(df.index)):
        curr, prev = i, i-1
        
        # if current close price crosses above upperband
        if close[curr] > final_upperband[prev]:
            supertrend[curr] = True
        # if current close price crosses below lowerband
        elif close[curr] < final_lowerband[prev]:
            supertrend[curr] = False
        # else, the trend continues
        else:
            supertrend[curr] = supertrend[prev]
            
            # adjustment to the final bands
            if supertrend[curr] == True and final_lowerband[curr] < final_lowerband[prev]:
                final_lowerband[curr] = final_lowerband[prev]
            if supertrend[curr] == False and final_upperband[curr] > final_upperband[prev]:
                final_upperband[curr] = final_upperband[prev]

        # to remove bands according to the trend direction
        if supertrend[curr] == True:
            final_upperband[curr] = np.nan
        else:
            final_lowerband[curr] = np.nan
    
    return pd.DataFrame({
        'Supertrend': supertrend,
        'Final Lowerband': final_lowerband,
        'Final Upperband': final_upperband
    }, index=df.index)
def tr(data):
    data['previous_close'] = data['close'].shift(1)
    data['high-low'] = abs(data['high'] - data['low'])
    data['high-pc'] = abs(data['high'] - data['previous_close'])
    data['low-pc'] = abs(data['low'] - data['previous_close'])

    tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)

    return tr

def atr(data, period):
    data['tr'] = tr(data)
    atr = data['tr'].rolling(period).mean()

    return atr

def supertrend(df, period=10, atr_multiplier=5):
    df['low']=df['Low'].apply(float)
    df['high']=df['High'].apply(float)
    df['close']=df['Close'].apply(float)
    hl2 = (df['high'] + df['low']) / 2
    df['atr'] = atr(df, period)
    df['Final Upperband'] = hl2 + (atr_multiplier * df['atr'])
    df['Final Lowerband'] = hl2 - (atr_multiplier * df['atr'])
    df['Supertrend'] = True

    for current in range(1, len(df.index)):
        previous = current - 1

        if df['close'][current] > df['Final Upperband'][previous]:
            df['Supertrend'][current] = True
        elif df['close'][current] < df['Final Lowerband'][previous]:
            df['Supertrend'][current] = False
        else:
            df['Supertrend'][current] = df['Supertrend'][previous]

            if df['Supertrend'][current] and df['Final Lowerband'][current] < df['Final Lowerband'][previous]:
                df['Final Lowerband'][current] = df['Final Lowerband'][previous]

            if not df['Supertrend'][current] and df['Final Upperband'][current] > df['Final Upperband'][previous]:
                df['Final Upperband'][current] = df['Final Upperband'][previous]
        
    return df