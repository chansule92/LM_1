from django.db import models


class team(models.Model):
    name = models.CharField(max_length=20)
    league = models.CharField(max_length=20)
    short = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)



class player(models.Model):
    team =models.ForeignKey(team, on_delete=models.CASCADE)
    nick = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    nation = models.CharField(max_length=20)
