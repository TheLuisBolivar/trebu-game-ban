from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "id: " + str(self.pk) + ", name: " + str(self.name)


class Reason(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "id: " + str(self.pk) + ", reason: " + str(self.name)


class Blacklist(models.Model):
    game = models.ForeignKey(Game, related_name="games", on_delete=models.PROTECT)
    reason = models.ForeignKey(Reason, on_delete=models.PROTECT, null=True)
    email = models.EmailField(max_length=200)
    date_report = models.DateField(default=timezone.now())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "user: " + str(self.email) + ", is banned in the game: " + self.game.name + ", for: " + str(self.reason.name) + "reason"
