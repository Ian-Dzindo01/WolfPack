from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

from .forms import TweetForm, NewUserForm
from .models import Tweet
import random 


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *arg, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        # if request.is_ajax():                      # ajax is deprecated
        #     return JsonResponse({}, status=201)    # 201 is for created items


        if next_url != None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()

    return render(request, 'components/form.html', context={"form":form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]   # implement a real like function, working on rands now 
    data = {
        "isUser":False,                       # change this in the future
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):    # output additional detailed info for each tweet
    data = {
    "id": tweet_id
    }  
    status = 200 
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404

    return JsonResponse(data, status=status)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
          
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
          
		messages.error(request, "Unsuccessful registration. Invalid information.")
          
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			
			else:
				messages.error(request,"Invalid username or password.")
		else:   
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")