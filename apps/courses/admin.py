from django.contrib import admin
from .models import Author, Course, Module, Lesson, LessonResource, Enrollment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ("id", "first_name", "last_name", "experience_years", "created_at", "updated_at", "avatar")
    search_fields = ("first_name", "last_name")
    readonly_fields = ("id", "created_at", "updated_at")
    list_filter = ("first_name", "last_name", "created_at")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "category",
        "is_active",
        "description",
        "is_published",
        "reward_stars",
        "created_at",
        "updated_at"
    )
    search_fields = ("name", "author__first_name", "author__last_name", "category__name", "tags__name")
    list_filter = ("is_active", "is_published", "category", "tags", "created_at")
    filter_horizontal = ("tags",)
    readonly_fields = ("id", "created_at", "updated_at")

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course", "course_order", "created_at", "updated_at")
    search_fields = ("name", "course__name")
    list_filter = ("course", "created_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "module", "type", "lesson_order", "is_active", "created_at", "updated_at")
    search_fields = ("name", "module__name", "type")
    list_filter = ("is_active", "type", "module__course", "created_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(LessonResource)
class LessonResourceAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "caption", "created_at", "updated_at")
    search_fields = ("caption", "lesson__name")
    list_filter = ("lesson", "created_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "created_at", "finished_at", "updated_at")
    search_fields = ("user__username", "course__name", "user__first_name", "user__last_name", "course__name")
    list_filter = ("created_at", "finished_at")
    readonly_fields = ("id", "created_at", "updated_at")
