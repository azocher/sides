from django.urls import path

#import local views file
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:flight_id>", views.flight)
]
