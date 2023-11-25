from django.apps import AppConfig


# creating a configuration class for your Django app named "tracker".
class TrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracker"
