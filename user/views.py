from django.core.serializers import serialize
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
import secrets


class User_sigin_up(ListCreateAPIView):
    queryset = User_signup.objects.all()
    serializer_class = User_sign_up_serializer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            login_data = {
                "user_name":user.user_name,
                "password":user.password,
            }
            login_serializer = Login_serializer(data=login_data)
            if login_serializer.is_valid():
                login_serializer.save(unique_id=user)
            else:
                return Response(
                    {
                        "msg":"login serializer validation error",
                        "error":login_serializer.errors
                    },status=status.HTTP_400_BAD_REQUEST
                )
            random_token = secrets.token_hex(16)
            token_data = {
                "user_name": user.user_name,
                "random_token":random_token

            }
            random_token_serializer = Random_token_serialzer(data=token_data)
            if random_token_serializer.is_valid():
                random_token_serializer.save(unique_id=user)
            else:
                return Response(
                    {
                        "msg":"random token serializer error",
                        "error":random_token_serializer.errors
                    },status=status.HTTP_400_BAD_REQUEST
                )
            return  Response(
                {
                    "msg":"user created"
                },status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "msg":"validation failed",
                    "error":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST
            )