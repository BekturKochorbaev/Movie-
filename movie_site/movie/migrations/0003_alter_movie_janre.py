# Generated by Django 5.1.1 on 2024-10-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_favoritemovie_movie_alter_history_movie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='janre',
            field=models.ManyToManyField(blank=True, related_name='janre', to='movie.janre'),
        ),
    ]
