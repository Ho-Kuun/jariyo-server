from django import forms
from .models import Shop

class ShopCreateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            'name',
            'main_photo',
            'latitude',
            'longitude',
            'shop_type',
            'site',
            'sit_over4_max',
            'sit_4_max',
            'sit_2_max',
        ]

class ShopUpdateForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = [
            '',
        ]