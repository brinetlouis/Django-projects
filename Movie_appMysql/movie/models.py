from django.db import models
class Movie(models.Model):
    movie_name=models.CharField(max_length=30)
    description=models.TextField()
    director_name=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    year=models.IntegerField()
    image=models.ImageField(upload_to='movie')
