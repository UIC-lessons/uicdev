from django.contrib import admin
from .models import Author, Course, Module, Lesson, LessonResource, Enrollment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "experience_years")
    search_fields = ("first_name", "last_name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "author",
        "category",
        "is_active",
        "is_published",
        "reward_stars",
    )
    search_fields = ("name", "author__first_name", "author__last_name")
    list_filter = ("is_active", "is_published", "category")
    filter_horizontal = ("tags",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course", "course_order")
    search_fields = ("name", "course__name")
    list_filter = ("course",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "module", "type", "lesson_order", "is_active")
    search_fields = ("name", "module__name", "type")
    list_filter = ("is_active", "type", "module__course")


@admin.register(LessonResource)
class LessonResourceAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "caption", "created_at")
    search_fields = ("caption", "lesson__name")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "created_at", "finished_at")
    search_fields = ("user__username", "course__name")
    list_filter = ("created_at", "finished_at")
