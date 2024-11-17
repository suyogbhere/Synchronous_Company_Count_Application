from allauth.account.forms import LoginForm, SignupForm,BaseSignupForm
from django import forms
from app .models import File, Company_data 




class CustomLoginForm(LoginForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter your password',}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply your custom widget or class to the login field
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
    
    
class CustomSignupForm(SignupForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Apply your custom widget or class to the login field
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password(Again)',
        })