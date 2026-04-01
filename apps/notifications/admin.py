from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "course", "is_send_to_all", "created_at")
    search_fields = ("title", "message", "user__username")
    list_filter = ("is_send_to_all", "created_at", "category")
