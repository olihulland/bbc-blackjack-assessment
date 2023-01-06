from src.logic.controller import Controller
from src.gui.table import Table
import arcade


def play():
    # setup the game logic
    controller = Controller()
    controller.add_player("Oli")
    controller.add_player("Tom")

    # setup the gui
    table = Table()
    table.setup()

    # start the gui
    arcade.run()


if __name__ == '__main__':
    play()
    