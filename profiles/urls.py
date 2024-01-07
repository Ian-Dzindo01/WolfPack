from django.urls import path
from .views import profile_detailed_view

urlpatterns = [
    path('profiles/<str:username>', profile_detailed_view)
]