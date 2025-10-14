from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm , SetPasswordForm
from django.contrib.auth.models import User


class ChangePasswordForm(SetPasswordForm):
    class Meta : 
        model : User
        fields = ['new_password1','new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs.update({
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'رمز عبور'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'تایید رمز عبور'
        })

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'ایمیل'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'نام کاربری'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'رمز عبور'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'تایید رمز عبور'
        })


class UpdateUserFrom(UserChangeForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'ایمیل'
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserFrom, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'block w-full rounded-lg bg-gray-100 px-3 py-2 text-sm md:text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600',
            'placeholder': 'نام کاربری'
        })
