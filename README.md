Equally well known as Twenty-One.<br>
<br>
Blackjack is the one card game that can be found in every casino.<br>
<br>
The Deck<br>
The standard 52-card deck is used, but in most casinos several decks of cards are shuffled together. The six-deck game (312 cards) is the most popular.
<br>
Object of the Game<br>
Player attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

Card Values/scoring<br>
An Ace is worth 1 or 11 (for player's/dealer's hand value over 11 is 1). Face cards are 10 and any other card is its face value.<br>
<br>
For playing game only requirement is python3 interpreter or higher.<br>
<br>
Copy main.py, deck.py, game.py, player.py and table.py.<br>
In console go to copied files directory and type:<br>
<br>
for win: python main.py<br>
<br>
for linux: python3 main.py<br>
<br>
Automaticly player gain two cards, dealer one.
Then you will be asked for 'hit' or 'stand'.  For 'hit' put letter h and press enter. For 'stand' just press enter. If you 'stand' dealer automatically draw cards. The result will be shown on the screen.<br>
<br>
In default it is set to six-deck game (312 cards). This can be changed in main.py by changing decks_number on desired number (integer) of decks: game = BlackJackTable(decks_number).