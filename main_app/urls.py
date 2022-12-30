from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dragons/', views.dragons_index, name='index'),
    path('dragons/<int:dragon_id>/', views.dragons_detail, name='detail'),
    path('dragons/create/', views.DragonCreate.as_view(), name='dragons_create'),
    path('dragons/<int:pk>/update/', views.DragonUpdate.as_view(), name='dragons_update'),
    path('dragons/<int:pk>/delete/', views.DragonDelete.as_view(), name='dragons_delete'),
    path('dragons/<int:dragon_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]