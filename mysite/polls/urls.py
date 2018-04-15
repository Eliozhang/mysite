from django.conf.urls import url
from . import views
from . import classes


urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^testdb', views.testdb, name='testdb'),
    url(r'^search-form/$', views.search_form, name='search_form',),
    url(r'search/$', views.search, name='search'),
    url(r'search_post/$', views.search_post, name='search_post'),
    url(r'tasklist/$', views.tasklist, name='tasklist'),
    url(r'get_classes.html$', classes.get_classes),
    url(r'add_classes.html$', classes.add_classes),
    url(r'del_classes.html$', classes.del_classes),
    url(r'edit_classes.html$', classes.edit_classes),
    url(r'find_classes.html$', classes.find_classes),
]
