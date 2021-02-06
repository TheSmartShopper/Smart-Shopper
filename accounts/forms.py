from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.CustomerProfilemodel import CustomerProfile
from accounts.models import StoreAdminProfile


class SignupForm(UserCreationForm, forms.ModelForm):
    user_type = (
        ('Customer', 'Customer'),
        ('StoreAdmin', 'StoreAdmin'),
    )

    typee = forms.ChoiceField(choices=user_type, label="Account Type is ? ")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'typee',
        ]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', ]


class StoreAdminEditForm(forms.ModelForm):
    class Meta:
        model = StoreAdminProfile
        fields = ['image', 'country', 'address']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['address', 'image', 'country', ]
