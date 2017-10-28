from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^register/$',views.index),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    # url(r'^info/$',views.info),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^user_center_site_add/$', views.user_center_site_add),
    url(r'^logout/$', views.logout),
]
