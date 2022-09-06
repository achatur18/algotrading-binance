from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config
from strategy import Strategy
from buy_sell import buy, sell
from utils import get_balance
client = Client(config.APIKey, config.SecretKey, testnet =True)

symbol='BTCUSDT'
# quantity=50
eth_price=client.get_symbol_ticker(symbol=symbol)
quantity = get_balance(client, symbol)
quantity=1
print(quantity, eth_price)
# print(sell(client, symbol, quantity), quantity)

# acc_info=client.get_account()
# for bal in (acc_info['balances']):
#     print(bal)

# print(Strategy(client))