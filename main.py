from loguru import logger

logger.configure(extra={"table_id": "AT7UP01"})
logger.add("./publish_log.log",format="{extra[table_id]} - [{time}] - {message}", rotation="12:00", compression="gz")


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
logger.info("Start!!!")
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
        logger.info("\n")
        logger.info("BUY!!!")
        logger.info("Balance: {}".format(get_balance(client, "USDT")))
        logger.info("Coin balance:  {}".format(get_balance(client, symbol[:-4])))
    elif flag!="SELL" and (not Strategy(client, symbol)):
        flag='SELL'
        quantity = 1
        sell(client, symbol, quantity)
        logger.info("\n")
        logger.info("SELL!!!")
        logger.info("Balance:  {}".format(get_balance(client, "USDT")))
        logger.info("Coin balance:  {}".format(get_balance(client, symbol[:-4])))
    else:
        logger.info("\n")
        logger.info("HOLD!!!")
        logger.info("Coin balance: {}".format(get_balance(client, symbol[:-4])))
        logger.info("Coin price: {}".format(get_price(client, symbol)))
    time.sleep(60)

                
        
