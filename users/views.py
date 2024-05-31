from django.shortcuts import render
# Lo necesario para "auth"
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

# Paginación
from django.core.paginator import Paginator

# Nuestro formulario del CustomUser
from .forms import CustomUserCreationForm

# Respuestas http
from django.http import HttpResponse

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import openpyxl # type: ignore


User = get_user_model()

# metodo que requiera que sea super user o admin
def admin_required(login_url=None):
    return user_passes_test(lambda usuario:usuario.is_superuser, login_url=login_url)

## @login_required # este metodo necesita que sea un usuario autenticado pero no necesariamente un Admin
def user_list(request):
    users = User.objects.all()
    paginator = Paginator(users, 5) # Mostrar 5 usuarios por página
    page_number = request.GET.get('page') # 2
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/user_list.html', {'page_obj': page_obj })
    

# add_user require este decorador @admin_required(login_url='/login/')
# export_users_to_excel require este decorador @admin_required(login_url='/login/')



