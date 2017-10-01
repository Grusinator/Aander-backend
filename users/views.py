from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
#from users.serializers import UserRegistrationSerializer, UserLoginSerializer, TokenSerializer
from users.serializers import TokenSerializer

from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from adventures.permissions import IsOwnerOrReadOnly
#from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination

User = get_user_model()

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["auth_token"] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    # def post(self, request, *args, **kwargs):
    #     data = request.data
    #     serializer = UserLoginSerializer(data=data)
    #     if serializer.is_valid(raise_exception=True):
    #         new_data = serializer.data
    #         print(new_data['username'])
    #         user = User.objects.filter(username=new_data['username'])
    #
    #         return Response(new_data, status=HTTP_200_OK)
    #     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.filter(username=serializer.data['username']).first()
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid():
    #         user = serializer.user
    #         token, _ = Token.objects.get_or_create(user=user)
    #         return Response(
    #             data=TokenSerializer(token).data,
    #             status=status.HTTP_200_OK,
    #         )
    #     else:
    #         return Response(
    #             data=serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )


# class UserRegistrationAPIView(CreateAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserRegistrationSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#
#         user = serializer.instance
#         token, created = Token.objects.get_or_create(user=user)
#         data = serializer.data
#         data["auth_token"] = token.key
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(data, status=status.HTTP_201_CREATED, headers=headers)

#
# class UserLoginAPIView(GenericAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserLoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.user
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response(
#                 data=TokenSerializer(token).data,
#                 status=status.HTTP_200_OK,
#             )
#         else:
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#
#
# class UserLogoutAPIView(APIView):
#
#     def post(self, request, *args, **kwargs):
#         Token.objects.filter(user=request.user).delete()
#         return Response(status=status.HTTP_200_OK)
