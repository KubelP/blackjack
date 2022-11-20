"""
This module contains Card class and Deck class.
"""

import random

class ColorError(Exception):

    """
    Excetpion for wrong card color.
    """


class CardValueError(Exception):

    """
    Excetpion for wrong card value.
    """



class Card:

    '''
    Classic game card. Have value and color.
    Possible colors are spades, hearts, dimonds,
    and clubs.
    Possible values are 2 to 10 as intiger for
    numbers and face cards as Ace, Jack, Queen
    and King as string.
    '''

    possible_collors = {
        'spades' : '\u2664',
        'hearts' : '\u2661',
        'dimonds' : '\u2662',
        'clubs' : '\u2667'
    }

    possible_values = list(range(2, 11)) + [
        'Ace',
        'Jack',
        'Queen',
        'King'
    ]

    def __init__(self, value, color):

        if value in self.possible_values:
            self.value = value
        else:
            raise CardValueError(f'{value} is wrong card value! '
                             'Available values are 2-10, Jack, Queen, King or Ace')

        if self.possible_collors.get(color):
            self.color = self.possible_collors[color]
        else:
            raise ColorError(f'{color} is wrong card color! '
                             'Available colors are spades, hearts, dimonds or clubs.')


    def __repr__(self):
        return str(self.value) + self.color


class Deck:

    """
    Returns a shuffle deck consist of
    deck_number * 52 standard game cards.
    In default deck_number is set to 6.
    """

    def __init__(self, deck_number):
        self.deck_number = deck_number
        self.deck = []


    def deck_builder(self):

        """
        Creates deck of all available cards
        and shuffle them.
        """

        for i in range(self.deck_number):
            for value in Card.possible_values:
                for color in Card.possible_collors:
                    card = Card(value, color)
                    self.deck.append(card)
            random.shuffle(self.deck)
        return self.deck

    def __str__(self):
        return f'{self.deck}'
