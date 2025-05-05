import traceback
from typing import MutableSet

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.status import HTTP_200_OK

from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
import random
import string
import uuid

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
        input_data['turf_uuid'] = uuid.uuid4()
        print(input_data)
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
        serializer = self.serializer_class(turf_data,many=True)
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
class Turf_details_updation(RetrieveUpdateDestroyAPIView):
    # queryset = Turf_registration.objects.all()
    # serializer_class = Turf_details_updation_serializers
    def delete(self, request, *args, **kwargs):
        turf_id = request.query_params.get("turf_id","")
        if turf_id:
            try:
                turf_obj = Turf_registration.objects.get(turf_id=turf_id)
                turf_obj.delete()
                return Response(
                    {
                        "msg":"Turf deleted"
                    },status=status.HTTP_200_OK
                )
            except Exception as e:
                print(" :: Turf_details_updation error :: "+str(e)+" :: traceback :: "+traceback.format_exc())
                return Response({"msg": "Turf not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"msg": "turf_username param is required"}, status=status.HTTP_400_BAD_REQUEST)

        # obj = self.get_object()
        # if obj:
        #     obj.delete()
        #     return Response(
        #         {
        #             "msg":"Turf deleted"
        #         },status=status.HTTP_200_OK
        #     )
        # else:
        #     return Response(
        #         {
        #             "msg":"Turf not deleted"
        #         },status=status.HTTP_200_OK
        #     )


