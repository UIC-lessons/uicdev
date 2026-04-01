from django.db import models
from django.conf import settings
from apps.common.models import BaseModel


class LessonQuestion(BaseModel):
    lesson = models.ForeignKey(
        "courses.Lesson",
        verbose_name="lesson",
        on_delete=models.CASCADE,
        related_name="questions",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="user", on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name="text")

    class Meta:
        verbose_name = "Lesson Question"
        verbose_name_plural = "Lesson Questions"

    def __str__(self):
        return f"Question {self.id} on Lesson {self.lesson_id}"


class LessonAnswer(BaseModel):
    lesson = models.ForeignKey(
        "courses.Lesson", verbose_name="lesson", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="user", on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        LessonQuestion,
        verbose_name="question",
        on_delete=models.CASCADE,
        related_name="answers",
    )
    text = models.TextField(verbose_name="text")
    is_deleted = models.BooleanField(verbose_name="is deleted", default=False)

    class Meta:
        verbose_name = "Lesson Answer"
        verbose_name_plural = "Lesson Answers"


class LessonRate(BaseModel):
    lesson = models.ForeignKey(
        "courses.Lesson",
        verbose_name="lesson",
        on_delete=models.CASCADE,
        related_name="ratings",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="user", on_delete=models.CASCADE
    )
    star_count = models.PositiveSmallIntegerField(verbose_name="star count", default=0)
    comment = models.TextField(verbose_name="comment", blank=True)

    class Meta:
        verbose_name = "Lesson Rate"
        verbose_name_plural = "Lesson Rates"


class UserHomeworkAttempt(BaseModel):
    lesson = models.ForeignKey(
        "courses.Lesson",
        verbose_name="lesson",
        on_delete=models.CASCADE,
        related_name="homework_attempts",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="user", on_delete=models.CASCADE
    )
    work_file = models.ForeignKey(
        "common.Media",
        verbose_name="work file",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    title = models.CharField(verbose_name="title", max_length=255)
    description = models.TextField(verbose_name="description", blank=True)

    class Meta:
        verbose_name = "User Homework Attempt"
        verbose_name_plural = "User Homework Attempts"
