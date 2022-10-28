from django.core.management.base import BaseCommand
from scores.models import Team,Tournament,Fixture

TEAMS = [
    "Arsenal",
    "Aston Villa",
    "Brentford",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Leeds United",
    "Leicester City",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Norwich City",
    "Southampton",
    "Tottenham Hotspur",
    "Watford",
    "West Ham United",
    "Wolverhampton Wanderers",
]


class Command(BaseCommand):
    help = "Load EPL teams and fixtures"

    def handle(self, *args, **kwargs):
        
        tournament = Tournament.objects.get_or_create(name="Premier League")[0]


        if Team.objects.count() == 0:
            team_objs = [Team(name=team_name) for team_name in TEAMS]
            teams = Team.objects.bulk_create(team_objs)
            teams = Team.objects.all()
        else:
            teams = Team.objects.all()



        fixtures = [] 
        for i in range(0,len(teams),2):
            fixtures.append(
                Fixture(home_team=teams[i],away_team=teams[i+1],tournament=tournament)
            )



        if Fixture.objects.count() == 0:
            fixtures = Fixture.objects.bulk_create(fixtures)