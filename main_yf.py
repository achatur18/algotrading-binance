from loguru import logger

logger.configure(extra={"table_id": "AT7UP01"})
logger.add("./publish_log.log",format="{extra[table_id]} - [{time}] - {message}", rotation="12:00", compression="gz")


from binance import Client
import config
from strategy import Strategy_1_5_15,Strategy_1_5_15_yf, Strategy_1_5_yf
from buy_sell import buy, sell
from utils import get_balance, get_price, available_quantity
import time
client = Client(config.APIKey, config.SecretKey, testnet =True)
import sys
import datetime as dt
# sys.stdout = open('output_{}.txt'.format(dt.datetime.now()),'wt')
symbol='BTCUSDT'
flag='SELL'

logger.info("Start!!!")
logger.info("Balance: {}".format(get_balance(client, "USDT")))
logger.info("Coin balance:  {}".format(get_balance(client, symbol[:-4])))
logger.info("Coin price: {}".format(get_price(client, symbol)))

while(True):
    flags = None
    while flags is None:
        try:   
            flags = Strategy_1_5_15_yf(flag=[True,True,True], index=-1)
        except:
            logger.info("Data fetching failed!!! ... Retrying again in 5 secs.")
            time.sleep(5)
            pass

    logger.info("Flag Info: {} - {}".format(dt.datetime.now(), flags))

    StrategyFlag = flags[0]
    for signal in flags:
        StrategyFlag=StrategyFlag and signal

    logger.info("{} - {}".format(flag, flags))
    if (flag=="SELL" and (StrategyFlag )):  # and (not prev_StrategyFlag)
        flag='BUY'
        quantity=1
        buy(client, symbol, quantity)
        logger.info("\n")
        logger.info("BUY!!!")
        logger.info("Balance: {}".format(get_balance(client, "USDT")))
        logger.info("Coin balance:  {}".format(get_balance(client, symbol[:-4])))
        logger.info("Coin price: {}".format(get_price(client, symbol)))
    elif (flag=="BUY" and (not StrategyFlag)):
        flag='SELL'
        quantity = available_quantity(client, symbol[:-4])
        print(quantity)
        sell(client, symbol, quantity)
        logger.info("\n")
        logger.info("SELL!!!")
        logger.info("Balance:  {}".format(get_balance(client, "USDT")))
        logger.info("Coin balance:  {}".format(get_balance(client, symbol[:-4])))
        logger.info("Coin price: {}".format(get_price(client, symbol)))
    else:
        logger.info("\n")
        logger.info("HOLD!!!")
        logger.info("Balance:  {}".format(get_balance(client, "USDT")))
        logger.info("Coin balance: {}".format(get_balance(client, symbol[:-4])))
        logger.info("Coin price: {}".format(get_price(client, symbol)))
    time.sleep(1)
    while(True):
        if time.time()%60<=2 and time.time()%60>1:
            break

                
        
