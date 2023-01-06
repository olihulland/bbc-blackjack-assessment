import arcade
from src.logic.deck import Deck
from src.gui.cardsprite import CardSprite

class DeckSprite(arcade.SpriteList):
    def __init__(self, deck: Deck, x: int, y: int):
        super().__init__()
        self.deck = deck
        self.x = x
        self.y = y
        self.add_cards()

    def add_cards(self) -> None:
        for i, card in enumerate(self.deck.cards[:5]):
            cardSprite = CardSprite(card)
            cardSprite.position = self.x + i, self.y + i
            self.append(cardSprite)

    def update(self) -> None:
        self.clear()
        self.add_cards()