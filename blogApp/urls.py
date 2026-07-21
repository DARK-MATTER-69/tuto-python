from django.urls import path
from blogApp import views
name_app = 'blogapp'

urlpatterns = [
    path('',views.accueil_view)
]
