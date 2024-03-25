from django.urls import path, include
from trollapp import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("lobby/", views.lobby, name="lobby"),
 
    # login-section
    path("auth/login/", LoginView.as_view #changed
         (template_name="login.html"), name="login-user"), #changed
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path("race/", views.race, name="race"),


    # lobbies
    path('joinedLobby/<int:lobby_id>/', views.joinedLobby, name='joinedLobby'),

    path('create-lobby/', views.create_lobby_page, name='create-lobby-page'),
    path('create-lobby/action', views.create_lobby, name='create-lobby-action'),

    path('check_lobby/<int:lobby_id>/', views.check_lobby, name='check_lobby'),
    path('increase_players_joined/<int:lobby_id>/', views.increase_players_joined, name='increase_players_joined'),
]