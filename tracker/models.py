from django.db import models


class Character(models.Model):
    PEACH = "C"
    BIRDO = "T"
    MARIO = "H"
    TYPE = (
        (PEACH, "peaches"),
        (BIRDO, "birdos"),
        (MARIO, "marios"),
    )

    name = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name


class Payment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.character.name} - {self.amount} - {self.date}"
