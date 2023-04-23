from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'name',
            'content'
        ]
        labels = {
            'author': 'Автор',
            'category': 'Категория:',
            'name': 'Название:',
            'content': 'Содержимое:'
        }
