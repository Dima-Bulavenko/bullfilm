from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('stream/<int:pk>/', get_streaming_video, name='stream'),
    path('', IndexView.as_view(), name='index'),
    path('accounts/password_reset/',
         CustomPasswordResetView.as_view(),
         name='password_reset'),
    path('accounts/password_reset/done/',
         CustomPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('ajax/', get_json_for_rating,),
    path('accounts/login/', LoginUser.as_view(), name='login'),
    path('accounts/logout/', logout_user, name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    # path('film/<slug:genre_slug>/', GenreView.as_view(), name='genre'),
    path('search/', SearchVideoView.as_view(), name='search_video'),
    path('new/', NewVideoView.as_view(), name='new_video'),
    path('<slug:genre_slug>/', GenreView.as_view(), name="genres"),
    path('<slug:genre_slug>/<slug:video_slug>/', ShowVideoView.as_view(), name="show_video"),
]
