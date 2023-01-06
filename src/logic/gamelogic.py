from src.logic.player import Player
from src.logic.deck import Deck
from src.logic.dealer import Dealer

class GameLogic:
    """Class that controls the game."""

    def __init__(self):
        """Create a new logic."""
        self.__deck = Deck()
        self.__players: list[Player] = []
        self.__dealer = Dealer(self.deck)

        self.__playing = False

    @property
    def deck(self) -> Deck:
        """Get the deck."""
        return self.__deck

    @property
    def players(self) -> list[Player]:
        """Get the players."""
        return self.__players

    @property
    def dealer(self) -> Dealer:
        """Get the dealer."""
        return self.__dealer

    def add_player(self, name: str):
        """Add a player to the game."""
        if self.__playing:
            raise Exception("Cannot add player while game is in progress")

        self.players.append(Player(name, self.deck))


    def print_hands(self):
        """Print the hands of the players and the dealer."""
        print(self.dealer.status)
        for player in self.players:
            print(player.status)

    def __str__(self):
        return f"Players: {self.players}\nDeck: {len(self.deck.cards)} cards"