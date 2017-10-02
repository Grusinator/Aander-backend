from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType



# Create your models here.


class Adventure(models.Model):
    adventureid = models.BigAutoField(primary_key =True) # Field name made lowercase.
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    difficulty = models.FloatField()


    def __str__(self):
        return self.title





class MyAdventure(models.Model):
    userid = models.ForeignKey(User)
    adventureid = models.ForeignKey(Adventure)
    progress = models.IntegerField()

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type



class Location(models.Model):
    title = models.CharField(max_length=20)
    locationid = models.BigAutoField(primary_key=True)
    longitude = models.FloatField()
    lattitude = models.FloatField()
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.title



class Clue(models.Model):
    clueid = models.BigAutoField(primary_key=True)
    adventureid = models.ForeignKey(Adventure, related_name='adventure')
    cluenumber = models.IntegerField()
    locationsid = models.ForeignKey(Location)
    cluetext = models.CharField(max_length=200)
    clue_image = models.CharField(max_length=50, blank=True)






