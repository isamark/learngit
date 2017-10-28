from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^detail/(?P<goods_id>[0-9]+)/$',views.detail,name='detail'),
    url(r'^list(\d+)_(\d+)/$',views.list),

]