from django.contrib import admin
from .models import History  # Import History from its correct location

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'method', 'summary', 'created_at')
    list_filter = ('method', 'created_at')
    search_fields = ('user__username', 'summary')