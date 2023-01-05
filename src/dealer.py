from src.player import Player
from src.deck import Deck

class Dealer(Player):
    """The dealer in the game."""

    def __init__(self, deck: Deck):
        super().__init__("Dealer", deck)

    @property
    def status(self) -> str:
        """Get the status of the dealer.

        Returns:
            str: The status of the dealer.
        """
        return f"{self.name}: [{self.cards[0]}, ?]"

    def play_turn(self):
        """Play the dealer's turn. The dealer continues to hit untile they have at least 17."""
        print("Time for the dealer to play")
        print(f"Dealer hand: {self.cards}")
        while self.score < 17:
            newCard = self.hit()
            print(f"Hit! New card: {newCard}")

        print("Dealer stands")
        print(f"Final hand: {self.cards}")