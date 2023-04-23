from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter
from django import forms

from .models import Category, Post


class PostsFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')
    added = DateFilter(field_name='added', lookup_expr='gt', label='Свежесть', widget=forms.DateInput(attrs={'type': 'date'}))
    category = ModelChoiceFilter(queryset=Category.objects.all(), field_name='category', label='Категория', empty_label='')

    class Meta:
        model = Post
        fields = ['name', 'added', 'category']
