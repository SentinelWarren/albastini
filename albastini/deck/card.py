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


class Card:
    """A simple playing card.

    A Card is characterized by two components:
        rank: a char or string value within the Rank enum, (Three-Ace)
        suit: a char or string representation of card categories i.e "HDSC"
    """
    __Ranks = Rank
    __Suits = Suit

    __RANK_NAMES = {r.repr: r.name for r in __Ranks}
    __RANK_SYMBOLS = {r.repr: r.repr for r in __Ranks}
    __RANK_ORDERS = {r.repr: r.order for r in __Ranks}
    __RANK_POINTS = {r.repr: r.point for r in __Ranks}

    __SUIT_SYMBOLS = {s.value: s.value for s in __Suits}
    __SUIT_NAMES = {s.value: s.name for s in __Suits}

    def __init__(self, rank: str, suit: str):
        """Initialize a Card with a rank and suit.

        rank in __RANK_SYMBOLS and suit in __SUIT_SYMBOLS
        """
        if rank not in self.__RANK_SYMBOLS:
            raise ValueError(f"Invalid rank! Should be one of {self.__RANK_SYMBOLS.values()}")
        if suit not in self.__SUIT_SYMBOLS:
            raise ValueError(f"Invalid suit! Should be one of {self.__SUIT_SYMBOLS.values()}")

        self.__rank = rank
        self.__suit = suit

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
        return self.__SUIT_NAMES[self.suit]

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
    