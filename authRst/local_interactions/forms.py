from django import forms
from .models import Rating, Post
from myapp.models import TiposRecursos
from django.forms import ModelForm, ModelMultipleChoiceField

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

class PostForm(ModelForm):
    tag_list = ModelMultipleChoiceField(queryset=TiposRecursos.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        fields = ['content']

