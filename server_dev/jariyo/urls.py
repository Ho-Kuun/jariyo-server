from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import base_views, manage_views, shop_views

app_name = 'jariyo'

urlpatterns = [
    # base_views.py
    path('main/', base_views.index, name='main'),
    path('restaurant/', login_required(shop_views.RestaurantView.as_view()), name='restaurant'),
    path('cafe/', login_required(shop_views.CafeView.as_view()), name='cafe'),
]