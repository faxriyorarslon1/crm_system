from django.contrib import admin
from django.urls import path

from .views import index 

urlpatterns = [
    path('',lead_list, name='lead-list'),
    path('<int:pk>/', lead_detail, name='lead_detail'),
    path('<int:pk>/update/', lead_update, name='lead_update'),
    path('<int:pk>/delete/', lead_delete, name='lead_delete'),
    path('create/', lead_create, name='lead_create'),
]