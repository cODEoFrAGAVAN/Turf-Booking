from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView


class User_sigin_up(ListCreateAPIView):
    queryset = User_signup.objects.all()
    serializer_class = User_sign_up_serializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        d = request.data

        return Response("done",status=status.HTTP_200_OK)