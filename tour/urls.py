from django.urls import path


from .views import *
urlpatterns = [
    path('tour/', tour, name='tour'),
    path('tour/<int:tour_id>/', TourDetailView.as_view(), name='tour'),
    # path('<str:slug>/', Filter.as_view(), name='filter')

]
