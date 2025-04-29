from django.db import models
from django.utils import timezone
from uuid import uuid4

class User_signup(models.Model):
    unique_id = models.UUIDField(default=uuid4(),primary_key=True)
    user_name = models.CharField(max_length=30,null=False,unique=False)
    name = models.CharField(max_length=50,null=False)
    mobile_number = models.CharField(max_length=10,null=False,unique=True)
    mailid = models.EmailField(unique=True,null=False,max_length=50)
    password = models.CharField(max_length=128,null=False)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user_name


class Login(models.Model):
    unique_id = models.ForeignKey(User_signup,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30,null=False,unique=False)
    password = models.CharField(max_length=128,null=False)
    def __str__(self):
        return self.user_name

class Random_token_generation(models.Model):
    unique_id = models.ForeignKey(User_signup,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30,null=False,unique=False)
    random_token = models.TextField(null=False,unique=True)
    def __str__(self):
        return  self.user_name


