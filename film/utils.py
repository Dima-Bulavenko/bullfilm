from .models import Genres

# categories = Categories.objects.all()
genres = Genres.objects.exclude(slug='serialy').order_by('name')


class DataMixin:
    paginate_by = 12

    def get_user_context(self, **kwargs):
        context = kwargs
        # context["categories"] = categories
        context['genres'] = genres
        return context


def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

