from django.shortcuts import render, get_object_or_404

from itertools import chain
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Adventure, MyAdventure,Clue,Location
# from .serializers import Adventureerializer, MyAdventureerializer, CluesSerializer, LocationsSerializer, UsersSerializer
from .serializers import CluesDetailSerializer, LocationsSerializer, UsersSerializer
from rest_framework.decorators import api_view



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

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    AdventureCreateUpdateSerializer,
    AdventureDetailSerializer,
    AdventureListSerializer
    )

from .serializers import (
    MyAdventureCreateUpdateSerializer,
    MyAdventureDetailSerializer,
    MyAdventureListSerializer
    )


# class AdventureList(APIView):
#     def get(self, response):
#         Adventure = Adventure.objects.all()
#         serializer = Adventureerializer(Adventure, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = Adventureerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#new type of api setup from codingforentrepreneurs

class AdventureCreateAPIView(CreateAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()#user=self.request.user)


class AdventureDetailAPIView(RetrieveAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureDetailSerializer
    #lookup_field = 'slug'
    #lookup_url_kwarg = "abc"


class AdventureUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureCreateUpdateSerializer
    #lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save()#user=self.request.user)


class AdventureDeleteAPIView(DestroyAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureDetailSerializer
    #lookup_field = 'slug'
    #lookup_url_kwarg = "abc"


class AdventureListAPIView(ListAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureListSerializer

    #def get_queryset()



#myAdventure

class MyAdventureCreateAPIView(CreateAPIView):
    queryset = MyAdventure.objects.all()
    serializer_class = MyAdventureCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyAdventureDetailAPIView(RetrieveAPIView):
    queryset = MyAdventure.objects.all()
    serializer_class = MyAdventureDetailSerializer
    #lookup_field = 'slug'
    #lookup_url_kwarg = "abc"


class MyAdventureUpdateAPIView(RetrieveUpdateAPIView):
    queryset = MyAdventure.objects.all()
    serializer_class = MyAdventureCreateUpdateSerializer
    #lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class MyAdventureDeleteAPIView(DestroyAPIView):
    queryset = MyAdventure.objects.all()
    serializer_class = MyAdventureDetailSerializer
    #lookup_field = 'slug'
    #lookup_url_kwarg = "abc"


class MyAdventureListAPIView(ListAPIView):
    queryset = MyAdventure.objects.all()
    serializer_class = MyAdventureDetailSerializer #MyAdventureListSerializer

    #def get_queryset()



# class MyAdventureView(APIView):
#     def get(self, response):
#
#         #get only elements used by user
#         myAdventure = MyAdventure.objects.filter(user=self.request.user)
#
#         myAdventureerializer = MyAdventureerializer(myAdventure, many=True)
#
#         return Response(myAdventureerializer.data)
#
#     def post(self, request):
#         serializer = MyAdventureerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UsersView(APIView):
#     def get(self, response):
#         user = User.objects.all()
#         serializer = UsersSerializer(user, many=False)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'POST'])
# def task_list(request):
#     """
#     List all tasks, or create a new task.
#     """
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Get, udpate, or delete a specific task
#     """
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(
#                 serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)