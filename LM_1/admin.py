from django.contrib import admin
from .models import team, player

class teamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'league', 'short','nation' ]
    search_fields = ['name', 'league','short']

class playerAdmin(admin.ModelAdmin):
    list_display = ['id', 'nick', 'name', 'position','team' ]
    search_fields = ['name', 'league','short']


admin.site.register(team, teamAdmin)
admin.site.register(player, playerAdmin)
