from django.urls import path

from adminapp.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, IndexTemplateView

app_name = 'adminapp'
urlpatterns = [
    path('',IndexTemplateView.as_view(),name='index'),
    path('users/',UserListView.as_view(),name='admin_users'),
    path('user-create/',UserCreateView.as_view(),name='admin_user_create'),
    path('user-update/<int:pk>/',UserUpdateView.as_view(),name='admin_user_update'),
    path('user-delete/<int:pk>/',UserDeleteView.as_view(),name='admin_user_delete'),
]
