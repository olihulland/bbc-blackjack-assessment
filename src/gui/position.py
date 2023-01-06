import arcade
from src.logic.player import Player
from src.logic.dealer import Dealer
from src.gui.cardsprite import CardSprite
from src.gui.constants import Constants
class Position():
    def __init__(self, pos: str, player: Player):
        self.pos = pos
        self.player = player
        self.cards = arcade.SpriteList()

        self.gen_dimensions()
        self.set_cards()

        print(f"Created {player.name} position at ({self.x}, {self.y})")

    def set_cards(self):
        self.cards = arcade.SpriteList()
        for i, card in enumerate(self.player.cards):
            cardSprite = CardSprite(card)
            if self.pos == "top" or self.pos == "bottom":
                totalL = len(self.player.cards) * (Constants.CARD_WIDTH + 5)
                cardSprite.position = ((self.x - (totalL/4)) + (i*(Constants.CARD_WIDTH + 5)), self.y)
            else:
                totalL = len(self.player.cards) * (Constants.CARD_HEIGHT*0.25)
                cardSprite.position = (self.x, (self.y + totalL/4) - (i * (Constants.CARD_HEIGHT*0.25)))
                cardSprite.angle = 90
            self.cards.append(cardSprite)

    def gen_dimensions(self):
        if self.pos == "top":
            self.width = Constants.POSITION_WIDTH_HORIZ
            self.height = Constants.POSITION_HEIGHT_HORIZ
            self.x = Constants.WINDOW_WIDTH/2
            self.y = Constants.WINDOW_HEIGHT - Constants.POSITION_HEIGHT_HORIZ/2
        elif self.pos == "bottom":
            self.width = Constants.POSITION_WIDTH_HORIZ
            self.height = Constants.POSITION_HEIGHT_HORIZ
            self.x = Constants.WINDOW_WIDTH/2
            self.y = Constants.POSITION_HEIGHT_HORIZ/2
        elif self.pos == "left":
            self.width = Constants.POSITION_WIDTH_VERT
            self.height = Constants.POSITION_HEIGHT_VERT
            self.x = Constants.POSITION_WIDTH_VERT/2
            self.y = Constants.WINDOW_HEIGHT/2
        elif self.pos == "right":
            self.width = Constants.POSITION_WIDTH_VERT
            self.height = Constants.POSITION_HEIGHT_VERT
            self.x = Constants.WINDOW_WIDTH - Constants.POSITION_WIDTH_VERT/2
            self.y = Constants.WINDOW_HEIGHT/2
        else:
            raise ValueError("Invalid position")

    def draw(self):
        # draw box and text
        rotation = 0
        textX = self.x
        textY = self.y
        colour = arcade.color.WHITE
        if self.pos == "left":
            rotation = -90
            textX += (self.width/2 + 20)
        elif self.pos == "right":
            rotation = 90
            textX -= (self.width/2 + 20)
        elif self.pos == "top":
            textY -= (self.height/2 + 20)
        elif self.pos == "bottom":
            textY += (self.height/2 + 20)
            colour = arcade.color.RED
        if isinstance(self.player, Dealer):
            colour = arcade.color.BANGLADESH_GREEN
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, colour, 2)
        arcade.draw_text(self.player.name, textX, textY, arcade.color.WHITE, 16, align="center", anchor_x="center", anchor_y="center", width=300, rotation=rotation)

        # draw cards
        self.cards.draw()



    def set_pos(self, pos: str):
        self.pos = pos
        self.gen_dimensions()