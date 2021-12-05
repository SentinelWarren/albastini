"""Testing card module exceptions"""
from pytest import raises
from albastini.deck.card import Card

def test_card_raises():
    """Test ValueError exception"""
    with raises(ValueError):
        Card('a', 'D')
        Card('7', 'c')
        Card(7, 'C')
