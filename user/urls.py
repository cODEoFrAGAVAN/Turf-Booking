from django.urls import path
from .views import *


urlpatterns = [
    path("sighup",User_sigin_up.as_view())
]