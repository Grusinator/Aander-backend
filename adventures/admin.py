from django.contrib import admin
from .models import Adventure, MyAdventure, Clue, Location
# Register your models here.

admin.site.register(Adventure)
admin.site.register(MyAdventure)
admin.site.register(Clue)
admin.site.register(Location)
