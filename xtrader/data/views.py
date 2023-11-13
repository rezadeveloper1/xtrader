# from xtrader import localsetting as local
import json
# from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from data.models import StockWatch as Symbol
from django.http import JsonResponse
from data import redis
from finance.models import Strategy
import pandas as pd
from data import stockwatch as stockwatchModel


def history(request):
    symbol_ids = redis.keys()
    histories = []
    for symbol_id in symbol_ids:
        symbol_id = symbol_id.decode()
        symbol_history_dict = {}
        symbol_history_dict[symbol_id] = {}
        for key in ['date', 'close', 'open', 'high', 'low', 'volume']:
            try:
                symbol_history_dict[symbol_id][key] = redis.hget(name=symbol_id, key=key)
            except Exception:
                pass
        histories.append(symbol_history_dict)
    return HttpResponse(json.dumps(histories))


def stockwatch(request, SymbolId):
    # stock = Symbol.objects.filter(SymbolId=SymbolId).first()
    # return HttpResponse(json.dumps(stock.read()))

    stock = stockwatchModel.stockWatchInfo(SymbolId, eps=True)
    return HttpResponse(json.dumps(stock))


def symbol_search(request, query):
    spots = redis.hgetall("exchangeInfo")
    symbols = [symbol for symbol in spots if query.upper() in symbol]
    result = []
    for symbol in symbols:
        info = redis.hget("exchangeInfo", symbol)
        result.append(dict(
            symbol_id=symbol,
            kind=info['quoteAsset'],
            category=info['baseAsset'],
            symbol_name=symbol,
            name=', '.join(info['permissions']),
            description='self.CompanyName',
            title='title',
        ))
    return HttpResponse(json.dumps({'items': result}, ensure_ascii=False).encode("utf8"),
                        content_type="application/json; charset=utf-8")
    # symbols = Symbol.objects.filter(InstrumentName__istartswith=query)
    # # | Symbol.objects.filter(mabna_english_name__icontains=query) \
    # # | Symbol.objects.filter(name__icontain=query)
    # symbol_max_results = 10
    # if symbols.count() < symbol_max_results:
    #     symbols = symbols | Symbol.objects.filter(InstrumentName__icontains=query)
    # results = [ob.as_json() for ob in symbols]
    # mydict = dict(
    #     items=results,
    # )
    # return HttpResponse(json.dumps(mydict, ensure_ascii=False).encode("utf8"),
    #                     content_type="application/json; charset=utf-8")


def get_data(request, symbol_id, interval):
    data_dict = redis.load_history(symbol_id, interval=interval)
    df = pd.DataFrame(data=data_dict, index=data_dict['date'])
    df = df.loc[:, ['date', 'open', 'high', 'low', 'close', 'volume']]
    pair = redis.hget("exchangeInfo", symbol_id.upper())
    stock_information = dict(
        per_name=pair['baseAsset'],
        measurement_name=pair['symbol'],
        name=pair['baseAsset'],
    )
    stock_history = df.to_json(orient='values')
    stock_information['items'] = stock_history

    # stock_information = dict(
    #     per_name="بیت کوین",
    #     measurement_name=,
    #     name="bitcoin",
    #     items=df.to_json(orient='values')
    # )
    # stock_information['items'] = json.dumps(data_dict)
    return JsonResponse(json.dumps(stock_information), safe=False)


def get_symbols(request):
    symbols = Symbol.objects.all()
    symbol_ids = [symbol.SymbolId for symbol in symbols]
    return JsonResponse({'symbols': symbol_ids})


def get_all_symbols(request):
    spots = redis.hgetall("exchangeInfo")
    symbols = [{'title': symbol} for symbol in spots]
    return JsonResponse({'symbols': symbols})


def get_intervals(request):
    if not request.user.username:
        return JsonResponse({'intervals': settings.INTERVALS})
    strategy = Strategy.objects.filter(trader=request.user).first()
    interval = strategy.interval if strategy else '4h'
    return JsonResponse({'intervals': settings.INTERVALS, 'userTimeFrame': interval})
