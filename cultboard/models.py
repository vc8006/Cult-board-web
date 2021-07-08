from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils import timezone


#content like welcome note , abouts us , what we do , our aim
class Note(models.Model):
    title = models.CharField(max_length=50, null = True, blank=True)
    note = models.CharField(max_length=300, null = True, blank=True)

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse('note-detail',kwargs={'pk': self.pk})


class GallaryEvent(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default = 'placeholder.png',upload_to="images")
    video_link = models.CharField(max_length=150, null=True, blank=True)

    def __str__ (self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

        
class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default = 'placeholder.png',upload_to="images")
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True) #about us , what we do , our aim
    gallary_event = models.ForeignKey(GallaryEvent, on_delete=models.SET_NULL, null=True)

    def __str__ (self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.logo.path)


#chairman or gensec details for homepage
class Detail(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  #chairman or gensec
    info = models.CharField(max_length=100)
    image = models.ImageField(default = 'placeholder.png',upload_to="images")
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100)

    def __str__ (self):
        return self.position

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('gensec-detail',kwargs={'pk': self.pk})


class TeamMember(models.Model):
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('member-detail',kwargs={'pk': self.pk})



class MajorEvent(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default = 'placeholder.png',upload_to="images")
    description = models.CharField(max_length=1000, null=True, blank=True)
    gallary_event = models.ForeignKey(GallaryEvent, on_delete=models.SET_NULL, null=True)
    fb_link = models.URLField(max_length =(300))
    insta_link = models.URLField(max_length =(300))
    linkedin_link = models.URLField(max_length =(300))

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('major_event-detail',kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.logo.path)


class UpcomingEvent(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default = 'placeholder.png',upload_to="images")
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('upcoming_event-detail',kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)
        if(img.height>300 or img.width>300):
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.logo.path)

