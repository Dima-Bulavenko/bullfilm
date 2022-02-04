from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin

from .forms import CommentForm, RegisterUserForm, LoginUserForm, CustomPasswordResetFrom, CustomSetPasswordForm
from .models import *
from .services import open_file
from .utils import *


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response


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
                                                "-rating", '-creat_time', 'name'), )
        return dict(list(context.items()) + list(context_def.items()))


class CategoriesView(DataMixin, ListView):
    model = Video
    template_name = "film/categories.html"
    context_object_name = "cats_video"

    def get_queryset(self):
        return Video.objects.filter(categories__slug=self.kwargs["cat_slug"]).order_by("-update_time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=Categories.objects.get(slug=self.kwargs["cat_slug"]), )
        return dict(list(context.items()) + list(context_def.items()))


class ShowVideoView(DataMixin, FormMixin, DetailView):
    model = Video
    template_name = "film/show_video.html"
    context_object_name = "video"
    slug_url_kwarg = "video_slug"
    form_class = CommentForm
    paginate_by = None

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid()

    def form_valid(self, form):
        object = form.save(commit=False)
        object.name = self.request.user
        object.video = self.get_object()
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("show_video", kwargs={"cat_slug": self.kwargs['cat_slug'],
                                                  "video_slug": self.kwargs['video_slug']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title=context["video"].name,
                                            genres=Genres.objects.all(), )
        print(context, context_def)
        return dict(list(context.items()) + list(context_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'film/auth/login.html'
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title="Вход")
        return dict(list(context.items()) + list(context_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetFrom
    template_name = 'film/auth/password_reset.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "film/auth/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = "film/auth/password_reset_confirm.html"


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'film/auth/password_reset_complete.html'


class RegisterView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "film/auth/register.html"
    success_url = reverse_lazy("login")
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title="Регистрация", )
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
        context_def = self.get_user_context(title=Genres.objects.get(slug=self.kwargs["genre_slug"]), )
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
        context_def = self.get_user_context(title="Поиск фильмов", query=self.request.GET.get('q'))
        return dict(list(context.items()) + list(context_def.items()))


class NewVideoView(DataMixin, ListView):
    model = Video
    template_name = 'film/new_video.html'
    context_object_name = 'new_videos'

    def get_queryset(self):
        return Video.objects.all().order_by("-update_time")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_def = self.get_user_context(title="Новинки", )
        return dict(list(context.items()) + list(context_def.items()))
