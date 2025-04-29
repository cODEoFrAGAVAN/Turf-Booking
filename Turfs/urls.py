from django.urls import path
from .views import *


urlpatterns = [
    path("registraion",Turf_registration_process.as_view())
]