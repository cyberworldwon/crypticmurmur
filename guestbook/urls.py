from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('guestbook/', views.guestbook, name='guestbook'),
    path('manifesto/', views.manifesto, name='manifesto'),
]