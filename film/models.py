from django.db import models
from django.urls import reverse

from .choices import *


class Video(models.Model):
    rating = models.IntegerField("Рейтинг", default=0)
    release_year = models.IntegerField("Год выпуска", blank=True)
    directors = models.ManyToManyField("Directors", verbose_name="Режиссер", blank=True)
    genres = models.ManyToManyField("Genres", verbose_name="Жанры", )
    actors = models.ManyToManyField("Actors", verbose_name="Актеры", blank=True)
    country = models.CharField("Страна", max_length=100)
    name = models.CharField("Название", max_length=100)
    categories = models.ForeignKey("Categories", on_delete=models.CASCADE, verbose_name="Категории")
    image = models.ImageField(upload_to="Poster", verbose_name="Постер", blank=True)
    video = models.FileField("Видео", upload_to="Video", blank=True)
    description = models.TextField("Описание", blank=True)
    creat_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField("Время изменения", auto_now=True)
    slug = models.SlugField("video_URL", unique=True, max_length=255, db_index=True, null=True)

    def get_absolute_url(self):
        return reverse("show_video", kwargs={ "cat_slug": self.categories.slug, "video_slug":self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["creat_time", "name"]
        verbose_name = "Видео"
        verbose_name_plural = "Видео"


class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name="Категории", choices=VIDEO_CATEGORIES_CHOICES, unique=True)
    slug = models.SlugField("cat_URL", unique=True, max_length=255, db_index=True, )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories", kwargs={"cat_slug": self.slug,})

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Directors(models.Model):
    name = models.CharField("Режиссеры", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"


class Actors(models.Model):
    name = models.CharField("Актеры", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"


class Genres(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанры", choices=VIDEO_GENRES_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
