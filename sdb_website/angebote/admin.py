from django.contrib import admin

from .models import Mitarbeiter
from .models import Sprecherinnen
from .models import Angebot

admin.site.register(Mitarbeiter)
admin.site.register(Sprecherinnen)
admin.site.register(Angebot)
