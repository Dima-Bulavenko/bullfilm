from django.contrib import admin
from . import models


class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(models.Video, VideoAdmin)
admin.site.register(models.Categories, CategoriesAdmin)
admin.site.register(models.Directors)
admin.site.register(models.Actors)
admin.site.register(models.Genres, GenresAdmin)
