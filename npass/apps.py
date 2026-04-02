from django.urls import path
from .views import home, cybersickness_predict_view

urlpatterns = [
    path("", home, name="home"),
    path("api/predict/", cybersickness_predict_view, name="predict"),
]