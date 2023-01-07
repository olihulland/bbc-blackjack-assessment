import arcade
from src.logic.player import Player
from src.logic.dealer import Dealer
from src.gui.cardsprite import CardSprite
from src.gui.constants import Constants
class Position():
    """The sprite for a player's position.
    Displays the cards in the player's hand and the player's name.
    """
    def __init__(self, pos: str, player: Player):
        """Initialises the position sprite.
        
        Args:
            pos (str): The position of the player. Can be "top", "bottom", "left" or "right".
            player (Player): The player (/or dealer) at the position.
        """
        self.__pos = pos
        self.player = player
        self.cards = arcade.SpriteList()

        self.gen_dimensions()
        self.set_cards()

    @property
    def pos(self):
        """The position of the player. Can be "top", "bottom", "left" or "right"."""
        return self.__pos

    def set_cards(self):
        """Adds the cards in the player's hand to the sprite list.
        The cards are displayed in a horizontal line for the top and bottom positions
        and a rotated vertical line for the left and right positions."""
        self.cards = arcade.SpriteList()
        for i, card in enumerate(self.player.cards):
            cardSprite = CardSprite(card)
            if self.__pos == "top" or self.__pos == "bottom":
                totalL = len(self.player.cards) * (Constants.CARD_WIDTH + 5)
                cardSprite.position = ((self.x - (totalL/2)) + (i*(Constants.CARD_WIDTH + 5) + Constants.CARD_WIDTH/2), self.y)
            else:
                totalL = len(self.player.cards) * (Constants.CARD_WIDTH * 0.3)
                cardSprite.position = (self.x, self.y - totalL/2 + (i * (Constants.CARD_WIDTH * 0.3)))
                cardSprite.angle = 90
            self.cards.append(cardSprite)

    def gen_dimensions(self):
        """Generates the dimensions of the position based on the position of the player.
        The dimensions are stored in the width, height, x and y attributes.
        """
        if self.__pos == "top":
            self.width = Constants.POSITION_WIDTH_HORIZ
            self.height = Constants.POSITION_HEIGHT_HORIZ
            self.x = Constants.WINDOW_WIDTH/2
            self.y = Constants.WINDOW_HEIGHT - Constants.POSITION_HEIGHT_HORIZ/2
        elif self.__pos == "bottom":
            self.width = Constants.POSITION_WIDTH_HORIZ
            self.height = Constants.POSITION_HEIGHT_HORIZ
            self.x = Constants.WINDOW_WIDTH/2
            self.y = Constants.POSITION_HEIGHT_HORIZ/2
        elif self.__pos == "left":
            self.width = Constants.POSITION_WIDTH_VERT
            self.height = Constants.POSITION_HEIGHT_VERT
            self.x = Constants.POSITION_WIDTH_VERT/2
            self.y = Constants.WINDOW_HEIGHT/2
        elif self.__pos == "right":
            self.width = Constants.POSITION_WIDTH_VERT
            self.height = Constants.POSITION_HEIGHT_VERT
            self.x = Constants.WINDOW_WIDTH - Constants.POSITION_WIDTH_VERT/2
            self.y = Constants.WINDOW_HEIGHT/2
        else:
            raise ValueError("Invalid position")

    def draw(self):
        """Draws the position and the cards in the player's hand.
        The position is drawn as a box with the player's name.
        If the player is a dealer, the box is green.
        If the player is bust, the text is red.
        If the player is the current player, the text is prefixed with "Current Player: ".
        """
        # draw box and text
        rotation = 0
        textX = self.x
        textY = self.y
        colour = arcade.color.WHITE
        prefix = ""
        if self.__pos == "left":
            rotation = -90
            textX += (self.width/2 + 20)
        elif self.__pos == "right":
            rotation = 90
            textX -= (self.width/2 + 20)
        elif self.__pos == "top":
            textY -= (self.height/2 + 20)
        elif self.__pos == "bottom":
            textY += (self.height/2 + 20)
            prefix = "Current Player: "
        if isinstance(self.player, Dealer):
            colour = arcade.color.BANGLADESH_GREEN
        if self.__pos != "bottom":
            arcade.draw_rectangle_outline(self.x, self.y, self.width, self.height, colour, 2)

        # draw name
        textColour = arcade.color.WHITE
        if self.player.bust:
            textColour = arcade.color.RED
        arcade.draw_text(prefix+self.player.name, textX, textY, textColour, 16, align="center", anchor_x="center", anchor_y="center", width=300, rotation=rotation)

        # draw cards
        self.cards.draw()

    def update(self):
        """Updates the cards in the player's hand."""
        self.set_cards()

    def set_pos(self, pos: str):
        """Sets the position of the player.
        Used to move the currently playing player.

        Args:
            pos (str): The position of the player. Can be "top", "bottom", "left" or "right".
        """
        self.__pos = pos
        self.gen_dimensions()
        self.set_cards()