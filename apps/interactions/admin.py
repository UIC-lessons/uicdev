from django.contrib import admin
from .models import LessonQuestion, LessonAnswer, LessonRate, UserHomeworkAttempt


@admin.register(LessonQuestion)
class LessonQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "user", "created_at")
    search_fields = ("user__username", "text", "lesson__name")
    list_filter = ("created_at",)


@admin.register(LessonAnswer)
class LessonAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "user", "question", "is_deleted", "created_at")
    search_fields = ("user__username", "text", "lesson__name")
    list_filter = ("is_deleted", "created_at")


@admin.register(LessonRate)
class LessonRateAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "user", "star_count", "created_at")
    search_fields = ("user__username", "comment", "lesson__name")
    list_filter = ("star_count", "created_at")


@admin.register(UserHomeworkAttempt)
class UserHomeworkAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "lesson", "user", "title", "created_at")
    search_fields = ("user__username", "title", "lesson__name")
    list_filter = ("created_at",)
