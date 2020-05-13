from django.urls import path, include
from .views import UserData

urlpatterns = [
    path('data/<str:username>/', UserData.as_view()),
]
