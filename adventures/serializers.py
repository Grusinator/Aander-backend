from rest_framework import serializers
from .models import Adventures,MyAdventures,Clues,Locations,User

class AdventuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventures

        fields = ('adventureid','title', 'description','difficulty')


class MyAdventuresSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='adventureid.title',read_only=True)
    description = serializers.CharField(source='adventureid.description', read_only=True)

    class Meta:
        model = MyAdventures

        fields = ('adventureid', 'progress', 'userid', 'title', 'description')


class CluesSerializer(serializers.ModelSerializer):
    longitude = serializers.CharField(source='locationsid.longitude',read_only=True)
    lattitude = serializers.CharField(source='locationsid.lattitude', read_only=True)
    loc_type = serializers.CharField(source='locationsid.type', read_only=True)

    class Meta:
        model = Clues
        fields = ('clueid', 'adventureid', 'cluenumber', 'cluetext', 'clue_image', 'longitude', 'lattitude', 'loc_type')


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ('longitude', 'lattitude', 'type')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

