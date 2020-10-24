from django.shortcuts import render, get_object_or_404
from .models import team,player,game,game_detail
from django.db.models import Count, Sum

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

    player_list = player.objects.order_by('nick')
    context = {'player_list': player_list}
    return render(request, 'LM_1/player_list.html', context)


def player_detail(request, player_id):

    player_content = player.objects.get(id=player_id)
    play = game_detail.objects.values_list('nick').filter(nick = player_content.nick).annotate(total_play=Count('number'))
    kill = game_detail.objects.values_list('nick').filter(nick = player_content.nick).annotate(total_kill=Sum('Kill'))
    most = game_detail.objects.values('champion').filter(nick = player_content.nick).annotate(most_champion=Count('champion')).order_by('-most_champion')[:5]

    context = {'player_content': player_content,'play':play, 'kill':kill, 'most':most}
    return render(request, 'LM_1/player_detail.html', context)

def league_index(request):

    team_list = team.objects.order_by('league').distinct()
    context = {'team_list': team_list}
    return render(request, 'LM_1/league_list.html', context)
