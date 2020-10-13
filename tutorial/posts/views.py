import urllib3
import json
from django.shortcuts import render
from rest_framework.response import Response
from posts.models import PostUserDetails
from posts.serializers import PostSerializerUser
from rest_framework import status
# from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from posts.validators import *


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        user = PostUserDetails.objects.all()
        serializer = PostSerializerUser(user, many=True)
        # print(request)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializerUser(data=request.data)

        if serializer.is_valid():
            if GBooks(serializer.validated_data['isbn']) == True:

                f = open("gbooks.txt", "r")
                details = (f.read()).split(",")
                serializer.validated_data['bookTitle'] = details[0]
                serializer.validated_data['bookAuthor'] = details[1]
                serializer.validated_data['date_Added'] = details[2]
                serializer.save()
                file2 = open("gbooks.txt", "w")
                file2.write('')
                file2.close()
            else:
                return Response("Invalid book. Please check ISBN.")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = PostUserDetails.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializerUser(user)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        queryset = PostUserDetails.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def search(request):
        user_list = PostUserDetails.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return Response(request)
