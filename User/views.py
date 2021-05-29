from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializers import UserSerializer  


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print("data", request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.errors, status=status.HTTP_201_CREATED)