import arcade
from src.logic.game import Game
from src.gui.position import Position
from src.gui.constants import Constants
from src.gui.decksprite import DeckSprite
from src.gui.roundendscreen import RoundEndScreen

# code takes inspiration from arcade docs - https://api.arcade.academy/en/latest/tutorials/card_game/index.html#
class Controller(arcade.View):
    """The controller for the game. Handles the game loop and the GUI.
    
    Attributes:
        game (Game): The game information.
        deck (Deck): The deck of cards.
        positions (list[Position]): The playing positions on the table.
        deckSprite (DeckSprite): The sprite for the deck.
        activePlayer (Player): The player whose turn it is.
        status (str): The status of the game. Used to determine text to display.
    """

    def __init__(self, game: Game):
        """Initialises the window and game with game information.
        
        Args:
            game (Game): The game information - players, etc.
        """
        window = arcade.Window(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, "Blackjack")
        super().__init__()
        window.show_view(self)

        arcade.set_background_color(arcade.color.AMAZON)

        self.__game = game
        self.__deck = game.deck
        self.__positions: list[Position] = []
        self.__deckSprite = DeckSprite(self.__deck, Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 + 70)
        self.__activePlayer = None
        self.__status = "playing"

        # used for a non-blocking pause - see pause() method and on_update()
        self.__pause_elapsed = None
        self.__pause_target = None
        self.__pause_action: callable = None

    def setup(self):
        """Sets up the game for a new round.
        
        Initialises starting values - can be used to reset the game.
        """
        # reinitialise - used for a new round
        self.__positions: list[Position] = []
        self.__deckSprite = DeckSprite(self.__deck, Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 + 70)
        self.__activePlayer = None
        self.__status = "playing"
        self.__pause_elapsed = None
        self.__pause_target = None
        self.__pause_action: callable = None

        self.__positions.append(Position("top", self.__game.dealer))
        pos = ["bottom", "left", "right"]
        for i, player in enumerate(self.__game.players):
            self.__positions.append(Position(pos[i], player))
            player.played = False
        self.__activePlayer = self.__game.players[0]

    def next_round(self):
        """Starts a new round."""
        self.__game.new_round()
        self.setup()
        self.window.show_view(self)

    def move_next_player(self):
        """Moves to the next player's turn.
        Once all players have played, the dealer's turn is started.
        """
        self.__activePlayer.played = True
        player_positions = []   # list of positions that are not top (dealer)
        possible_pos_str = []   # list of possible position location strings
        for position in self.__positions:
            if position.pos != "top":
                player_positions.append(position)
                possible_pos_str.append(position.pos)
        
        for i, position in enumerate(player_positions):
            nextPos = possible_pos_str[(i+1) % len(possible_pos_str)]
            if nextPos == "bottom":
                if position.player.played:          # if all players have played, dealer's turn
                    self.__status = "dealer"
                    self.__game.dealer_round()      # flip dealer's hidden card
                    self.update_dealer_cards()
                    self.pause(2, self.dealer_round)
                    return
                self.__activePlayer = position.player
            position.set_pos(nextPos)

    def handle_state(self):
        """Handles the state of the game.
        Controls the text to display and displayes round end screen when the round is over.
        """
        if self.__status == "playing":
            text = arcade.create_text_sprite("Click on the deck to hit or press any key to stand.", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.WHITE, 20, anchor_x="center")
            text.draw()
        elif self.__status == "stand":
            text = arcade.create_text_sprite("Stand! Next player...", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.WHITE, 20, anchor_x="center")
            text.draw()
        elif self.__status == "bust":
            text = arcade.create_text_sprite("Bust! You lose...", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.RED, 20, anchor_x="center")
            text.draw()
        elif self.__status == "dealer":
            text = arcade.create_text_sprite("Round finished! Time for the dealer to draw.", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.GOLD, 20, anchor_x="center")
            text.draw()
        elif "dealer_done" in self.__status:
            text = arcade.create_text_sprite("Dealer finished drawing ...", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.GOLD, 20, anchor_x="center")
            text.draw()
            if "paused" not in self.__status:       # only enter pause once
                self.pause(2, self.show_round_end)  # pause for 2 seconds before showing round end screen
                self.__status += "_paused"

    def hit(self):
        """Handles the hit action.
        If the player busts, the player's turn is ended.
        """
        isBust = self.__game.hit(self.__activePlayer)
        self.__deckSprite.update()
        self.update_active_cards()
        if isBust:
            self.__status = "bust"
            self.pause(2, self.resume_with_next)

    def stand(self):
        """Handles the stand action. Ends the player's turn."""
        if self.__status == "stand":
            return
        self.__status = "stand"
        self.__game.stand(self.__activePlayer)
        self.pause(1, self.resume_with_next)

    def pause(self, target: float, action: callable):
        """Asynchronously waits for a certain amount of time before performing an action.

        This method initialised the attributes for the pause. 
        The pause is then handled in the on_update() method.

        Args:
            target (float): The amount of time to pause for (in seconds).
            action (callable): The action to perform after the pause.

        Raises:
            Exception: If the pause is already in use.
        """
        if self.__pause_elapsed is not None:
            raise Exception("Already using pause")
        self.__pause_target = target
        self.__pause_action = action
        self.__pause_elapsed = 0

    def resume_with_next(self):
        """Proceeds the game with the next player's turn."""
        self.__status = "playing"
        self.move_next_player()

    def show_round_end(self):
        """Shows the round end screen."""
        self.window.show_view(RoundEndScreen(self.__game, self.next_round))

    def update_active_cards(self):
        """Updates the cards of the active player."""
        for position in self.__positions:
            if position.player == self.__activePlayer:
                position.update()

    def update_dealer_cards(self):
        """Updates the cards of the dealer."""
        for position in self.__positions:
            if position.player == self.__game.dealer:
                position.update()

    # DEALER GAME LOGIC

    def dealer_round(self):
        """Starts the dealer's turn."""
        self.__status = "dealer"
        self.update_dealer_cards()  # redraw since dealer's hidden card is now visible

        self.dealer_draw()

    def dealer_draw(self):
        """Handles the dealer's drawing.
        If the dealer's score is less than 17, the dealer draws another card recursively
        after a 2 second pause.
        
        If the dealer's score is 17 or more, the dealer's turn is ended.
        """
        if self.__game.dealer.score < 17:
            self.__game.hit(self.__game.dealer)
            self.__deckSprite.update()
            self.update_dealer_cards()
            self.pause(2, self.dealer_draw) # recursion here
        else: 
            self.__status = "dealer_done"

    # ARCADE EVENT HANDLERS

    def on_draw(self):
        """Render the screen."""
        self.clear()
        for position in self.__positions:
            position.draw()
        self.__deckSprite.draw()
        self.handle_state()
    
    def on_update(self, delta_time: float):
        """Handles the pause if one is active.
        Once __pause_elapsed is >= __pause_target, the __pause_action is performed."""
        if self.__pause_target is not None:
            self.__pause_elapsed += delta_time
            if self.__pause_elapsed >= self.__pause_target:
                action = self.__pause_action
                self.__pause_target = None  # resets the pause attributes
                self.__pause_elapsed = None
                self.__pause_action = None
                action()

    def on_key_press(self, symbol: int, modifiers: int):
        """Handles key presses. Used to stand."""
        if self.__status != "playing":
            return
        self.stand()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        """Handles mouse clicks. Used to hit when deck clicked."""
        if self.__status != "playing":
            return
        deck = arcade.get_sprites_at_point((x, y), self.__deckSprite)
        if len(deck) > 0:   # if any deckSprite is clicked then hit
            self.hit()