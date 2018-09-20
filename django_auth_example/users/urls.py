from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^edit_profile/', views.edit_profile, name='change'),
]