from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)/$',views.add),
    url(r'^set_cart/$', views.set_cart),
    url(r'^del_cart/(?P<cart_id>[0-9]+)/$', views.del_cart),

]
