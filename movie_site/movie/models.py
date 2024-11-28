from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class Profile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(18),
                                                                              MaxValueValidator(90)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=30)

    def __str__(self):
        return self.country_name


class Directory(models.Model):
    director_name = models.CharField(max_length=50)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    director_image = models.ImageField(upload_to='director_img/', null=True, blank=True)

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    bio = models.TextField()
    age = models.PositiveSmallIntegerField(default=0)
    actor_image = models.ImageField(upload_to='actor_img/', null=True, blank=True)

    def __str__(self):
        return self.actor_name


class Janre(models.Model):
    janre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.janre_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    year = models.DateField()
    country = models.ManyToManyField(Country,)
    director = models.ManyToManyField(Directory,)
    actor = models.ManyToManyField(Actor,)
    janre = models.ManyToManyField(Janre,)
    TYPES_CHOICES = (
        ('144p', '144p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    )
    types = MultiSelectField(choices=TYPES_CHOICES)
    movie_tame = models.PositiveSmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movie_trailer/', null=True, blank=True)
    movie_image = models.ImageField(upload_to='movie_image/', null=True, blank=True)
    MOVIE_STATUS_CHOICES = (
        ('pro', 'pro'),
        ('simple', 'simple')
    )
    status = models.CharField(max_length=10, choices=MOVIE_STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.movie_name

    def get_avarage_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(
                sum(int(rating.stars) if rating.stars is not None else 0 for rating in ratings) / ratings.count(), 1)
        return 0


class MovieLanguages(models.Model):
    language = models.CharField(max_length=100)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_language', null=True, blank=True)

    def __str__(self):
        return f'{self.language} - {self.movie}'


class Moments(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moments_movie', null=True, blank=True)
    movie_moments = models.ImageField(upload_to='movie_moments/')


class Rating(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rating_user', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name='ratings',
                              verbose_name='movie')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)], verbose_name='Рейтинг', null=True,
                                blank=True)
    text = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} - {self.user}- {self.stars} stars'


class Favorite(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='favorite_user', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class FavoriteMovie(models.Model):
    cart = models.ForeignKey(Favorite, on_delete=models.CASCADE, related_name='cart', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorite_movie', null=True, blank=True)

    def __str__(self):
        return f'{self.movie} - {self.cart}'


class History(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='history_user', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='history_movie', null=True, blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie} - {self.user}'
