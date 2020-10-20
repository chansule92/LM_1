from django.shortcuts import render, get_object_or_404
from .models import team,player,game,game_detail
from django.db.models import Count, Sum, F

def index(request):

    return render(request, 'LM_1/index.html')

def team_index(request):

    team_list = team.objects.order_by('-name')
    context = {'team_list': team_list}
    return render(request, 'LM_1/team_list.html', context)


def team_detail(request, team_id):

    team_content = team.objects.get(id=team_id)
    context = {'team_content': team_content}
    return render(request, 'LM_1/team_detail.html', context)


def player_index(request):

    player_list = player.objects.order_by('-nick')
    context = {'player_list': player_list}
    return render(request, 'LM_1/player_list.html', context)


def player_detail(request, player_id):

    player_content = player.objects.get(id=player_id)
    context = {'player_content': player_content}
    n=game_detail.objects.filter(nick='players.Nick').annotate(count = Count('nick'))

    kill = game_detail.objects.values('nick').annotate(total_kill=Sum('Kill'))
    return render(request, 'LM_1/player_detail.html', context)

def league_index(request):

    team_list = team.objects.order_by('league').distinct()
    context = {'team_list': team_list}
    return render(request, 'LM_1/league_list.html', context)
