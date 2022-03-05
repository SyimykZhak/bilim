from django.urls import path
from .views import core,About,Main,LoginView,RegisterView,ProfilePage
from . import views
from django.urls import re_path

urlpatterns=[
    path('', Main.as_view(), name='home_page'),
    path('2', core,name='core_list'),
    path('about/', About.as_view(), name='about'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/profile/', ProfilePage.as_view(), name='profile'),
    path('accounts/register/', RegisterView.as_view(), name="register"),
]
# path('accounts/profile/', profile, name='profile'),
# url(r'^accounts/register/$', RegisterView.as_view(), name="register"),
