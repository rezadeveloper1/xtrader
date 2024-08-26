from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from aum.models import FundInvestor, Fund
import json


@login_required(login_url='accounts:userena_signin')
def management(request):
    return render(request, 'fundManagement.html')


@csrf_exempt
@login_required(login_url='accounts:userena_signin')
def issue_redeem_unit(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode())
        fund = Fund.objects.filter(manager=request.user).first()
        investor = FundInvestor.objects.filter(fund=fund, id=params['investor_id']).first()
        if fund and investor:
            result = fund.issue_redeem(investor, params)
            investor.save()
            fund.save()
        else:
            result = {'msg': 'شناسه سرمایه‌گذار اشتباه است'}
        return JsonResponse(result)
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)


@csrf_exempt
@login_required(login_url='accounts:userena_signin')
def redeem_unit(request):
    if request.method == 'POST':
        return JsonResponse({'msg': 'ok'})
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)


@csrf_exempt
@login_required(login_url='accounts:userena_signin')
def add_investor(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode())
        national_code = params['nationalCode']
        fund = Fund.objects.filter(manager=request.user).first()
        if FundInvestor.objects.filter(nationalCode=national_code, fund=fund).first():
            result = {'msg': 'investor already exists!'}
        elif len(params['first_name']) > 20 or len(params['last_name']) > 20:
            result = {'msg': 'firstName or lastName must be less than 20 characters!'}
        else:
            params['fund'] = fund
            investor = FundInvestor(**params)
            investor.save()
            result = {'c': 200, 'msg': 'investor already exists!'}
        return JsonResponse(result)
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)


@login_required(login_url='accounts:userena_signin')
def investors(request):
    if request.method == 'GET':
        fund = Fund.objects.filter(manager=request.user).first()
        investors = FundInvestor.objects.filter(fund=fund)
        result = []
        for investor in investors:
            result.append({
                'id': investor.id,
                'name': '{} {}'.format(investor.first_name, investor.last_name),
                'units': investor.units,
                'national_code': investor.nationalCode,
            })
        return JsonResponse({'data': result})
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)


@login_required(login_url='accounts:userena_signin')
def get_fund(request):
    if request.method == 'GET':
        fund = Fund.objects.filter(manager=request.user).first()
        if fund:
            result = fund.get_fund_info()
        else:
            result = {}
        return JsonResponse(result)
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)


@login_required(login_url='accounts:userena_signin')
def transactions_history(request):
    if request.method == 'GET':
        fund = Fund.objects.filter(manager=request.user).first()
        result = []
        if fund:
            result = fund.get_transactions()
        return JsonResponse({'data': result})
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)


@login_required(login_url='accounts:userena_signin')
def init_fund_performance(request):
    if request.method == 'GET':
        if not request.GET.get('pass', '') == 'XTreasury':
            return JsonResponse({'msg': 'not authorize'}, status=401)
        fund = Fund.objects.filter(manager=request.user).first()
        result = []
        if fund:
            result = fund.init_fund_performance()
        return JsonResponse({'data': result})
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)

@login_required(login_url='accounts:userena_signin')
def get_fund_performance(request):
    if request.method == 'GET':
        fund = Fund.objects.filter(manager=request.user).first()
        result = []
        if fund:
            mode = request.GET.get('mode', 'all')
            result = fund.get_fund_performance(mode=mode)
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({'msg': 'bad request'}, status=403)
