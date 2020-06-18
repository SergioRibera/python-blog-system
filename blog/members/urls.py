from django.urls import path
from .views import UserRegisterVew

urlpatterns = [
    path('register/', UserRegisterVew.as_view(), name='register'),
    path('login/', UserRegisterVew.as_view(), name='login'),
]
