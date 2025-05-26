from django.contrib import admin
from django.urls import path

from .views import get_view_home_page

urlpatterns = [
    path("", get_view_home_page, name="home"),
]
