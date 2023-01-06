from src.logic.game import Game
from src.gui.table import Table
import arcade


def play():
    # setup the game logic
    logic = Game()
    logic.add_player("Oli")
    logic.add_player("Tom")
    logic.add_player("Emi")

    # setup the gui
    table = Table(logic)
    table.setup()

    # start the gui
    arcade.run()

if __name__ == '__main__':
    play()
    