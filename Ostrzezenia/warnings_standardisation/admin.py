from django.contrib import admin
from .models import Warning
# Register your models here.


@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ['name', 'voltage']
    search_fields = ['name', 'voltage']
    list_filter = ['date_now']