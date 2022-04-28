from django.urls import path

from ordersapp.views import OrderUpdate,OrderList,OrderRead,OrderCreate,OrderDelete,order_forming_complete

app_name = 'ordersapp'
urlpatterns = [
    path('',OrderList.as_view(),name='list'),
    path('create/',OrderCreate.as_view(),name='create'),
    path('update/<int:pk>/',OrderUpdate.as_view(),name='update'),
    path('read/<int:pk>/',OrderRead.as_view(),name='read'),
    path('delete/<int:pk>/',OrderDelete.as_view(),name='delete'),
    path('forming_complete/<int:pk>/',order_forming_complete,name='forming_complete'),
]
