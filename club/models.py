from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title =models.CharField(max_length=(100))
    content =models.TextField()
    date=models.DateTimeField(default = timezone.now)
    author = models.CharField(max_length=(100))

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(default = 'default.jpg',upload_to="media/images")

class Member(models.Model):
    title = models.CharField(default = None,max_length=(100))
    image = models.ImageField(default = 'default.jpg',upload_to="media/team")
    position = models.CharField(default= None,max_length=(100))
    phone_number = models.IntegerField(blank=True)
    fb_link = models.URLField(max_length =(300))
    insta_link = models.URLField(max_length =(300))
    linkedin_link = models.URLField(max_length =(300))

    def __str__(self):
        return self.position
