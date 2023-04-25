from django.contrib.auth.models import Group
from allauth.account import forms
from django import forms as django_forms

from news.models import Category


class BasicSignupForm(forms.SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class CategorySubscribersForm(django_forms.Form):
    categories = django_forms.MultipleChoiceField(choices=[(category.id, category.name) for category in Category.objects.all()])
