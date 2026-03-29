from django.urls import path

from . import views

app_name = "studio"

urlpatterns = [
    path("", views.home, name="home"),
    path("games/", views.game_list, name="game_list"),
    path("games/<slug:slug>/", views.game_detail, name="game_detail"),
]
