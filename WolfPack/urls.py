from django.contrib import admin
from django.urls import path, include
from tweets import views
from tweets.views import (home_view, tweet_detail_view, tweet_list_view, tweet_create_view, register_request)
from django.conf import settings
from django.conf.urls.static import static


app_name = "main"   

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view ),
    path('create-tweet', tweet_create_view),
    path('tweets', tweet_list_view),    
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path("logout", views.logout_request, name= "logout"),
    path("login", views.login_request, name="login"),
    path("register/", register_request),
    path('',include('todo.urls'))
    # path('',include('users.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)