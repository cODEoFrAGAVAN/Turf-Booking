import traceback
from typing import MutableSet

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.status import HTTP_200_OK

from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
import random
import string

# Create your views here.
class Turf_registration_process(ListCreateAPIView):
    queryset = Turf_registration.objects.all()
    serializer_class = Turf_registration_serializer
    parser_classes = [MultiPartParser,FormParser]

    def turid_generation(self,length = 10)->str:
        try:
            chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
            return ''.join(random.choices(chars, k=length))
        except Exception as e:
            print(" :: turid_generation error :: "+str(e)+" :: traceback :: "+traceback.format_exc())
            return "ERROR"

    def post(self, request, *args, **kwargs):
        input_data = request.data.copy()
        turf_id:str = self.turid_generation()
        if turf_id.upper() == "ERROR":
            return Response(
                {
                    "msg":"Turf registration failed",
                    "error":"Turf id creation error"
                },status=status.HTTP_400_BAD_REQUEST
            )
        input_data['turf_id'] = turf_id
        serializer = self.serializer_class(data=input_data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg":"Turf registration successfully"
                },status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "msg":"Turf registration failed",
                    "error":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST
            )
    def get(self,request,*args,**kwargs):
        user_name = request.query_params.get('user_name', None)
        if user_name:
            turf_data = Turf_registration.objects.filter(turf_username=user_name)
        else:
            turf_data = Turf_registration.objects.all()
        serializer = self.get_serializer(turf_data,many=True)
        return Response({
            "data":serializer.data,
            "msg":"Success"
        }
            ,status=HTTP_200_OK
        )
        # else:
        #     return  Response(
        #         {
        #             "msg":"Something went wrong. Please try again later.",
        #             "error":serializer.errors
        #         }
        #     )


