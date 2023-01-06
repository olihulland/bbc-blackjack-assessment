import arcade
from src.logic.player import Player
from src.gui.cardsprite import CardSprite

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
            cardSprite.position = (self.x + (i * 80), self.y)
            self.cards.append(cardSprite)

    def gen_dimensions(self):
        if self.pos == "top":
            self.width = 600
            self.height = 200
            self.x = 512
            self.y = 700
        elif self.pos == "bottom":
            self.width = 600
            self.height = 200
            self.x = 512
            self.y = 100
        elif self.pos == "left":
            self.width = 150
            self.height = 400
            self.x = 100
            self.y = 400
        elif self.pos == "right":
            self.width = 150
            self.height = 400
            self.x = 924
            self.y = 400
        else:
            raise ValueError("Invalid position")

    def draw(self):
        # draw box and text
        rotation = 0
        textX = self.x
        textY = self.y
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
        arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, arcade.color.BLACK, 2)
        arcade.draw_text(self.player.name, textX, textY, arcade.color.BLACK, 16, align="center", anchor_x="center", anchor_y="center", width=300, rotation=rotation)

        # draw cards
        self.cards.draw()



    def set_pos(self, pos: str):
        self.pos = pos
        self.gen_dimensions()