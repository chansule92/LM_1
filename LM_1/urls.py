from django.urls import path

from . import views

app_name = 'LM_1'

urlpatterns = [
    path('index', views.index, name='index'),
    path('team', views.team_index, name='team_index'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
]
