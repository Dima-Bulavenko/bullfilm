from django import template
from film.models import *

register = template.Library()


@register.inclusion_tag('film/my_templates/show_content.html')
def show_content(queryset, title, query=None):
    genres = Genres.objects.all()
    return {'list_video': queryset, 'genres': genres, 'content_title': title, 'query': query}


@register.inclusion_tag('film/my_templates/show_form.html')
def show_form(form, button, forgot_password=False):
    return {'form': form,
            'button': button,
            "forgot_password": forgot_password,}
