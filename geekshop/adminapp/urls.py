from django.urls import path

from adminapp.views import UserListView, UserCreateView, UserUpdateView, \
    UserDeleteView, IndexTemplateView, CategoryListView, CategoryDeleteView, \
    CategoryUpdateView, ProductListView

app_name = 'adminapp'
urlpatterns = [
    path('',IndexTemplateView.as_view(),name='index'),
    path('users/',UserListView.as_view(),name='admin_users'),
    path('user-create/',UserCreateView.as_view(),name='admin_user_create'),
    path('user-update/<int:pk>/',UserUpdateView.as_view(),name='admin_user_update'),
    path('user-delete/<int:pk>/',UserDeleteView.as_view(),name='admin_user_delete'),

    path('category/', CategoryListView.as_view(), name='admin_category'),
    path('category-delete/<int:pk>/', CategoryDeleteView.as_view(),
         name='admin_category_delete'),
    path('category-update/<int:pk>/', CategoryUpdateView.as_view(),
         name='admin_category_update'),
    # path('category-detail/<int:pk>/', CategoryDetailView.as_view(), name='admin_category_detail'),

    path('product/', ProductListView.as_view(), name='admin_product'),
]
