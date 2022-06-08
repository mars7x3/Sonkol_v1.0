from django.contrib import admin
from .models import *


class PriceInline(admin.TabularInline):
    model = Price
    max_num = 10
    extra = 1


class DayInline(admin.TabularInline):
    model = Day
    max_num = 20
    extra = 0


class TourImageInline(admin.TabularInline):
    model = TourImage
    max_num = 3
    extra = 1


class TourAdmin(admin.ModelAdmin):
    inlines = [PriceInline, DayInline, TourImageInline]




admin.site.register(Tour, TourAdmin)
