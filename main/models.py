from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Genre(models.Model):
    slug = models.SlugField(max_length=100,
                            primary_key=True, unique=True)
    name = models.CharField('Жанр', max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    slug = models.SlugField(max_length=100,
                            primary_key=True, unique=True)
    name = models.CharField('Категория', max_length=50)

    def __str__(self):
        return self.name


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    gender = models.CharField(max_length=1,
                              choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        else:
            return f'Актрисса {self.first_name} {self.last_name}'


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    # name = first_name, last_name

    def __str__(self):
        return f'Режисер {self.first_name} {self.last_name}'


class Movie(models.Model):
    preview = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=45)
    genre = models.ManyToManyField(Genre, related_name='movie_genre')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL, null=True,
                                 related_name='movie_category')
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100)], null=True)
    year = models.IntegerField(null=True)
    slug = models.SlugField(default=True,
                            null=False, db_index=True)
    actors = models.ManyToManyField(Actor)
    directors = models.ForeignKey(Director, null=True,
                                  on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True)
    created_at = models.DateTimeField(auto_now=True,
                                      null=True)


class Review(models.Model):
    owner = models.ForeignKey('account.CustomUser',
                              related_name='review',
                              on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,
                              related_name='movie_review',
                              on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.owner} -> {self.movie} -> {self.created_at}'


class PostImages(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/')
    post = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

    @staticmethod
    def generate_name():
        import random
        return 'image' + str(random.randint(100000, 999999))

    def save(self, *args, **kwargs):
        self.title = self.generate_name()
        return super(PostImages, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} -> {self.post.id}'


class Likes(models.Model):
    post = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='liked')

    class Meta:
        unique_together = ['post', 'user']
