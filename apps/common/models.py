from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(verbose_name="id", primary_key=True)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        abstract = True


class Media(BaseModel):
    file_url = models.URLField(verbose_name="file url", max_length=500)

    class Meta:
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __str__(self):
        return self.file_url


class Category(BaseModel):
    name = models.CharField(verbose_name="name", max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(verbose_name="name", max_length=255)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(verbose_name="name", max_length=255)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(verbose_name="name", max_length=255)
    country = models.ForeignKey(
        Country, verbose_name="country", on_delete=models.RESTRICT
    )

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
