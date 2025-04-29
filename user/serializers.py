from .models import *
from rest_framework.serializers import ModelSerializer


class User_sign_up_serializer(ModelSerializer):
    class Meta:
        model = User_signup
        fields = ['user_name','name','mobile_number','mailid','password']

class Login_serializer(ModelSerializer):
    class Meta:
        model = Login
        fields = ['user_name','password']


class Random_token_serialzer(ModelSerializer):
    class Meta:
        model = Random_token_generation
        fields = ['user_name','random_token']

class Update_password_serializer(ModelSerializer):
    class Meta:
        model = User_signup
        fields = ['password']

class get_single_user_data_serializer(ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'


