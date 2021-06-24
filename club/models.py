from django.db import models
from django.urls import reverse

# Create your models here.
class MyModelName(models.Model):

    my_field_name=models.CharField(max_length=20,help_text='Enter field ')


    class Meta:
        ordering = ['-my_field_name']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.my_field_name


class Event(models.Model):

    event_name=models.CharField(max_length=20,help_text='Enter Event Name')
    event_description=models.TextField(max_length=200,help_text='Enter Description')
    event_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('event-detail',args=[str(self.id)])
class Note(models.Model):

    welcome_note=models.TextField(max_length=1000,help_text='Welcome Note')

    def __str__(self):
        return self.welcome_note




class Team(models.Model):

    name=models.CharField(max_length=20,help_text='Name')
    designation=models.CharField(max_length=20,help_text='Designation')
    branch=models.CharField(max_length=20,help_text='Branch')
    roll_no=models.CharField(max_length=20,help_text='roll_no')
    mobile_no=models.CharField(max_length=10,help_text='number')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('team-member-detail',args=[str(self.id)])
