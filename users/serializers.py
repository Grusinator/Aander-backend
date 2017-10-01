from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

User = get_user_model()


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token",)


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    #email = EmailField(label='Email Address')
    #email2 = EmailField(label='Confirm Email')

    class Meta:
        model = User
        fields = [
            'username',
            #'email',
            #'email2',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    # def validate_email(self, value):
    #     data = self.get_initial()
    #     email1 = data.get("email2")
    #     email2 = value
    #     if email1 != email2:
    #         raise ValidationError("Emails must match.")
    #
    #     user_qs = User.objects.filter(email=email2)
    #     if user_qs.exists():
    #         raise ValidationError("This user has already registered.")
    #
    #     return value

    # def validate_email2(self, value):
    #     data = self.get_initial()
    #     email1 = data.get("email")
    #     email2 = value
    #     if email1 != email2:
    #         raise ValidationError("Emails must match.")
    #     return value

    def create(self, validated_data):
        username = validated_data['username']
        #email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            #email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=True)
    #email = EmailField(label='Email Address')

    class Meta:
        model = User
        fields = [
            'username',
            #'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data



#
# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ("id", "username", "email", "password", "confirm_password", "date_joined")
#
#     def create(self, validated_data):
#         del validated_data["confirm_password"]
#         return super(UserRegistrationSerializer, self).create(validated_data)
#
#     def validate(self, attrs):
#         if attrs.get('password') != attrs.get('confirm_password'):
#             raise serializers.ValidationError("Those passwords don't match.")
#         return attrs
#
#
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)
#
#     default_error_messages = {
#         'inactive_account': _('User account is disabled.'),
#         'invalid_credentials': _('Unable to login with provided credentials.')
#     }
#
#     def __init__(self, *args, **kwargs):
#         super(UserLoginSerializer, self).__init__(*args, **kwargs)
#         self.user = None
#
#     def validate(self, attrs):
#         self.user = authenticate(username=attrs.get("username"), password=attrs.get('password'))
#         if self.user:
#             if not self.user.is_active:
#                 raise serializers.ValidationError(self.error_messages['inactive_account'])
#             return attrs
#         else:
#             raise serializers.ValidationError(self.error_messages['invalid_credentials'])
#
# class UserInfoSerializer(serializers.Serializer):
#     location = serializers.CharField(source='locationsid.lattitude',)
#
#     class Meta:
#         model = User
#         fields = ("id", "username", "email", "confirm_password", "date_joined", 'location')
#

