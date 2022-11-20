"""
Main module. This module should be executed for run game.
Here may be changed number of decks. Defult decks_number is 6.
"""

from table import BlackJackTable

if __name__ == '__main__':
    game = BlackJackTable(decks_number = 6)#change of deck numbers
    game.play()
