from django.contrib import admin
from .models import Post,Photo,Member,Achieve,Club,Events,WelcomeNote
# Register your models here.

admin.site.register(Club)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Member)
admin.site.register(Achieve)
admin.site.register(Events)
admin.site.register(WelcomeNote)
