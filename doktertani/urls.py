"""
URL configuration for doktertani project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include

app_name = 'doktertaniapp'


from django.urls import path
from doktertaniapp import views
from .views import detect, product
from django.views.generic import RedirectView
from doktertaniapp.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sarancabai', CabaiViewset)
router.register('obat', ObatViewset)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home),
    re_path('predict/', include('doktertaniapp.urls')),
    re_path('bm/', include('predict_bawangm.urls')),
    path('', include('doktertaniapp.urls')),
    re_path(r'^option/$', detect),
    path('option/', RedirectView.as_view(url='/', permanent=True)),
    re_path(r'^product/$', product),
    path('product/', RedirectView.as_view(url='/', permanent=True)),
]
