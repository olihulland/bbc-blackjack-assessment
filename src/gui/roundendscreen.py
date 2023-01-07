import arcade
from src.gui.constants import Constants
from src.logic.game import Game
from src.gui.cardsprite import CardSprite

class RoundEndScreen(arcade.View):
    def __init__(self, game: Game, on_next_round: callable):
        super().__init__()
        self.__game = game
        self.__on_next_round = on_next_round
        self.results = self.__game.end_round_calc()

    def on_draw(self):
        self.clear()
        arcade.draw_text("Round End", Constants.WINDOW_WIDTH/2, Constants.WINDOW_HEIGHT - 50, arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")

        # draw the dealers hand and score
        dealer = self.__game.dealer
        dealerXLeft = 30
        dealerYCenter = Constants.WINDOW_HEIGHT - 200
        dealerHeader = arcade.Text("Dealer", dealerXLeft, dealerYCenter, arcade.color.WHITE, 20, anchor_x="left", anchor_y="center")
        dealerHeader.draw()

        dealerHand = arcade.SpriteList()
        dealerHandX = dealerXLeft + dealerHeader.content_width + 30
        for i, card in enumerate(dealer.cards):
            cardSprite = CardSprite(card)
            cardSprite.set_position((dealerHandX+Constants.CARD_WIDTH/2) + (i*(Constants.CARD_WIDTH*0.25)), dealerYCenter)
            dealerHand.append(cardSprite)
        dealerHand.draw()

        dealerScoreX = dealerHandX + (len(dealer.cards) * (Constants.CARD_WIDTH*0.25)) + Constants.CARD_WIDTH + 30
        scoreColor = arcade.color.RED if dealer.bust else arcade.color.WHITE
        arcade.draw_text(f"({dealer.score})", dealerScoreX, dealerYCenter, scoreColor, 20, anchor_x="left", anchor_y="center")

        # draw each players hand and score and total wins and ties
        playerXLeft = 30
        playerYCenter = Constants.WINDOW_HEIGHT - 300
        for playerI, player in enumerate(self.__game.players):
            playerHeader = arcade.Text(player.name, playerXLeft, playerYCenter, arcade.color.WHITE, 20, anchor_x="left", anchor_y="center")
            playerHeader.draw()

            playerHand = arcade.SpriteList()
            playerHandX = playerXLeft + playerHeader.content_width + 30
            for i, card in enumerate(player.cards):
                cardSprite = CardSprite(card)
                cardSprite.set_position((playerHandX+Constants.CARD_WIDTH/2) + (i*(Constants.CARD_WIDTH*0.25)), playerYCenter)
                playerHand.append(cardSprite)
            playerHand.draw()

            playerScoreX = playerHandX + (len(player.cards) * (Constants.CARD_WIDTH*0.25)) + Constants.CARD_WIDTH + 30
            scoreColor = arcade.color.WHITE
            result = self.results[playerI]
            if "Lose" in result:
                scoreColor = arcade.color.RED
            elif "Win" in result:
                scoreColor = arcade.color.GOLD
            arcade.draw_text(f"({player.score})", playerScoreX, playerYCenter, scoreColor, 20, anchor_x="left", anchor_y="center")
            arcade.draw_text(result, playerScoreX + 50, playerYCenter, scoreColor, 20, anchor_x="left", anchor_y="center")

            arcade.draw_text(f"Wins: {player.wins}  Ties: {player.ties}", Constants.WINDOW_WIDTH-30, playerYCenter, arcade.color.WHITE, 20, anchor_x="right", anchor_y="center")

            playerYCenter -= 100

        # press any key to play another round text
        arcade.draw_text("Press any key to play another round", Constants.WINDOW_WIDTH/2, 50, arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")

    def on_key_press(self, symbol: int, modifiers: int):
        self.__on_next_round()
