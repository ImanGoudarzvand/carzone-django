from django.contrib import admin
from .models import Team
from django.utils.html import format_html

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'thumbnail','first_name' ,'last_name', 'designation']
    readonly_fields = ['thumbnail']
    list_display_links = ['id', 'thumbnail','first_name']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']


    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail"/>')
        return ""

    thumbnail.short_description = 'photo'
    class Media:
        css = {
            'all': ['css/thumbnail2.css']
        }
    