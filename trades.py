from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config
from strategy import Strategy
from buy_sell import buy, sell
client = Client(config.APIKey, config.SecretKey, testnet =True)
for trade in client.get_my_trades(symbol='ETHUSDT'):
    print(trade)