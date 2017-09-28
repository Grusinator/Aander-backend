from django.db import models

# Create your models here.


class Adventures(models.Model):
    adventureid = models.BigAutoField(primary_key =True) # Field name made lowercase.
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    difficulty = models.FloatField()


    def __str__(self):
        return self.title


class User(models.Model):
    userid = models.BigAutoField(primary_key=True)

class MyAdventures(models.Model):
    userid = models.ForeignKey(User)
    adventureid = models.ForeignKey(Adventures)
    progress = models.IntegerField()



class Locations(models.Model):
    locationid = models.BigAutoField(primary_key=True)
    longitude = models.FloatField()
    lattitude = models.FloatField()
    type = models.CharField(max_length=40)


class Clues(models.Model):
    clueid = models.BigAutoField(primary_key=True)
    adventureid = models.ForeignKey(Adventures, related_name='adventure')
    cluenumber = models.IntegerField()
    locationsid = models.ForeignKey(Locations)
    cluetext = models.CharField(max_length=200)
    clue_image = models.CharField(max_length=50)






