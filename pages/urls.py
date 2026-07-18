from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(),name="home"),
    path('contact/', views.contact_page_view, name="contact"),
    path('messages/', views.MessageListView.as_view(),name="messages")
]
