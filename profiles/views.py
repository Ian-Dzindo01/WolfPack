from django.shortcuts import render

def profile_detailed_view(request, username, *args, **kwargs):
    return render(request, "profiles/detail.html", {"username":username})