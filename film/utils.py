from .models import Categories

categories = Categories.objects.all()


class DataMixin:
    paginate_by = 12

    def get_user_context(self, **kwargs):
        context = kwargs
        context["categories"] = categories
        return context
