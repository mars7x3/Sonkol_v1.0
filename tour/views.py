from django.shortcuts import render
from django.views.generic import DetailView, ListView
from other.views import dinnur
from .models import *
from other.models import *


def tour(request):
    tours = Tour.objects.all()
    tour_price = Price.objects.all().order_by('-id')[:1]
    return render(request, 'tour/tour.html', {'tours': tours, 'tour_price': tour_price, **dinnur()})


class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour/tour-detail.html'
    context_object_name = 'tour'
    pk_url_kwarg = 'tour_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['contact'] = Contact.objects.all()
        context['logo'] = Logo.objects.all()
        context['price'] = Price.objects.all()
        context['day'] = Day.objects.all()
        context['image_tour'] = TourImage.objects.all()
        context['category'] = Category.objects.all()

        return context


# class Filter(DetailView):
#     model = Category
#     template_name = 'tour-category.html'
#     context_object_name = 'category'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['category'] = self.model.objects.all()
#         context['slug'] = self.kwargs['slug']
#         context['contact'] = Contact.objects.all()
#         context['logo'] = Logo.objects.all()
#         return context
