class Card:
    """A class representing a playing card.
    
    Attributes:
        suit (str): The suit of the card.
        rank (str): The rank of the card.
    """

    SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, suit: str, rank: str, upside_down: bool = False):
        """Create a new card with the given suit and rank.

        Args:
            suit (str): The suit of the card.
            rank (str): The rank of the card.

        Raises:
            ValueError: If the suit or rank is invalid.
        """
        if suit.capitalize() not in Card.SUITS:
            raise ValueError("Invalid suit")
        if rank.upper() not in Card.RANKS:
            raise ValueError("Invalid value")

        self.suit = suit.capitalize()
        self.rank = rank.upper()
        self.upside_down = upside_down

    def __str__(self):
        if self.upside_down:
            return "?"
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.__str__()

    def getValue(self) -> list[int]:
        """Get the value of the card.

        Returns:
            list[int]: The possible values of the card, normally len of 1 unless multiple choices such as Ace.
        """
        if self.rank == "A":
            return [1, 11]
        elif self.rank in ["J", "Q", "K"]:
            return [10]
        else:
            return [int(self.rank)]