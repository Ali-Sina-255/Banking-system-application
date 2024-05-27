from django.urls import path
from . import views
urlpatterns = [
    path('', views.UserRegister,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.login_view,name='logout'),
]
