from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model  = Cliente
        fields = ['nome', 'email', 'telefone', 'cidade']
        widgets = {
            'nome':     forms.TextInput(attrs={
                'placeholder': 'Seu nome completo',
                'class': 'form-input'
            }),
            'email':    forms.EmailInput(attrs={
                'placeholder': 'seu@email.com',
                'class': 'form-input'
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': '(11) 99999-9999',
                'class': 'form-input'
            }),
            'cidade':   forms.TextInput(attrs={
                'placeholder': 'Sua cidade',
                'class': 'form-input'
            }),
        }