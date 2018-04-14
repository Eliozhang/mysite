from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^testdb', views.testdb, name='testdb'),
    url(r'^search-form/$', views.search_form, name='search_form',),
    url(r'search/$', views.search, name='search'),
    url(r'search_post/$', views.search_post, name='search_post'),
    url(r'tasklist/$', views.tasklist, name='tasklist'),
]