# Generated by Django 4.0.4 on 2022-06-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='main.actor'),
        ),
    ]
