from django.shortcuts import render
from .models import *
from blog.models import *
from tour.models import *


def dinnur() -> dict:
    contact = Contact.objects.all()
    logo = Logo.objects.all()
    abouts = About.objects.all()
    review = Review.objects.all()
    category = Category.objects.all()
    context = {'contact': contact, "logo": logo, "abouts": abouts, 'review': review, 'category': category}
    return context


def home(request):
    banner = Banner.objects.all()
    region = Region.objects.all()
    tour = Tour.objects.all()
    tour_price = Price.objects.all().order_by('-id')[:1]
    last_three = Blog.objects.all().order_by('-created_at')[:3]
    context = {'banner': banner, "region": region, 'tour': tour, 'tour_price': tour_price, **dinnur(),
               'last_three': last_three}
    return render(request, "home/home.html", context)


def about(request):
    context = {**dinnur(), }
    return render(request, 'about/about.html', context)


def contacts(request):
    context = {**dinnur(), }
    return render(request, 'contact/contact.html', context)


def kyrgyzstan(request):
    context = {**dinnur(), }
    return render(request, 'about/kyrgyz.html', context)

