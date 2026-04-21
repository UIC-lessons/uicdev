from django.db import models
from django.conf import settings
from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _

class Author(BaseModel):
    first_name = models.CharField(verbose_name=_("first name"), max_length=255)
    last_name = models.CharField(verbose_name=_("last name"), max_length=255)
    description = models.TextField(verbose_name=_("description"))
    avatar = models.ForeignKey(
        "common.Media",
        verbose_name=_("avatar"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    experience_years = models.PositiveIntegerField(
        verbose_name=_("experience years"), default=0
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(BaseModel):
    author = models.ForeignKey(
        Author, verbose_name=_("author"), on_delete=models.RESTRICT, related_name="courses"
    )
    banner = models.ForeignKey(
        "common.Media",
        verbose_name=_("banner"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(verbose_name=_("name"), max_length=255)
    description = models.TextField(verbose_name=_("description"))
    category = models.ForeignKey(
        "common.Category",
        verbose_name=_("category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField("common.Tag", verbose_name=_("tags"), blank=True)
    reward_stars = models.PositiveIntegerField(verbose_name=_("reward stars"), default=0)
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)
    is_published = models.BooleanField(verbose_name=_("is published"), default=False)

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name


class Module(BaseModel):
    course = models.ForeignKey(
        Course, verbose_name=_("course"), on_delete=models.CASCADE, related_name="modules"
    )
    name = models.CharField(verbose_name=_("name"), max_length=255)
    course_order = models.PositiveIntegerField(verbose_name=_("course order"), default=0)

    class Meta:
        ordering = ["course_order"]
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")

    def __str__(self):
        return f"{self.course.name} - {self.name}"


class Lesson(BaseModel):
    module = models.ForeignKey(
        Module, verbose_name=_("module"), on_delete=models.RESTRICT, related_name="lessons"
    )
    video = models.ForeignKey(
        "common.Media",
        verbose_name=_("video"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(verbose_name=_("name"), max_length=255)
    description = models.TextField(verbose_name=_("description"), blank=True)
    current_rating = models.FloatField(verbose_name=_("current rating"), default=0.0)
    type = models.CharField(verbose_name=_("type"), max_length=100)
    max_attempts_count = models.PositiveIntegerField(
        verbose_name=_("max attempts count"), default=1
    )
    attempt_interval = models.PositiveIntegerField(
        verbose_name=_("attempt interval"), default=0, help_text="In minutes"
    )
    lesson_order = models.PositiveIntegerField(verbose_name=_("lesson order"), default=0)
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)

    class Meta:
        ordering = ["lesson_order"]
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")

    def __str__(self):
        return self.name


class LessonResource(BaseModel):
    lesson = models.ForeignKey(
        Lesson,
        verbose_name=_("lesson"),
        on_delete=models.CASCADE,
        related_name="resources",
    )
    media = models.ForeignKey(
        "common.Media", verbose_name=_("media"), on_delete=models.CASCADE
    )
    caption = models.CharField(verbose_name=_("caption"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("Lesson Resource")
        verbose_name_plural = _("Lesson Resources")


class Enrollment(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_("course"),
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    started_at = models.DateTimeField(
        verbose_name=_("started at"), null=True, blank=True
    )
    finished_at = models.DateTimeField(
        verbose_name=_("finished at"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Enrollment")
        verbose_name_plural = _("Enrollments")
        unique_together = ("user", "course")
