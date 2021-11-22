from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('film/<slug:genre_slug>/', GenreView.as_view(), name='genre'),
    path('search/', SearchVideoView.as_view(), name='search_video'),
    path('<slug:cat_slug>/', CategoriesView.as_view(), name="categories"),
    path('<slug:cat_slug>/<slug:video_slug>/', ShowVideoView.as_view(), name="show_video"),
]