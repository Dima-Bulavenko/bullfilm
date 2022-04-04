from django import template
from film.models import *
import datetime

register = template.Library()


@register.inclusion_tag('film/my_templates/show_content.html')
def show_content(queryset, title, paginator, page_obj, query=None):
    genres = Genres.objects.all()
    return {'videos': queryset,
            'genres': genres,
            'content_title': title,
            'query': query,
            'paginator':paginator,
            'page_obj': page_obj,}


@register.inclusion_tag('film/my_templates/show_form.html')
def show_form(form, button, forgot_password=False):
    return {'form': form,
            'button': button,
            "forgot_password": forgot_password, }


@register.simple_tag()
def chek_date_difference(date_updating,):
    date = datetime.date.today() - datetime.date(date_updating.year,
                                                 date_updating.month,
                                                 date_updating.day)

    days = date.days
    dic = {'date': f"Год выпуска"}
    if days == 0:
        dic.update({'time': f'Сегодня, {date_updating.strftime("%H:%M")}'})
        return dic
    elif days == 1:
        dic.update({'time': f'Вчера, {date_updating.strftime("%H:%M")}'})
        return dic
    else:
        dic.update({'time': f'{date_updating.strftime("%d-%m-%Y")}'})
        return dic
