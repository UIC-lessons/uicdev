from django.db import models
from django.conf import settings
from apps.common.models import BaseModel


class Author(BaseModel):
    first_name = models.CharField(verbose_name="first name", max_length=255)
    last_name = models.CharField(verbose_name="last name", max_length=255)
    description = models.TextField(verbose_name="description")
    avatar = models.ForeignKey(
        "common.Media",
        verbose_name="avatar",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    experience_years = models.PositiveIntegerField(
        verbose_name="experience years", default=0
    )

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(BaseModel):
    author = models.ForeignKey(
        Author, verbose_name="author", on_delete=models.RESTRICT, related_name="courses"
    )
    banner = models.ForeignKey(
        "common.Media",
        verbose_name="banner",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(verbose_name="name", max_length=255)
    description = models.TextField(verbose_name="description")
    category = models.ForeignKey(
        "common.Category",
        verbose_name="category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField("common.Tag", verbose_name="tags", blank=True)
    reward_stars = models.PositiveIntegerField(verbose_name="reward stars", default=0)
    is_active = models.BooleanField(verbose_name="is active", default=True)
    is_published = models.BooleanField(verbose_name="is published", default=False)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name


class Module(BaseModel):
    course = models.ForeignKey(
        Course, verbose_name="course", on_delete=models.CASCADE, related_name="modules"
    )
    name = models.CharField(verbose_name="name", max_length=255)
    course_order = models.PositiveIntegerField(verbose_name="course order", default=0)

    class Meta:
        ordering = ["course_order"]
        verbose_name = "Module"
        verbose_name_plural = "Modules"

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class Lesson(BaseModel):
    module = models.ForeignKey(
        Module, verbose_name="module", on_delete=models.RESTRICT, related_name="lessons"
    )
    video = models.ForeignKey(
        "common.Media",
        verbose_name="video",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(verbose_name="name", max_length=255)
    description = models.TextField(verbose_name="description", blank=True)
    current_rating = models.FloatField(verbose_name="current rating", default=0.0)
    type = models.CharField(verbose_name="type", max_length=100)
    max_attempts_count = models.PositiveIntegerField(
        verbose_name="max attempts count", default=1
    )
    attempt_interval = models.PositiveIntegerField(
        verbose_name="attempt interval", default=0, help_text="In minutes"
    )
    lesson_order = models.PositiveIntegerField(verbose_name="lesson order", default=0)
    is_active = models.BooleanField(verbose_name="is active", default=True)

    class Meta:
        ordering = ["lesson_order"]
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.name


class LessonResource(BaseModel):
    lesson = models.ForeignKey(
        Lesson,
        verbose_name="lesson",
        on_delete=models.CASCADE,
        related_name="resources",
    )
    media = models.ForeignKey(
        "common.Media", verbose_name="media", on_delete=models.CASCADE
    )
    caption = models.CharField(verbose_name="caption", max_length=255, blank=True)

    class Meta:
        verbose_name = "Lesson Resource"
        verbose_name_plural = "Lesson Resources"


class Enrollment(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        verbose_name="course",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    finished_at = models.DateTimeField(
        verbose_name="finished at", null=True, blank=True
    )

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
