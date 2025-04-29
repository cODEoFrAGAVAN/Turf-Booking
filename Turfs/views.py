import traceback

from django.core.serializers import serialize
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
import random
import string

# Create your views here.
class Turf_registration_process(ListCreateAPIView):
    queryset = Turf_registration
    serializer_class = Turf_registration_serializer

    def turid_generation(self,length = 10)->str:
        try:
            chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
            return ''.join(random.choices(chars, k=length))
        except Exception as e:
            print(" :: turid_generation error :: "+str(e)+" :: traceback :: "+traceback.format_exc())
            return "ERROR"

    def post(self, request, *args, **kwargs):
        input_data = request.data
        turf_id:str = self.turid_generation()
        if turf_id.upper() == "ERROR":
            return Response(
                {
                    "msg":"Turf registration failed",
                    "error":"Turf id creation error"
                },status=status.HTTP_400_BAD_REQUEST
            )
        input_data['turf_id'] = turf_id
        serializer = self.serializer_class(data=request.data)
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


