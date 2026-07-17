from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('contact/', views.contact_page_view),
    path('messages/', views.MessageListView.as_view())
]
