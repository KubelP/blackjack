"""
Module with tests for BlackJack game.
Tests are performed for DECK_NUMBER = 6.
"""

import pytest
from deck import Card, ColorError, Deck, CardValueError
from game import Game

DECK_NUMBER = 6

def test_colors():

    """
    Test for color card validation.
    """

    with pytest.raises(ColorError) as message:
        card = Card(2, 'vorbiden color')
        assert message == ColorError


def test_values():

    """
    Test for value card validation.
    """

    with pytest.raises(CardValueError) as message:
        card = Card(1, 'spades')
        assert message == CardValueError


def test_deck_lenght():

    """
    Validation for deck lenght.
    """

    deck = Deck(DECK_NUMBER)
    len_deck = deck.deck_builder()
    assert len(len_deck) == DECK_NUMBER*52


def test_draw_card():

    """
    Check is drawn card is diminishing
    deck size and if it returned that card.
    """

    deck = Deck(DECK_NUMBER)
    cards_deck = deck.deck_builder()
    card = cards_deck.pop()
    assert len(cards_deck) == 52*DECK_NUMBER-1 and card.value


def test_game_card():

    """
    Check is game mechanics returns drawn card.
    """

    game = Game(DECK_NUMBER)
    card = game.draw(game.deck_shuffle())
    print(card)
    assert card.value and card.color

def test_players_card():

    """
    Validate if player gain drawn card.
    """

    game = Game(DECK_NUMBER)
    card = game.draw(game.deck_shuffle())
    player_hand = game.cards_in_hand(game.player, card)
    print(card, player_hand)
    assert player_hand[0] == card


def test_players_hand():

    """
    Validate lenght of player's drawn cards
    and duplicates.
    """

    range_set = 10 #drawn 10 cards
    game = Game(DECK_NUMBER)
    deck = game.deck_shuffle()
    for i in range(range_set):
        card = game.draw(deck)
        player_hand = game.cards_in_hand(game.player, card)
    player_hand_set = set(player_hand) #easy way to eliminate duplicates
    final_deck = game.deck.deck # for check if deck is diminished by numbers of drawn cards
    print(card, player_hand, player_hand_set)
    assert (len(game.player) == 10 and len(player_hand_set) == 10
            and len(final_deck) == DECK_NUMBER*52 - range_set)

def test_game_enter():

    """
    Validate enter cards deal. Two cards
    should be for player and one for dealer.
    """

    game = Game(DECK_NUMBER)
    deck = game.deck_shuffle()
    game.game_enter(game, deck)
    assert len(game.player) == 2 and len(game.dealer) == 1


def test_points_counter():

    """
    Validation of points counter.
    """

    game = Game(DECK_NUMBER)
    game.player.hand = [Card(6, 'spades'),
                        Card('Jack', 'clubs')
                       ] # manually created tested hand with 16 points
    points = game.points_counter(game.player)
    assert points == 16


def test_points_counter_with_aces():

    """
    Check if Ace value change to 1.
    """

    game = Game(DECK_NUMBER)
    game.player.hand = [Card('Ace', 'spades'),
                        Card('Ace', 'clubs'),
                        Card(9, 'dimonds')
                       ] # manually created tested hand with Aces
    points = game.points_counter(game.player)
    assert points == 21
