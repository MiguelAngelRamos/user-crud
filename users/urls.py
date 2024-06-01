from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('add/', views.add_user, name='add_user' ),
]
