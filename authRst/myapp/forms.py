from django.forms import ModelForm
from django import forms
from django.db import models
from .models import UserProfile

class UserProfileForm(ModelForm):
    acompanhamento = forms.ChoiceField(choices=[('sim', 'Sim'), ('nao', 'Não')], widget=forms.RadioSelect, initial='nao')
    duracao_condicao = forms.ChoiceField(choices=UserProfile.DURACAO_CONDICAO_CHOICES, initial='temporaria')
    tipo_usuario = forms.ChoiceField(choices=UserProfile.TIPO_USUARIO_CHOICES, initial='acompanhantes')

    class Meta:
        model = UserProfile
        exclude = ['user']

   
