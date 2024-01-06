from django.urls import path
from .views import profile_detailed_view

urlpatterns = [
    path('profile/<str:username>', profile_detailed_view)
]