from src.logic.game import Game
from src.gui.controller import Controller
import arcade


def play():
    # setup the game logic
    logic = Game()
    print("Welcome to Blackjack! This implementation supports 2-3 players (limited by GUI).")
    numPlayers = 0
    while numPlayers < 3:
        name = input(f"Type player {numPlayers+1}'s name and press enter or type 'start' to start the game: \n")
        if name.lower() == "start":
            if numPlayers < 2:
                print("You need at least 2 players to play!")
                continue
            break
        logic.add_player(name)
        numPlayers += 1

    print("Players added. Starting game...")

    # setup the gui
    table = Controller(logic)
    table.setup()

    # start the gui
    arcade.run()

if __name__ == '__main__':
    play()
    