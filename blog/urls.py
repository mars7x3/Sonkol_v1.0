from django.urls import path
from .views import *


urlpatterns = [
    path('blog/', all_blogs, name='blog'),
    path('blog/<int:blog_id>/', single_blog, name='blog_detail'),
    path('destination/', destination, name='destination'),
    path('destination/<int:region_id>/', DestinationView.as_view(), name='destination'),

]
