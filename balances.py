from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import config

client = Client(config.APIKey, config.SecretKey, testnet =True)

acc_info=client.get_account()
for bal in (acc_info['balances']):
    print(bal)

# print(client.get_asset_balance(asset='BTC'))