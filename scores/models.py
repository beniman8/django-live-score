from django.db import models

class Tournament(models.Model):
    name=models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Team(models.Model):
    name=models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='fixture', on_delete=models.CASCADE)
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.home_team} vs {self.away_team}"

