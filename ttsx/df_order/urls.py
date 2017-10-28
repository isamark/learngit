from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.order),
    url(r'^order_detail',views.order_detail),
    url(r'^now_pay/(\w+)$',views.now_pay),

]