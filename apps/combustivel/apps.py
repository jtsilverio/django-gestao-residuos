from django.apps import AppConfig


class CombustivelConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.combustivel"

def get_model():
    return apps.get_app_config('Combustivel').get_model("Combustivel")