from django.shortcuts import render, get_object_or_404
from .models import team


def index(request):

    return render(request, 'LM_1/index.html')

def team_index(request):

    team_list = team.objects.order_by('-id')
    context = {'team_list': team_list}
    return render(request, 'LM_1/team_list.html', context)


def team_detail(request, team_id):

    team_content = team.objects.get(id=team_id)
    context = {'team_content': team_content}
    return render(request, 'LM_1/team_detail.html', context)
