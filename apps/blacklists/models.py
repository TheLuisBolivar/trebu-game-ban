from django.db import models
from django.utils import timezone
from apps.games.models import Game
from apps.reasons.models import Reason


class Blacklist(models.Model):
    game = models.ForeignKey(Game, related_name="games", on_delete=models.PROTECT)
    reason = models.ForeignKey(Reason, on_delete=models.PROTECT, null=True)
    email = models.EmailField(max_length=200)
    date_report = models.DateField(default=timezone.now())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.email}: {self.game}, {self.reason}'
