from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product

class Formcreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Logincreation(AuthenticationForm):
    username = forms.CharField(label="Username",max_length=100)
    password = forms.CharField(widget=forms.PasswordInput,label="Password",max_length=20)

class new_item(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_categorie','product_name','product_description','product_price',]
        widgets = {
            'product_categorie': forms.Select(),
            'product_name': forms.TextInput(attrs={'placeholder': 'Enter product name'}),
            'product_description': forms.Textarea(attrs={'placeholder': 'Enter product description'}),
            'product_price': forms.NumberInput(attrs={'placeholder': 'Enter product price'}),
        }
        labels = {
            'product_name': 'Product Name:',
            'product_description': 'Product Description:',
            'product_price': 'Product Price:'
        }