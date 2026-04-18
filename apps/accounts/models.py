from django.db import models
from django.conf import settings
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Note: Custom User model is handled by the user themselves.
class User(AbstractUser):
    bio = models.TextField(verbose_name=_("bio"), blank=True)
    avatar = models.ForeignKey(
        "common.Media",
        verbose_name=_("avatar"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_avatars",
    )
    phone = models.CharField(verbose_name=_("phone"), max_length=255, blank=True)

    def __str__(self):
        return f"{self.username}'s profile"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class Education(BaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    type = models.CharField(verbose_name=_("type"), max_length=100, blank=True)
    website_url = models.URLField(verbose_name=_("website url"), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)

    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")

    def __str__(self):
        return self.name


class UserEducation(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.RESTRICT,
        related_name="educations",
    )
    education = models.ForeignKey(
        Education, verbose_name=_("education"), on_delete=models.RESTRICT
    )
    field = models.CharField(verbose_name=_("field"), max_length=255)
    start_date = models.DateField(verbose_name=_("start date"), null=True, blank=True)
    end_date = models.DateField(verbose_name=_("end date"), null=True, blank=True)

    class Meta:
        verbose_name = _("User Education")
        verbose_name_plural = _("User Educations")


class UserExperience(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="experiences",
    )
    name = models.CharField(verbose_name=_("name"), max_length=255)
    position = models.CharField(verbose_name=_("position"), max_length=255)
    website_url = models.URLField(verbose_name=_("website url"), blank=True, null=True)
    skills = models.TextField(verbose_name=_("skills"), blank=True)
    start_date = models.DateField(verbose_name=_("start date"), null=True, blank=True)
    end_date = models.DateField(verbose_name=_("end date"), null=True, blank=True)

    class Meta:
        verbose_name = _("User Experience")
        verbose_name_plural = _("User Experiences")


class UserCertificate(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    course = models.ForeignKey(
        "courses.Course", verbose_name=_("course"), on_delete=models.CASCADE
    )
    name = models.CharField(verbose_name=_("name"), max_length=255)
    attachment = models.ForeignKey(
        "common.Media",
        verbose_name=_("attachment"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("User Certificate")
        verbose_name_plural = _("User Certificates")
