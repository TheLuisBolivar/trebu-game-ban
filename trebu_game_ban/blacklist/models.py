from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "id: " + str(self.pk) + ", name: " + str(self.name)


class Reason(models.Model):
    reason = models.CharField(max_length=200)

    def __str__(self):
        return "id: " + str(self.pk) + ", reason: " + str(self.reason)


class Blacklist(models.Model):
    game = models.ForeignKey("Game", on_delete=models.PROTECT)
    reason = models.ForeignKey("Reason", on_delete=models.PROTECT)
    email = models.CharField(max_length=200)
    date_report = models.DateField
    is_active = models.BooleanField(default=True)
