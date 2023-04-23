from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProfileView
from django.contrib.auth.views import LogoutView
from .views import upgrade_me

urlpatterns = [
    path('', login_required(ProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('upgrade/', upgrade_me, name='upgrade')
]
