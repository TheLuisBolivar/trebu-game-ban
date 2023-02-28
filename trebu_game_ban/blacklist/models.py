from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)


class Blacklist(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    reason = models.IntegerField()
    email = models.CharField(max_length=200)
    date_report = models.DateField
    is_active = models.BooleanField(default=True)