from django.contrib import admin
from .models import Note, Detail, TeamMember, GallaryEvent, MajorEvent, Club, UpcomingEvent
# Register your models here.

admin.site.register(Note)
admin.site.register(Detail)
admin.site.register(TeamMember)
admin.site.register(GallaryEvent)
admin.site.register(MajorEvent)
admin.site.register(Club)
admin.site.register(UpcomingEvent)