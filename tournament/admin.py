from django.contrib import admin
from .models import Tournament, TournamentJoin


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(TournamentJoin)
class TournamentJoinAdmin(admin.ModelAdmin):
    list_display = (
        'player_name',
        'freefire_uid',
        'phone_number',
        'transaction_id',
        'is_approved',
        'joined_at'
    )

    list_filter = (
        'is_approved',
    )

    search_fields = (
        'player_name',
        'freefire_uid',
        'phone_number'
    )