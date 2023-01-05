from src.logic.controller import Controller


def play():
    controller = Controller()
    controller.add_player("Oli")
    controller.add_player("Tom")

    controller.start_game()


if __name__ == '__main__':
    play()
    