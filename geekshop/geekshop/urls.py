"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mainapp.views import index, products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('mainapp.urls',namespace='mainapp')),
    path('authapp/', include('authapp.urls',namespace='authapp')),
    path('basket/', include('basket.urls',namespace='basket')),
    path('adminapp/', include('adminapp.urls',namespace='adminapp')),
    path('ordersapp/', include('ordersapp.urls',namespace='orders')),
    path('',include('social_django.urls',namespace='social'))

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += [path('debug/',include(debug_toolbar.urls))]
