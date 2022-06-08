from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView

from other.views import dinnur
from .models import *
from other.models import *

def all_blogs(request):
    return render(request, 'blog/blogs.html', {'blogs': Blog.objects.all().order_by('-created_at'), **dinnur()})


def single_blog(request, blog_id: int):
    blog = Blog.objects.get(id=blog_id)
    last_three = Blog.objects.filter(~Q(id=blog.id)).order_by('-created_at')[:3]
    return render(request, 'blog/blog_detail.html', {'blog': blog, 'last_three': last_three, **dinnur()})


def destination(request):
    region = Region.objects.all()
    context = {"region": region, **dinnur()}
    return render(request, 'destination/destination.html', context)


class DestinationView(DetailView):
    model = Region
    template_name = 'destination/destination-detail.html'
    context_object_name = 'region'
    pk_url_kwarg = 'region_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['contact'] = Contact.objects.all()
        context['logo'] = Logo.objects.all()
        return context
