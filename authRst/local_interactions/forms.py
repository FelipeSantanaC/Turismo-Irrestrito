from django import forms
from .models import Rating, Post

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']