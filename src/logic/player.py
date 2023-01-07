from src.logic.card import Card
from src.logic.deck import Deck
from src.logic.hand import Hand

class Player:
    """A player in the game."""

    def __init__(self, name: str, deck: Deck):
        """Create a new player with the given name."""
        self.name = name
        self.deck = deck
        self.__hand = Hand([deck.draw(), deck.draw()])
        self.played = False
        self.__wins = 0
        self.__ties = 0

    def __str__(self):
        return self.name + ": " + str(self.__hand)

    def __repr__(self) -> str:
        return self.__str__()

    def new_round(self) -> None:
        """Sets up for a new round - redeals cards"""
        self.__hand = Hand([self.deck.draw(), self.deck.draw()])

    def hit(self) -> Card:
        """The player chooses to hit. Draws a card from the deck and adds it to the hand."""
        newCard = self.deck.draw()
        self.__hand.addCard(newCard)
        return newCard

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

    @property
    def status(self) -> str:
        """Get the status of the player.
        
        Returns:
            str: The status of the player.
        """
        return self.name + ": " + str(self.__hand)

    @property
    def wins(self) -> int:
        """Get the number of wins for the player.
        
        Returns:
            int: The number of wins for the player.
        """
        return self.__wins

    @property
    def ties(self) -> int:
        """Get the number of ties for the player.
        
        Returns:
            int: The number of ties for the player.
        """
        return self.__ties

    def add_win(self):
        """Add a win to the player."""
        self.__wins += 1

    def add_tie(self):
        """Add a tie to the player."""
        self.__ties += 1