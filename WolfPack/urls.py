from django.contrib import admin
from django.urls import path, include
from tweets import views
from tweets.views import (home_view, tweet_detail_view, tweet_list_view, tweet_create_view, register_request)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
    
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view ),
    path('create-tweet', tweet_create_view),
    path('tweets', tweet_list_view),    
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path("logout", views.logout_request, name= "logout"),
    path("login", views.login_request, name="login"),
    path("register/", register_request),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)