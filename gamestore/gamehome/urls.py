from django.urls import path
from gamehome import views
urlpatterns = [
    path('', views.gamehome),
    path('', views.showgame, name="showgame")
]
