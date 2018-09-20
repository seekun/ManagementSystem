from django.conf.urls import url
from . import views
# from .views import GeneratePDF

app_name = 'web'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^paper/', views.paper, name='paper'),
    url(r'^search/', views.search, name='search'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^detail/(?P<page_num>.*?)$', views.detail, name='detail'),
    url(r'^introduce/', views.introduce, name='introduce'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^parse_paper/', views.parse_paper, name='parse_paper'),
    # url(r'^GeneratePDF/', views.GeneratePDF, name='GeneratePDF'),
    # url(r'^hello.pdf$', views.HelloPDFView, name='HelloPDFView'),
    # url(r'^pdf/$', views.GeneratePDF, name='GeneratePDF'),
    # url(r'^pdf/$', GeneratePDF.as_view(), name='pdf'),

    # url(r'^pdf/', views.pdf, name='pdf'),
    url(r'^print_paper/', views.print_paper, name='print_paper'),
]
