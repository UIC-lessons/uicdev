from django.db import models
from django.conf import settings
from apps.common.models import BaseModel


class Notification(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="notifications",
    )
    course = models.ForeignKey(
        "courses.Course",
        verbose_name="course",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    module = models.ForeignKey(
        "courses.Module",
        verbose_name="module",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "common.Category",
        verbose_name="category",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(verbose_name="title", max_length=255)
    message = models.TextField(verbose_name="message")
    is_send_to_all = models.BooleanField(verbose_name="is send to all", default=False)
    image = models.ForeignKey(
        "common.Media",
        verbose_name="image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return self.title
