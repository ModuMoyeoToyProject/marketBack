from .models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'firstName',
                  'lastName',
                  'emailAddress']
        widgets = {
            'username': TextInput(attrs={
                'class': 'signup_input',
                'placeholder': 'Username'
            }),
            'password': PasswordInput(attrs={
                'class': 'signup_input',
                'placeholder': 'Password'
            }),
            'firstName': TextInput(attrs={
                'class': 'signup_input',
                'placeholder': 'First Name'
            }),
            'lastName': TextInput(attrs={
                'class': 'signup_input',
                'placeholder': 'Last Name'
            }),
            'emailAddress': EmailInput(attrs={
                'class': 'signup_input',
                'placeholder': 'Email Address'
            })
        }
        labels = {
            'username': '',
            'password': '',
            'firstName': '',
            'lastName': '',
            'emailAddress': ''
        }