from rest_framework.serializers import ModelSerializer
from .models import *

class Turf_registration_serializer(ModelSerializer):
    class Meta:
        model = Turf_registration
        fields = ['turf_id',
                'turf_name',
                'turf_address',
                'turf_pincode',
                'turf_owner_name',
                'turf_email_id',
                'turf_mobile_number',
                'turf_alternate_mobile_number',
                'turf_land_line_number',
                'turf_images_path',
                'turf_username',
                'turf_password',
                'turf_starting_time',
                'turf_ending_time',
                'turf_available_games']


