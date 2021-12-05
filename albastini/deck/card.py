"""Implements Albastini card related classes.

This module exports the following classes:
    * Rank - enum representing all ranks supported by Albastini cards: 3456QJK7A
    * Suit - enum representing all suits: Hearts, Diamonds, Spades, Clubs
    * Card - Albastini Card
"""
# TODO: improve doctring

from enum import Enum


class Rank(Enum):
    """Card ranks enum class."""
    # order, repr, point
    THREE = 0, '3', 0
    FOUR  = 1, '4', 0
    FIVE  = 2, '5', 0
    SIX   = 3, '6', 0
    QUEEN = 4, 'Q', 2
    JACK  = 5, 'J', 3
    KING  = 6, 'K', 4
    SEVEN = 7, '7', 10
    ACE   = 8, 'A', 11

    def __init__(self, order: int, repr_: str, point: int):
        self.order = order
        self.repr = repr_
        self.point = point

    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.order > other.order
        return NotImplemented

    def __repr__(self):
        return f"{self.repr}"


class Suit(Enum):
    """Card suits enum class."""
    HEARTS = "H"
    DIAMONDS = "D"
    SPADES = "S"
    CLUBS = "C"

    def __repr__(self):
        return f"{self.value}"

# __RANK_NAMES = {r.repr: r.name for r in Rank}
# __RANK_SYMBOLS = {r.repr: r.repr for r in Rank}
# __RANK_ORDERS = {r.repr: r.order for r in Rank}
# __RANK_POINTS = {r.repr: r.point for r in Rank}

# SUITS = {s.value: s.name for s in Suit}

class Card:
    """Represents a single Albastini Card, given a valid rank and suit.

    A Card is characterized by two components:
        rank: a string value within the Rank enum, (Three-Ace)
        suit: a string representation of card categories i.e 'H', 'D', 'S' or 'C'

    >>> card = Card('A', 'D')
    """
    __Ranks = Rank

    __RANK_NAMES = {r.repr: r.name for r in __Ranks}
    __RANK_SYMBOLS = {r.repr: r.repr for r in __Ranks}
    __RANK_ORDERS = {r.repr: r.order for r in __Ranks}
    __RANK_POINTS = {r.repr: r.point for r in __Ranks}

    __SUITS = {s.value: s.name for s in Suit}

    def __init__(self, rank: str, suit: str):
        """Initialize a Card with a rank and suit.

        rank in __RANK_SYMBOLS and suit in __SUITS
        """
        self._validate(rank, suit)
        self.__rank = rank
        self.__suit = suit

    def _validate(self, rank, suit):
        """Check the card is valid, raise exception if not.
        """
        if rank not in self.__RANK_SYMBOLS:
            raise ValueError(f"Invalid rank! Should be one of {self.__RANK_SYMBOLS.values()}")
        if suit not in self.__SUITS:
            raise ValueError(f"Invalid suit! Should be one of {self.__SUITS.keys()}")

    @property
    def rank(self):
        """Return the Card's self.__rank value."""
        return self.__rank

    @property
    def rank_point(self):
        """Return the Card's self.__RANK_POINTS[self.rank] value."""
        return self.__RANK_POINTS[self.rank]

    @property
    def rank_order(self):
        """Return the Card's self.__RANK_ORDERS[self._rank] value."""
        return self.__RANK_ORDERS[self.rank]

    @property
    def rank_sym(self):
        """Return the Card's rank symbol corresponding
        to self's rank."""
        return self.__RANK_SYMBOLS[self.rank]

    @property
    def rank_name(self):
        """Return the Card's rank name corresponding
        to self's rank."""
        return self.__RANK_NAMES[self.rank]

    @property
    def suit(self):
        """Return the Card's self.__suit value."""
        return self.__suit

    @property
    def suit_name(self):
        """Return the Card's self.suit name."""
        return self.__SUITS[self.suit]

    @property
    def image_name(self):
        """Return the Card's image file name."""
        return (str(self).replace(' ', '_') + '.png').lower()

    def __str__(self):
        """Return string representation for str()."""
        ranks = [str(i) for i in range(3, 8)]
        return(
            f'{self.rank_sym} of {self.suit_name}' if self.rank in ranks
            else f'{self.rank_name} of {self.suit_name}'
        )

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(rank='{self.rank_name}', suit='{self.suit_name}')"

    def __format__(self, frmt):
        """Return formatted string representation."""
        return f'{str(self):{frmt}}'

    def __eq__(self, other):
        """Returns True if two cards are equal, False otherwise."""
        return self.rank_order == other.rank_order

    def __gt__(self, other):
        """Returns True if self > other, False otherwise."""
        return self.rank_order > other.rank_order

    def __ge__(self, other):
        """Returns True if self >= other, False otherwise."""
        return self > other or self == other

    def __lt__(self, other):
        """Returns True if self < other, False otherwise."""
        return self.rank_order < other.rank_order

    def __le__(self, other):
        """Returns True if self <= other, False otherwise."""
        return self < other or self == other

    def __ne__(self, other):
        """Returns True if two cards are not equal, False otherwise."""
        return not self == other
    