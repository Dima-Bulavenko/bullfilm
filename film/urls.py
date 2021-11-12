from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:cat_slug>/', CategoriesView.as_view(), name="categories"),
    path('<slug:cat_slug>/<slug:video_slug>/', ShowVideoView.as_view(), name="show_video")
]