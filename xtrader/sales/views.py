from django.shortcuts import render
from sales.models import Package, Subscription
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
import json


# from accounts.models import Membership , Subscribe ,Profile
# from .models import Payment
# from finance.views import get_user
# from django.contrib.auth.decorators import login_required
#
# # Create your views here.
def get_packages(request):
    packages = Package.objects.filter(active=True).order_by('month_price')
    result = [pack.info() for pack in packages]
    subscription = Subscription.objects.filter(user=request.user, expiry__gte=timezone.now()).order_by(
        '-expiry').first()
    if subscription:
        pack = subscription.package.info()
        pack['expiry'] = str(subscription.expiry)[:10]
    else:
        pack = packages.first().info()
        pack['expiry'] = 'همیشه'
    return JsonResponse({'packages': result, 'currentPack': pack})


@csrf_exempt
def subscribe(request):
    pack_id = json.loads(request.body).get('subscribe', -1)
    pack = Package.objects.filter(active=True, id=pack_id).first()
    if not pack:
        return JsonResponse({'s': 403, 'm': 'پکیج موجود نیست'})
    result = Subscription.subscribe(request.user, pack)
    return JsonResponse(result)


def packages_view(request):
    return render(request, "packages.html")
