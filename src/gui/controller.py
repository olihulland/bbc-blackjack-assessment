import arcade
from src.logic.game import Game
from src.gui.position import Position
from src.gui.constants import Constants
from src.gui.decksprite import DeckSprite
from src.gui.roundendscreen import RoundEndScreen

# code takes inspiration from arcade docs - https://api.arcade.academy/en/latest/tutorials/card_game/index.html#
class Controller(arcade.View):
    def __init__(self, game: Game):
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

    def move_next_player(self):
        self.__activePlayer.played = True
        player_positions = []
        possible_pos = []
        for position in self.__positions:
            if position.pos != "top":
                player_positions.append(position)
                possible_pos.append(position.pos)
        
        for i, position in enumerate(player_positions):
            nextPos = possible_pos[(i+1) % len(possible_pos)]
            if nextPos == "bottom":
                if position.player.played:
                    self.__status = "dealer"
                    self.__game.dealer_round()      # flip dealer's hidden card
                    self.update_dealer_cards()
                    self.pause(2, self.dealer_round)
                    return
                self.__activePlayer = position.player
            position.set_pos(nextPos)

    def handle_state(self):
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
            if "paused" not in self.__status:
                self.pause(2, self.show_round_end)
                self.__status += "_paused"

    def show_round_end(self):
        self.window.show_view(RoundEndScreen(self.__game, self.next_round))

    def next_round(self):
        self.__game.new_round()
        self.setup()
        self.window.show_view(self)

    def update_active_cards(self):
        for position in self.__positions:
            if position.player == self.__activePlayer:
                position.update()

    def update_dealer_cards(self):
        for position in self.__positions:
            if position.player == self.__game.dealer:
                position.update()

    def pause(self, target: float, action: callable):
        if self.__pause_elapsed is not None:
            raise Exception("Already using pause")
        self.__pause_target = target
        self.__pause_action = action
        self.__pause_elapsed = 0

    def resume_with_next(self):
        self.__status = "playing"
        self.move_next_player()

    def hit(self):
        isBust = self.__game.hit(self.__activePlayer)
        self.__deckSprite.update()
        self.update_active_cards()
        if isBust:
            self.__status = "bust"
            self.pause(2, self.resume_with_next)

    def stand(self):
        if self.__status == "stand":
            return
        self.__status = "stand"
        self.__game.stand(self.__activePlayer)
        self.pause(1, self.resume_with_next)

    def dealer_round(self):
        self.__status = "dealer"
        self.update_dealer_cards()

        self.dealer_draw()


    def dealer_draw(self):
        if self.__game.dealer.score < 17:
            self.__game.hit(self.__game.dealer)
            self.__deckSprite.update()
            self.update_dealer_cards()
            self.pause(2, self.dealer_draw)
        else: 
            self.__status = "dealer_done"

    def on_draw(self):
        """Render the screen."""
        self.clear()
        for position in self.__positions:
            position.draw()
        self.__deckSprite.draw()
        self.handle_state()
    
    def on_update(self, delta_time: float):
        if self.__pause_target is not None:
            self.__pause_elapsed += delta_time
            if self.__pause_elapsed >= self.__pause_target:
                action = self.__pause_action
                self.__pause_target = None
                self.__pause_elapsed = None
                self.__pause_action = None
                action()

    def on_key_press(self, symbol: int, modifiers: int):
        if self.__status != "playing":
            return
        self.stand()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.__status != "playing":
            return
        deck = arcade.get_sprites_at_point((x, y), self.__deckSprite)
        if len(deck) > 0:
            self.hit()