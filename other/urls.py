from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contacts, name='contact'),
    path('kyrgyzstan', kyrgyzstan, name='kyrgyzstan'),

]
