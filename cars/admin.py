from django.contrib import admin
from .models import Car
from django.utils.html import format_html


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'thumbnail','title', 'color' ,'city', 'year','model', 'price', 'condition', 'is_featured' , 'fuel_type','miles', 'no_of_owners']
    list_display_links = ['id', 'thumbnail', 'title']
    list_editable = ['is_featured']
    search_fields = ['title', 'city']
    list_filter = ['city', 'year']

    def thumbnail(self, instance):
        if instance.car_image.name != '':
            return format_html(f'<img src="{instance.car_image.url}" class="thumbnail"/>')
        return ""

    thumbnail.short_description = 'photo'
    class Media:
        css = {
            'all': ['pages/css/thumbnail2.css']
        }
