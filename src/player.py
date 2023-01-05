from src.card import Card
from src.deck import Deck
from src.hand import Hand

class Player:
    """A player in the game."""

    def __init__(self, name: str, deck: Deck):
        """Create a new player with the given name."""
        self.name = name
        self.deck = deck
        self.__hand = Hand([deck.draw(), deck.draw()])

    def __str__(self):
        return self.name + ": " + str(self.__hand)

    def __repr__(self) -> str:
        return self.__str__()

    def hit(self):
        """The player chooses to hit. Draws a card from the deck and adds it to the hand."""
        self.__hand.addCard(self.deck.draw())

    def stand(self):
        """The player chooses to stand. Does nothing."""
        # do nothing, have included for extensibility
        pass

    @property
    def cards(self) -> list[Card]:
        """Get the cards in the player's hand.
        
        Returns:
            list[Card]: The cards in the player's hand.
        """
        return self.__hand.cards

    @property
    def score(self) -> int:
        """Get the score of the player.
        
        Returns:
            int: The score of the player.
        """
        return self.__hand.score

    @property
    def bust(self) -> bool:
        """Get whether the player is bust.
        
        Returns:
            bool: Whether the player is bust.
        """
        return self.__hand.bust