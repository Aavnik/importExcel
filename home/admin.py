from django.contrib import admin
from .models import *

# Register your models here.

class Albumadmin(admin.ModelAdmin):
    list_display=['artist','name','release_date','num_stars']

admin.site.register(Musician)
admin.site.register(Album, Albumadmin)

