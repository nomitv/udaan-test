from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registerUser/', views.UserDetails.as_view()),
    path('selfAssessment/<int:id>/', views.UserAssessment.as_view()),
    path('getZoneInfo', views.GetZoneDetails.as_view())
]