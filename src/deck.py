from random import randint
from src.card import Card

class Deck:
    """A class representing a deck of 52 cards.

    Attributes:
        cards (list[Card]): The cards in the deck.
    """

    def __init__(self):
        """Create a new deck of cards."""
        self.cards: list[Card] = []

        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return str(self.cards)

    def draw(self) -> Card:
        """Draw a random card from the deck.

        Returns:
            Card: The card that was drawn.
        """
        index = randint(0, len(self.cards) - 1)
        return self.cards.pop(index)