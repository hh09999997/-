from django.contrib import admin
from .models import DashboardLog

@admin.register(DashboardLog)
class DashboardLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'created_at')
