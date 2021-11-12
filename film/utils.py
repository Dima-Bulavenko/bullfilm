from .models import Categories

# menu = [
#     {"title": "Фильмы", "url_name":"film"},
#     {"title": "Сериалы", "url_name":""},
#     {"title": "Аниме", "url_name":""},
#     {"title": "Мультфильмы", "url_name": ""},
# ]
categories = Categories.objects.all()


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context["categories"] = categories
        return context
