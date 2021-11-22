from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
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
        context_def = self.get_user_context(title="Главная страница",
                                            filter_video=Video.objects.exclude(
                                                categories__name__in=["Аниме", "Сериалы"]).order_by(
                                                "-rating", '-creat_time', 'name'), genres=Genres.objects.all())
        print(dict(list(context.items()) + list(context_def.items())))
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
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context_def = self.get_user_context(title=context["video"].name)
        return dict(list(context.items()) + list(context_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'film/login.html'
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(context_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterView(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = "film/register.html"
    success_url = reverse_lazy("login")
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(context_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')


class GenreView(DataMixin, ListView):
    model = Video
    template_name = 'film/genre.html'
    context_object_name = "genre_video"

    def get_queryset(self):
        return Video.objects.filter(genres__slug=self.kwargs["genre_slug"]).order_by("-update_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(self.__dict__)
        context_def = self.get_user_context(title=f'{Genres.objects.get(slug=self.kwargs["genre_slug"])}',
                                            genre=Genres.objects.get(slug=self.kwargs["genre_slug"]),
                                            genres=Genres.objects.all())
        return dict(list(context.items()) + list(context_def.items()))


class SearchVideoView(DataMixin, ListView):
    model = Video
    template_name = 'film/searchvideo.html'
    context_object_name = 'searched_video'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Video.objects.filter(name__icontains=query)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title="gav")
        return dict(list(context.items()) + list(context_def.items()))
