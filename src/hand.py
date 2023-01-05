from src.card import Card
from src.deck import Deck

class Hand:
    """A class representing a hand of cards - starting with 2."""

    def __init__(self, deck: Deck):
        """Create a new hand with two cards to start."""
        self.cards: list[Card] = []

        self.cards.append(deck.draw())
        self.cards.append(deck.draw())

    def __str__(self):
        return str(self.cards)

    def getBestTotal(self) -> int:
        """Get the best total of the hand.
        
        Returns:
            int: The best total of the hand.
        """
        total = 0
        numOfAces = 0

        for card in self.cards:
            value = card.getValue()
            total += value[0]

            if len(value) > 1:   # if card has choices then is an ace
                numOfAces += 1
        
        while numOfAces > 0 and total <= 21-10:  # if have room for big ace then add one
            total += 10
            numOfAces -= 1
        
        return total

    def checkBust(self) -> bool:
        """Check if the hand is bust.
        
        Returns:
            bool: True if the hand is bust, False otherwise.
        """
        return self.getBestTotal() > 21
