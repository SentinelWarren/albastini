"""Card class that represents a playing card and its image file name."""
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

    def __init__(self, order, repr_, point):
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
    Ranks = Rank
    Suits = Suit

    RANK_NAMES = {r.repr: r.name for r in Ranks}
    RANK_SYMBOLS = {r.repr: r.value[1] for r in Ranks}
    RANK_ORDERS = {r.repr: r.value[0] for r in Ranks}
    RANK_POINTS = {r.repr: r.value[2] for r in Ranks}
    #a string value in the range '2'-'10'-'JQKA', (2-Ace)
    # RANKS = range(2,15)
    # RANK_SYM = [str(n) for n in range(2,11)] + list('JQKA')
    # RANK_NAMES = ['Two', 'Three', 'Four', 'Five', 'Six',
    #               'Seven', 'Eight', 'Nine', 'Ten',
    #               'Jack', 'Queen', 'King', 'Ace']

    SUIT_SYMBOLS = {s.value: s.value for s in Suits}
    SUIT_NAMES = {suit.value: suit.name for suit in Suits}

    def __init__(self, rank, suit):
        """Initialize a Card with a rank and suit.

        rank in RANK_SYMBOLS and suit in SUIT_SYMBOLS
        """
        if rank not in self.RANK_SYMBOLS:
            raise ValueError(f"Invalid rank! Should be one of {self.RANK_SYMBOLS.values()}")
        if suit not in self.SUIT_SYMBOLS:
            raise ValueError(f"Invalid suit! Should be one of {self.SUIT_SYMBOLS.values()}")

        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """Return the Card's self._rank value."""
        return self._rank

    @property
    def rank_point(self):
        """Return the Card's self.RANK_POINTS[self._rank] value."""
        return self.RANK_POINTS[self.rank]

    @property
    def rank_order(self):
        """Return the Card's self.RANK_ORDERS[self._rank] value."""
        return self.RANK_ORDERS[self.rank]

    @property
    def rank_sym(self):
        """Return the Card's rank symbol corresponding
        to self's rank."""
        return self.RANK_SYMBOLS[self.rank]

    @property
    def rank_name(self):
        """Return the Card's rank name corresponding
        to self's rank."""
        return self.RANK_NAMES[self.rank]

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    @property
    def suit_name(self):
        """Return the Card's self._suit name."""
        return self.SUIT_NAMES[self.suit]

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
    