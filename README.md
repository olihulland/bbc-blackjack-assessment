# Blackjack Tech Test - BBC Software Engineering Graduate Scheme

The code in this repository is my attempt at the tech test. It provides a playable game of Blackjack with 2D graphics.

The game is limited to 2-3 players (& a dealer), this is to simplify the graphics however the classes in `logic/` don't have such limitations.

## Structure

The code is split into 3 main parts:
- `logic/` - this contains the game information and logic for scoring hands. This alone should satisfy the scenario requirements of the test.
- `gui/` - this contains the graphical user interface for the game. It is written using the arcade library and is a simple 2D game.
- `test/` - this contains the unit tests for the game logic. They test for the scenarios given in the brief and some additional tests to support my test driven development. The tests representing the scenarios are commented with the scenario description.

## Running
### Requirements
- Python 3 (I used 3.9 - earlier versions of python may work but are untested. Type hintings may cause issues in earlier versions.)
- Arcade library for graphics - this can be installed using `pip install arcade` or `pip3 install arcade` depending on your setup.

### Running the game
- Open a terminal window and navigate to the folder containing this README.
- Run `python3 blackjack.py` (or `python blackjack.py` depending on setup)
*Note: If you are running on a Mac you may be prompted to grant permissions for input monitoring to enable to game to run.*
- Complete the steps as prompted in the terminal window. The game window should appear once the players have been added.

### Running the unit tests
- Open a terminal window and navigate to the folder containing this README.
- Run `python3 -m unittest discover test` (or `python -m unittest discover test` depending on setup)


## Credits
The card images are sourced from [here](https://opengameart.org/content/boardgame-pack).
Credit: [kenney.nl](https://www.kenney.nl/)
Licence: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

The code is built upon the provided starter code.