from django import forms
from .models import ShippingAddress


class shippingForm(forms.ModelForm):
   shipping_full_name = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={
        'class': '',
        'placeholder': 'نام'
    }),
    required=False
    )
   shipping_email = forms.CharField(
    label='',
    widget=forms.TextInput(attrs={
        'class': '',
        'placeholder': 'ایمیل'
    }),
    required=False
    )
   shipping_address1 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'آدرس اول'
        }),
        required=False
    )
   shipping_address2 = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'آدرس دوم'
        }),
        required=False
    )
   shipping_city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'شهر'
        }),
        required=False
    )
   shipping_zipcode = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'کد پستی'
        }),
        required=False
    )
   shipping_country = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': '',
            'placeholder': 'کشور'
        }),
        required=False
    )
   class Meta:
        model = ShippingAddress
        fields = ('shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_zipcode' ,'shipping_country')
     
        exclude = ['user',]