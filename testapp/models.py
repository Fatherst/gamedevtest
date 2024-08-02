from django.utils import timezone
from django.db import models


class Boost(models.Model):
    title = models.CharField(max_length=150)


class Player(models.Model):
    player_id = models.CharField(max_length=100)
    username = models.CharField(max_length=150, blank=True)
    prizes = models.ManyToManyField('Prize', related_name='players', null=True, blank=True)

    def assign_boost(self, boost):
        player_boost, created = PlayerBoost.objects.get_or_create(
            player=self,
            boost=boost
        )
        return player_boost, created


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField()


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def complete_level(self):
        self.completed = True
        self.completed = timezone.now()
        self.save()

        level_prizes = LevelPrize.objects.filter(level=self.level)
        for level_prize in level_prizes:
            self.player.prizes.add(level_prize.prize)

class PlayerBoost(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost = models.ForeignKey(Boost, on_delete=models.CASCADE)

