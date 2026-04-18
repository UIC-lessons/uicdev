from django.contrib import admin
from .models import Notification
from modeltranslation.admin import TranslationAdmin

@admin.register(Notification)
class NotificationAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("id", "title", "user", "course", "is_send_to_all", "category", "module", "created_at", "updated_at")
    search_fields = ("title", "message", "user__username")
    readonly_fields = ("id", "created_at", "updated_at")
    list_filter = ("is_send_to_all", "created_at", "category", "module", "course")
