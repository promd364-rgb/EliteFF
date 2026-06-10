from django.urls import path
from .views import home, join_tournament, add_money

urlpatterns = [
    path('', home, name='home'),
    path('join/<int:tournament_id>/', join_tournament, name='join_tournament'),
    path('add-money/', add_money, name='add_money'),
]