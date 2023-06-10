from django import forms
from orders.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Игорь'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пупкин'}))
    email = forms.EmailField(label='Эл.почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
    address = forms.CharField(label='Адрес', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Россия, Сургут, ул. Ленина, дом 1',
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')