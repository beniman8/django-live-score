from django.contrib import admin
from django.urls import path
from .views import index,fixtures

urlpatterns = [
    path("", index,name='index'),
    path("fixtures/", fixtures,name='fixtures'),

]