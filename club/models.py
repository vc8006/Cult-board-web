from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Club(models.Model):
    name = models.CharField(default=None,max_length= 40)

    def __str__(self):
        return self.name

class Member(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    name = models.CharField(default = None,max_length=(100))
    image = models.ImageField(default = 'default.jpg',upload_to="media/team")
    position = models.CharField(default= None,max_length=(100))
    phone_number = models.IntegerField(blank=True)
    fb_link = models.URLField(max_length =(300))
    insta_link = models.URLField(max_length =(300))
    linkedin_link = models.URLField(max_length =(300))

    def __str__(self):
        return self.position

    def get_absolute_url(self):
        return reverse('member-detail',kwargs={'pk': self.pk})

class Post(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title =models.CharField(max_length=(100))
    content =models.TextField()
    date=models.DateTimeField(default = timezone.now)
    author = models.CharField(max_length=(100))

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail',kwargs={'pk': self.pk})

class Photo(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title = models.CharField(max_length=(100))
    image = models.ImageField(default = 'default.jpg',upload_to="media/images")

    def __str__(self):
        return self.title

class Achieve(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE)
    title = models.CharField(default = None, max_length=(200))
    image = models.ImageField(default='default.jpg',upload_to='media/achieve')
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('achieve-detail',kwargs={'pk': self.pk})
