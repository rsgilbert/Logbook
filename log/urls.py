from django.urls import path
from . import views

app_name = "log"


urlpatterns = [
    path('', views.log, name="log"),
    path('log/', views.log, name="log"),
]