from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


class UserIpAndRatingInLineAdmin(admin.StackedInline):
    model = UserIpAndRating
    can_delete = False


class ProfileInLineAdmin(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = "Профиль"
    verbose_name_plural = "Профили"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLineAdmin,)


# class CategoriesAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("name",)}


class VideoAdmin(admin.ModelAdmin):
    inlines = (UserIpAndRatingInLineAdmin,)
    prepopulated_fields = {"slug": ("name",)}


class GenresAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'comment')


admin.site.register(Video, VideoAdmin)
# admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Directors)
admin.site.register(Actors)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
