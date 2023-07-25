from django import forms
from django.contrib.auth.forms import  UserCreationForm , AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class UserForm(UserCreationForm):
    rol = forms.CharField(max_length=100)
    imagen = forms.ImageField(required=False)
    documento = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['documento','username','email','password1','password2','rol','imagen']

class LoginForm(AuthenticationForm):
    class Meta:
        model : User
        fields = ['username','password']