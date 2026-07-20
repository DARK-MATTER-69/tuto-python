from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    
    #autoriser l'utilisation de signals.py
    def ready(self):
        import blog.signals
