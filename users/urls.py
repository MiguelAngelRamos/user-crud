from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('add/', views.add_user, name='add_user' ),
    path('export/', views.export_user_to_excel, name='export_users_to_excel'),
    path('delete/<int:user_id>', views.delete_user, name='delete_user')
]

