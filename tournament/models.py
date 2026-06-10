from django.db import models


class Tournament(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TournamentJoin(models.Model):
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        related_name='players'
    )

    player_name = models.CharField(max_length=100)
    freefire_uid = models.CharField(max_length=50)

    phone_number = models.CharField(
        max_length=20,
        help_text="BKash/Nagad Number"
    )

    payment_number = models.CharField(
        max_length=20,
        default='0000000000'
    )

    transaction_id = models.CharField(
        max_length=50,
        blank=True
    )

    is_approved = models.BooleanField(
        default=False
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.player_name} ({self.freefire_uid})"