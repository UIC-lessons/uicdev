from django.contrib import admin
from .models import Education, UserEducation, UserExperience, UserCertificate


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "is_active")
    search_fields = ("name", "type")
    list_filter = ("is_active", "type")


@admin.register(UserEducation)
class UserEducationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "education", "field", "start_date", "end_date")
    search_fields = ("user__username", "field", "education__name")
    list_filter = ("start_date", "end_date")


@admin.register(UserExperience)
class UserExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "position", "start_date", "end_date")
    search_fields = ("user__username", "name", "position")
    list_filter = ("start_date", "end_date")


@admin.register(UserCertificate)
class UserCertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "name")
    search_fields = ("user__username", "name", "course__name")
