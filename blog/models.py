from django.db import models
from django.contrib.auth.models import User

# Model de type ForeignKey (plusieurs a un)

class Auteur(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(
        to= Auteur,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.name} - {self.Auteur}"

# model one to one

class Profile(models.Model):
    user = models.OneToOneField(
        to= User,
        on_delete=models.CASCADE
    )
    bio = models.TextField()
    site_web = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
