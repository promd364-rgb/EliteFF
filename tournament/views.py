from django.shortcuts import render, redirect, get_object_or_404
from .models import Tournament, TournamentJoin

def home(request):
    tournaments = Tournament.objects.all()
    return render(request, 'index.html', {
        'tournaments': tournaments
    })


def join_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        TournamentJoin.objects.create(
            tournament=tournament,
            player_name=request.POST['player_name'],
            freefire_uid=request.POST['freefire_uid'],
            phone_number=request.POST['phone_number'],
            payment_number=request.POST['payment_number'],
            transaction_id=request.POST['transaction_id']
        )
        return redirect('/')

    return render(request, 'join.html', {
        'tournament': tournament
    })


# 💰 ADD MONEY PAGE
def add_money(request):
    return render(request, 'add_money.html')