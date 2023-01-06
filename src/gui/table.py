import arcade
from src.logic.dealer import Dealer
from src.logic.player import Player
from src.logic.deck import Deck
from src.gui.position import Position
from src.gui.constants import Constants
from src.gui.decksprite import DeckSprite

# code takes inspiration from arcade docs - https://api.arcade.academy/en/latest/tutorials/card_game/index.html#

class Table(arcade.Window):
    def __init__(self):
        super().__init__(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, "Blackjack")
        arcade.set_background_color(arcade.color.AMAZON)

        self.deck = Deck() # this should be passed instead TODO
        self.positions: list[Position] = []
        self.deckSprite = DeckSprite(self.deck, Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2)

    def setup(self):
        self.positions.append(Position("top", Dealer(self.deck)))
        self.positions.append(Position("bottom", Player("Player", self.deck)))
        self.positions.append(Position("left", Player("Player", self.deck)))
        self.positions.append(Position("right", Player("Player", self.deck)))


    def on_draw(self):
        """Render the screen."""
        self.clear()
        for position in self.positions:
            position.draw()
        self.deckSprite.draw()

