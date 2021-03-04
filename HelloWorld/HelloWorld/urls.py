from django.conf.urls import url
from . import views,testdb,search,search2
from django.urls import re_path,path # 用re_path 需要引入

urlpatterns = [
    path('index/', views.page),# 普通path用法
    url(r'^articles-(\d+).html', views.articles), # 正则路径 例：http://127.0.0.1:8000/articles-5555.html
    url(r'^articles/([0-9]{4})/$', views.articles), # 正则路径 例：http://127.0.0.1:8000/articles/5555/
    url(r'^detail-(\d+)-(\d+).html', views.detail),  # 正则路径 例：http://127.0.0.1:8000/detail-7-8.html
    # url(r'^index/$',  views.page),# url用法
    path('search-form/', search.search_form),
    path('search/', search.search),
    path('search-post/', search2.search_post),
]