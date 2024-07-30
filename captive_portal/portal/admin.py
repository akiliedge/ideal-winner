# portal/admin.py
from django.contrib import admin
from .models import CaptivePortalContent

@admin.register(CaptivePortalContent)
class CaptivePortalContentAdmin(admin.ModelAdmin):
    list_display = ('message', 'image')
    search_fields = ('message',)

# Register your models here.
