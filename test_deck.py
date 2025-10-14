# test_deck.py – Enhetstest med pytest

from deck import Deck

def test_draw_21_length():
    d = Deck()
    cards = d.draw_21()
    assert len(cards) == 21  # Ska alltid vara 21 namn

def test_unique_cards():
    d = Deck()
    cards = d.draw_21()
    values = [str(c) for c in cards]
    assert len(values) == len(set(values))  # Inga dubbletter
