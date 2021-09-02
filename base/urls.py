from django.urls import path 
from .views import predict_view

app_name = 'base'

urlpatterns = [
    path('', predict_view, name="predict-view")
]