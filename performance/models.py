from django.db import models
from player.models import Player


class PerformanceTotal(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    tournaments = models.BigIntegerField()
    matches = models.BigIntegerField()
    batting_innings = models.BigIntegerField()
    batting_runs = models.BigIntegerField()
    high_score = models.BigIntegerField()
    batting_avg = models.FloatField()
    batting_best = models.BigIntegerField()
    strike_rate = models.FloatField()
    hundreds = models.BigIntegerField()
    fifties = models.BigIntegerField()
    sixes = models.IntegerField()
    fours = models.IntegerField()
    bowling_runs = models.BigIntegerField()
    bowling_innings = models.BigIntegerField()
    wickets = models.BigIntegerField()
    bowling_avg = models.FloatField()
    bowling_best = models.FloatField()
    economy = models.FloatField()

    def __str__(self):
        return self.player.get_full_name()


class PerformanceMatchWise(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    match = models.ForeignKey('tournament.Match', on_delete=models.CASCADE, null=True)
    tournament = models.ForeignKey('tournament.Tournament', on_delete=models.CASCADE, null=True)
    team = models.ForeignKey('tournament.Team', on_delete=models.CASCADE, null=True)
    batting_runs = models.BigIntegerField(default=0)
    strike_rate = models.FloatField(default=0)
    sixes = models.IntegerField(default=0)
    fours = models.IntegerField(default=0)
    bowling_runs = models.BigIntegerField(default=0)
    bowling_overs = models.BigIntegerField(default=0)
    wickets = models.BigIntegerField(default=0)
    bowling_avg = models.FloatField(default=0)
    economy = models.FloatField(default=0)
    status = models.BooleanField(default=False)

