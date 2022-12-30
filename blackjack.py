from src.controller import Controller


def play():
    print("Starting")
    controller = Controller()
    controller.add_player("Oli")
    controller.add_player("Tom")
    print(controller)


if __name__ == '__main__':
    play()
    