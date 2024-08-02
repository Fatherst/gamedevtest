from django.contrib import admin
from .models import Player, Level, Prize, LevelPrize, PlayerLevel

@admin.register(Player)
class PLayerAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'username', 'get_prizes']

    def get_prizes(self, obj):
        return "\n".join([p.title for p in obj.prizes.all()])


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(LevelPrize)
class LevelPrizeAdmin(admin.ModelAdmin):
    list_display = ['level', 'prize']

@admin.register(PlayerLevel)
class PlayerLevelAdmin(admin.ModelAdmin):
    list_display = ['player', 'level']