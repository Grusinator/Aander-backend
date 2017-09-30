from django.shortcuts import render, get_object_or_404

from itertools import chain
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Adventures, MyAdventures,Clues,Locations,User
from .serializers import AdventuresSerializer, MyAdventuresSerializer, CluesSerializer, LocationsSerializer, UsersSerializer
from rest_framework.decorators import api_view


class AdventuresList(APIView):
    def get(self, response):
        adventures = Adventures.objects.all()
        serializer = AdventuresSerializer(adventures, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdventuresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyAdventuresView(APIView):
    def get(self, response):

        userid = 1

        #get only elements used by user
        myadventures = MyAdventures.objects.filter(userid__exact=userid)

        myadventureserializer = MyAdventuresSerializer(myadventures, many=True)

        return Response(myadventureserializer.data)

    def post(self, request):
        serializer = MyAdventuresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    def get(self, response):
        user = User.objects.all()
        serializer = UsersSerializer(user, many=False)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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