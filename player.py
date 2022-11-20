"""
This module contains Player class.
"""

class Player:

    """
    Player class creates player and/or dealer instance
    Receive cards from deck by __add__ method.
    """

    def __init__(self):
        self.hand = []


    def __add__(self, card):
        return self.hand.append(card)


    def __len__(self):
        return len(self.hand)


    def __str__(self):
        if not self.hand:
            return 'Hand is empty'
        return f'{self.hand}'
