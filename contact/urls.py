from django.urls import path
from . import views

urlpatterns=[
path('', views.ContactTemplateView.as_view(), name='contacts'),
path('form', views.ContactView.as_view(), name='contact_view'),
]
