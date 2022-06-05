from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, \
    CategoryUpdateFormAdmin
from authapp.models import User
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
from django.db import connection
from adminapp.mixin import BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin
from mainapp.models import Product, ProductCategories


def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x: type in x['sql'], queries))
    print(f'db_profile {type} for {prefix}:')
    [print(query['sql']) for query in update_queries]

class IndexTemplateView(TemplateView,BaseClassContextMixin,CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главня страница'


class UserListView(ListView,BaseClassContextMixin,CustomDispatchMixin,UserDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title =  'Админка | Пользователи'
    context_object_name = 'users'

class UserCreateView(CreateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title ='Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')

class UserUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title ='Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')

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


# category


class CategoryListView(ListView,BaseClassContextMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-read.html'
    title = 'Админка | Категории'




class CategoryDeleteView(DeleteView,CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.product_set.update(is_active=False)
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryUpdateView(UpdateView,CustomDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')
    form_class = CategoryUpdateFormAdmin


    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                print(f'применяется скидка {discount} % к товарам категории {self.object.name}')
                self.object.product_set.update(price=F('price')*(1-discount/100))
                db_profile_by_type(self.__class__,'UPDATE',connection.queries)
        return HttpResponseRedirect(self.get_success_url())


    # def get_context_data(self, **kwargs):
    #     context = super(CategoryUpdateView, self).get_context_data(**kwargs)
    #     obj = self.get_object()
    #     context['key'] = obj.id
    #     context['cat'] = obj.name
    #     return  context


# Product

class ProductListView(ListView,CustomDispatchMixin,BaseClassContextMixin):
    model = Product
    template_name = 'adminapp/admin-product-read.html'
    title = 'Админка | Продукты'

    def get_queryset(self):
        return Product.objects.all().select_related()