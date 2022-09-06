from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config
from strategy import Strategy
from buy_sell import buy, sell
from utils import get_balance, get_price
import time
client = Client(config.APIKey, config.SecretKey, testnet =True)
import sys
import datetime as dt
# sys.stdout = open('output_{}.txt'.format(dt.datetime.now()),'wt')
symbol='BTCUSDT'
print("Start!!!")
flag='SELL'
while(True):
    if flag!="BUY" and Strategy(client, symbol):
        flag='BUY'
        # quantity_usdt = get_balance(client, "USDT")
        # quantity_usdt = 100000
        # price_symbol = get_price(client, symbol)+10
        # info = client.get_symbol_info(symbol)
        # maxQty=float(info['filters'][2]['maxQty'])
        # minQty=float(info['filters'][2]['minQty'])
        # quantity =float(round(float(quantity_usdt/price_symbol), 8))
        # quantity=min(quantity, maxQty)
        # quantity=max(quantity, minQty)
        quantity=1
        buy(client, symbol, quantity)
        print("\n")
        print("BUY!!!")
        print("Balance: ",  get_balance(client, "USDT"))
        print("Coin balance: ",  get_balance(client, symbol[:-4]))
    elif flag!="SELL" and (not Strategy(client, symbol)):
        flag='SELL'
        quantity = 1
        sell(client, symbol, quantity)
        print("\n")
        print("SELL!!!")
        print("Balance: ",  get_balance(client, "USDT"))
        print("Coin balance: ",  get_balance(client, symbol[:-4]))
    else:
        print("\n")
        print("HOLD!!!")
        print("Coin balance:", get_balance(client, symbol[:-4]))
        print("Coin price:", get_price(client, symbol))
    time.sleep(60)

                
        
