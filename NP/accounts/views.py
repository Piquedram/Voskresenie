from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CategorySubscribersForm
from news.models import Author, CategorySubscribers, Category


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['is_author'] = self.request.user.groups.filter(name='authors').exists()
        return context


@login_required
def upgrade_me(request):
    user = request.user
    authors = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors.user_set.add(user)
    Author.objects.create(user=user)
    return redirect('profile')


@login_required
def subscribe(request):
    if request.method == 'POST':
        form = CategorySubscribersForm(request.POST)
        if form.is_valid():
            categories = form.cleaned_data['categories']
            subscriber = request.user
            CategorySubscribers.objects.filter(subscriber=subscriber).delete()
            for category_id in categories:
                category = Category.objects.get(id=category_id)
                CategorySubscribers.objects.create(category=category, subscriber=subscriber)
            return redirect('profile')
    else:
        form = CategorySubscribersForm()
    return render(request, 'accounts/subscribe.html', {'form': form})
