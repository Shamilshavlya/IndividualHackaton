# Generated by Django 4.0.4 on 2022-06-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_movie_category_alter_movie_directors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='preview',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
