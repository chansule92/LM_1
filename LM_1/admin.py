from django.contrib import admin
from .models import team, player, game, game_detail

class teamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'league', 'short','nation' ]
    search_fields = ['name', 'league','short']

class playerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'name', 'position','team' ]
    search_fields = ['name', 'league','short']

class gameAdmin(admin.ModelAdmin):
    list_display = ['date', 'blue', 'purple', 'time','winner','loser' ]
    search_fields = ['date', 'blue','purple']


class game_detailAdmin(admin.ModelAdmin):
    list_display = ['nick', 'champion', 'Kill', 'death','assist' ]
    search_fields = ['nick', 'champion']



admin.site.register(team, teamAdmin)
admin.site.register(player, playerAdmin)
admin.site.register(game, gameAdmin)
admin.site.register(game_detail, game_detailAdmin)
