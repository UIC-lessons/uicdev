from django.contrib import admin
from .models import Media, Category, Tag, Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country", "created_at", "updated_at")
    search_fields = ("name", "country__name")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("id", "file_url", "created_at", "updated_at")
    search_fields = ("file_url",)
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)
    readonly_fields = ("id", "created_at", "updated_at")
