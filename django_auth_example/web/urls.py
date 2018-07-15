from django.conf.urls import url
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^paper/', views.paper, name='paper'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^detail/(?P<page_num>.*?)$', views.detail, name='detail'),
    url(r'^introduce/', views.introduce, name='introduce'),
    url(r'^contact/', views.contact, name='contact'),
]