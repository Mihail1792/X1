from django import forms
from django.forms import TextInput, ModelForm

from .models import Links

"""Делал свою форму"""
# class LinksForm(ModelForm):
#     """Создаёт форму, куда юзер вводит URL"""
#     class Meta:
#         model = Links
#         fields = ('original_url',)
#
#         widgets = {
#                     'original_url': TextInput(attrs={
#                         'class': 'form-control_c',
#                         'placeholder': 'Введите URL'
#                     }),
#                 }


