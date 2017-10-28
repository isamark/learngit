from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',views.index),
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^cate/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
]


# 关于正则表达式
# (?P<id>[0-9]+)与(\d+)