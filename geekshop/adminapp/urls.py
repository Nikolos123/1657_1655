from django.urls import path

from adminapp.views import admin_users,index,admin_user_create,admin_user_update,admin_user_delete

app_name = 'adminapp'
urlpatterns = [
    path('',index,name='index'),
    path('users/',admin_users,name='admin_users'),
    path('user-create/',admin_user_create,name='admin_user_create'),
    path('user-update/<int:id>/',admin_user_update,name='admin_user_update'),
    path('user-delete/<int:id>/',admin_user_delete,name='admin_user_delete'),
]
