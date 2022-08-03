from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'text', 'data']


        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Название статьи'
            }),
            "intro": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'
            })

        }

