from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .utils import *


class IndexView(DataMixin, ListView):
    model = Video
    template_name = "film/index.html"
    context_object_name = "video"

    def get_queryset(self):
        return Video.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(context_def.items()))


class CategoriesView(DataMixin, ListView):
    model = Video
    template_name = "film/categories.html"
    context_object_name = "cats_video"

    def get_queryset(self):
        return Video.objects.filter(categories__slug=self.kwargs["cat_slug"]).order_by("-update_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=Categories.objects.get(slug=self.kwargs["cat_slug"]))
        print(dict(list(context.items()) + list(context_def.items())))
        return dict(list(context.items()) + list(context_def.items()))


class ShowVideoView(DataMixin, DetailView):
    model = Video
    template_name = "film/show_video.html"
    context_object_name = "video"
    slug_url_kwarg = "video_slug"



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context_def = self.get_user_context(title=context["video"].name)
        return dict(list(context.items()) + list(context_def.items()))




