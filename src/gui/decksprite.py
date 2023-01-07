import arcade
from src.logic.deck import Deck
from src.gui.cardsprite import CardSprite

class DeckSprite(arcade.SpriteList):
    """The sprite for the deck of cards. Displays the top 5 cards in an offset stack.
    Chose not to display all for performance reasons.
    
    Attributes:
        deck (Deck): The deck of cards.
        x (int): The x position of the deck.
        y (int): The y position of the deck.
    """
    def __init__(self, deck: Deck, x: int, y: int):
        """Initialises the deck sprite."""
        super().__init__()
        self.deck = deck
        self.x = x
        self.y = y
        self.add_cards()

    def add_cards(self) -> None:
        """Adds the top 5 cards to the sprite list with an offset position."""
        for i, card in enumerate(self.deck.cards[:5]):
            cardSprite = CardSprite(card)
            cardSprite.position = self.x + i, self.y + i
            self.append(cardSprite)

    def update(self) -> None:
        """Updates the stack with the new top 5 cards."""
        self.clear()
        self.add_cards()