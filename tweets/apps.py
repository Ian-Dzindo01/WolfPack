from django.apps import AppConfig



class TweetsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tweets"


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        import users.signals