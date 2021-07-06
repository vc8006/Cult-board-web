from django.contrib import admin
from .models import BlogPost,Photo,Member,Achieve,Club,Events,WelcomeNote
# Register your models here.

admin.site.register(Club)
admin.site.register(BlogPost)
admin.site.register(Photo)
admin.site.register(Member)
admin.site.register(Achieve)
admin.site.register(Events)
admin.site.register(WelcomeNote)
