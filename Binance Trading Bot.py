import json
from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException
import time
from binance import Client
symbol="CRVUSDT"

from binance import ThreadedWebsocketManager
from binance.enums import *
import openpyxl
m={}
api_key=""
api_secret=""
client=Client(api_key,api_secret)
def main():

    ws = None
    thread = None
    thread_running = False
    thread_keepalive = None

    def websocket_thread():
        global ws
        global m
        timee = 0
        ws = create_connection("wss://stream.binance.com:9443/ws")
        ws.send(
            json.dumps(
                {
                    "method": "SUBSCRIBE",
                    "params": ["crvusdt@miniTicker"],
                    "id": 1,
                }
            )
        )

        thread_keepalive.start()
        while not thread_running:
            try:
                data = ws.recv()
                if data != "":
                    msg = json.loads(data)
                else:
                    msg = {}
            except ValueError as e:
                print(e)
                print("{} - data: {}".format(e, data))
            except Exception as e:
                print(e)
                print("{} - data: {}".format(e, data))
            else:
                if "result" not in msg:
                    print("p")
                    if timee==0:
                        client.order_market_buy(
                            symbol=symbol,
                            quoteOrderQty=client.get_asset_balance(asset='USDT')['free'])
                        price=float(msg['c'])
                        timee=1
                        print("Buy Executed")
                    if timee==1 and ((float(msg['c'])-price)*100/price)>2:
                        info = client.get_symbol_info(symbol)
                        minQty = float(info['filters'][2]['minQty'])
                        precision = 0
                        while (10 ** (-(precision)) != minQty):  # precision is basically power to 10.
                            precision = precision + 1
                        client.order_market_sell(
                            symbol=symbol,
                            quantity=(int((float(msg['c'])) * (10 ** precision))) / 10 ** precision
                        )
                        print("Sell Executed")
        try:
            if ws:
                ws.close()
        except WebSocketConnectionClosedException:
            pass
        finally:
            thread_keepalive.join()

    def websocket_keepalive(interval=30):
        global ws
        while ws.connected:
            ws.ping("keepalive")
            time.sleep(interval)

    thread = Thread(target=websocket_thread)
    thread_keepalive = Thread(target=websocket_keepalive)
    thread.start()


if __name__ == "__main__":
    main()




