from django.db import models
from django.contrib.gis.db import models
#from django.urls import 

class Location(models.Model):
    place = models.PointField()
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)   

    def __str__(self):
        return {self.place}


class Category(models.Model):
    created_at = models.CharField(max_length=30, verbose_name='Created At')
    updated_at = models.CharField(max_length=30, verbose_name='Updated At')
    title = models.CharField(max_length=30, verbose_name='Title')
    PHOTO_CHOICE = (
        ('land','Landscape'),
        ('sun','Sunset pictures'),
        ('moring','Morning Breeze'),
        ('tree','Forest'),
        ('ocean','Ocean'),
        ('celeb','Celebrity'),
        ('city','Cities')
    )
    group = models.CharField(max_length=1, choices=PHOTO_CHOICE)

class Image(models.Model):
    image = models.ImageField(upload_to='media/', default='media/image.jpg')
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    post_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, default='ngong lane plaza')
    category = models.ForeignKey(Category, default='')

    def __str__(self):
        return {self.name}


# Create your models here.
