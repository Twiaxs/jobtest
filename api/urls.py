from django.urls import path
from api.views import SomeAPI



urlpatterns = [
    path('api/meta/', SomeAPI.as_view()),
]