from django.db import models
from django.contrib.auth.models import User





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



class Location(models.Model):
    locationid = models.BigAutoField(primary_key=True)
    longitude = models.FloatField()
    lattitude = models.FloatField()
    type = models.CharField(max_length=40)


class Clue(models.Model):
    clueid = models.BigAutoField(primary_key=True)
    adventureid = models.ForeignKey(Adventure, related_name='adventure')
    cluenumber = models.IntegerField()
    locationsid = models.ForeignKey(Location)
    cluetext = models.CharField(max_length=200)
    clue_image = models.CharField(max_length=50)






