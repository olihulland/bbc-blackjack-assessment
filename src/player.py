from src.deck import Deck
from src.hand import Hand

class Player:
    """A player in the game."""

    def __init__(self, name: str, deck: Deck):
        """Create a new player with the given name."""
        self.name = name
        self.hand = Hand(deck)
        self.deck = deck

    def __str__(self):
        return self.name + ": " + str(self.hand)

    def __repr__(self) -> str:
        return self.__str__()