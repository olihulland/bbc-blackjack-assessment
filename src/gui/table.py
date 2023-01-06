import arcade
from src.logic.card import Card as LogicCard
from src.logic.dealer import Dealer
from src.logic.player import Player
from src.logic.deck import Deck
from src.gui.cardsprite import CardSprite
from src.gui.position import Position
import time

# code takes inspiration from arcade docs - https://api.arcade.academy/en/latest/tutorials/card_game/index.html#

class Table(arcade.Window):
    def __init__(self):
        super().__init__(1024, 768, "Blackjack")
        arcade.set_background_color(arcade.color.AMAZON)

        self.positions: list[Position] = []

    def setup(self):
        deck = Deck()
        self.positions.append(Position("top", Dealer(deck)))
        self.positions.append(Position("bottom", Player("Player", deck)))
        self.positions.append(Position("left", Player("Player", deck)))
        self.positions.append(Position("right", Player("Player", deck)))

    def on_draw(self):
        """Render the screen."""
        self.clear()
        for position in self.positions:
            position.draw()

