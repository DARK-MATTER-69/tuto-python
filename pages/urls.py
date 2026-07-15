from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view),
    path('contact/', views.contact_page_view),
    path('messages/', views.message_list_view)
]
