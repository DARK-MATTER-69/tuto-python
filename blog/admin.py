from django.contrib import admin
from blog.models import Auteur, Article, Profile, Tag

admin.site.register(Auteur)
admin.site.register(Article)
admin.site.register(Profile)
admin.site.register(Tag)
