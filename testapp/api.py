import csv

from django.http import HttpResponse
from ninja import Router
from .schemas import CompletedLevelSchema
from django.shortcuts import get_object_or_404
from .models import Player, Boost, Prize, PlayerLevel, Level, LevelPrize

testapp_router = Router()


@testapp_router.get("/csv_players")
def export_players(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="players.csv"'

    writer=csv.writer(response)
    writer.writerow(['Player ID','Level','Completed', 'Prize'])
    players = Player.objects.all()
    for player in players:
        player_levels = PlayerLevel.objects.filter(player=player)
        for player_level in player_levels:
            level_prizes = LevelPrize.objects.filter(level=player_level.level)
            prizes = [level_prize.prize.title for level_prize in level_prizes]
            prize_titles = ', '.join(prizes) if prizes else "No prize"
            writer.writerow([
                player.player_id,
                player_level.level.title,
                player_level.is_completed,
                prize_titles
            ])
    return response

@testapp_router.post("/assign_boost")
def boost_assignment(request, data: CompletedLevelSchema):
    player = get_object_or_404(Player, player_id=data.player_id)
    level = get_object_or_404(Level, id=data.level_id)
    player_level = get_object_or_404(PlayerLevel, player=player, level=level)
    player_level.complete_level()
    prizes = player.prizes.filter(levelprize__level=level)
    return f"{prizes}"
