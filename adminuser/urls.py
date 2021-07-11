from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registerAdmin/', views.AdminUserDetails.as_view()),
    path('updateCovidResult/<int:id>/', views.UpdateUserResult.as_view())
]