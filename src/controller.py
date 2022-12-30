from src.player import Player
from src.deck import Deck

class Controller:
    """Class that controls the game."""

    def __init__(self):
        """Create a new controller."""
        self.deck = Deck()
        self.players: list[Player] = []

    def add_player(self, name: str):
        """Add a player to the game."""
        self.players.append(Player(name, self.deck))

    def __str__(self):
        return f"Players: {self.players}\nDeck: {len(self.deck.cards)} cards"