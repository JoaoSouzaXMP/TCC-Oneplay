from django.urls import path
from .views import all_games, one_game

urlpatterns = [
    path('all-games', all_games, name='all_games'),
    path('one-game/<int:jogo_id>', one_game, name='one_game'),
]