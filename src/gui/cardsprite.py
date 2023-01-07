import arcade
from src.logic.card import Card as LogicCard
from src.gui.constants import Constants

class CardSprite(arcade.Sprite):
    """The sprite for a card. Displays the card image.

    Image either matches the suit and rank of the card or is the back of the card
    if the card is upside down.
    
    Images sourced from https://opengameart.org/content/boardgame-pack
    Credit: www.kenney.nl
    """
    def __init__(self, card: LogicCard):
        """Create a new card with the given suit and rank."""
        if not card.upside_down:
            imageFile = f"src/gui/assets/Cards/card{card.suit.capitalize()}{card.rank.upper()}.png"
        else:
            imageFile = f"src/gui/assets/Cards/cardBack_red4.png"

        super().__init__(imageFile, scale=Constants.CARD_SCALE, hit_box_algorithm="None")