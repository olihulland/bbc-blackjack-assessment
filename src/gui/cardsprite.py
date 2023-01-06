import arcade
from src.logic.card import Card as LogicCard

class CardSprite(arcade.Sprite):
    def __init__(self, card: LogicCard):
        """Create a new card with the given suit and rank."""
        if not card.upside_down:
            imageFile = f"src/gui/assets/Cards/card{card.suit.capitalize()}{card.rank.upper()}.png"
        else:
            imageFile = f"src/gui/assets/Cards/cardBack_red4.png"

        super().__init__(imageFile, scale=0.5, hit_box_algorithm="None")