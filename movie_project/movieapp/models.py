from django.db import models

# Create your models here.

class movie_list(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(blank=True)
    director = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
