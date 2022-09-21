from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=5)
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.TextField()
