from src.logic.card import Card

class Hand:
    """A class representing a hand of cards. Keeps track of scores."""

    def __init__(self, initCards: list[Card]):
        """Create a new hand with initial cards.
        
        Args:
            initCards (list[Card]): The initial cards in the hand. In blackjack, this should be 2 cards.
        """
        self.__cards: list[Card] = []

        if initCards is not None:
            self.__cards = initCards

        self.__score = Hand.get_best_total(self.__cards)

    def __str__(self):
        return str(self.__cards)

    @staticmethod
    def get_best_total(cards: list[Card]) -> int:
        """Get the best total of a list of cards.

        Needs to consider aces to determine the best total since aces can be 1 or 11.

        Args:
            cards (list[Card]): The cards in the list.
        
        Returns:
            int: The best total of the list.
        """
        total = 0
        numOfAces = 0

        for card in cards:
            value = card.get_value()
            total += value[0]

            if len(value) > 1:   # if card has choices then is an ace
                numOfAces += 1
        
        while numOfAces > 0 and total <= 21-10:  # if have room for big ace then add one
            total += 10
            numOfAces -= 1
        
        return total

    @property
    def cards(self) -> list[Card]:
        """Get the cards in the hand.
        
        Returns:
            list[Card]: The cards in the hand.
        """
        return self.__cards

    @property
    def score(self) -> int:
        """Get the score of the hand.
        
        Returns:
            int: The score of the hand.
        """
        return self.__score

    @property
    def bust(self) -> bool:
        """Check if the hand is bust.
        
        Returns:
            bool: True if the hand is bust, False otherwise.
        """
        return self.__score > 21

    def add_card(self, card: Card):
        """Add a card to the hand and update the score.
        
        Args:
            card (Card): The card to add.
        """
        self.__cards.append(card)
        self.__score = Hand.get_best_total(self.__cards)