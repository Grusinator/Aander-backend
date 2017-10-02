from .models import Adventure,MyAdventure,Clue,Location,User

from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField



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


from .models import Clue

class MyAdventureDetailSerializer(ModelSerializer):
    title = CharField(source='adventureid.title',read_only=True)
    description = CharField(source='adventureid.description', read_only=True)

    clues = SerializerMethodField()
    class Meta:
        model = MyAdventure
        fields = [
            'adventureid',
            'progress',
            'title',
            'description',
            'clues'
        ]

    def get_clues(self, obj):
        content_type = obj.get_content_type
        object_id = obj.id
        clues_qs = Clue.objects.filter(adventureid=obj.adventureid)
        clues = CluesListSerializer(clues_qs, many=True).data
        return clues

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


class CluesListSerializer(ModelSerializer):
    loc_type = CharField(source='locationsid.type', read_only=True)

    class Meta:
        model = Clue
        fields = ('clueid',
                  'cluenumber',
                  'cluetext',
                  'clue_image',
                  'loc_type')


class CluesDetailSerializer(ModelSerializer):
    loc_title = CharField(source='locationsid.title',read_only=True)
    longitude = CharField(source='locationsid.longitude',read_only=True)
    lattitude = CharField(source='locationsid.lattitude', read_only=True)
    loc_type = CharField(source='locationsid.type', read_only=True)

    class Meta:
        model = Clue
        fields = ('clueid',
                  'adventureid',
                  'cluenumber',
                  'cluetext',
                  'clue_image',
                  'longitude',
                  'lattitude',
                  'loc_type',
                  'loc_title')


class LocationsSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ('title',
                  'longitude',
                  'lattitude',
                  'type')


class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

