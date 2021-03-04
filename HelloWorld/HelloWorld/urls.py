from django.conf.urls import url
from . import views,testdb,search,search2
from django.urls import re_path,path # 用re_path 需要引入

urlpatterns = [
    path('index/', views.page),# 普通path用法
    url(r'^detail-(\d+).html', views.articles), # 正则路径
    url(r'^detail/([0-9]{4})/$', views.articles), # 正则路径
    # url(r'^index/$',  views.page),# url用法
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', search2.search_post),
]