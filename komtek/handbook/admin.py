from django.contrib import admin
from .models import Handbook, Element


class ElementAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'handbook')
    list_display_links = ('code', 'value')
    search_fields = ('code', 'value')


class HandbookAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'date')
    list_display_links = ('title', 'version', 'date')
    search_fields = ('title', 'version', 'date')


admin.site.register(Handbook, HandbookAdmin)
admin.site.register(Element, ElementAdmin)
