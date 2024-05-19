from django import forms
from .models import Client, ClientType, Product, Order

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ClientTypeForm(forms.ModelForm):
    class Meta:
        model = ClientType
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
