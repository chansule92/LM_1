from django.urls import path

from . import views

app_name = 'LM_1'

urlpatterns = [
    path('index', views.index, name='index'),
    path('team', views.team_index, name='team_index'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('player', views.player_index, name='player_index'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('league', views.league_index, name='league_index'),
    path('schedule', views.schedule_index, name='schedule_index'),
    path('tounament', views.tounament_index, name='tounament_index'),

]
