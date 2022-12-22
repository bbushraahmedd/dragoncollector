from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dragons/', views.dragons_index, name='index'),
    path('dragons/<int:dragon_id>/', views.dragons_detail, name='detail'),
]