from django.contrib import admin
from .models import *




class ImageDestinationInline(admin.TabularInline):
    model = ImageDestination


class DestinationInline(admin.ModelAdmin):
    inlines = [ImageDestinationInline,]


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    fields = ('image', 'is_banner')
    max_num = 5
    extra = 1


class BlogDescriptionInline(admin.TabularInline):
    model = BlogDescription
    fields = ('description', 'is_main', 'is_title', 'is_list_item')
    max_num = 10
    min_num = 1
    extra = 1


@admin.register(Blog)
class BlogAdminModel(admin.ModelAdmin):
    list_display = ('main_title', 'main_description', 'author', 'created_at')
    inlines = [BlogImageInline, BlogDescriptionInline]


admin.site.register(Destination, DestinationInline)
