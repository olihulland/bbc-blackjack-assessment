import arcade
from src.logic.deck import Deck
from src.gui.cardsprite import CardSprite
from src.gui.constants import Constants

class DeckSprite(arcade.SpriteList):
    def __init__(self, deck: Deck, x: int, y: int):
        super().__init__()
        self.deck = deck
        self.x = x
        self.y = y

        for i, card in enumerate(deck.cards[:5]):
            cardSprite = CardSprite(card)
            cardSprite.position = self.x + i, self.y + i
            self.append(cardSprite)


