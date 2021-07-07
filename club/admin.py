from django.contrib import admin
from .models import BlogPost,Photo,Achieve,Events,WelcomeNote
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Photo)
admin.site.register(Achieve)
admin.site.register(Events)
admin.site.register(WelcomeNote)
