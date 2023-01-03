# Blackjack

This project is prepare for Pycamp bootcamp. 

Equally well known as Twenty-One. Blackjack is very popular hazard card game.

## Requirements

For playing game only requirement is python3 interpreter or higher.

## Installation

Clone this repositiry on your machine:

```bash
git clone https://github.com/KubelP/blackjack.git
```

Go to directory:

```bash
cd blackjack/
```

and run scrpit:

```bash
python3 main.py
```

## Game rules

### The Deck

The standard 52-card deck is used, but in most casinos several decks of cards are shuffled together. The six-deck game (312 cards) is the most popular.

### Setting deck number

In default it is set to six-deck game (312 cards). This can be changed in main.py by changing `decks_number` on desired number (integer) of decks: 

    game = BlackJackTable(decks_number)

### Object of the game

Player attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.

### Card Values/scoring

An Ace is worth 1 or 11 (for player's/dealer's hand value over 11 is 1). Face cards are 10 and any other card is its face value.

### Game run

For starter player automatically gains two cards, dealer one. Then you will be asked for 'hit' or 'stand'.  For 'hit' put letter h and press enter. For 'stand' just press enter. If you 'stand' dealer automatically draw cards. The result will be shown on concole.
