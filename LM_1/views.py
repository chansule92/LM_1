from django.shortcuts import render, get_object_or_404
from .models import team,player,game,game_detail,game_entire
from django.db.models import Count, Sum
from django.db import connection

def index(request):

    return render(request, 'LM_1/index.html')

def test(request):

    return render(request, 'LM_1/test.html')


def team_index(request):

    team_list = team.objects.order_by('-name')
    context = {'team_list': team_list}
    return render(request, 'LM_1/team_list.html', context)


def team_detail(request, team_id):
    team_content = team.objects.get(id=team_id)
    cursor=connection.cursor()
    player = "SELECT lm_1_game_detail.nick, count(lm_1_game_detail.nick) AS play, lm_1_player.team_id,lm_1_player.position,lm_1_player.nation from lm_1_game_detail join lm_1_player on lm_1_game_detail.nick=lm_1_player.nick and lm_1_player.team_id=1 group by nick limit 5;"
    result=cursor.execute(player)
    ranking= cursor.fetchall()
    connection.commit()
    connection.close()

    context = {'team_content': team_content, 'player':player}
    return render(request, 'LM_1/team_detail.html', context)


def player_index(request):

    player_list = player.objects.order_by('nick')
    context = {'player_list': player_list}
    return render(request, 'LM_1/player_list.html', context)


def player_detail(request, player_id):

    player_content = player.objects.get(id=player_id)
    play = game_detail.objects.values_list('nick').filter(nick = player_content.nick).annotate(total_play=Count('number'))
    kill = game_detail.objects.values_list('nick').filter(nick = player_content.nick).annotate(total_kill=Sum('slay'))
    most = game_detail.objects.values('champion').filter(nick = player_content.nick).annotate(most_champion=Count('champion')).order_by('-most_champion')[:5]

    context = {'player_content': player_content,'play':play, 'kill':kill, 'most':most}
    return render(request, 'LM_1/player_detail.html', context)

def league_index(request):

    cursor=connection.cursor()
    win = "SELECT team,Sum(win) AS win ,18-Sum(win) AS lose, count_win.count_win, lose.count_lose, count_win.count_win-lose.count_lose AS games  FROM(SELECT home AS team,count(home) AS win FROM loldb.lm_1_game_entire where homescore=2 GROUP BY home union all SELECT away AS team,count(away) AS win FROM loldb.lm_1_game_entire where awayscore=2 GROUP BY away) ad JOIN count_win ON ad.team=count_win.win_team JOIN lose ON ad.team=lose_team group by team order by -sum(win)"
    result=cursor.execute(win)
    ranking= cursor.fetchall()
    connection.commit()
    connection.close()

    context = {'ranking': ranking,}
    return render(request, 'LM_1/league_list.html', context)

def schedule_index(request):

    schedule_list = game_entire.objects.order_by('date')
    context = {'schedule_list': schedule_list}
    return render(request, 'LM_1/schedule.html', context)


def tounament_index(request):
    schedule_list = game_entire.objects.order_by('-date')[:5]

    cursor=connection.cursor()
    win = "SELECT team,Sum(win) AS win ,18-Sum(win) AS lose, count_win.count_win, lose.count_lose, count_win.count_win-lose.count_lose AS games  FROM(SELECT home AS team,count(home) AS win FROM loldb.lm_1_game_entire where homescore=2 GROUP BY home union all SELECT away AS team,count(away) AS win FROM loldb.lm_1_game_entire where awayscore=2 GROUP BY away) ad JOIN count_win ON ad.team=count_win.win_team JOIN lose ON ad.team=lose_team group by team order by -sum(win)"
    result=cursor.execute(win)
    ranking= cursor.fetchall()
    connection.commit()
    connection.close()

    cursor=connection.cursor()
    sum_kill = "SELECT nick, sum(slay) FROM loldb.lm_1_game_detail GROUP by nick order by -sum(slay) limit 5;"
    result=cursor.execute(sum_kill)
    kill_record = cursor.fetchall()
    connection.commit()
    connection.close()

    cursor=connection.cursor()
    sol_kill = "SELECT nick,sum(solo_kill) FROM loldb.lm_1_game_detail GROUP by nick order by -sum(solo_kill) limit 5;"
    result=cursor.execute(sol_kill)
    solo_kill_record = cursor.fetchall()
    connection.commit()
    connection.close()

    cursor=connection.cursor()
    sum_assist = "SELECT nick, sum(assist) FROM loldb.lm_1_game_detail GROUP by nick order by -sum(assist) limit 5;"
    result=cursor.execute(sum_assist)
    assist_record = cursor.fetchall()
    connection.commit()
    connection.close()

    cursor=connection.cursor()
    avg_deal = "SELECT nick, ROUND(sum(champion_damage)/count(nick)) FROM loldb.lm_1_game_detail GROUP by nick order by -sum(champion_damage)/count(nick) limit 5;"
    result=cursor.execute(avg_deal)
    avg_deal = cursor.fetchall()
    connection.commit()
    connection.close()

    cursor=connection.cursor()
    avg_vision = "SELECT nick, ROUND(sum(vision)/count(nick)) FROM loldb.lm_1_game_detail GROUP by nick order by -sum(vision)/count(nick) limit 5;"
    result=cursor.execute(avg_vision)
    avg_vision = cursor.fetchall()
    connection.commit()
    connection.close()

    context = {'schedule_list': schedule_list, 'ranking': ranking,'kill_record':kill_record ,'assist_record':assist_record, 'avg_deal':avg_deal, 'avg_vision':avg_vision,'solo_kill_record':solo_kill_record }
    return render(request, 'LM_1/tounament.html', context)
