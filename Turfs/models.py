from django.db import models
from uuid import uuid4
from django.utils import timezone

class Turf_registration(models.Model):
    turf_uuid = models.UUIDField(primary_key=True,default=uuid4())
    turf_id = models.CharField(max_length=20,unique=True,null=False)
    turf_name = models.CharField(max_length=100,null=False)
    turf_address = models.TextField(null=False)
    turf_pincode = models.CharField(max_length=20,null=False)
    turf_owner_name = models.CharField(max_length=50,null=False)
    turf_email_id = models.EmailField(unique=True,null=False)
    turf_mobile_number = models.CharField(max_length=10,unique=True,null=False)
    turf_alternate_mobile_number = models.CharField(max_length=10,default='',null=False)
    turf_land_line_number = models.CharField(max_length=30,default='',null=False)
    turf_images_path = models.TextField(null=False)
    turf_username = models.CharField(max_length=20,unique=True,null=False)
    turf_password = models.CharField(max_length=128,null=False)
    turf_starting_time = models.CharField(max_length=10,null=False,default='6 A.M')
    turf_ending_time = models.CharField(max_length=10,null=False,default='12 P.M')
    turf_register_date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  self.turf_id


