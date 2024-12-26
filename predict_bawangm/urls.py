from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView
from .views import detect
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^option/$', detect),
]

from django.urls import path
from predict_bawangm import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]
