from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request,'adminapp/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):

    context = {
        'title' : 'Админка | Пользователи',
        'users':User.objects.all()
    }
    return render(request,'adminapp/admin-users-read.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):

    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Админка | Регистрация',
        'form':form
    }

    return render(request,'adminapp/admin-users-create.html',context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request,id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
         'title': 'Админка | Обновление пользователя',
         'form':form,
         'user_select':user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request,id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))