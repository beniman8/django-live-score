import time
import random
from django.core.management.base import BaseCommand
from scores.models import Team, Fixture


class Command(BaseCommand):
    help = "Load EPL teams and fixtures"

    def handle(self, *args, **kwargs):
        ITERATIONS = 10

        for i in range(ITERATIONS):
            time.sleep(random.randint(1, 6))

            update_count = random.randint(1, 6)

            fixtures = Fixture.objects.filter(game_finished=False).order_by("?")

            fixtures = fixtures[:update_count]

            self.update_fixtures(fixtures)

            self.is_game_finished(fixtures)

    def update_fixtures(self, fixtures):

        for fixture in fixtures:
            home_goal = random.randint(1, 2)
            away_goal = random.randint(1, 2)
            fixture.home_goals += home_goal
            fixture.away_goals += away_goal

        Fixture.objects.bulk_update(fixtures, ["home_goals", "away_goals"])

    def is_game_finished(self, fixtures):

        for fixture in fixtures:

            P = random.uniform(0, 1)
            if P < 0.3:
                fixture.game_finished = True
                fixture.save()
