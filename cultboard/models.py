from django.db import models
from django.utils import timezone

#content like welcome note , abous us , what we do , our aim
class Note(models.Model):
    title = models.CharField(max_length=50, null = True, blank=True)
    note = models.CharField(max_length=300, null = True, blank=True)

    def __str__ (self):
        return self.title

#chairman or gensec details for homepage
class Detail(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  #chairman or gensec
    info = models.CharField(max_length=100)
    image = models.ImageField(default = 'placeholder,png',upload_to="images")
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100)

    def __str__ (self):
        return self.position


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default = 'placeholder.png',upload_to="images")
    position = models.CharField(max_length=100)  
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100)

    def __str__ (self):
        return self.position


class GallaryEvent(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default = 'placeholder.png',upload_to="images")
    video_link = models.CharField(max_length=150, null=True, blank=True)

    def __str__ (self):
        return self.name


class MajorEvent(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default = 'placeholder.png',upload_to="images")
    desription = models.CharField(max_length=1000, null=True, blank=True)
    gallary_event = models.ForeignKey(GallaryEvent, on_delete=models.SET_NULL, null=True)
    fb_page = models.CharField(max_length=100, null=True, blank=True)
    inta_page = models.CharField(max_length=100, null=True, blank=True)

    def __str__ (self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default = 'placeholder.png',upload_to="images")
    note = models.ForeignKey(Note, on_delete=models.SET_NULL, null=True) #about us , what we do , our aim
    gallary_event = models.ForeignKey(GallaryEvent, on_delete=models.SET_NULL, null=True)

    def __str__ (self):
        return self.name


class UpcomingEvent(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default = 'placeholder.png',upload_to="images")
    desription = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__ (self):
        return self.name

