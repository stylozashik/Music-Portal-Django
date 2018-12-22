from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.songs, name='songs'),
    path('contact/', views.contact_form, name='contact_form'),
    path('create/', views.create, name='create'),
    path('addsong/', views.add_song, name='add_song'),
    ]