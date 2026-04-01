from django.db import models
from django.conf import settings
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser


# Note: Custom User model is handled by the user themselves.
class User(AbstractUser):
    bio = models.TextField(verbose_name="bio", blank=True)
    avatar = models.ForeignKey(
        "common.Media",
        verbose_name="avatar",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_avatars",
    )
    phone = models.CharField(verbose_name="phone", max_length=255, blank=True)

    def __str__(self):
        return f"{self.username}'s profile"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Education(BaseModel):
    name = models.CharField(verbose_name="name", max_length=255)
    type = models.CharField(verbose_name="type", max_length=100, blank=True)
    website_url = models.URLField(verbose_name="website url", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="is active", default=True)

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"

    def __str__(self):
        return self.name


class UserEducation(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.RESTRICT,
        related_name="educations",
    )
    education = models.ForeignKey(
        Education, verbose_name="education", on_delete=models.RESTRICT
    )
    field = models.CharField(verbose_name="field", max_length=255)
    start_date = models.DateField(verbose_name="start date", null=True, blank=True)
    end_date = models.DateField(verbose_name="end date", null=True, blank=True)

    class Meta:
        verbose_name = "User Education"
        verbose_name_plural = "User Educations"


class UserExperience(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    name = models.CharField(verbose_name="name", max_length=255)
    position = models.CharField(verbose_name="position", max_length=255)
    website_url = models.URLField(verbose_name="website url", blank=True, null=True)
    skills = models.TextField(verbose_name="skills", blank=True)
    start_date = models.DateField(verbose_name="start date", null=True, blank=True)
    end_date = models.DateField(verbose_name="end date", null=True, blank=True)

    class Meta:
        verbose_name = "User Experience"
        verbose_name_plural = "User Experiences"


class UserCertificate(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    course = models.ForeignKey(
        "courses.Course", verbose_name="course", on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name="name", max_length=255)
    attachment = models.ForeignKey(
        "common.Media",
        verbose_name="attachment",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "User Certificate"
        verbose_name_plural = "User Certificates"
