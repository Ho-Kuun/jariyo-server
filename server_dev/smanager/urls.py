from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

app_name = 'smanager'

urlpatterns = [
    path('list/', login_required(views.ShopView.as_view()), name='list'),
    path('update/', login_required(views.ShopView.as_view()), name='update'),
]