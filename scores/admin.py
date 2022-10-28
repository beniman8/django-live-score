from django.contrib import admin
from .models import Fixture,Tournament,Team


admin.site.register(Fixture)
admin.site.register(Tournament)
admin.site.register(Team)
