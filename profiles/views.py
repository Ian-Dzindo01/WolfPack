from django.shortcuts import render
from django.http import Http404

from .models import Profile

def profile_detailed_view(request, username, *args, **kwargs):
    qs = Profile.objects.filter(user_username=username)
    if not qs.exists():
        raise Http404
    
    profile_object = qs.first()
    
    context = {
        "username": username,
        "profile": profile_obj
    }
    
    return render(request, "profiles/detail.html", context)