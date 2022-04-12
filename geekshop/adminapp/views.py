from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView

# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request,'adminapp/admin.html')
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin


class IndexTemplateView(TemplateView,BaseClassContextMixin,CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главня страница'

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return  super(IndexTemplateView, self).dispatch(request, *args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(IndexTemplateView, self).get_context_data(**kwargs)
    #     context['title'] = 'Главня страница'
    #     return context

class UserListView(ListView,BaseClassContextMixin,CustomDispatchMixin,UserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title =  'Админка | Пользователи'
    context_object_name = 'users'

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#
#     context = {
#         'title' : 'Админка | Пользователи',
#         'users':User.objects.all()
#     }
#     return render(request,'adminapp/admin-users-read.html',context)

class UserCreateView(CreateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title ='Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegisterForm()
#     context = {
#         'title': 'Админка | Регистрация',
#         'form':form
#     }
#
#     return render(request,'adminapp/admin-users-create.html',context)


class UserUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title ='Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')

# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request,id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#          'title': 'Админка | Обновление пользователя',
#          'form':form,
#          'user_select':user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)


class UserDeleteView(DeleteView,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request,id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))