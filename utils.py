def get_balance(client, symbol):
    return float(round(float(client.get_asset_balance(asset=symbol).get('free')), 8))

def get_price(client, symbol):
    return float(round(float(client.get_symbol_ticker(symbol=symbol)['price']), 8))