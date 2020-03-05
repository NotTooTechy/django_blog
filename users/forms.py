from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    '''
        Inhering user creation form and ADD email
    '''
    email = forms.EmailField()

    class Meta:
        '''
            keeps config in one place
            fields in form with order
        '''
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()

        class Meta:
            '''
                keeps config in one place
                fields in form with order
            '''
            model = User
            fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
