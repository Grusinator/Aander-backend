from .models import Adventure,MyAdventure,Clue,Location,User

from rest_framework.serializers import ModelSerializer, CharField



class AdventureCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Adventure
        fields = [
            #'adventureid',
            'title',
            'description',
            'difficulty'
        ]

class AdventureDetailSerializer(ModelSerializer):
    class Meta:
        model = Adventure
        fields = [
            'adventureid',
            'title',
            'description',
            'difficulty'
        ]

class AdventureListSerializer(ModelSerializer):
    class Meta:
        model = Adventure
        fields = [
            'adventureid',
            'title',
            'description',
            'difficulty'
        ]
        
        


#MyAdventure

class MyAdventureCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = MyAdventure
        fields = [
            'adventureid',
            'progress',
        ]

class MyAdventureDetailSerializer(ModelSerializer):
    title = CharField(source='adventureid.title',read_only=True)
    description = CharField(source='adventureid.description', read_only=True)
    class Meta:
        model = MyAdventure
        fields = [
            'adventureid',
            'progress',
            'title',
            'description'
        ]

class MyAdventureListSerializer(ModelSerializer):
    title = CharField(source='adventureid.title',read_only=True)
    description = CharField(source='adventureid.description', read_only=True)
    class Meta:
        model = MyAdventure
        fields = [
            'adventureid',
            'progress',
            'title',
            'description'
        ]







# class AdventureSerializer(ModelSerializer):
#     class Meta:
#         model = Adventure
#
#         fields = ('adventureid','title', 'description','difficulty')
#
#
# class MyAdventureSerializer(ModelSerializer):
#     title = CharField(source='adventureid.title',read_only=True)
#     description = CharField(source='adventureid.description', read_only=True)
#
#     class Meta:
#         model = MyAdventure
#
#         fields = ('adventureid', 'progress', 'userid', 'title', 'description')


class CluesSerializer(ModelSerializer):
    longitude = CharField(source='locationsid.longitude',read_only=True)
    lattitude = CharField(source='locationsid.lattitude', read_only=True)
    loc_type = CharField(source='locationsid.type', read_only=True)

    class Meta:
        model = Clue
        fields = ('clueid', 'adventureid', 'cluenumber', 'cluetext', 'clue_image', 'longitude', 'lattitude', 'loc_type')


class LocationsSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('longitude', 'lattitude', 'type')


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

