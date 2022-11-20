"""
This module consist BlackJackTable class.
"""

from game import Game

class BlackJackTable:

    """
    This class is base for game. Initiates
    game, deck and first cards deal.
    Contains one method - play.
    """

    def __init__(self, decks_number):
        self.game = Game(decks_number)
        self.deck = self.game.deck_shuffle() # initiate deck
        self.game.game_enter(self.game, self.deck) # enter card deal


    def play(self):

        """
        Method play runs BlackJack game, counts
        points and returns final result.
        """

        print('\nFor hit press h and enter, for stand press enter\n')
        print('\u2664\u2661\u2662\u2667'*12)

        while True:
            move = input('Hit or stand: ')
            
            if move == 'h':
                print('\u2664\u2661\u2662\u2667'*12)
                card = self.game.draw(self.deck) # drwan of one card
                self.game.cards_in_hand(self.game.player, card)
                player_points = self.game.points_counter(self.game.player)
                print(f'\nYour hand :{self.game.player} - value: {player_points}\n')

                if player_points > 21:
                    print("Your hand is greater then 21. You lose.\n")
                    print('\u2664\u2661\u2662\u2667'*12)
                    # break
                    return "Your hand is greater then 21. You lose.\n"

                if player_points == 21:
                    print("BlackJack! You are winner!\n")
                    print('\u2664\u2661\u2662\u2667'*12)
                    return "BlackJack! You win!"
                    # break
            else:
                player_points = self.game.points_counter(self.game.player)
                dealer_points = self.game.points_counter(self.game.dealer)

                while dealer_points <= 18:
                    print('\u2664\u2661\u2662\u2667'*12)
                    card = self.game.draw(self.deck) # drwan of one card
                    self.game.cards_in_hand(self.game.dealer, card)
                    dealer_points = self.game.points_counter(self.game.dealer)
                    print(f"\nDealer's hand: {self.game.dealer}"
                          f" - value: {dealer_points}\n")

                    if dealer_points == 21:
                        print("Dealer's BlackJack. Player lose.")
                        print('\u2664\u2661\u2662\u2667'*12)
                        return "Dealer's BlackJack. You lose."

                    if dealer_points > 21:
                        print("Dealer's hand is grater then 21. You win!")
                        print('\u2664\u2661\u2662\u2667'*12)
                        return "Dealer's hand is grater then 21. You win!"

                    if dealer_points > player_points:
                        print(f"Dealer has greater hand: {dealer_points} "
                              f"against yours {player_points}. Dealer's wins.")
                        print('\u2664\u2661\u2662\u2667'*12)
                        return (f"Dealer has greater hand: {dealer_points} "
                                f"against yours {player_points}. Dealer's wins.")

                    if dealer_points == player_points:
                        print('Tie. No winner.')
                        print('\u2664\u2661\u2662\u2667'*12)
                        return 'Tie. No winner.'
