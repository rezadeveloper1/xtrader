# from binance.websockets import BinanceSocketManager
# from binance.depthcache import DepthCacheManager
# from binance.client import Client
# from django.conf import settings
# from data.models import StockWatch
# from finance import scan
# from data import redis
# import threading
# import json
# import time
#
#
# def process_ticker(msg):
#     event = '24hrTicker'
#     # print(event)
#     try:
#         if msg['e'] == event:
#             symbol = msg['s']
#             msg['lastupdate'] = get_time()
#             data = json.dumps(msg)
#             redis.hset(symbol, event, data)
#     except Exception as e:
#         print("process_ticker", e)
#
#
# def get_time():
#     return int(time.time() * 1000)
#
#
# def process_depth(dcm):
#     event = 'depth'
#     # print(event)
#     try:
#         symbol = dcm.symbol
#         data = json.dumps({
#             'bids': dcm.get_bids(),
#             'asks': dcm.get_asks(),
#             'lastupdate': get_time()
#         })
#         redis.hset(symbol, event, data)
#     except Exception as e:
#         print("process_depth", e)
#
#
# def process_kline(msg):
#     key = "OpenCandleTime"
#     current_candle_time = msg['k']['t']
#     try:
#         t = int(redis.get(key))
#     except Exception as e:
#         t = current_candle_time
#         redis.set(key, current_candle_time)
#     if current_candle_time > t:
#         redis.set(key, current_candle_time)
#         print('new candle')
#         time.sleep(5)
#         scan.screener()
#
#
# def stream():
#     print("stream")
#     # API_KEY = 'UVFWIL0JENoQmUfIadAcnLjhcXEVLzcoiQRdnw65WTpqQFiasthjnAbOHw61gVZ8'
#     # SECRET_KEY = 'YOR8uI3CKVrgTTBPl3jdVb94YoDHV9znjhc3sQUXWwkVTEIHZa6XZqrhuHrTfEOd'
#     # client = Client(API_KEY, SECRET_KEY)
#     client = Client()
#     bm = BinanceSocketManager(client)
#     symbols = StockWatch.objects.all()
#     symbol_ids = [symbol.SymbolId for symbol in symbols]
#     bm.start_kline_socket("BTCUSDT", callback=process_kline, interval=settings.CANDLES_INTERVAL)
#     for symbol_id in symbol_ids:
#         bm.start_symbol_ticker_socket(symbol_id, process_ticker)
#         DepthCacheManager(client=client, symbol=symbol_id, callback=process_depth, bm=bm)
#         print(symbol_id)
#
#
# def run_stream():
#     # stream()
#     print("run_stream")
#     try:
#         thread = threading.Thread(target=stream)
#         thread.start()
#     except Exception as e:
#         print("run_stream", e)
#         time.sleep(1)
#         run_stream()
