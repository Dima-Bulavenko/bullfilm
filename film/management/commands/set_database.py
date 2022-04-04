from django.core.management.base import BaseCommand, CommandError
from film.models import Video, Directors, Actors, Genres, UserIpAndRating
import json
from transliterate import slugify
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        with open(r'C:\Programing\my_program\Parsing_prongramm\baskinoParser\data.json', encoding='utf-8') as file:
            videos_info = json.load(file)
            for video_info in videos_info:
                vid = Video.objects.update_or_create(
                    name=video_info['name'],
                    original_name=video_info['original_name'],
                    release_year=int(video_info['year']),
                    country=video_info['country'],
                    video=video_info['video'],
                    image=video_info['image'],
                    description=video_info['description'],
                    rating=video_info['rating']
                )[0]
                self.stdout.write(f'{vid.name}-{vid.id}')

                try:
                    vid.slug = slugify(video_info['name']) if slugify(video_info['name']) else video_info['name']
                    vid.save()
                except IntegrityError:
                    vid.slug = slugify(f"{video_info['name']}-{vid.id}") if slugify(
                        video_info['name']) else f"{video_info['name']}-{vid.id}"
                    vid.save()
                UserIpAndRating.objects.update_or_create(ip='127.0.0.1',
                                                         video=vid,
                                                         defaults={'user_rating_value': vid.rating})
                vid.directors.add(*[Directors.objects.get_or_create(name=i)[0] for i in video_info['director']])
                vid.genres.add(*[Genres.objects.get_or_create(name=i if slugify(i) else "Сериалы",
                                                              slug=slugify(i) if slugify(i) else "serialy")[0] for i in
                                 video_info['genre']])
                vid.actors.add(*[Actors.objects.get_or_create(name=i)[0] for i in video_info['actors']])
