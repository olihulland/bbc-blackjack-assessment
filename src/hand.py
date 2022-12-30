from src.card import Card
from src.deck import Deck

class Hand:
    """A class representing a hand of cards - starting with 2."""

    def __init__(self, deck: Deck):
        """Create a new hand with two cards to start."""
        self.cards: list[Card] = []

        self.cards.append(deck.draw())
        self.cards.append(deck.draw())

    def __str__(self):
        return str(self.cards)
