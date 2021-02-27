from django.conf.urls import url
from . import views,testdb,search,search2

urlpatterns = [
    url(r'^index/$', views.page),
    url(r'^testdb/$', testdb.testdb),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search2.search_post),
]