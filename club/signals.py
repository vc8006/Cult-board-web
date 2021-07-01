from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Events

@receiver(post_save, sender=Events)
def create_event(sender,instance,created,**kwargs):
    if created:
        Events.objects.create(event=instance)

@receiver(post_save, sender=Events)
def save_event(sender,instance, **kwargs):
    instance.home.save()

