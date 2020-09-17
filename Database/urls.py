from django.urls import path, include
from . import views

app_name = "authentication"
urlpatterns = [
    path('', views.index, name="index")
]
