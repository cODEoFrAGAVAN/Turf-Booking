from django.core.serializers import serialize
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
import secrets
from datetime import datetime,timedelta
import jwt
import traceback


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

class User_login(ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = Login_serializer

    def create_session(self,cc:str,random_token:str)->str:
        try:
            payload = {
                'login': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'logout': (datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S"),
                'cc': cc
            }
            encode = jwt.encode(payload=payload, key=random_token, algorithm="HS256")
            return  encode
        except Exception as e:
            print(
                " :: create session error :: "+str(e)+" :: traceback :: "+traceback.format_exc()
            )
            return "ERROR"

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token_values = Random_token_generation.objects.get(user_name=request.data.get('user_name'))
            sess:str = self.create_session(cc=request.data.get('user_name'),random_token=token_values.random_token)
            if sess.upper() == "ERROR":
                return Response(
                    {
                        'session': '',
                        'msg': 'Login failed'
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            return Response(
                {
                    'session':sess,
                    'msg':'Login successfully'
                },status=status.HTTP_200_OK
            )
        else:
            return  Response(
                {
                    'session':'',
                    'msg':'Login failed'
                },status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request, *args, **kwargs):
        user_name = request.query_params.get('user_name', None)
        if user_name:
            logins = Login.objects.filter(user_name=user_name)
        else:
            logins = Login.objects.all()

        serializer = self.get_serializer(logins, many=True)
        return Response(serializer.data)


class Update_user_password(RetrieveUpdateDestroyAPIView):
    queryset = User_signup.objects.all()
    serializer_class = Update_password_serializer

    def patch(self,request,pk):
        user = get_object_or_404(User_signup, pk=pk)
        serializer = self.serializer_class(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg":"Password updated"
                },status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "msg":"Password not updated",
                    "error":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST
            )


class getting_user_data(ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = get_single_user_data_serializer
    def get(self, request, *args, **kwargs):
        user_name = request.query_params.get('user_name', None)
        if user_name:
            logins = Login.objects.filter(user_name=user_name)
        else:
            logins = Login.objects.all()

        serializer = self.get_serializer(logins, many=True)
        return Response(serializer.data)
