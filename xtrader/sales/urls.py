from django.urls import re_path
from sales import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^packages/$', views.get_packages),
    re_path(r'^subscribe/$', views.subscribe),
    # re_path(r'^payment_callback/$', views.payment_callback),
    # re_path(r'^start/(?P<subscribe_id>\d+)/$', views.start_pay),
]
