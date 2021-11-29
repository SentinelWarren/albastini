"""Testing card module"""
from albastini.deck.card import Rank, Suit, Card

card1 = Card('7', 'S')
card2 = Card('A', 'H')
card3 = Card('J', 'C')
card4 = Card('Q', 'D')
card5 = Card('J', 'S')

def test_rank():
    """Test Rank enum class."""
    ranks_order = {0:'THREE', 1:'FOUR', 2:'FIVE', 3:'SIX',
             4:'QUEEN', 5:'JACK', 6:'KING', 7:'SEVEN', 8:'ACE'}
    rank_points = {'3':0, '4':0, '5':0, '6':0, 'Q':2, 'J':3, 'K':4, '7':10, 'A':11}

    assert ranks_order == {r.order: r.name for r in Rank}
    assert rank_points == {r.repr: r.point for r in Rank}

def test_suit():
    """Test Suit enum class."""
    suit_values = ['H', 'D', 'S', 'C']
    suit_names = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']

    assert suit_names == [s.name for s in Suit]
    assert suit_values == [s.value for s in Suit]

def test_card_methods():
    """Test Card class methods."""
    assert card1.rank == '7'
    assert card1.rank_name == 'SEVEN'
    assert card2.suit == 'H'
    assert card2.suit_name == 'HEARTS'
    assert card3.rank_order == 5
    assert card3.rank_point == 3
    assert card4.rank_sym == 'Q'
    assert str(card4) == 'QUEEN of DIAMONDS'
    assert card5.image_name == 'jack_of_spades.png'
    assert repr(card5) == "Card(rank='JACK', suit='SPADES')"

def test_card_ops():
    """Test Card class operators."""
    assert card1 > card3 and card4
    assert card1 and card3 and card4 < card2
    assert card2 > card1 and card3 and card4
    assert card3 == card5 >= card3 <= card5
    assert card3 <= card1 and card2 >= card4
    assert card4 != card5
