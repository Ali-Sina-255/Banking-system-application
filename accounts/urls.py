from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserRegister,name='register')
]
