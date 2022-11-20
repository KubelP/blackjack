"""
Main Blackjack game mechanics.
"""

from deck import Deck
from player import Player

class Game:

    """
    Creates player, dealer, deck and
    has Blackjack mechanics.

    Contains methodes:
    - deck_shuffle - creates and returns new deck,
    - draw - drwas card from deck,
    - cards_in_hand - adds cards for player's or dealer's hand,
    - points_counter - summing values of cards,
    - game_enter - initial cards deal - it run only once in game.
    """

    def __init__(self, decks_number):
        self.player = Player()
        self.dealer = Player()
        self.deck = Deck(decks_number)


    def deck_shuffle(self):

        """
        Retruns ready to play shuffled deck.
        """

        deck = self.deck.deck_builder()

        return deck


    def draw(self, deck):

        """
        Returns drawn card from deck.
        """

        card = deck.pop()

        return card


    def cards_in_hand(self, player, card):

        """
        Creates hand of cards for player
        or dealer.
        """

        player += card

        return self.player.hand



    def points_counter(self, player):

        """
        Counts points for player or dealer.
        """

        points = 0
        for card in player.hand: # assign values for faces cards

            if (card.value == 'Jack' or
                card.value == 'Queen' or
                card.value == 'King'
               ):
                points += 10

            elif card.value == 'Ace': # assign values for ace: 1 or 10

                if points <= 10:
                    points += 11
                else:
                    points += 1

            else:
                points += card.value

        return points


    def game_enter(self, game, deck):

        """
        Initial cards deal - two for player,
        one for dealer.
        """

        for i in range(2):
            card = game.draw(deck)
            game.cards_in_hand(game.player, card)

        card = game.draw(deck)
        game.cards_in_hand(game.dealer, card)
        print('\u2664\u2661\u2662\u2667'*12)
        print(f"\nYour hand: {game.player} - value: "
              f"{game.points_counter(self.player)}\n")
        print(f"Dealer's hand: {game.dealer} - value: "
              f"{game.points_counter(self.dealer)}\n")
        print('\u2664\u2661\u2662\u2667'*12)

        return game.player, game.dealer
