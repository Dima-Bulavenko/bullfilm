# Generated by Django 3.2.9 on 2021-11-14 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_auto_20211109_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, upload_to='Poster', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, upload_to='Video', verbose_name='Видео'),
        ),
    ]