from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Ig-home'),
    path('about/', views.about, name='Ig-about'),

]
