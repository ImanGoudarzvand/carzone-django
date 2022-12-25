from django.contrib import admin
from .models import Team
from django.utils.html import format_html

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'designation']
    readonly_fields = ['thumbnail']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thumbnail"/>')
        return ""

    class Media:
        css = {
            'all': ['css/thumbnail.css']
        }
    