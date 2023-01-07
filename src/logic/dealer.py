from src.logic.player import Player
from src.logic.deck import Deck

class Dealer(Player):
    """The dealer in the game. Extends the Player class.
    
    The dealer has it's second card flipped upside down.
    """

    def __init__(self, deck: Deck):
        """Creates a new dealer with the given deck. With a flipped second card."""
        super().__init__("Dealer", deck)
        self.cards[1].upside_down = True

    def new_round(self) -> None:
        """Sets up for a new round - redeals cards and flips the second card upside down."""
        super().new_round()
        self.cards[1].upside_down = True