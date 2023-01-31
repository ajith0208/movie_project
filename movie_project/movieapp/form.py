from django import forms
from .models import movie_list


class Movieform(forms.ModelForm):
    class Meta:
        model = movie_list
        fields = ['name', 'year', 'director', 'img']


