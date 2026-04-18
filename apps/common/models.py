from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    id = models.BigAutoField(verbose_name="id", primary_key=True)
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class Media(BaseModel):
    file_url = models.URLField(verbose_name=_("file url"), max_length=500)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")

    def __str__(self):
        return self.file_url


class Category(BaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    country = models.ForeignKey(
        Country, verbose_name=_("country"), on_delete=models.RESTRICT
    )

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name
