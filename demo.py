from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config
client = Client(config.APIKey, config.SecretKey, testnet =True)
from binance.enums import *
order=client.create_order(
    symbol='BTCUSDT',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=0.0004
)
# print(order)

# exc_info=client.get_exchange_info()

acc_info=client.get_account()
for bal in (acc_info['balances']):
    print(bal)

# info = client.get_symbol_info("BNBBTC")
# print(info)

# depth = client.get_order_book(symbol='BNBBTC')
# for i in depth:
#     print(i)

# candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)
# print(len(candles))
# for i in candles:
#     print(i)

# tickers = client.get_ticker(symbol='BNBBTC')
# tickers = client.get_orderbook_tickers()
# tickers = client.get_all_tickers()


# print(tickers.keys())
# for i in tickers:
#     print(tickers[i])


# cols=["Kline open time",
# "Open price",
# "High price",
# "Low price",
# "Close price",
# "Volume",
# "Kline close time",
# "Quote asset volume",
# "Number of trades",
# "Taker buy base asset volume",
# "Taker buy quote asset volume",
# "Unused field"]


# import pandas as pd
# df=pd.DataFrame(candles, columns=cols)
# print(df.head(5))
# print(df.shape)
# df.to_csv("data.csv")
