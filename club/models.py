from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

from cultboard.models import Club
from cultboard.models import TeamMember

# Create your models here.
# class Club(models.Model):
#     name = models.CharField(default=None,max_length= 40)
#
#     def __str__(self):
#         return self.name

class Events(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title = models.CharField(default = None,max_length=(100))
    content = models.TextField()
    expired_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self): # new
        return reverse('event-detail', kwargs={'pk': self.pk,'club_name':self.club})

    def __str__(self):
        return self.title

class WelcomeNote(models.Model):
    content = models.TextField()

    def get_absolute_url(self): # new
        return reverse('welcomenote-detail', kwargs={'pk': self.pk,'club_name':self.club})

# class Member(models.Model):
#     club = models.ForeignKey(Club,on_delete=models.CASCADE)
#     name = models.CharField(default = None,max_length=(100))
#     image = models.ImageField(default = 'default.jpg',upload_to="media/team")
#     position = models.CharField(default= None,max_length=(100))
#     phone_number = models.IntegerField(blank=True)
#     fb_link = models.URLField(max_length =(300))
#     insta_link = models.URLField(max_length =(300))
#     linkedin_link = models.URLField(max_length =(300))
#
#     def __str__(self):
#         return self.position
#
#     def get_absolute_url(self):
#         return reverse('member-detail',kwargs={'pk': self.pk})

STATUS = {
    (0,"Draft"),
    (1,"Publish")
}

class BlogPost(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title =models.CharField(max_length=100, unique=True)
    slug= models.SlugField(max_length=200)
    content =models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    status= models.IntegerField(choices=STATUS , default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk': self.pk,'club_name':self.club})

class Photo(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title = models.CharField(max_length=(100))
    image = models.ImageField(default = 'default.jpg',upload_to="media/images")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo-detail',kwargs={'pk': self.pk,'club_name':self.club})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Achieve(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title = models.CharField(default = None, max_length=(200))
    image = models.ImageField(default='default.jpg',upload_to='media/achieve')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('achieve-detail',kwargs={'pk': self.pk,'club_name': self.club})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
