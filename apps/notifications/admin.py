from django.contrib import admin
from .models import Notification
from modeltranslation.admin import TranslationAdmin

@admin.register(Notification)
class NotificationAdmin(TranslationAdmin, admin.ModelAdmin):
    list_display = ("title", "user", "course", "is_send_to_all", "category", "module", "created_at", "updated_at")
    search_fields = ("title", "message", "user__first_name", "user__last_name")
    readonly_fields = ("created_at", "updated_at")
    list_filter = ("is_send_to_all", "created_at", "category", "module", "course")
    
