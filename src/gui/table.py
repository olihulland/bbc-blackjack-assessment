import arcade
from src.logic.gamelogic import GameLogic
from src.gui.position import Position
from src.gui.constants import Constants
from src.gui.decksprite import DeckSprite

# code takes inspiration from arcade docs - https://api.arcade.academy/en/latest/tutorials/card_game/index.html#

class Table(arcade.Window):
    def __init__(self, logic: GameLogic):
        super().__init__(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT, "Blackjack")
        arcade.set_background_color(arcade.color.AMAZON)

        self.__logic = logic
        self.__deck = logic.deck
        self.__positions: list[Position] = []
        self.__deckSprite = DeckSprite(self.__deck, Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 + 70)
        self.__activePlayer = None

        self.__prompt_status = "playing"

        self.__pause_elapsed = None
        self.__pause_target = None
        self.__pause_action: callable = None

    def setup(self):
        self.__positions.append(Position("top", self.__logic.dealer))
        pos = ["bottom", "left", "right"]
        for i, player in enumerate(self.__logic.players):
            self.__positions.append(Position(pos[i], player))
        self.__activePlayer = self.__logic.players[0]

    def move_next_player(self):
        player_positions = []
        possible_pos = []
        for position in self.__positions:
            if position.pos != "top":
                player_positions.append(position)
                possible_pos.append(position.pos)
        
        for i, position in enumerate(player_positions):
            nextPos = possible_pos[(i+1) % len(possible_pos)]
            position.set_pos(nextPos)
            if nextPos == "bottom":
                self.__activePlayer = position.player

    def draw_prompt(self):
        if self.__prompt_status == "playing":
            text = arcade.create_text_sprite("Click on the deck to hit or press any key to stand.", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.WHITE, 20, anchor_x="center")
            text.draw()
        elif self.__prompt_status == "stand":
            text = arcade.create_text_sprite("Stand! Next player...", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT/2 - 80, arcade.color.WHITE, 20, anchor_x="center")
            text.draw()

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.__prompt_status != "playing":
            return
        deck = arcade.get_sprites_at_point((x, y), self.__deckSprite)
        if len(deck) > 0:
            self.hit()

    def update_active_cards(self):
        for position in self.__positions:
            if position.player == self.__activePlayer:
                position.update()

    def hit(self):
        self.__activePlayer.hit()
        self.__deckSprite.update()
        self.update_active_cards()

    def pause(self, target: float, action: callable):
        self.__pause_target = target
        self.__pause_action = action
        self.__pause_elapsed = 0

    def stand(self):
        if self.__prompt_status == "stand":
            return
        self.__prompt_status = "stand"
        self.pause(1, self.after_stand)

    def after_stand(self):
        self.__prompt_status = "playing"
        self.move_next_player()

    def on_draw(self):
        """Render the screen."""
        self.clear()
        for position in self.__positions:
            position.draw()
        self.__deckSprite.draw()
        self.draw_prompt()
    
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
        self.stand()

