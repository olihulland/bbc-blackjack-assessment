from src.player import Player
from src.deck import Deck
from src.dealer import Dealer

class Controller:
    """Class that controls the game."""

    def __init__(self):
        """Create a new controller."""
        self.deck = Deck()
        self.players: list[Player] = []
        self.dealer = Dealer(self.deck)

        self.__playing = False

    def add_player(self, name: str):
        """Add a player to the game."""
        if self.__playing:
            raise Exception("Cannot add player while game is in progress")

        self.players.append(Player(name, self.deck))

    def start_game(self):
        """Start the game."""
        if self.__playing:
            raise Exception("Game is already in progress")

        self.__playing = True

        print("Starting game")

        self.play_round()

    def play_round(self):
        """Play a round of the game."""
        if not self.__playing:
            raise Exception("Game is not in progress")

        print("Playing round")

        self.print_hands()

        for player in self.players:
            player.play_turn()

        self.dealer.play_turn()

        if self.dealer.bust:
            print("Dealer busts! All players win!")
        else:
            dealerScore = self.dealer.score
            print("Round over, the dealer scores " + str(dealerScore))
            for player in self.players:
                if player.bust:
                    print(player.name + " busts! They lose this round!")
                playerScore = player.score
                if playerScore > dealerScore:
                    print(f"{player.name} wins with {playerScore}!")
                elif playerScore == dealerScore:
                    print(f"{player.name} draws with {playerScore}!")
                else:
                    print(f"{player.name} loses with {playerScore}!")

        
    def print_hands(self):
        """Print the hands of the players and the dealer."""
        print(self.dealer.status)
        for player in self.players:
            print(player.status)

    def __str__(self):
        return f"Players: {self.players}\nDeck: {len(self.deck.cards)} cards"