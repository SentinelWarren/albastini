"""Implements Albastini deck related classes.

This module exports the following classes:
    Deck: Albastini deck of Cards.
"""
# TODO: improve docstring

import pprint
from random import choice, shuffle
from albastini import Card


# A basic immutable Card class.
#Card = namedtuple('Card', ['rank', 'suit'])

class Deck:
    """A basic class for the deck of cards."""

    ranks = [str(n) for n in range(3,8)] + list('JQKA')
    suits = 'S D C H'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card


# suit values for cards ranking.
# suit_values = dict(Spades=3, Hearts=2, Diamonds=1, Clubs=0)

def ace_high(card):
    """Cards ranking helper function."""
    return card.rank_order

    # rank_value = Deck.ranks.index(card.rank)
    # return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':

    deck = Deck()

    print(f'\nThe deck has {len(deck)} cards.\n')
    print('All cards in the deck:')
    pprint.pp(deck[:])

    print(f'\nAll Aces from deck:')
    pprint.pp(deck[8::9])

    ranked_deck = [card for card in sorted(deck, key=ace_high)]
    print(f'\nRanked deck:')
    pprint.pprint(ranked_deck)

    print(f'\nFive randomly selected cards from the deck:')
    pprint.pprint([choice(deck), choice(deck), choice(deck), choice(deck), choice(deck)])

    shuffle(deck)
    print(f'\nShuffled deck:')
    pprint.pp(deck[:])

    shuffle(deck)
    print(f'\nShuffled deck once more!')
    pprint.pp(deck[:])

