from django.contrib import admin
from homepage.models import welcomenote,upcomingevent,majorevent,aboutus

# Register your models here.
admin.site.register(welcomenote)
admin.site.register(upcomingevent)
admin.site.register(majorevent)
admin.site.register(aboutus)