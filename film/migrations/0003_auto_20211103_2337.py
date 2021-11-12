# Generated by Django 3.2.9 on 2021-11-03 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_alter_genres_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actors',
            options={'ordering': ['name'], 'verbose_name': 'Актер', 'verbose_name_plural': 'Актеры'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='directors',
            options={'ordering': ['name'], 'verbose_name': 'Режиссер', 'verbose_name_plural': 'Режиссеры'},
        ),
        migrations.AlterModelOptions(
            name='genres',
            options={'ordering': ['name'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['creat_time', 'name'], 'verbose_name': 'Видео', 'verbose_name_plural': 'Видео'},
        ),
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='video_URL'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(choices=[('Фильмы', 'Фильмы'), ('Мультфильмы', 'Мультфильмы'), ('Аниме', 'Аниме'), ('Сериалы', 'Сериалы')], max_length=100, unique=True, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='cat_URL'),
        ),
        migrations.AlterField(
            model_name='video',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='Время изменения'),
        ),
    ]