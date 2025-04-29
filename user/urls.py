from django.urls import path
from .views import *


urlpatterns = [
    path("sighup",User_sigin_up.as_view()),
    path("login",User_login.as_view()),
    path("user_datas",getting_user_data.as_view()),
    path("update_password/<uuid:pk>",Update_user_password.as_view(),name="password_update")
]