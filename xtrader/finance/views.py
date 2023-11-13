from finance import notification, oms, data_handling, volume, data_handling as dh, indicator
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from aum.models import Fund
import json
from finance import strategy, scan, marketwatch
# from finance import data_handling as dh, indicator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseNotFound
from accounts.forms import AuthenticationForm
import requests as r
from data.backup import filters_data
# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import inspect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from datetime import datetime
from finance.models import TradingView, Watchlist, WatchlistSymbol
import requests
from sales.models import Subscription
from django.conf import settings
import time
import threading

all_functions = dict(inspect.getmembers(data_handling, inspect.isfunction))


def calculate_indicators(request, interval):
    data = json.loads(request.GET['param'])
    kind = data['kind'].lower()
    function = all_functions['give_result_' + kind]
    result = function(data, interval=interval)
    return JsonResponse(result, safe=False)


@login_required(login_url='accounts:userena_signin')
@csrf_exempt
def add_new_watch_list(request):
    if not request.method == "POST":
        return JsonResponse({}, status=403)
    if strategy.get_watchlist_counts(request.user) + 1 > strategy.get_pack_limit(request.user)['watchlist']:
        return JsonResponse(
            {'redirect': '/profile/setup/?s=packages', 'm': 'برای ساخت واچ‌لیست جدید نیاز به ارتقا اشتراک دارید',
             's': 302})
    watchlist_name = request.POST.get('name', '')
    if not watchlist_name:
        return JsonResponse({'m': 'name is empty', 's': 403})
    user = request.user
    if not user:
        return JsonResponse({'m': 'login required', 's': 403})
    if Watchlist.objects.filter(user=user, name=watchlist_name):
        return JsonResponse({'m': 'نام واچ‌لیست تکراری است', 's': 403})
    watchlist = Watchlist(user=user, name=watchlist_name)
    watchlist.save()
    return JsonResponse({'id': watchlist.id, 's': 200})


@login_required(login_url='accounts:userena_signin')
def get_watch_lists(request):
    if not request.method == "GET":
        return JsonResponse({}, status=403)
    user = request.user
    if not user:
        return JsonResponse({'m': 'login required', 's': 403})
    watchlist_id = request.GET.get('id', '')
    if not watchlist_id:
        watchlists = Watchlist.objects.filter(user=user).order_by('-id')
        result = []
        for watchlist in watchlists:
            result.append({
                'id': watchlist.id,
                'name': watchlist.name,
            })
        result.append({
            'id': 0,
            'name': 'پیش فرض',
        })
        return JsonResponse({'watchlists': result, 'type': 'list', 's': 200})
    else:
        if request.GET.get('action', 'add') == 'remove':
            if watchlist_id == '0':
                return JsonResponse({'m': ' حذف واچ لیست پیش فرض امکانپذیر نیست.', 's': 403})
            Watchlist.objects.filter(user=user, id=watchlist_id).delete()
            return JsonResponse({
                's': 200
            })
        else:
            return JsonResponse({
                'symbols': WatchlistSymbol.get_symbols(watchlist_id),
                's': 200
            })
    # return JsonResponse({'watchlists': [], 'm': 'واچ لیست یافت نشد', 's': 403})


@login_required(login_url='accounts:userena_signin')
def update_symbol2watchlist(request):
    if not request.method == "GET":
        return JsonResponse({}, status=403)
    user = request.user
    if not user:
        return JsonResponse({'m': 'login required', 's': 403})
    watchlist_id = request.GET.get('watchListId', '')
    symbol = request.GET.get('symbol', 'BTCUSDT')
    action = request.GET.get('action', 'add')
    if watchlist_id == '0':
        return JsonResponse({'m': 'امکان حذف یا اضافه کردن نماد به واچ لیست پیش فرض وجود ندارد', 's': 403})
    watchlist = Watchlist.objects.filter(user=user, id=watchlist_id).first()
    if not watchlist:
        return JsonResponse({'m': 'آیدی واچ لیست اشتباه است', 's': 403})
    if action == 'add':
        if WatchlistSymbol.objects.filter(watchlist=watchlist, symbol=symbol).first():
            return JsonResponse({'m': 'نماد قبلا به واچ لیست اضافه شده است.', 's': 403})
        else:
            WatchlistSymbol(watchlist=watchlist, symbol=symbol).save()
            return JsonResponse({'m': 'نماد به واچ لیست اضافه شد.', 's': 200})
    elif action == 'remove':
        WatchlistSymbol.objects.filter(watchlist=watchlist, symbol=symbol).delete()
        return JsonResponse({'m': 'نماد از واچ لیست حذف شد.', 's': 200})


@csrf_exempt
def save_strategy(request):
    data = json.loads(request.POST['param'])
    result = strategy.add_strategy_to_db(data, request.user)
    return JsonResponse(result)


def get_strategy_names(request):
    names = strategy.load_strategy_names(request.user)
    return JsonResponse({'strategies': names})


def load_strategy(request):
    strategy_id = int(request.GET['id'])
    filters = strategy.load_strategy_from_db(request.user, strategy_id)
    return JsonResponse(json.dumps(filters), safe=False)


def scan_market(request):
    strategy_id = request.GET.get('strategyId', '')
    if not strategy_id:
        return JsonResponse({}, status=500)
    scan_result = scan.scan_market(request.user, strategy_id)
    # scan_result = scan.scan_market(request.user, strategy_id, interval=interval)
    return JsonResponse(json.dumps(scan_result), safe=False)


@transaction.atomic
def strategy_notif(request, interval):
    t = threading.Thread(target=scan.screener, args=(interval,))
    t.start()
    if interval == '1d':
        t = threading.Thread(target=Fund.get_daily_snapshots)
        t.start()
    return JsonResponse({'s': 'ok'})


def update_indicators(request):
    if request.method == 'GET':
        data = json.loads(request.GET['param'])
        result = data_handling.give_update_indicators(data)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse('only GET', safe=False)


@login_required(login_url='accounts:userena_signin')
def market_watch(request):
    profile = Profile.objects.get(user=User.objects.get_by_natural_key(request.user))
    if profile.expire >= datetime.today().date():
        return render(request, 'payment.html', {'subscribes': 0, **get_user(request)})
    else:
        return render(request, 'marketwatch.html', get_user(request))
        # subscribtions = Subscribe.objects.all()
        # return render(request, 'payment.html', {'subscribes': subscribtions, **get_user(request)})


@login_required(login_url='accounts:userena_signin')
def display(request):
    return render(request, 'back.html', {'SymbolId': 'BTCUSDT', **get_user(request=request)})
    # profile = Profile.objects.get(user=User.objects.get_by_natural_key(request.user))
    # if profile.expire >= datetime.today().date():
    #     return render(request, 'back.html', {'SymbolId': 'BTCUSDT', **get_user(request=request)})
    # else:
    #     subscribtions = Subscribe.objects.all()
    #     return render(request, 'payment.html', {'subscribes': subscribtions, **get_user(request)})


def getfilters(request):
    return HttpResponse(json.dumps(filters_data))


def filtermarket(request):
    filters = json.loads(request.GET['filters'])
    from data import dates as d
    last = d.Check().last_market()
    from data.models import MarketWatch
    stocks = MarketWatch.objects.filter(stockWatch__LastTradeDate=last).order_by('-stockWatch__TotalTradeValue')
    if len(filters) > 0:
        D = {}
        for f in filters:
            d = json.loads(f)
            D = {**D, **d}
        stocks = stocks.filter(**D)
    paginator = Paginator(stocks, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        stocks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        stocks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.num_pages
        stocks = paginator.page(paginator.num_pages)
    d = {'last': paginator.num_pages, 'former': paginator.num_pages - 1, 'former2': paginator.num_pages - 2}
    a = render(request, 'marketwatchTable.html', {'stocks': stocks, **d})
    return a


def indicators_api(request):
    if request.method == 'GET':
        return JsonResponse(json.dumps(indicator.get_group_api()), safe=False)
    else:
        return JsonResponse(json.dumps({'api': 'null'}), safe=False)


def back_test(request):
    if request.method == 'GET':
        data = json.loads(request.GET['param'])
        name = data['name']
        res = json.loads(data['trades'])
        interval = data['interval']
        result = dh.give_result_backtest(name, res, data['config'], interval=interval)
        return JsonResponse(result, safe=False)
    else:
        return Http404('this is not a GET!')


def about_us(request):
    return render(request, 'aboutus.html', {'username': request.user.username})


@transaction.atomic
def index(request):
    referral_code = request.GET.get('ref', '')
    referred_by = Profile.objects.filter(referral_code=referral_code).first()
    if referral_code and referred_by:
        request.session['ref_id'] = referred_by.id
    # login_status = True if not request.user.username else False
    return render(request, 'newindex.html',
                  # {'form': AuthenticationForm, 'login_status': login_status, 'username': request.user.username}
                  )
    # return render(request, 'index.html')


@login_required(login_url='accounts:userena_signin')
def stockwatch(request, SymbolId):
    if not SymbolId:
        return redirect('/spot/BTCUSDT')
    return redirect('/spot/' + SymbolId)
    # return redirect('/stockwatch/BTCUSDT')
    # from data.models import StockWatch as st
    # stock = st.objects.filter(SymbolId=SymbolId).first()
    # stockWatchDict = {'SymbolId': stock.SymbolId, 'title': stock.InstrumentName, **get_user(request)}
    # return render(request, 'stockwatch1.html', stockWatchDict)


@login_required(login_url='accounts:userena_signin')
def spot(request, symbol_id):
    try:
        result = oms.Binance.get_symbol_info(symbol_id)
    except Exception as e:
        return redirect('/spot/BTCUSDT')
    stockWatchDict = {'SymbolId': symbol_id, 'title': result['baseAsset'], **get_user(request)}
    return render(request, 'stockwatch1.html', stockWatchDict)


def get_user(request):
    username = request.user.username
    user = User.objects.get_by_natural_key(username=username)
    name = user.get_full_name()
    url = '/media/pictures/hadi.jpeg' if username == 'hadi' else 'https://www.awicons.com/free-icons/download/application-icons/dragon-soft-icons-by-artua.com/png/512/User.png'
    return {'name': name, 'img_url': url}


def profile_setup(request):
    extra_context = get_user(request)
    return render(request, 'setup.html', extra_context)


def ssl(request):
    return HttpResponse('S40flyGXu3pwdfdYzH-MLgUCromgJXv8WMbnAO_LXwE.KJYdMS38SO4zyA2XwO0QVtXlrcWShUZNvEdvbDeDAHc')


@csrf_exempt
def trade(request):
    data = request.POST['order']
    order = json.loads(data)
    ex_obj, ex = oms.OMSManager.get_exchange(request)
    if ex_obj:
        result = ex.send_order(ex_obj, order)
        return JsonResponse(result)
    else:
        return JsonResponse({'msg': 'ابتدا در تنظیمات اکسچنج خود را متصل کنید'}, status=403)


def portfo(request):
    ex_obj, ex = oms.OMSManager.get_exchange(request)
    if ex_obj:
        assets = ex.get_portfolio(ex_obj)
        return JsonResponse({'assets': assets})
    else:
        return JsonResponse({'msg': 'NoExchange'}, status=403)


def get_orders(request):
    ex_obj, ex = oms.OMSManager.get_exchange(request)
    if ex_obj:
        symbol = request.GET['symbol']
        orders = ex.get_orders(ex_obj, symbol)
        return JsonResponse({'orders': orders})
    else:
        return JsonResponse({'msg': 'NoExchange'}, status=403)


def account_status(request):
    ex_obj, ex = oms.OMSManager.get_exchange(request)
    balance = ex.get_balance(ex_obj)
    # account = {'WithdrawableMoneyRemain': 2089426.0, 'BlokedValue': 0.0, 'WithdrawableBlockedMoney': 0.0, 'CreditMoney': 0.0, 'CreditBlockedMoney': 0.0, 'TotalAsset': 2619560.0, 'NonWithdrawableMoneyRemain': 0.0, 'CreditMoneyRemain': 0.0, 'PercentageProfit': 26.0, 'Profit': 109384.0, 'BuyingPower': 2089426.0, 'NonWithdrawableBlockedMoney': 0.0}
    account = {'BuyingPower': balance['BuyingPower']}
    return JsonResponse(account)


def cancelOrder(request):
    ex_obj, ex = oms.OMSManager.get_exchange(request)
    result = ex.cancel_order(ex_obj, symbol=request.GET['symbol'], order_id=request.GET['OrderId'])
    if result is None:
        return HttpResponse('e', status=400)
    return HttpResponse('OK')


def editOrder(request):
    output = 'o'
    return HttpResponse(output)


def test_volume(request):
    return render(request, 'test_volume.html', {'SymbolId': 'IRO1IKCO0001', **get_user(request=request)})


def manage_volume(request):
    data = json.loads(request.GET['param'])
    result = volume.run_test(data)
    # print(result['history'])
    return render(request, 'volumetest.html', result)


def testAPI(request):
    return render(request, 'testAPI.html', {'SymbolId': 'IRO1IKCO0001'})


def get_exchanges(request):
    exs = oms.OMSManager.get_exchanges(request)
    return JsonResponse({"exchanges": exs})


@csrf_exempt
def save_exchange(request):
    public = request.POST.get('public', None)
    private = request.POST.get('secret', None)
    name = request.POST.get('name', None)
    exchange = request.POST.get('exchange', None)
    if public is None or private is None or name is None or exchange is None:
        return JsonResponse({'status': False})
    result = {
        "status": oms.OMSManager.verify_and_create_exchange(trader=request.user, name=name, public=public,
                                                            private=private, exchange=exchange.upper())
    }
    return JsonResponse(result)


@csrf_exempt
def remove_exchange(request):
    result = {
        "status": oms.OMSManager.remove_exchange(trader=request.user, ex_name="BINANCE")
    }
    return JsonResponse(result)


@csrf_exempt
@login_required(login_url='accounts:userena_signin')
def tradingview(request):
    if request.method == 'GET':
        tw = TradingView.objects.filter(trader=request.user).first()
        if not tw:
            hook = TradingView.create_hook()
            tw = TradingView(webhook=hook, trader=request.user, trading=False, notification=False)
            tw.save()
        result = {
            "webhook": 'https://ramzservat.com/webhook/{}'.format(tw.webhook),
            "trading": tw.trading,
            "notification": tw.notification,
        }
        return JsonResponse(result)
    elif request.method == 'POST':
        tw = TradingView.objects.filter(trader=request.user).first()
        if not tw:
            return JsonResponse({})
        data = json.loads(request.body)
        error = tw.activate(trading=data['trading'], notification=data['notification'])
        result = {
            "webhook": 'https://ramzservat.com/webhook/{}'.format(tw.webhook),
            "trading": tw.trading,
            "notification": tw.notification,
            "msg": error,
        }
        return JsonResponse(result)


@csrf_exempt
def tradingview_trade(request, token):
    """
    curl -H 'Content-Type: text/plain; charset=utf-8' -d 'binance spot buy btcusdt 0.001 m' -X POST http://127.0.0.1:8000/webhook/3pMoxlHtXT5R
    """
    if request.method == 'GET':
        return JsonResponse({
            'Ramzservat': 'Welcome to Ramzservat. Congratulations, this webhook works!',
        })
    if request.method == 'POST':
        msg = request.body.decode()
        tw = TradingView.objects.filter(webhook=token).first()
        if not tw:
            return JsonResponse({'msg': 'invalid webhook'})
        order_result = ''
        if tw.trading:
            ex_obj, ex = oms.OMSManager.get_exchange(request=None, trader=tw.trader)
            if ex_obj:
                try:
                    params = msg.split(' ')
                    exchange = params[0].upper()
                    if exchange not in ['BINANCE']:
                        order_result = 'نام اکسچنج اشتباه است'
                    market = params[1].upper()
                    if not order_result and market not in ['SPOT']:
                        order_result = 'نام بازار اشتباه است'
                    action = params[2].upper()
                    if not order_result and action not in ['BUY', "SELL"]:
                        order_result = 'دستور خرید یا فروش است'
                    symbol = params[3].upper()
                    volume_text = params[4]
                    if '%' in volume_text:
                        if 'n' in volume_text:
                            quantity = 0
                        else:
                            assets = ex.get_portfolio(ex_obj)
                            ratio = float(volume_text.replace('%', ''))
                            symbol_info = oms.Binance.get_symbol_info(symbol=symbol)
                            base_asset = symbol_info['baseAsset']
                            quote_asset = symbol_info['quoteAsset']
                            if action == 'BUY':
                                value = 12
                                for asset in assets:
                                    if asset['symbol'] == quote_asset:
                                        value = asset['free'] * (ratio / 100)
                                        break
                                ticker = oms.Binance.get_last_price(symbol=symbol)
                                quantity = value / ticker
                            else:
                                quantity = 0
                                for asset in assets:
                                    if asset['symbol'] == base_asset:
                                        quantity = asset['free'] * (ratio / 100)
                                        break
                    else:
                        quantity = float(params[4])
                    price = params[5].upper()
                    order = {
                        'symbol': symbol,
                        'quantity': quantity,
                        'side': action,
                    }
                    if price == 'M':
                        order['type'] = 'MARKET'
                    else:
                        order['price'] = float(price)
                        order['type'] = 'LIMIT'
                    if not order_result:
                        result = ex.send_order(ex_obj, order)
                        if result['error']:
                            order_result = result['msg']
                        else:
                            order_result = 'سفارش با موفقیت ارسال شد'
                except Exception as e:
                    order_result += '\n'
                    order_result += 'دستور ارسال سفارش مشکل دارد، سفارشی ارسال نشد'
        telegram_result = 'در تلگرام ارسال نشد'
        if tw.notification:
            profile = Profile.objects.filter(user=tw.trader).first()
            if profile:
                telegram_id = profile.telegram_id
                if order_result:
                    msg += '\n' + order_result
                telegram_result = notification.send_telegram_message(msg, telegram_id)
        return JsonResponse({'order': order_result, 'telegram': telegram_result})


@csrf_exempt
def telegram_webhook(request):
    """
        curl --tlsv1.2 -v -k -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache"  -d '{
        "update_id":10000,
        "message":{
          "date":1441645532,
          "chat":{
             "last_name":"Test Lastname",
             "id":1111111,
             "first_name":"Test",
             "username":"Test"
          },
          "message_id":1365,
          "from":{
             "last_name":"Test Lastname",
             "id":121366977,
             "first_name":"Test",
             "username":"Test"
          },
          "text":"ON0rtC"
        }
        }' "http://127.0.0.1:8000/telegram/webhook"
    """
    if request.method == 'POST':
        data = request.body.decode()
        try:
            data = json.loads(data)
            message = data['message']
            user_id = message['from']['id']
            text = message['text']
            reply = 'سلام، برای اتصال تلگرام به حساب خود، پس از ورود به سایت وارد بخش تنظیمات شوید و کد فعالسازی را ارسال کنید.'
            if not text == '/start':
                profile = Profile.objects.filter(telegram_activation_code=text).first()
                if profile:
                    if profile.telegram_activation_timestamp and int(
                            time.time()) < profile.telegram_activation_timestamp:
                        profile.telegram_id = str(user_id)
                        profile.save()
                        reply = 'حساب شما به تلگرام متصل شد'
                    else:
                        reply = 'کد فعالسازی شما منقضی شده، لطفا کد جدید دریافت کنید'
                else:
                    profile = Profile.objects.filter(telegram_id=str(user_id)).first()
                    if profile:
                        reply = 'حساب شما به تلگرام متصل است'
                    else:
                        reply = 'کدفعالسازی اشتباه است'

            notification.send_telegram_message(reply, user_id=user_id)
        except Exception as e:
            print(e)
            pass
        return JsonResponse({'msg': 'ok'})
    else:
        return JsonResponse({'msg': 'are you kidding me?'})


def redi(request):
    return redirect('/')
