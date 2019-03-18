from django.urls import path

#import local views file
from . import views

urlpatterns = [
    path("", views.index)
]
