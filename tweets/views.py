from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .forms import TweetForm
from .models import Tweet
import random 

    
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *arg, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
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