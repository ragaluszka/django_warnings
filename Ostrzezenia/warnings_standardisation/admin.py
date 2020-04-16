from django.contrib import admin
from .models import Warning, Direction, Voltage
# Register your models here.


@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['date_now']


admin.site.register(Direction)
admin.site.register(Voltage)