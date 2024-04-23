from django.urls import path

from . import views

app_name = "liftover"
urlpatterns = [
    path("", views.index, name="index"),
]