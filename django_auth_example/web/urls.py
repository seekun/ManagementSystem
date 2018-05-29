from django.conf.urls import url
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
]