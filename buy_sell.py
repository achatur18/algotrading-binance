from binance.enums import *


def buy(client, symbol='BNBBTC', quantity=0.1):
    return client.create_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )

def sell(client, symbol='BNBBTC', quantity=0.1):
    return client.create_order(
        symbol=symbol,
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )
