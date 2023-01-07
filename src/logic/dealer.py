from src.logic.player import Player
from src.logic.deck import Deck

class Dealer(Player):
    """The dealer in the game."""

    def __init__(self, deck: Deck):
        super().__init__("Dealer", deck)
        self.cards[1].upside_down = True

    def play_turn(self):
        """Play the dealer's turn. The dealer continues to hit untile they have at least 17."""
        print("Time for the dealer to play")
        print(f"Dealer hand: {self.cards}")
        while self.score < 17:
            newCard = self.hit()
            print(f"Hit! New card: {newCard}")

        print("Dealer stands")
        print(f"Final hand: {self.cards}")

    def new_round(self) -> None:
        """Sets up for a new round - redeals cards and flips the second card upside down."""
        super().new_round()
        self.cards[1].upside_down = True