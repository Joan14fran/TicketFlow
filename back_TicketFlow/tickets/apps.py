from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_category(sender, **kwargs):
    """Crea la categoría por defecto al iniciar la app"""
    from .models import Category
    if not Category.objects.filter(name='Soporte General').exists():
        Category.objects.create(name='Soporte General')
        print("--- Categoría 'Soporte General' creada automáticamente ---")

class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tickets'

    def ready(self):
        post_migrate.connect(create_default_category, sender=self)
