from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('Hair-oil/', views.hairoil, name='Hairoil'),
    path('Henna-dye/', views.Hennadye, name='Hennadye'),
    path('bath-soap/', views.Bathsoap, name='Bathsoap'),
]
