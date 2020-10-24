from django.db import models
from django.db.models import Count



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

class game_entire(models.Model):
    date = models.DateField()
    home = models.CharField(max_length=20)
    homescore = models.IntegerField(1)
    away = models.CharField(max_length=20)
    awayscore = models.IntegerField(4)


class game(models.Model):
    number = models.AutoField(primary_key = True)
    date =  models.DateField()
    blue = models.CharField(max_length=20)
    purple = models.CharField(max_length=20)
    time = models.TimeField()
    winner  = models.CharField(max_length=20)
    loser = models.CharField(max_length=20)


class game_detail(models.Model):
    number = models.ForeignKey(game,on_delete=models.CASCADE)
    nick = models.CharField(max_length=20)
    champion = models.CharField(max_length=20)
    Kill = models.IntegerField(3)
    death = models.IntegerField(3)
    assist = models.IntegerField(3)
    CS = models.IntegerField(4)
    CS_in_teamjungle = models.IntegerField(3)
    CS_in_enemyjungle = models.IntegerField(3)
    gold = models.IntegerField(10)
    vision = models.IntegerField(3)
    ward_place = models.IntegerField(3)
    ward_destroyed = models.IntegerField(3)
    Pinkward_purchase = models.IntegerField(3)
    champion_damage = models.IntegerField(10)
    solo_kill = models.IntegerField(2)
    GD_15 = models.IntegerField(10)
    CSD_15 = models.IntegerField(10)
    XPD_15 = models.IntegerField(10)
    LVLD_15 = models.IntegerField(10)
    turet_damage = models.IntegerField(10)
    taken_damage = models.IntegerField(10)
