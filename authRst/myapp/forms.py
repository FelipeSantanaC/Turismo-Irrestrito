from django.forms import ModelForm, ModelMultipleChoiceField
from django import forms
from .models import UserProfile, TiposLocais, TiposRecursos, TiposDispositivos
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class BRDateField(forms.DateField):
    def to_python(self, value):
        if value in self.empty_values:
            return None
        try:
            return datetime.strptime(value, '%Y-%m-%d').date()
        except ValueError:
            raise forms.ValidationError('Data inválida. Use o formato dd/mm/aaaa.')

class UserProfileForm(ModelForm):
    acompanhamento = forms.ChoiceField(choices=[('sim', 'Sim'), ('nao', 'Não')], widget=forms.RadioSelect, initial='nao')
    duracao_condicao = forms.ChoiceField(choices=UserProfile.DURACAO_CONDICAO_CHOICES, initial='temporaria')
    tipo_usuario = forms.ChoiceField(choices=UserProfile.TIPO_USUARIO_CHOICES, initial='acompanhantes') #Posteriormente trocar por um upload
    preferencia_locais = ModelMultipleChoiceField(queryset=TiposLocais.objects.all(), widget=forms.CheckboxSelectMultiple)
    preferencia_recursos = ModelMultipleChoiceField(queryset=TiposRecursos.objects.all(), widget=forms.CheckboxSelectMultiple)
    preferencia_dam = ModelMultipleChoiceField(queryset=TiposDispositivos.objects.all(), widget=forms.CheckboxSelectMultiple)
    data_nascimento = BRDateField(widget=DateInput, input_formats=['%d/%m/%Y'])
    
    class Meta:
        model = UserProfile
        exclude = ['user']

   
